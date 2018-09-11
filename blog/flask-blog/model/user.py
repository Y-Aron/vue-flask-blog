from model import Model
from config import STATUS
from utils import md5_encrypt, logger, make_tree, getTree

class AuthGroup(Model):

    __tablename__ = 'tb_auth_group'

    def fetchGroup(self):
        sql = 'select `id`, `name` from {table}'.format(table=self.__tablename__)
        ret = self.select(sql)
        if ret: return self.respData(data=ret)

    def fetchData(self, uuid):
        sql = 'select * from {table} WHERE `id`=%s'.format(table=self.__tablename__)
        ret = self.select(sql, uuid, one=True)

        if not ret:
            return self.respData(STATUS.DATA_NULL_ERR, error='id={id}的用户组不存在~'.format(id=uuid))

        sql = 'select rule_id from tb_auth_group_rule WHERE `group_id`=%s'

        rule_ret = self.select(sql, uuid)

        rule_array = []

        for vol in rule_ret:
            rule_array.append(vol['rule_id'])

        data = dict(
            group_data = ret,
            rule_data = rule_array
        )
        return self.respData(error='用户组查询成功~', data=data)

    def fetchList(self, start:int, length:int):
        sql = 'select * from {table} LIMIT %s,%s'.format(table=self.__tablename__)

        ret = self.paging(sql, start, length)
        if ret:
            return self.respData(STATUS.OK, data=ret)

        return self.respData(STATUS.DATA_NULL_ERR, error='用户组数据不存在~')

    def fetchUserAuth(self, uuid):
        sql = 'SELECT a.id, a.username, b.group_id FROM ' \
              'tb_user AS a LEFT JOIN tb_auth_user_group as b ON a.id=b.uid WHERE a.id=%s'
        ret = self.select(sql, uuid)

        if not ret: return self.respData(error='id={id}的用户不存在~'.format(id=uuid))

        group_array = []
        for vol in ret:
            if not vol['group_id']: continue
            group_array.append(vol['group_id'])

        data = dict(
            uid = ret[0]['id'],
            username = ret[0]['username'],
            group_array = group_array
        )
        return self.respData(data=data, error='查询用户组成功~')

    def remove(self, uuid):
        ret = self.delete(uuid)

        if ret: return self.respData(STATUS.OK, error='用户组删除成功~')

        return self.respData(STATUS.DARA_DELETE_ERR, error='用户组删除失败~')

    def create(self, data):
        sql = 'select count(*) AS total from {table} WHERE `name`=%s'.format(table=self.__tablename__)

        ret = self.select(sql, data['name'], one=True)
        if ret['total']: return self.respData(STATUS.DATA_EXISTS_ERR, error='该用户组已存在~')

        rule_array = data['rule_array']
        del data['rule_array']
        ret = self.join_extend_field_insert(data)

        if not ret: return self.respData(STATUS.DATA_CREATE_ERR, error='用户组创建失败~')

        group_rule_data = []

        for index in rule_array:
            tmp = dict(
                rule_id = index,
                group_id = ret
            )
            group_rule_data.append(tmp)
        ret = self.join_extend_field_insert(group_rule_data, table='tb_auth_group_rule')
        self.__tablename__ = 'tb_auth_group'

        return self.respData(error='用户组创建成功~')

    def edit(self, data, uuid):
        rule_array = data['rule_array']
        del data['rule_array']

        ret = self.join_extend_field_update(data, uuid)

        sql = 'select rule_id from tb_auth_group_rule WHERE `group_id`=%s'

        rules = self.select(sql, uuid)

        copy_rules = {}
        for vol in rules:
            copy_rules[vol['rule_id']] = vol

        insert_data = []
        for vol in rule_array:
            if vol not in copy_rules:
                insert_data.append(dict(
                    rule_id = vol,
                    group_id = uuid
                ))
            else:
                del copy_rules[vol]

        if insert_data: self.join_extend_field_insert(insert_data, table='tb_auth_group_rule')
        if copy_rules: self.delete(list(copy_rules.keys()), table='tb_auth_group_rule', pk_name='rule_id')

        self.__tablename__ = 'tb_auth_group'

        return self.respData(STATUS.OK, error='用户组更新成功~')

    def editAuth(self, uuid, auth_group):
        postData = []
        sql = 'select `group_id` from tb_auth_user_group WHERE `uid`=%s'

        ret = self.select(sql, uuid)

        copy_group = {}
        for vol in ret:
            copy_group[vol['group_id']] = vol

        insert_data = []

        for vol in auth_group:
            if vol not in copy_group:
                insert_data.append(dict(
                    uid = uuid,
                    group_id = vol
                ))
            else:
                del copy_group[vol]

        if insert_data:
            self.join_extend_field_insert(insert_data, table='tb_auth_user_group')
        if copy_group:
            for vol in list(copy_group.keys()):
                sql = 'delete from tb_auth_user_group WHERE `uid`=%s AND `group_id`=%s'
                self.execute(sql, uuid, vol)

        self.__tablename__ = 'tb_auth_group'
        return self.respData(STATUS.OK, error='用户组授权成功~')

class AuthRule(Model):

    __tablename__ = 'tb_auth_rule'

    def remove(self, uuid):
        ret = self.delete(uuid)

        if ret:
            self.update({'pid': 0}, {'pid': uuid})
            return self.respData(STATUS.OK, error='删除节点成功~')
        return self.respData(STATUS.DARA_DELETE_ERR)

    def fetchRoutes(self, uid, method):
        pname = 'get_routes'
        IN = dict(
            uid = uid,
            method = method
        )
        resultSet, ret = self.callProcedure(pname, IN)

        if not resultSet: return None

        routes = []
        for vol in resultSet:
            routes.append(vol['route'])
        return routes

    def create(self, data):
        logger.debug(data)
        root_id = 0
        if data['pid'] != 0:
            sql = 'select `root_id` from {table} WHERE `id`=%s'.format(table=self.__tablename__)
            ret = self.select(sql, data['pid'], one=True)
            if ret['root_id'] == 0:
                root_id = data['pid']
            else:
                root_id = ret['root_id']
        data['root_id'] = root_id

        ret = self.join_extend_field_insert(data)
        if ret: return self.respData(STATUS.OK, error='角色节点创建成功~')

        return self.respData(STATUS.DATA_CREATE_ERR, error='角色节点创建失败~')

    def edit(self, data, uuid):
        logger.debug(data)
        ret = self.join_extend_field_update(data, uuid)
        if ret: return self.respData(STATUS.OK, error='角色节点修改成功~')

        return self.respData(STATUS.DATA_CREATE_ERR, error='角色节点修改失败~')

    def fetchData(self, uuid):
        sql = 'select * from {table} WHERE `id`=%s'.format(table=self.__tablename__)

        ret = self.select(sql, uuid, one=True)
        if ret: return self.respData(data=ret)
        return self.respData(error='id={id}的角色节点信息不存在~'.format(id=uuid))

    def fetchRules(self):
        sql = 'select `id`, `pid`, `name`,`root_id` from {table}'.format(table=self.__tablename__)
        ret = self.select(sql)
        if not ret: return self.respData(STATUS.DATA_NULL_ERR, error='请先设置角色节点哦~')

        return self.respData(STATUS.OK, data=make_tree(ret, p_name='root_id'))


    def fetchList(self, start:int, length:int):
        sql = 'select * from {table} ORDER BY `sorts` LIMIT %s,%s'.format(table=self.__tablename__)

        ret = self.paging(sql, start, length)
        ret['list'] = getTree(ret['list'], c_name='id', t_name='name')
        if ret:
            return self.respData(STATUS.OK, data=ret)

        return self.respData(STATUS.DATA_NULL_ERR, error='用户组规则数据不存在~')


    def fetchOptions(self):
        sql = 'select id as value, `name` as text, pid from {table}'.format(table=self.__tablename__)
        ret = self.select(sql)

        tree_ret = getTree(ret)
        if ret:
            return self.respData(STATUS.OK, data=tree_ret)
        return self.respData(STATUS.DATA_NULL_ERR, error='没有角色节点数据哦~')

class User(Model):
    __tablename__ = 'tb_user'

    def login(self, username, password):
        sql = 'SELECT a.id, a.`password`,a.nickname, b.avatar FROM tb_user AS a LEFT JOIN tb_user_info AS b ON a.id=b.id WHERE `username`=%s'
        ret = self.select(sql, username, one=True)

        if not ret:
            return self.respData(STATUS.DATA_NULL_ERR, error='用户不存在哦~')

        if ret['password'] == md5_encrypt(password):
            data = dict(
                uid = ret['id'],
                username = ret['nickname'],
                avatar = '/api/download/{}'.format(ret['avatar'])
            )
            update_sql = 'UPDATE {table} SET `logins` = logins+1 WHERE id=%s'.format(table=self.__tablename__)
            self.execute(update_sql, ret['id'])
            return self.respData(STATUS.OK, data=data)

        return self.respData(STATUS.DATA_MATCH_ERR, error='密码错误~')

    def fetchOption(self):
        sql = 'select `id` as value ,`username` as text from {table}'.format(table=self.__tablename__)
        ret = self.select(sql)
        if ret:
            return self.respData(STATUS.OK, data=ret)
        return self.respData(STATUS.DATA_NULL_ERR, error='用户不存在~')

    def fetchList(self, start:int, length:int):
        sql = "SELECT a.id, a.username, a.nickname, a.email, a.mobile, a.logins, " \
              "a.`status`, b.avatar from {table} AS a LEFT JOIN tb_user_info AS b " \
              "ON a.id=b.id LIMIT %s,%s".format(table=self.__tablename__)

        ret = self.paging(sql, start, length)
        if ret:
            return self.respData(STATUS.OK, data=ret)

        return self.respData(STATUS.DATA_NULL_ERR, error='用户数据不存在~')

    def remove(self, uuid):
        ret = self.delete(uuid)
        if ret: return self.respData(STATUS.OK, error='用户删除成功~')

        return self.respData(STATUS.DARA_DELETE_ERR, error='用户删除失败~')

    def create(self, data):
        pname = 'register'
        data['password'] = md5_encrypt(data['password'])

        OUT = dict(
            status_code = 0
        )
        resultSet, ret = self.callProcedure(pname, data, OUT)
        if ret['status_code'] == 0:
            return self.respData(error='用户添加成功~')

        return self.respData(STATUS.DATA_CREATE_ERR, error='用户添加失败~')

    def fetchData(self, uuid):
        sql = 'SELECT a.username, a.nickname, a.email, a.mobile,a.`status`,b.* ' \
              'FROM {table} AS a LEFT JOIN tb_user_info AS b ON a.id=b.id WHERE a.id=%s'.format(table=self.__tablename__)
        ret = self.select(sql, uuid, one=True)

        if ret: return self.respData(STATUS.OK, data=ret)

        return self.respData(STATUS.DATA_NULL_ERR, error='id={id}的用户不存在'.format(id=uuid))

    def edit(self, user_data, user_info_data, uuid, up):

        user_ret = self.update(user_data, uuid)

        user_info_ret = self.update(user_info_data, uuid, table='tb_user_info')
        self.__tablename__ = 'tb_user'

        if user_ret or user_info_ret:
            if up: up.save()
            return self.respData(error='用户信息更新成功~')
        return self.respData(STATUS.DATA_NOT_CHANGE_ERR, error='用户信息更新失败~')

user_model = User()
auth_group_model = AuthGroup()
auth_rule_model = AuthRule()