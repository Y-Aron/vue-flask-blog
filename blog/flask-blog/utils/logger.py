
def __init_logger():
    import logging
    import os.path, time
    from config import BASE_DIR
    # 1. 创建一个logger
    _logger = logging.getLogger()
    _logger.setLevel(logging.DEBUG)
    # 2. 创建一个handler 用于输出在控制台与写入文件
    rq = time.strftime('%Y%m%d', time.localtime(time.time()))
    # 初始化日志文件目录
    log_dirs = os.path.join(BASE_DIR,'logs')
    if not os.path.exists(log_dirs): os.makedirs(log_dirs)
    # error log file
    error_logfile = os.path.join(log_dirs, 'error-'+rq+'.log')
    efh = logging.FileHandler(error_logfile)
    efh.setLevel(level=logging.ERROR)
    # info log file
    info_logfile = os.path.join(log_dirs, 'info-'+rq+'.log')
    ifh = logging.FileHandler(info_logfile)
    ifh.setLevel(level=logging.INFO)
    # 输出到控制台
    ch = logging.StreamHandler()
    # 3. 定义handler的输出格式
    '''
        %(name)s：   打印Logger的名字
        %(levelno)s: 打印日志级别的数值
        %(levelname)s: 打印日志级别名称
        %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s: 打印当前执行程序的文件名
        %(funcName)s: 打印日志的当前函数
        %(lineno)d:  打印日志的当前行号
        %(asctime)s: 打印日志的时间
        %(thread)d:  打印线程ID
        %(threadName)s: 打印线程名称
        %(process)d: 打印进程ID
        %(message)s: 打印日志信息
    '''
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] "
                                  "- %(levelname)s: %(message)s")
    efh.setFormatter(formatter)
    ch.setFormatter(formatter)
    ifh.setFormatter(formatter)
    # 4. 将logger添加到handler里面
    _logger.addHandler(efh)
    _logger.addHandler(ifh)
    _logger.addHandler(ch)
    return _logger

logger = __init_logger()