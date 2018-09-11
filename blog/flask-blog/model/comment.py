
from model import Model
from config import STATUS
from utils import make_tree, logger

class Comment(Model):

    __tablename__ = 'tb_comment'
    def create(self, data, putData=None, isAdmin=False):

        if data['type'] == 0: del data['type']
        if isAdmin: data['isAdmin'] = 1
        if data['content']:
            ret = self.join_extend_field_insert(data)
            if ret: return self.respData(error="评论成功~ 请等待管理员审核~")
            return self.respData(STATUS.DATA_CREATE_ERR, error="评论失败~")
        elif putData:
            uuid = putData['id']
            del putData['id']
            ret = self.update(putData, uuid)
            if ret: return self.respData(STATUS.OK, error='评论数据修改成功~')
            return self.respData(STATUS.DATA_NOT_CHANGE_ERR, error='评论数据没有改变哦~')

    def fetchTreeList(self, type_id):
        data = dict(
            treeList=[],
            user_total=0,
        )
        if type_id:
            # 文章评论
            sql = 'select * from {table} WHERE `status`=1 AND `type`=%s'.format(
                table=self.__tablename__,
            )
            ret = self.select(sql, type_id)
            total_sql = 'SELECT count(distinct username) as total, count(*) AS comment_total from {table} WHERE `type`=%s'\
                .format(table=self.__tablename__)
            total_ret = self.select(total_sql, type_id, one=True)

        else:
            # 留言板
            sql = 'select * from {table} WHERE `status`=1 AND `type` is NULL '.format(
                table=self.__tablename__,
            )
            ret = self.select(sql)
            total_sql = 'SELECT count(distinct username) as total, count(*) AS comment_total from {table} WHERE `type` is NULL '\
                .format(table=self.__tablename__)
            total_ret = self.select(total_sql, one=True)

        if ret: data['treeList'] = make_tree(ret)

        if total_ret:
            data['user_total'] = total_ret['total']
            data['comment_total'] = total_ret['comment_total']

        return self.respData(data=data)

    def fetchList(self, start, length, guestbook = False):
        if not guestbook:
            typeVal = 'is NOT NULL'
        else:
            typeVal = 'is NULL'

        sql = 'SELECT a.*, b.title, c.username as reply_target from ({table} AS a LEFT JOIN tb_archive AS b ON a.type=b.id ) ' \
              'LEFT JOIN {table} as c ON a.pid=c.id WHERE a.`type` {typeVal} LIMIT %s,%s'.format(
            table=self.__tablename__,
            typeVal = typeVal
        )
        total_sql = 'SELECT count(*) as total FROM {table} WHERE `type` {typeVal}'.format(
            table=self.__tablename__,
            typeVal = typeVal
        )
        ret = self.paging(sql, start, length, total_sql)

        if ret and 'list' in ret:
            for vol in ret['list']:
                if vol['status'] == 1: vol['status'] = True
                else: vol['status'] = False
            return self.respData(data=ret)

        return self.respData(STATUS.DATA_NULL_ERR, error='不存在任何留言/评论~')

    def fetchData(self, uuid):
        sql = 'SELECT a.*, b.title, c.username as reply_target from ({table} AS a LEFT JOIN tb_archive AS b ON a.type=b.id ) ' \
              'LEFT JOIN {table} as c ON a.pid=c.id WHERE a.`id`=%s '.format(
            table=self.__tablename__,
        )
        ret = self.select(sql, uuid, one=True)
        if ret: return self.respData(data=ret)
        return self.respData(STATUS.DATA_NULL_ERR, error='id={id}的评论数据不存在~'.format(id=uuid))

    def fetchCount(self):
        sql = 'select count(*) as comment_total from {table}'.format(table=self.__tablename__)
        ret = self.select(sql, one=True)
        return ret['comment_total']

    def editStatus(self, uuid, status):
        ret = self.update(dict(status=status), uuid)
        if ret: return self.respData(error='更新留言状态成功~')
        return self.respData(STATUS.DATA_NOT_CHANGE_ERR, error='留言状态更新失败~')

    def remove(self, uuid):
        ret = self.delete(uuid)
        if ret: return self.respData(error='数据删除成功~')
        return self.respData(STATUS.DARA_DELETE_ERR, error='数据删除失败')


comment_model = Comment()