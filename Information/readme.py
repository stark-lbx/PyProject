'''
ipv4:       192.168.30.128
localhost:  127.0.0.1

mysql:
    username:   stark
    password:   2396573637
    port:       3306

redis:
    host:       127.0.0.1
    password:   123456
    port:       6379
'''

# 用户表: mysql-gamedb-user
# --------------------------------------------------------------------------
# FIELD           TYPE            NULL    KEY     DEFAULT     备注信息
# --------------------------------------------------------------------------
# userid          bigint          NO      PRI     NULL        用户id
# password        varchar(20)     NO              NULL        用户密码
# secpassword     varchar(20)     YES             123456      二级密码
# nick            varchar(20)     NO              NULL        用户昵称
# phonenum        varchar(11)     NO              NULL        电话号码
# sex             char(1)         YES             1           性别
# idcard          char(18)        YES             NULL        身份证号
# status          int             YES             0           状态
# createtime      datetime        NO              NULL        创建时间
# lastlogintime   datetime        YES             NULL        最后登录时间
# --------------------------------------------------------------------------


'''
host             # 主机名ip
port             # 端口号
user             # 用户名
password         # 密码
charset          # 字符编码方式
database         # 数据库名
cursorclass      # cursor类型, 指定返回类型, 不指定则返回元组
init_command     # 连接建立时运行的初始语句
connect_timeout  # 连接超时时间
autocommit       # 是否自动提交事务
'''
# --------------------操作练习模板-----------------------------#


import pymysql.cursors
import time
import pymysql
dbconn = pymysql.connect(
    host='192.168.30.128',
    port=3306,
    user='stark',
    password='2396573637',
    charset='utf8',
    database='gamedb',
    cursorclass=pymysql.cursors.DictCursor
)
# 常用操作

# 游标
# 创建游标对象
cursor = dbconn.cursor
# 选择数据库
dbconn.select_db('gamedb')

# 1.不带参数
sqlStr = "select * from user"
cursor.execute(sqlStr)

# 2.带参数，带多个参数在第二个参数中传入即可
# 尽量不要使用%s和format去进行字符串替换操作，以此来防止sql注入
# sql = "select * from user where userid = {}".format('u1 or 1=1')
# 如果format中的替换字符串为客户端传入参数，那么就会发生sql注入，继而查询出所有的用户信息
# 解决SQL注入问题：参数化查询
sqlStr = "select * from user where userid = %s"
cursor.execute(sqlStr, ('stark',))

# 获取结果
cursor.fetchone()     # 获取一个记录
cursor.fetchall()     # 获取所有记录
cursor.fetchmany(3)  # 获取指定个数记录

# 示例
# ----------------------------------------------
sqlStr = "select * from user"
cursor.execute(sqlStr)
res = cursor.fetchall()
for r in res:
    print(r)
# ----------------------------------------------


# 更新数据
sqlStr = "update user set pwd = '123456' where userid = '123'"
cursor.execute(sqlStr)
dbconn.commit()


# 删除数据
sqlStr = "delete from user where userid = '123'"
cursor.execute(sqlStr)
dbconn.commit()

# 示例
# 模拟数据
data = []
for i in range(1, 101):
    data.append((i, '123456'))

start = time.time()

# 使用循环依次执行：0.02866387367248535
for d in data:
    sqlStr = "insert into test values(%s, %s)"
    cursor.execute(sqlStr, d)

# 使用executemany()提升效率：0.00733184814453125
# sqlStr = "insert into test values(%s, %s)"
# Config.gdb.executemany(sqlStr, data)
dbconn.commit()

end = time.time()
print(end - start)


# 示例
# 模拟数据
data = []
for i in range(1, 101):
    data.append((i, '123456'))

# 分批
stepSize = 10
for i in range(0, len(data), stepSize):
    stepData = data[i:i+stepSize]
    sqlStr = "insert into test values(%s, %s)"
    cursor.executemany(sqlStr, stepData)
    dbconn.commit()


# def app(env, start_response):
#     url = env.get('PATH_INFO')
#     if url is None or url not in pattern_url.keys():
#         start_response('404 not found',[('content-type','text/plain')])
#         return[b'404 page not found']

#     res = pattern_url.get(url)
#     if res is None:
#         start_response('404 not found',[('content-type','text/plain')])
#         return[b'404 page not found']

#     start_response('200 ok',[('content-type','text/plain')])
#     return [res().encode()]

# server = make_server(Config.DB_HOST, 8888, app)
# server.serve_forever()


'''
protobuf通信协议
-文件编译工具protoc (.proto文件)
-代码提示插件mypy (.pyi文件)
protoc -I ./ --python_out=./ --mypy_out=./ *.proto
'''
