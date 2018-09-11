import pymysql, contextlib
from utils import logger
import time

# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def make_cursor():
    from config import MySQL
    conn = pymysql.connect(**MySQL)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    except Exception as e:
        logger.debug('MYSQL Exception ~')
        logger.error(e)
    finally:
        conn.commit()
        cursor.close()
        conn.close()


class Handler(object):

    @staticmethod
    def get_time(timestamp):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    def handler(self, obj: dict):
        if 'create_time' in obj:
            obj['create_time'] = self.get_time(obj['create_time'])
        if 'edit_time' in obj:
            obj['edit_time'] = self.get_time(obj['edit_time'])

        return obj
    def handler_data(self, data):
        if isinstance(data, dict):
            return self.handler(data)
        elif isinstance(data, list):
            ret = []
            for vol in data:
                ret.append(self.handler(vol))
            return ret
        return data


class MySQL(object):

    __tablename__:str = None

    @staticmethod
    def execute(sql, *args):
        row = 0
        with make_cursor() as cursor:
            row = cursor.execute(sql,args)
        return row


    def replace(self, replace_data=None, table:str=None):
        if not replace_data: raise Exception('Please enter a list of the dict type data ')
        self.set_tableName(table)

        sql = 'REPLACE INTO {table} SET {replace_data}'

        dict_data = replace_data
        if isinstance(replace_data, list):
            dict_data = replace_data[0]

        replace_sql = self.__make_set_sql(dict_data, suffix=', ')

        sql = sql.format(table=self.__tablename__, replace_data=replace_sql)

        row = 0

        with make_cursor() as cursor:
            real_data = []
            if isinstance(replace_data, dict):
                real_data.extend(replace_data.values())
                row = cursor.execute(sql, real_data)

            if isinstance(replace_data, list):
                for value in replace_data:
                    real_data.append(tuple(value.values()))
                row = cursor.executemany(sql, real_data)

            logger.info('Successful replace {row} data'.format(row=row))
            return cursor.lastrowid

    def paging(self, sql, start, length, total_sql:str=None):

        data_list = self.select(sql, start, length)
        if total_sql is None:
            total_sql = 'select count(*) AS total from {table}'.format(table=self.__tablename__)

        total = self.select(total_sql, one=True)

        data = dict(
            list = data_list,
            total = total['total']
        )
        return data

    @staticmethod
    def select(sql, *args, one:bool=False):
        data = []
        with make_cursor() as cursor:
            cursor.execute(sql,args)
            if one: data = cursor.fetchone()
            else: data = cursor.fetchall()
            handler = Handler()
            data = handler.handler_data(data)
        return data

    @staticmethod
    def callProcedure(name, IN:dict=None, OUT:dict=None):
        """
        :param name: this is procedure name
        :param IN: this is input params
        :param OUT: this is output params
        :return: out data
        """
        # 查询输出参数的值
        def fetchOUT(cursor, pre = 0):
            if not OUT: return {}
            if IN: pre = len(IN)
            sql = 'select '
            # 查询需要返回的值
            for index, key in enumerate(OUT):
                if index != len(OUT) - 1:
                    sql += '@_{name}_{index} as {key},'.format(name=name, index=pre + index, key=key)
                else:
                    sql += '@_{name}_{index} as {key}'.format(name=name, index=pre + index, key=key)
            cursor.execute(sql)
            return cursor.fetchone()

        # 获取所有的结果集 并保存到列表中
        def fetchALL(cursor):
            ret = cursor.fetchall()
            if not ret: return []
            while cursor.nextset():
                ret.extend(cursor.fetchall())
            return ret
        res1, res2 = None, None
        with make_cursor() as cursor:
            args = dict()
            # 存储过程带输入参数
            if IN: args.update(IN)
            # 存储过程带输出参数
            if OUT: args.update(OUT)
            cursor.callproc(procname=name, args=args.values())
            logger.info('Execute the stored procedure !')
            res1, res2 = fetchALL(cursor), fetchOUT(cursor)

        return res1, res2

    """
    :param pk: 查询主键 或查询条件 type: int/str, tuple/list, dict
    :param pk_name: 表的主键字段
    :param table: 查询的表名 默认为 __tablename__
    :return: 受影响行数
    """
    def delete(self, pk, pk_name:str='id', table:str=None):

        if not pk: raise Exception("The primary key can't be empty")

        self.set_tableName(table)

        sql = 'DELETE FROM {table} WHERE {condition} '

        condition_sql, real_data = self.__make_condition_or_data(pk, pk_name)

        sql = sql.format(table=self.__tablename__, condition=condition_sql)
        row = 0
        with make_cursor() as cursor:
            row = cursor.execute(sql, real_data)
        logger.info('Deleted successfully {row} data'.format(row=row))
        return row

    def __make_condition_or_data(self, pk, pk_name):
        real_data, condition_sql = [], ''

        if isinstance(pk, dict):
            condition_sql = self.__make_set_sql(pk, suffix=' AND ')
            for key in pk:
                val = pk[key]
                if isinstance(val, tuple) or isinstance(val, list):
                    real_data.extend(val)
                    continue
                real_data.append(pk[key])

        if isinstance(pk, tuple) or isinstance(pk, list):
            condition_sql = self.__make_list_sql(pk_name, pk)
            real_data.extend(pk)

        if isinstance(pk, int) or isinstance(pk, str):
            condition_sql = self.__make_str_sql(pk_name, pk)
            real_data.append(pk)

        return condition_sql, real_data

    """
    :param update: 需要更新的值 -> type:dict
    :param condition: 更新条件 ->  type: dict, int/str, tuple/list
    :param pk_name: 表的主键字段名
    :param table: 查询的表名 默认为 __tablename__
    :return: 受影响行数
    """
    def update(self, update:dict, condition=None, pk_name:str='id', table:str=None):

        if not condition: raise Exception("The condition key can't be empty")

        self.set_tableName(table)

        sql = 'UPDATE {table} SET {update} WHERE {condition}'

        update_sql = self.__make_set_sql(update, suffix=', ')

        real_data = []

        real_data.extend(update.values())

        condition_sql, condition_data = self.__make_condition_or_data(condition, pk_name)

        real_data.extend(condition_data)

        sql = sql.format(table=self.__tablename__, update=update_sql, condition=condition_sql)
        row = 0
        with make_cursor() as cursor:
            row = cursor.execute(sql, real_data)

        logger.info('Data updated successfully {row}'.format(row=row))
        return row

    @staticmethod
    def cut_suffix(sql:str='', suffix:str=''):
        last_comma = sql.rfind(suffix)
        ret_sql = sql[:last_comma]
        return ret_sql

    def __make_list_sql(self, key, val, suffix:str=''):

        if isinstance(val, tuple) or isinstance(val, list):
            val_sql = '%s, ' * len(val)
            val_sql = self.cut_suffix(val_sql, ',')

            sql = '{table}.`{key}` IN ({val}) {suffix}'\
                .format(table=self.__tablename__, key=key, val=val_sql, suffix=suffix)
            return sql
        raise Exception('Please enter a list of the tuple type data ~')

    def __make_str_sql(self, key, val, suffix:str=''):

        if isinstance(val, int) or isinstance(val, str):
            sql = '{table}.`{key}`=%s {suffix}' \
                .format(table=self.__tablename__, key=key, suffix=suffix)
            return sql
        raise Exception('Please enter a list of the tuple type data ~')

    def __make_set_sql(self, data, suffix:str=''):
        if not data: raise Exception('The data can not be empty ')
        sql = ''
        for key in data:
            val = data[key]
            if isinstance(val, tuple) or isinstance(val, list):
                sql += self.__make_list_sql(key, val, suffix)
                continue
            if isinstance(val, int) or isinstance(val, str):
                sql += self.__make_str_sql(key, val, suffix)
                continue

        return self.cut_suffix(sql, suffix)

    # 设置表名
    def set_tableName(self, table):
        if table:
            self.__tablename__ = table

        if not self.__tablename__:
            raise Exception('__tablename_ cannot be empty ')

    """
    :param insert_data: 插入的数据 -> type: dict/list
    :param table: 表名 default = self.__tablename__
    :return: 自增ID的值
    """
    def insert(self, insert_data=None, table:str=None):

        if not insert_data: raise Exception('Please enter a list of the dict type data ')

        self.set_tableName(table)

        sql = 'INSERT INTO {table} SET {insert_data}'

        dict_data = insert_data
        if isinstance(insert_data, list):
            dict_data = insert_data[0]

        insert_sql = self.__make_set_sql(dict_data, suffix=', ')

        sql = sql.format(table=self.__tablename__, insert_data=insert_sql)

        row = 0
        with make_cursor() as cursor:
            real_data = []
            if isinstance(insert_data, dict):
                real_data.extend(insert_data.values())
                row = cursor.execute(sql, real_data)

            if isinstance(insert_data, list):
                for value in insert_data:
                    real_data.append(tuple(value.values()))
                row = cursor.executemany(sql, real_data)

            logger.info('Successful insertion {row} data'.format(row=row))
            return cursor.lastrowid

    # 带创建时间, 编辑时间, 或其他公共字段的 sql 增加
    def join_extend_field_insert(self, insert_data=None,
                                 table:str=None, public_field:dict=None):

        public_field = public_field or dict()

        now_time = int(time.time())
        public_field['create_time'] = now_time
        public_field['edit_time'] = now_time

        insert_data = self.extend_field(insert_data, public_field)
        return self.insert(insert_data, table)


    def join_extend_field_update(self, update_data=None, condition=None, pk_name:str='id',
                                 table:str=None, public_field:dict=None):
        public_field = public_field or dict()

        now_time = int(time.time())
        public_field['edit_time'] = now_time
        update_data = self.extend_field(update_data, public_field)

        return self.update(update_data, condition, pk_name, table)

    # 带创建时间, 编辑时间, 或其他公共字段的 sql 增加
    def join_extend_field_replace(self, replace_data=None,
                                 table: str = None, public_field: dict = None):
        public_field = public_field or dict()

        now_time = int(time.time())
        public_field['create_time'] = now_time
        public_field['edit_time'] = now_time

        replace_data = self.extend_field(replace_data, public_field)
        return self.replace(replace_data, table)


    @staticmethod
    def extend_field(data, public_field):

        def extend_field_one(dict_data):
            for key in public_field:
                if key not in dict_data:
                    dict_data[key] = public_field[key]

        if isinstance(data, list):
            for vol in data:
                extend_field_one(vol)

        if isinstance(data, dict):
            extend_field_one(data)
        return data

if __name__ == '__main__':
    model = MySQL()
    sql = 'select table_name,table_rows from information_schema.tables where TABLE_SCHEMA = %s order by table_rows desc; '
    ret = model.select(sql, 'learn')
    import pprint
    pprint.pprint(ret)

    # d = dict(
    #     rule_id = 8,
    #     group_id = 1
    # )
    # l = [d,d]
    # ret = model.join_extend_field_replace(l, table='tb_auth_group_rule')
    # logger.debug(ret)

    # ------------------- 增加
    # d = dict(
    #     name = 'admin',
    #     password = None
    # )
    # l = [
    #     d,d
    # ]
    # ret = model.join_extend_field_insert(d)
    # logger.debug(ret)
    # ------------------- 修改
    # update_data = dict(
    #     name = 'update',
    #     password = 'admin'
    # )
    # condition_data = dict(
    #     id = [39,40,41],
    #
    # )
    # l = [36,37,38]
    # ret = model.join_extend_field_update(update_data, condition_data)
    # logger.debug(ret)
    #  ------------------- 删除
    # d = dict(
    #     id=(10, 2, 3),
    #     name = 'update'
    # )
    # id = (7,8,9)
    # ret = model.delete(id)





