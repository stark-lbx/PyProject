# logging
import logging
from logging import StreamHandler
from logging.config import fileConfig

# 日志级别-输出设置日志级别往上的错误(默认是WARNING)
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0

# 日志设置 level-等级 filename-日志输出文件
# logging.basicConfig(
#     format="%(asctime)s | %(levelname)s | %(filename)s | %(lineno)s | %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     level=logging.DEBUG,
#     filename="applog.log"
# )
#
# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")  # logging.warn("This is a warning log")
# logging.error("This is a error log")
# logging.fatal("This is a fatal log")
# logging.critical("This is a critical log")

##################################################################################################################################
# logging 日志库的高级应用

# 格式化器
# formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(filename)s | %(lineno)s | %(message)s")

# 记录器
# logger = logging.getLogger(name="applog")
# logger.setLevel(logging.DEBUG)
# print(logger)

# 处理器
# StreamHandler - 标准输出流处理器-控制台输出
# consoleHandler = logging.StreamHandler()
# consoleHandler.setLevel(logging.DEBUG)
# consoleHandler.setFormatter(formatter)

# FileHandler -单文件处理器-文件输出
# fileHandler = logging.FileHandler(filename="app.log", mode='a')
# fileHandler.setLevel(logging.ERROR)
# consoleHandler.setFormatter(formatter)

# RotatingFileHandler -日志多文件 -按照文件大小规定，达到文件大小后. 开辟新的文件存储日志
# r_fh = logging.RotatingFileHandler()

# TimeRotatingFileHandler -按照时间开辟新的文件存储日志
# tr_fh = logging.TimeRotatingFileHandler()

# 过滤器
# logging.Filter("dq.zz") #grep ""


# 自定义过滤器
# class ModuleFilter(logging.Filter):
#     def __init__(self, module_name):
#         super().__init__()
#         self.module_name = module_name
#
#     def filter(self, record):
#         return record.modulename == self.module_name
#
#
# # 创建记录器
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
#
# # 创建处理器
# consoleHandler = logging.StreamHandler()
# consoleHandler.setLevel(logging.DEBUG)
#
# # 创建过滤器
# module_filter = ModuleFilter("my_module")
#
# # 创建格式化器
# formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(filename)s | %(lineno)s | %(message)s")
#
# # 记录器绑定处理器
# logger.addHandler(consoleHandler)
# # 处理器绑定过滤器
# consoleHandler.addFilter(module_filter)
# # 处理器绑定格式化器
# consoleHandler.setFormatter(formatter)
#
# # 输出日志测试
# logger.debug("This is a debug msg from my_module", extra={"modulename": "my_module"})
# logger.debug("This is a debug msg from another_module", extra={"modulename": "another_module"})

# ------------------------------------------------------------------------------------------------------------------------------------------------------
logging.config.fileConfig("logging.conf")  # 加载日志配置文件

root_Logger = logging.getLogger()  # 生成root记录器
applog_logger = logging.getLogger("applog")  # 生成applog记录器

applog_logger.debug("this is a applog")  # 生成日志信息
