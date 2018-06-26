# coding=utf-8
from import_file import *

current_time=time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
pid = os.getpid()

'''
if system() == 'Windows':
    log_path = r"C:\rms\%s_%s"%(current_time, pid)
else:
    log_path = "/var/log/rms/%s_%s"%(current_time, pid)
'''

if system() == 'Windows':
    log_path = r"C:\rms\tornado" 
else:
    log_path = "/var/log/rms/tornado" 
    
FILE = dict(
    log_path=log_path, # 末尾自动添加 @端口号.txt_日期
    when="D", # 以什么单位分割文件
    interval=1, # 以上面的时间单位，隔几个单位分割文件
    backupCount=30, # 保留多少历史记录文件
    fmt="%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s",
)

def init(console_handler=True, file_handler=True, log_path=FILE['log_path'], base_level="INFO"):
    try:
        if system() == 'Windows':
            os.makedirs(r"C:\rms")
        else:
            os.makedirs(r"/var/log/rms")
    except:
        pass
    
    logger = logging.getLogger()
    logger.setLevel(base_level)
    # 配置控制台输出
    if console_handler:
        channel_console = logging.StreamHandler()
        channel_console.setFormatter(tornado.log.LogFormatter())
        logger.addHandler(channel_console)
    # 配置文件输出
    if file_handler:
        if not log_path:
            log_path = FILE['log_path']
        log_path = log_path+".log"
        formatter = logging.Formatter(FILE['fmt']);
        channel_file = logging.handlers.TimedRotatingFileHandler(
            filename=log_path,
            when=FILE['when'],
            interval=FILE['interval'],
            backupCount=FILE['backupCount'])
        channel_file.setFormatter(formatter)
        logger.addHandler(channel_file)