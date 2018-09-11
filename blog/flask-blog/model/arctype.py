from model import Model
from utils import  getTree, logger, make_tree, parents
from config import STATUS

class ArcTypeMod(Model):
    __tablename__ = 'tb_arctype_mod'

    # 创建文章分类模型
    def create(self, data):
        sql = 'select count(*) as total from {table} WHERE {table}.`name`=%s'.format(table=self.__tablename__)
        ret = self.select(sql, data['name'], one=True)
        if ret['total']:
            return self.respData(STATUS.DATA_EXISTS_ERR, error='该文章分类模型已存在~')

        ret = self.join_extend_field_insert(data)
        if ret:
            return self.respData(STATUS.OK, error='文章分类模型创建成功~')

        return self.respData(STATUS.DATA_CREATE_ERR, error='文章分类模型创建失败 !')

    def edit(self, data, mid):
        ret = self.update(data, mid)
        if ret: return self.respData(STATUS.OK, error='文章分类模型更新成功~')
        return self.respData(STATUS.DATA_NOT_CHANGE_ERR, error='文章分类模型数据没变哦 ~')

    def fetchList(self, start, length):

        sql = 'select * from {table} ORDER BY `sorts` LIMIT %s,%s'.format(table=self.__tablename__)

        ret = self.paging(sql, start, length)
        if ret:
            return self.respData(STATUS.OK, data=ret)

        return self.respData(STATUS.DATA_NULL_ERR, error='文章分类模型数据不存在~')

    def remove(self, pk):
        ret = self.delete(pk)
        if ret: return self.respData(STATUS.OK, error='文章分类模型删除成功~')

        return self.respData(STATUS.DARA_DELETE_ERR, error='文章分类模型删除失败~')

    def fetchData(self, mid):
        sql = 'select * from {table} WHERE {table}.`id`=%s'.format(table=self.__tablename__)
        ret = self.select(sql, mid, one=True)
        if ret: return self.respData(STATUS.OK, data=ret)

        return self.respData(STATUS.DATA_NULL_ERR, error='id={} 的文章分类模型不存在~'.format(mid))

    def fetchOptions(self):
        sql = 'select `id` as value, `name` as text from {table} ORDER BY sorts'.format(table=self.__tablename__)
        ret = self.select(sql)
        if ret:
            return self.respData(STATUS.OK, data=ret)
        else:
            return self.respData(STATUS.DATA_NULL_ERR, error='没有任何文章模型哦~')


class ArcType(Model):
    __tablename__ = 'tb_arctype'

    def fetchList(self, start, length):
        sql = 'SELECT a.id, a.model_id, typename, a.pid, b.`name` as modname, dirs,a.`status`,a.sorts ' \
              'from tb_arctype as a LEFT JOIN tb_arctype_mod as b ON a.model_id=b.id ORDER BY a.sorts LIMIT %s,%s '
        ret = self.paging(sql, start, length)
        ret['list'] = getTree(ret['list'], c_name='id', t_name='typename')

        return self.respData(STATUS.OK, data=ret)

    def fetchOptions(self):
        sql = 'select id as value, typename as text, pid from {table}'.format(table=self.__tablename__)
        ret = self.select(sql)

        tree_ret = getTree(ret)
        if ret:
            return self.respData(STATUS.OK, data=tree_ret)
        return self.respData(STATUS.DATA_NULL_ERR, error='没有分类数据哦~')

    def fetchData(self, uuid):
        sql = 'select * from {table} WHERE `id`=%s'.format(table=self.__tablename__)
        ret = self.select(sql, uuid, one=True)
        if ret:
            return self.respData(STATUS.OK, data=ret)
        else:
            return self.respData(STATUS.DATA_NULL_ERR, error='id={id}的数据不存在哦~'.format(id=uuid))

    def fetchArctype(self, uuid):
        sql = 'select * from {table} WHERE `id`=%s'.format(table=self.__tablename__)
        ret = self.select(sql, uuid, one=True)
        if ret:
            import markdown
            ret['description'] = markdown.markdown(ret['description'], ['extra'])
        return self.respData(STATUS.OK, data=ret)


    def call_edit_arctype(self, data):

        procname = 'edit_arctype'
        OUT = dict( status_code = 0)
        resultSet, ret = self.callProcedure(procname, data, OUT)
        return ret

    def create(self, data, up):
        ret = self.call_edit_arctype(data)
        if not ret: return self.respData(STATUS.DB_ERR, error='数据库异常~')

        if ret['status_code'] == STATUS.OK:
            # 缩略图保存
            if up: up.save()
            return self.respData(STATUS.OK, error='分类创建成功~')

        if ret['status_code'] == STATUS.DATA_EXISTS_ERR:
            return self.respData(STATUS.DATA_EXISTS_ERR, error='该分类已存在哦~')

        if ret['status_code'] == STATUS.DATA_CREATE_ERR:
            return self.respData(STATUS.DATA_CREATE_ERR, error='分类创建失败~')

    def edit(self, data, up):
        ret = self.call_edit_arctype(data)
        if not ret: return self.respData(STATUS.DB_ERR, error='数据库异常~')
        if ret['status_code'] == STATUS.OK:
            # 缩略图保存
            if up: up.save()
            return self.respData(STATUS.OK, error='分类信息修改成功~')

        if ret['status_code'] == STATUS.DATA_EXISTS_ERR:
            return self.respData(STATUS.DATA_EXISTS_ERR, error='该分类已存在哦~')

        if ret['status_code'] == STATUS.DATA_NOT_CHANGE_ERR:
            return self.respData(STATUS.DATA_EXISTS_ERR, error='分类信息一样哦~')

    def remove(self, uuid):
        ret = self.delete(uuid)

        if ret:
            self.update({'pid':0}, {'pid':uuid})
            return self.respData(STATUS.OK, error='删除分类成功~')
        return self.respData(STATUS.DARA_DELETE_ERR)

    def fetchTreeList(self):
        sql = 'select `id`, `model_id`, `pid`, `typename`,`dirs`, `icon` from {table}'.format(table=self.__tablename__)
        ret = self.select(sql)

        if ret:
            return self.respData(STATUS.OK, data=make_tree(ret))
        return self.respData(STATUS.DATA_NULL_ERR, error='分类数据不存在~')

    def fetchParents(self, uuid):
        sql = 'select `id`, `typename`, `pid` from {table}'.format(table=self.__tablename__)
        ret = self.select(sql)
        type_parents = []
        if ret:
            type_parents = parents(ret, uuid)

        return self.respData(STATUS.OK, data=type_parents)

    def fetchHotList(self):
        start = 0
        length = 5
        sql = 'SELECT b.typename, b.id, b.dirs, b.model_id, count(*) AS archive_num FROM tb_archive AS a ' \
              'LEFT JOIN tb_arctype AS b ON a.type_id=b.id GROUP BY type_id ' \
              'ORDER BY SUM(a.views) DESC, SUM(a.click) desc LIMIT %s,%s'
        ret = self.select(sql, start, length)
        return ret


arctype_model = ArcType()
arctype_mod_model = ArcTypeMod()
