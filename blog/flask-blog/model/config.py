from model import Model
from config import STATUS
from utils import logger


class Config(Model):
    __tablename__ = 'tb_config'

    def fetchList(self, start, length):
        sql = 'select * from {table} LIMIT %s, %s'.format(table=self.__tablename__)
        ret = self.paging(sql, start, length)
        return self.respData(data=ret)

    def remove(self, uuid):
        ret = self.delete(uuid)

        if ret:
            return self.respData(STATUS.OK, error='删除配置字段~')
        return self.respData(STATUS.DARA_DELETE_ERR, error='配置删除失败~')

    def fetchData(self, uuid):
        sql = 'select * from {table} WHERE `id`=%s'.format(table=self.__tablename__)
        ret = self.select(sql, uuid, one=True)
        if ret: return self.respData(STATUS.OK, data=ret)
        return self.respData(STATUS.DATA_NULL_ERR, error='id={id}的配置字段不存在~'.format(id=uuid))

    def create(self, data):
        ret = self.insert(data)
        if ret: return self.respData(STATUS.OK, error='配置字段添加成功~')
        return self.respData(STATUS.DATA_NOT_CHANGE_ERR, error='配置字段添加失败~')

    def edit(self, uuid, data):
        ret = self.update(data, uuid)
        if ret: return self.respData(STATUS.OK, error='配置字段更新成功~')
        return self.respData(STATUS.DATA_NOT_CHANGE_ERR, '配置字段更新失败~')

    def fetchConfig(self, type:str='sys'):
        sql = 'select * from {table} WHERE `type`=%s'.format(table=self.__tablename__)
        ret = self.select(sql, type)
        data = dict()
        if ret:
            for vol in ret:
                data[vol['key']] = vol['value']
        return data

config_model = Config()