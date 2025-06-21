import datetime
import math
import Common
import Config
import DBManage
import myConfig.ShopCfg as ShopCfg
import myConfig.ErrorCfg as ErrorCfg


def GetShopCfg(version):
    shoplist = []
    shop = ShopCfg.SHOP_LIST
    for id in shop:
        if id not in ShopCfg.SHOP_CFG:
            continue
        cfg = ShopCfg.SHOP_CFG[id]
        if version < cfg['version']:
            continue
        prodict = {
            'pid': cfg['pid'], 'ename': cfg['ename'], 'name': cfg['name'],
            'type': cfg['type'], 'paytype': cfg['paytype'], 'discount': cfg['discount'],
            'inventory': cfg['inventory'], 'iconid': cfg['iconid'], 'version': cfg['version'],
            'buylimittype': cfg['buylimittype'], 'buylimitnum': cfg['buylimitnum'], 'initnum': cfg['initnum'],
            'pay': cfg['pay'], 'proplist': cfg['proplist']
        }
        shoplist.append(prodict)

    return {'shopversion': ShopCfg.SHOP_VERSION, 'shoplist': shoplist}


def PresentProp(userid, propid, propnum, now):
    strKey = Config.KEY_PACKAGE.format(userid=userid)
    proplist = ShopCfg.SHOP_CFG[propid]['proplist']
    dbproplist = []
    propdict = {}
    for prop in proplist:
        pid = prop['pid']
        num = Config.grds.hincrby(strKey, pid, prop['num']*propnum)
        dbproplist.append((num, now, userid, pid))
    propdict['freshtime'] = str(now)
    Config.grds.hset(strKey, mapping=propdict)
    DBManage.DBModifyPackageByUid_Pid(dbproplist)


def ShopBuy(userid, propid, propnum, shopversion, version, paytype):
    # 判断商城版本号
    if shopversion < ShopCfg.SHOP_VERSION:
        return {'code': ErrorCfg.EC_SHOP_VERSION_LOW, 'reason': ErrorCfg.ER_SHOP_VERSION_LOW}

    # 判断道具是否存在
    if propid not in ShopCfg.SHOP_CFG:
        return {'code': ErrorCfg.EC_SHOP_NOT_EXIST, 'reason': ErrorCfg.ER_SHOP_NOT_EXIST}

    # 获取道具配置、验证客户端版本是否支持该道具
    cfg = ShopCfg.SHOP_CFG[propid]
    if version < cfg['version']:
        return {'code': ErrorCfg.EC_CLIENT_VERSION_LOW, 'reason': ErrorCfg.ER_CLIENT_VERSION_LOW}

    # 判断库存逻辑

    # 计算实际花费-货币消费、折扣、
    if paytype not in cfg['paytype']:
        return {'code': ErrorCfg.EC_SHOP_PAYTYPE_ERROR, 'reason': ErrorCfg.ER_SHOP_PAYTYPE_ERROR}

    needmoney = int(math.floor(cfg['pay'][paytype] * cfg['discount']*propnum))

    coinID = paytype + 999
    # 判断余额是否足够
    havemoney = int(Common.GetMoney(userid, coinID))
    while havemoney < needmoney:
        return {'code': ErrorCfg.EC_SHOP_MONEY_NOT_ENONGH, 'reason': ErrorCfg.ER_SHOP_MONEY_NOT_ENONGH}

    # 扣款
    strKey = Config.KEY_PACKAGE.format(userid=userid)
    havemoney = Config.grds.hincrby(strKey, coinID, -needmoney)
    if havemoney < 0:
        Config.grds.hincrby(strKey, coinID, needmoney)
        return {'code': ErrorCfg.EC_SHOP_MONEY_NOT_ENONGH, 'reason': ErrorCfg.ER_SHOP_MONEY_NOT_ENONGH}

    now = datetime.datetime.now()
    dbproplist = [(havemoney, now, userid, coinID,)]
    DBManage.DBModifyPackageByUid_Pid(dbproplist)

    # 发货
    Config.grds.hset(strKey, 'freshtime', str(now))
    PresentProp(userid=userid, propid=propid, propnum=propnum, now=now)

    return {'code': 0, 'money': havemoney}
