from wsgiref.simple_server import make_server
import Common
from RedisStore import RedisStore
import web
import json
import Account
import Config
import Shop
import Task
import myConfig.ErrorCfg as ErrorCfg
import Error

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/shop/cfg', 'Shopcfg',
    '/shop/buy', 'Shopbuy',
    '/task/cfg', 'Taskcfg',
    '/task/reward', 'Taskreward',
    '/sign', 'Sign',
    '/mail/send', 'Mailsend',
    '/mail/list', 'Maillist',
)
app = web.application(urls, globals())

# 无法解决session绘画一致性问题
if web.config.get('_session') is None:
    # session = web.session.Session(app, web.session.DiskStore('sessions'))
    session = web.session.Session(app, RedisStore(
        Config.grds, Config.SESSION_EXPIRETIME))

    # session['userid']=userid
    # 使用数据库对session进行存储
    # DBStore创建需要两个参数、db对象和表名
    # session_store = web.session.DBStore(数据库连接,'sessions')

    web.config._session = session
else:
    session = web.config._session


# 主页类
class Home:
    def GET(self):
        return {'code': 0, 'words': "hello,get home"}

    def POST(self):
        return {'code': 0, 'words': "hello,post home"}


# 注册类
class Register:
    @Error.CatchError
    def POST(self):
        req = web.input(phonenum='', password='', nick='', sex='', idcard='')
        phonenum = req['phonenum']
        password = req['password']
        nick = req['nick']
        sex = req['sex']
        idcard = req['idcard']

        if not Account.CheckPhonenum(phonenum):
            # 检查账号格式
            return Error.ErrResult(ErrorCfg.EC_REGISTER_PHONENUM_TYPE_ERROR, ErrorCfg.ER_REGISTER_PHONENUM_TYPE_ERROR)
        if not Account.CheckPassword(password):
            # 检查密码格式
            return Error.ErrResult(ErrorCfg.EC_REGISTER_PASSWORD_TYPE_ERROR, ErrorCfg.ER_REGISTER_PASSWORD_TYPE_ERROR)
        if not Account.CheckIdcard(idcard):
            # 检查身份证号格式
            return Error.ErrResult(ErrorCfg.EC_REGISTER_IDCARD_TYPE_ERROR, ErrorCfg.ER_REGISTER_IDCARD_TYPE_ERROR)
        if not Account.CheckUserIdNotRepeat(phonenum):
            # 这里账号不重复not true说明账号重复了，不能注册
            return Error.ErrResult(ErrorCfg.EC_REGISTER_USERID_REPEAT, ErrorCfg.ER_REGISTER_USERID_REPEAT)

        Account.InitUser(phonenum, password, nick, sex, idcard)

        return json.dumps({'code': ErrorCfg.EC_REQ_NORMAL})


# 登陆类-未完成
class Login:
    @Error.CatchError
    def POST(self):
        req = web.input(userid='', password=' ')
        userid = req['userid']
        password = req['password']

        ret = Account.VerifyAccount(userid, password)
        if ret['code'] != ErrorCfg.EC_REQ_NORMAL:
            return Error.ErrResult(ret['code'], ret['reason'])

        # 设置登录状态、加载登录后的个人信息等
        ret = Account.HandleLogin(userid, session)
        if ret['code'] != ErrorCfg.EC_REQ_NORMAL:
            return Error.ErrResult(ret['code'], ret['reason'])

        return json.dumps({'code': ErrorCfg.EC_REQ_NORMAL})


# 商城配置类
class Shopcfg:
    @Error.CatchError
    @Account.ChekLogin
    def GET(self):
        req = web.input(version='')
        version = int(req['version'])
        shopcfg = Shop.GetShopCfg(version)
        return json.dumps({'code': 0, 'shopcfg': shopcfg})


# 商城购买类
class Shopbuy:
    @Error.CatchError
    @Account.ChekLogin
    def POST(self):
        req = web.input(userid='', propid='', propnum='',
                        shopversion='', version='', paytype='')
        userid = int(req['userid'])
        propid = int(req['propid'])
        propnum = int(req['propnum'])
        shopversion = int(req['shopversion'])
        version = int(req['version'])
        paytype = int(req['paytype'])

        dictInfo = Shop.ShopBuy(userid, propid, propnum,
                                shopversion, version, paytype)
        return json.dumps(dictInfo)


# 任务配置类-有错误
class Taskcfg:
    @Error.CatchError
    @Account.ChekLogin
    def GET(self):
        req = web.input(userid='', version='')
        userid = req['userid']
        version = req['version']
        taskcfg = Task.GetTaskCfg(userid, version)
        return json.dumps({'code': 0, 'taskcfg': taskcfg})


# 任务领奖类
class Taskreward:
    @Error.CatchError
    @Account.ChekLogin
    def POST(self):
        req = web.input(userid='', taskid='')
        # 领取奖励
        return {'code': 0}


# 签到
class Sign:
    @Error.CatchError
    @Account.ChekLogin
    def POST(self):
        req = web.input(userid='', signtype='0', date='')
        userid = int(req['userid'])
        signtype = int(req['signtype'])
        date = req['date']
        Task.UserSign(userid, signtype, date)
        return {'code': 0}


# 邮箱发送
class Mailsend:
    @Error.CatchError
    def POST(self):
        req = web.input(useridlist='', title='', context='', type='',
                        attach={}, isglobal=0, fromuserid='', buttontext='')
        req['userlist'] = req['userlist'].split(',')
        req['attach'] = json.loads(req['attach'])
        Common.SendMail(req)
        return json.dumps({'code': 0})

# 邮件获取


class Maillist:
    @Error.CatchError
    @Account.ChekLogin
    def GET(self):
        req = web.input(userid='', date='')
        return json.dumps({'code': 0})


# if __name__ == "__main__":
#     app.run()
application = app.wsgifunc()
