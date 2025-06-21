import json
import base64
import Account
import Config
import DBManage
import datetime
from myConfig import ShopCfg
from proto.general_pb2 import Mail


# 保证缓存存在
def GetMoney(userid, coinID):
    strKey = Config.KEY_PACKAGE.format(userid=userid)
    money = 0
    if Config.grds.exists(strKey):
        money = Config.grds.hget(strKey, coinID)
    else:
        res = DBManage.DBSearchPackageByUid_Pid(userid, coinID)
        money = int(res['propnum'])
        Account.InitPackage(userid, res['freshtime'])

    return money


def GetMonday(today):
    today = datetime.datetime.strptime(str(today), "%Y-%m-%d")
    return datetime.datetime.strftime(today - datetime.timedelta(today.weekday()), "%Y_%m_%d")


def SendMail(mailinfo):
    # (useridlist='', title='', context='', type='',attach={}, isglobal=0, fromuserid='', buttontext='')

    # 如果发送的邮件太多，请求被占有到发送邮箱请求，不合理，所以发送邮件的功能应该分发给其它服务器
    # 而本服务器只做校验、透传的工作，此时只需要关心数据的传输即可，服务器性能瓶颈就提高了。
    # 这个策略就类似于将不需要人工操作的任务 挂到后台

    # 分布式策略：
    # 校验
    # 组合数据到proto中
    mailproto = Mail()

    for userid in mailinfo['useridlist']:
        mailproto.userid.append(int(userid))

    mailproto.title = mailinfo['title']
    mailproto.context = mailinfo['context']
    mailproto.type = mailinfo['type']

    attach = {}
    for propid, propnum in mailinfo['attach'].items():
        if int(propid) not in ShopCfg.SHOP_LIST:
            continue
        attach[int(propid)] = int(propnum)

    mailproto.attach = json.dumps(attach)
    mailproto.buttontext = base64.b64encode(
        mailinfo['buttontext'].encode('utf-8'))
    mailproto.fromuserid = int(mailinfo['fromuserid'])
    mailproto.isglobal = int(mailinfo['isglobal'])
    mailproto.SerializePartialToString()
    # 发送给C++邮件服务器
    # service.SendSvrd()
