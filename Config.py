from dbutils.pooled_db import PooledDB
import pymysql.cursors
import pymysql
import web
import time
import redis
# import dbutils
# print(dbutils.__file__)

# 账号初始信息配置
DEFAULT_SECPASSWORD = 123456
USER_STATUS_NORMAL = 0
USER_STATUS_FREEZE = -1

# 数据库连接配置:
DB_HOST = '192.168.30.128'       # 主机ip
DB_PORT = 3306              # 端口号
DB_USER = 'stark'           # 数据库用户名
DB_PWD = '2396573637'       # 数据库用户密码
DB_NAME = 'gamedb'          # 数据库


pool = PooledDB(
    creator=pymysql,      # 数据库驱动，使用pymysql连接MySQL数据库
    maxconnections=10,    # 连接池中允许的最大连接数
    mincached=2,          # 初始化时创建的空闲连接数
    maxcached=5,          # 连接池中空闲连接的最大数量
    maxshared=3,          # 连接池中共享连接的最大数目
    blocking=True,        # 没有可用连接时, 是否允许阻塞等待
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PWD,
    db=DB_NAME,
    cursorclass=pymysql.cursors.DictCursor
)

# conn: pymysql.Connection = pool.connection()
# cursor: pymysql.cursors.Cursor = conn.cursor()

# 异常处理- 防止忘记归还连接池资源问题
# try:
#     sqlStr = "select * from user;"
#     cursor.execute(sqlStr)
#     res = cursor.fetchall()
#     for r in res:
#         print(r)
# except:
#     pass
# finally:
#     cursor.close()
#     conn.close()

grds = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='123456'
)

KEY_PACKAGE = "KEY_PACKAGE_{userid}"
KEY_PACKAGE_EXPIRE_TIME = 7*24*60*60

SESSION_EXPIRETIME = 10*60

# res = grds.set('key1', 'value1')
# print(res) #True

# 配置密码:
# sudo vim /etc/redis/redis.conf #:?requirepass -> 取消注释 -> 改为requirepass 123456
# sudo service redis restart
# redis-cli auth 123456 # OK

# $redis-cli
# >auth 'mypassword'
# >get 'key'
