from model import Model
from config import STATUS, MySQL, BACKUP_PATH
from utils import backup, recovery, get_file_list, logger
import os, time

class LoginLog(Model):
    __tablename__ = 'tb_login_log'

    def create(self, data):

        self.join_extend_field_insert(data)

    def fetchList(self, start, length):
        sql = 'SELECT a.*, b.username, b.nickname FROM {table} AS a ' \
              'LEFT JOIN tb_user AS b ON a.uid=b.id ORDER BY create_time DESC LIMIT %s, %s'.format(table=self.__tablename__)

        ret = self.paging(sql, start, length)
        if ret:
            return self.respData(STATUS.OK, data=ret)

        return self.respData(STATUS.DATA_NULL_ERR, error='用户数据不存在~')

    def remove(self, uuid):
        ret = self.delete(uuid)
        if ret: return self.respData(error='登陆日志删除成功~')
        return self.respData(STATUS.DARA_DELETE_ERR, error='登陆日志删除失败!')

class AdminIndex(Model):
    def fetchData(self):
        proname = 'init_index'
        IN = dict(
            first = 0,
            end = 7
        )
        OUT = dict(
            user_total = 0,
            article_total = 0,
            user_near_num = 0,
            comment_near_num = 0
        )
        resultSet, ret = self.callProcedure(proname, IN, OUT)
        ret['login_log_list'] = resultSet
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        ret['current_time'] = current_time
        return self.respData(data=ret)

class DataBase(Model):

    def fetchData(self):
        from config import MySQL
        sql = 'select TABLE_NAME,TABLE_ROWS, `ENGINE`, UNIX_TIMESTAMP(CREATE_TIME) as create_time from information_schema.tables where TABLE_SCHEMA = %s order by table_rows desc; '
        ret = self.select(sql, MySQL['db'])
        if ret: return self.respData(data={'list':ret})
        return self.respData(STATUS.DATA_NULL_ERR, error='当前数据库不存在任何表~')


    def dbBackup(self, table_list):
        backup(user=MySQL['user'], passwd=MySQL['passwd'],
               host=MySQL['host'], port=MySQL['port'], dbname=MySQL['db'], table_list=table_list)

        return self.respData(STATUS.OK, error='数据库备份成功~')

    def dbRecovery(self, timestamp):
        file_path = get_file_list(BACKUP_PATH)
        sql_path = None
        for path in file_path:
            if os.path.getctime(path) == float(timestamp):
                sql_path = path
                break
        if sql_path is None: return self.respData(STATUS.DATA_NULL_ERR, error='备份文件不存在~')

        recovery(user=MySQL['user'], passwd=MySQL['passwd'],
               host=MySQL['host'], port=MySQL['port'], dbname=MySQL['db'], sql_path=sql_path)
        return self.respData(STATUS.OK, error='数据库还原成功~')

    def fetchBackup(self):
        data = []
        file_path = get_file_list(BACKUP_PATH)
        for path in file_path:
            filename = os.path.basename(path)
            filesize = '{size}.KB'.format(size=round(os.path.getsize(path)/float(1024), 2))
            timestamp = os.path.getctime(path)
            filectime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
            data.append(dict(
                filename = filename,
                filesize = filesize,
                filectime = filectime,
                uuid = timestamp
            ))
        return self.respData(data={'list':data})

    @staticmethod
    def fetchBackupFile(uuid):
        file_path = get_file_list(BACKUP_PATH)
        for path in file_path:
            timestamp = os.path.getctime(path)
            if timestamp == float(uuid):
                return path, os.path.basename(path)

    def removeBackup(self, timestamp):
        file_path = get_file_list(BACKUP_PATH)
        backup_file_path = None
        for path in file_path:
            if os.path.getctime(path) ==  float(timestamp):
                backup_file_path = path
                break
        if backup_file_path is None: return self.respData(STATUS.DATA_NULL_ERR, error='备份文件不存在~')

        dirname = os.path.dirname(backup_file_path)
        os.remove(backup_file_path)
        if not os.listdir(dirname):
            os.rmdir(dirname)
        return self.respData(error='已成功删除备份文件~')

login_log_model = LoginLog()
database_model = DataBase()
admin_model = AdminIndex()