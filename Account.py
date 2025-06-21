import re
import pymysql
import pymysql.cursors
import web
import Error
import DBManage
import datetime
import Config
from myConfig import ErrorCfg, ShopCfg, AccountCfg


# 检测电话号码格式
def CheckPhonenum(phonenum):
    if len(phonenum) != 11:
        return False
    if not str(phonenum).isdigit():
        return False
    if int(phonenum[:3]) not in AccountCfg.PHONELIST:
        return False
    return True


# 检测密码格式
def CheckPassword(password):
    pattern = re.compile('^(?=.*[0-9])(?=.*[A-z])[0-9a-zA-Z]{8,16}$')
    if not re.match(pattern, password):
        return False
    return True


# 检测身份证号格式
def CheckIdcard(idcard):
    # return True
    stridcard = str(idcard)
    stridcard = stridcard.strip()
    idcard_list = list(stridcard)
    # 地区校验
    if (stridcard)[0:2] not in AccountCfg.AREAID:
        return False

    # 15位身份号码检测
    if len(stridcard) == 15:
        if ((int(stridcard[6:8]) + 1900) % 400 == 0 or (
                (int(stridcard[6:8]) + 1900) % 100 != 0 and (int(stridcard[6:8]) + 1900) % 4 == 0)):
            pattern = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
        else:
            pattern = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
        if re.match(pattern, stridcard):
            return True
        else:
            return False
    # 18位身份号码检测
    elif len(stridcard) == 18:
        # 出生日期的合法性检查
        # 闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
        # 平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
        if (int(stridcard[6:10]) % 400 == 0 or (int(stridcard[6:10]) % 100 != 0 and int(stridcard[6:10]) % 4 == 0)):
            # 闰年出生日期的合法性正则表达式
            pattern = re.compile(
                '[1-9][0-9]{5}(18|19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')
        else:
            # 平年出生日期的合法性正则表达式
            pattern = re.compile(
                '[1-9][0-9]{5}(18|19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')
        # 测试出生日期的合法性
        if re.match(pattern, stridcard):
            # 计算校验位
            ten = ['X', 'x']
            ID = ["10" if x in ten else x for x in idcard_list]  # 将字母X/x替换为10
            IDWeight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            Checkcode = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
            sum = 0
            for i in range(17):
                sum += int(ID[i]) * IDWeight[i]
            if Checkcode[sum % 11] == int(ID[17]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# 检测用户是否已经存在
def CheckUserIdNotRepeat(userid):
    # 判断数据库中是否存在--已经存在：return False
    res = DBManage.DBSearchUserInfoByUid(userid)
    if res and res['num'] == 1:
        return False
    return True


# 初始化背包信息
def InitPackage(userid, now):
    # 设置到缓存
    strKey = Config.KEY_PACKAGE.format(userid=userid)
    if not Config.grds.exists(strKey):
        res = DBManage.DBSearchPackageByUid(userid)
        print(res)
        if res:
            # 设置缓存
            packageInfo = {}
            for r in res:
                packageInfo[res['propid']] = res['propnum']
            Config.grds.hset(strKey, mapping=packageInfo)
        else:
            # 写入数据库，设置缓存
            packageInfo = {}
            packageInfoList = []
            for id in ShopCfg.INIT_LIST:
                if id not in ShopCfg.SHOP_CFG:
                    continue
                cfg = ShopCfg.SHOP_CFG[id]
                info = {
                    'propid': cfg['pid'],
                    'propnum': cfg['initnum'],
                    'proptype': cfg['type']
                }
                packageInfo[cfg['pid']] = cfg['initnum']
                packageInfoList.append(info)
            Config.grds.hset(strKey, mapping=packageInfo)
            DBManage.DBInitPackage(userid, packageInfoList, now)
    Config.grds.expire(strKey, Config.KEY_PACKAGE_EXPIRE_TIME)


# 初始化用户信息
def InitUser(phonenum, password, nick, sex, idcard):
    # 向数据库中插入一条记录
    now = datetime.datetime.now()
    DBManage.DBInsertRegisterUser(phonenum, password, nick, sex, idcard, now)
    # 初始化用户背包信息
    InitPackage(phonenum, now)


# 校验用户账号
def VerifyAccount(userid, password, cursor: pymysql.cursors.DictCursor = None):
    res = DBManage.DBSearchUserInfoByUid(userid)
    realpwd = res.get('password')
    if not realpwd:
        return {"code": ErrorCfg.EC_LOGIN_USERID_ERROR, 'reason': ErrorCfg.ER_LOGIN_USERID_ERROR}
    if realpwd != password:
        return {"code": ErrorCfg.EC_LOGIN_PASSWORD_ERROR, 'reason': ErrorCfg.ER_LOGIN_PASSWORD_ERROR}
    return {'code': ErrorCfg.EC_REQ_NORMAL}


# 处理登录任务
@Error.DBCatchError
def HandleLogin(userid, session, cursor: pymysql.cursors.DictCursor = None):
    now = datetime.datetime.now()  # 获取时间

    # 设置登录缓存信息
    session['userid'] = userid  # 登录
    strKey = AccountCfg.KEY_LOGIN.format(userid=userid)
    logininfo = {
        'userid': userid,
        'freshtime': str(now)
    }
    Config.grds.hset(strKey, mapping=logininfo)

    # 更新最后一次登陆时间
    Config.grds.expire(strKey, AccountCfg.KEY_LOGIN_EXPIRE_TIME)
    sqlStr = "update user set lastlogintime = %s where userid = %s"
    cursor.excute(sqlStr, (now, userid))

    return {'code': ErrorCfg.EC_REQ_NORMAL}


# 检测登陆状态
def ChekLogin(func):
    def wrapper(*args, **kwargs):
        if web.config._session.get('userid'):
            return func(*args, **kwargs)
        else:
            return Error.ErrResult(ErrorCfg.EC_LOGIN_INVALID, ErrorCfg.ER_LOGIN_INVALID)
    return wrapper
