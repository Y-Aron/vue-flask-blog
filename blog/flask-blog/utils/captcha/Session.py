
"""
sessoin = Session(requestHandler)

1.用户登录 -> 保存用户信息的cookie -> Session获取cookie -> 生成session_id 设置成cookie
2.在redis 中设置key为session_{session_id}的 对象{}
3.set(key,val,ex=None)
4.get(key)
5.clear()

"""
import uuid,logging,json

SESSION_EXPIRE = 3600

class Session(object):

    data,session_id = dict(),None

    def __init__(self,request):
        self.request = request
        self.redis = request.redis

    def set(self,key,val):
        self.data[key] = val

    def commit(self):
        session_id = self.request.get_secure_cookie('session_id') or self.session_id

        if not session_id:
            session_id = 'session_{id}'.format(id=uuid.uuid4().hex)
            self.request.set_secure_cookie('session_id',session_id)
            self.session_id = session_id

        if session_id and self.data:
            try:
                real_data = self.redis.get(session_id)
            except Exception as e:
                logging.error(e)
                raise Exception('commit data to redis go wrong')

            if real_data:
                new_data = json.loads(real_data)
                for key in self.data:
                    new_data[key] = self.data[key]
            else:
                new_data = self.data

            try:
                new_data = json.dumps(new_data)
                self.redis.set(session_id,new_data,ex=SESSION_EXPIRE)
            except Exception as e:
                logging.error(e)
                raise Exception('set value to redis go wrong')

        return True

    def get(self, key):
        session_id = self.request.get_secure_cookie('session_id') or self.session_id
        if not session_id:
            return None
        try:
            data = self.redis.get(session_id)
        except Exception as e:
            logging.error(e)
            raise Exception('get value of redis go wrong')
        if data:
            real_data = json.loads(data)
            return real_data[key]
        return None


    def clear(self, key=None):
        session_id = self.request.get_secure_cookie('session_id') or self.session_id

        if not session_id:
            raise Exception('session_id is not exist')

        if not key:
            try:
                self.redis.delete(session_id)
            except Exception as e:
                logging.error(e)
                raise Exception('delete data of redis go wrong!')
            else:
                return True

        try:
            data = json.loads(self.redis.get(session_id))
            if key in data: del data[key]
            data = json.dumps(data)
            self.redis.set(session_id,data)
        except Exception as e:
            logging.error(e)
            raise Exception('clear key value of redis is go wrong!')
        else:
            return True

