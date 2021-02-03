"""
============================
Author:柠檬班-木森
Time:2019/8/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
设置日志输出渠道
"""

import logging
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler

# 第一步：创建日志收集器
mylog = logging.getLogger('mylog')
mylog.setLevel('DEBUG')

# 第二步：设置输出渠道
# 1、输出到控制台
sh = logging.StreamHandler()
sh.setLevel('INFO')

# 2、输出到文件
# fh = logging.FileHandler(filename='my.log', mode='a', encoding='utf8')
# 创建一个按文件大小进行轮转的输出渠道（文件）
# 8bit = 1bytes(字节)   1024字节 = 1kb  1024kb=1mb  1024MB = 1GB
# fh = RotatingFileHandler(filename='my.log', mode='a', encoding='utf8',maxBytes=1024*1024*20,backupCount=3)
# 按时间间隔轮转进行轮转的输出渠道（文件）
fh = TimedRotatingFileHandler(filename='my.log',encoding='utf8',when='D',interval=1,backupCount=7)


fh.setLevel('DEBUG')

# 第三步：将渠道添加到日志收集器中
mylog.addHandler(sh)
mylog.addHandler(fh)

# 设置日志输出格式
formatter = logging.Formatter('%(asctime)s-【%(filename)s-->line:%(lineno)d】-%(levelname)s:%(message)s')

#5.设置handler的log信息格式
fh.setFormatter(formatter)
sh.setFormatter(formatter)



mylog.debug('---这个是debug等级的日志,一般用于调试')
mylog.info('---这个是info等级的日志，常规信息的输出')
mylog.warning('---这个是warning等级的日志，警告信息')
mylog.error('---这个是error等级的日志，错误信息')
mylog.critical('---这个是critical等级的日志，严重的错误，程序要崩溃')
