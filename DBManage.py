# --------------------------------------------------------------
# 管理数据库的接口
# --------------------------------------------------------------
import Config
import Error
import pymysql
import pymysql.cursors


# 向用户表注册一条记录
@Error.DBCatchError
def DBInsertRegisterUser(phonenum, password, nick, sex, idcard, now, cursor: pymysql.cursors.DictCursor = None):
    sqlStr = "insert into user(userid, password, secpassword, nick, phonenum, sex, idcard, status, createtime) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sqlStr, (int(phonenum), password, Config.DEFAULT_SECPASSWORD,
                   nick, phonenum, sex, idcard, Config.USER_STATUS_NORMAL, now,))


# 根据userid在用户表中搜索指定用户的所有信息
@Error.DBCatchError
def DBSearchUserInfoByUid(userid, cursor: pymysql.cursors.DictCursor = None):
    sqlStr = "select *,count(*) as num from user where userid = %s"
    cursor.execute(sqlStr, (userid,))
    return cursor.fetchone()


# 初始化背包信息
@Error.DBCatchError
def DBInitPackage(userid, packageInfoList, now, cursor: pymysql.cursors.DictCursor = None):
    sqlStr = "insert into package(userid,propid,propnum,proptype,freshtime) values(%s,%s,%s,%s,%s)"

    data = []
    for info in packageInfoList:
        data.append((userid, info['propid'],
                    info['propnum'], info['proptype'], now,))

    cursor.executemany(sqlStr, data)


# 根据userid搜索用户的背包信息
@Error.DBCatchError
def DBSearchPackageByUid(userid, cursor: pymysql.cursors.DictCursor = None):
    sqlStr = "select propid,propnum from package where userid = %s"
    cursor.execute(sqlStr, (userid,))
    return cursor.fetchall()


# 根据userid和propid搜索背包表
@Error.DBCatchError
def DBSearchPackageByUid_Pid(userid, propid, cursor: pymysql.cursors.DictCursor = None):
    sqlStr = "select *,count(*) as num from package where userid = %s and propid = %s"
    cursor.execute(sqlStr, (userid, propid,))
    return cursor.fetchone()


# 根据userid和propid修改背包表
@Error.DBCatchError
def DBModifyPackageByUid_Pid(data, cursor: pymysql.cursors.DictCursor = None):
    sqlStr = "update package set propnum = %s,freshtime=%s where userid =%s and propid = %s"
    cursor.executemany(sqlStr, data)
