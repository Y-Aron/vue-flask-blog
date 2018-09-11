from config import STATUS
from model import Model
from utils import parents, logger

class Archive(Model):
    __tablename__ = 'tb_archive'

    def create(self, data, up):
        sql = 'select count(*) AS total from {table} ' \
              'WHERE type_id=%s AND uid=%s AND `title`=%s'.format(table=self.__tablename__)
        ret = self.select(sql, data['type_id'], data['uid'], data['title'], one=True)

        if ret['total']:
            return self.respData(STATUS.DATA_EXISTS_ERR, error='该文章已存在哦~')

        ret = self.join_extend_field_insert(insert_data=data)
        if ret:
            if up: up.save()
            return self.respData(STATUS.OK, error='文章创建成功~')
        return self.respData(STATUS.DATA_CREATE_ERR, '文章创建失败了哦~')

    def fetchList(self, start, length):
        sql = 'SELECT a.id, a.type_id, a.title, a.flag, a.`status`, b.typename, ' \
              'c.username, c.id as uid, a.click, a.create_time, a.edit_time' \
              ' from (tb_archive as a LEFT JOIN tb_arctype as b ON a.type_id=b.id) ' \
              'LEFT JOIN tb_user as c ON a.uid=c.id LIMIT %s,%s;'
        ret = self.paging(sql, start, length)

        return self.respData(STATUS.OK, data=ret)

    def remove(self, id):
        ret = self.delete(id)

        if ret:
            return self.respData(STATUS.OK, error='删除文章成功~')
        return self.respData(STATUS.DARA_DELETE_ERR, error='文章删除失败~')

    def edit(self, data, up, uuid):
        ret = self.update(data, uuid)

        if ret:
            # 缩略图保存
            if up: up.save()
            return self.respData(STATUS.OK, error='文章信息修改成功~')
        return self.respData(STATUS.DATA_NOT_CHANGE_ERR, error='文章信息修改失败~')

    def fetchData(self, uuid):
        sql = 'select * from {table} WHERE `id`=%s'.format(table=self.__tablename__)
        ret = self.select(sql, uuid, one=True)
        if ret:
            return self.respData(STATUS.OK, data=ret)
        else:
            return self.respData(STATUS.DATA_NULL_ERR, error='id={id}的数据不存在哦~'.format(id=uuid))

    def fetchDataByTid(self, type_id):
        if type_id == 0:
            sql = 'select * from {table}'.format(table=self.__tablename__)
            ret = self.select(sql)
        else:
            sql = 'SELECT * from {table} WHERE type_id IN ' \
                  '( SELECT id from tb_arctype WHERE `pid`=%s ' \
                  'UNION SELECT id from tb_arctype WHERE id=%s) ORDER BY `flag` DESC'.format(table=self.__tablename__)
            ret = self.select(sql, type_id, type_id)
        return self.respData(STATUS.OK, data=ret)

    def fetchDataById(self, uuid):
        resp_data = dict(
            pre_data={},
            current_data={},
            next_data={}
        )
        sql = 'select * from {table} WHERE `id`=%s'.format(table=self.__tablename__)
        current_data = self.select(sql, uuid, one=True)

        if current_data:

            pre_sql = 'select `id`,`type_id`, `title` from {table} WHERE ' \
                      'id = (SELECT MAX(id) from tb_archive WHERE id < %s)'.format(table=self.__tablename__)
            next_sql = 'select `id`, `type_id`, `title` from {table} ' \
                       'WHERE id = (SELECT MIN(id) from tb_archive WHERE id > %s)'.format(table=self.__tablename__)

            resp_data['pre_data'] = self.select(pre_sql, uuid, one=True)

            resp_data['next_data'] = self.select(next_sql, uuid, one=True)

            if current_data['content']:
                import markdown
                current_data['content'] = markdown.markdown(current_data['content'],['extra'])
            resp_data['current_data'] = current_data
            # 更新浏览 + 1
            sql = 'update {table} set `views`=`views`+1 WHERE `id`=%s'.format(table=self.__tablename__)
            self.execute(sql, uuid)

        return self.respData(STATUS.OK, data=resp_data)

    def refreshLike(self, uuid):
        sql = 'update {table} set `click`=`click`+1 WHERE `id`=%s'.format(table=self.__tablename__)
        ret = self.execute(sql, uuid)
        if ret:
            return self.respData(STATUS.OK)
        return self.respData(STATUS.DATA_NOT_CHANGE_ERR, error='点赞失败~')

    def fetchHotList(self):
        start = 0
        length = 5
        sql = 'SELECT `id`, `title`,`type_id` FROM {table} ORDER BY views DESC, click DESC LIMIT %s,%s'.format(table=self.__tablename__)
        ret = self.select(sql, start, length)
        return ret


archive_model = Archive()
