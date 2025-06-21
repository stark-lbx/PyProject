# ------------------------------------------------------------
#   pid 道具编号
#   name 道具名称
#   ename 英文名称
#   type 类型（按次数消耗、按时间消耗）
#   money 消耗铜钱数
#   coin 消耗金币数
#   paytype 支付类型
#   discount 折扣信息
#   iconid 客户端展示图标的id
#   version 版本
#   # description 描述
#   inventory 库存
#   buylimittype 限购方式（日限购、周限购、月限购、年限购等）
#   buylimitnum 限购量
#
#   proplist 道具id列表
#   initnum 初始道具数量
# ------------------------------------------------------------


# 商城版本 1.0.0
SHOP_VERSION = 10000

# 限购类型
BUYLIMITTYPE_INVALID = 0  # 不限购
BUYLIMITTYPE_DAY = 1  # 日限
BUYLIMITTYPE_WEEK = 2  # 周限
BUYLIMITTYPE_MONTH = 3  # 月限
BUYLIMITTYPE_YEAR = 4  # 年限

# 道具id
ID_MONEY = 1000  # 铜线道具id
ID_COIN = 1001  # 金币道具id
ID_EXPCARD = 1002  # 双倍经验卡
ID_RENAMECARD = 1003  # 改名卡
ID_GAMECLEARCARD = 1004  # 战绩清零卡-遗忘药水
ID_YEARVIP = 1005  # 年会员
ID_MONTHVIP = 1006  # 月会员
ID_YEARVIP_PACKAGE = 1007  # 年会员赠送大礼包
ID_MONTHVIP_PACKAGE = 1008  # 月会员赠送大礼包

# 道具类型
TYPE_USE = 1  # 消耗型
TYPE_TIME = 2  # 时限型

# 支付类型
TYPE_PAY_MONEY = 1  # 铜钱购买
TYPE_PAY_COIN = 2  # 金币购买
TYPE_PAY_RMB = 3  # 人民币支付

# 无库存限制
NO_INVENTORY = -1

# 展示商品的列表
SHOP_LIST = [
    ID_MONEY,
    ID_COIN,
    ID_EXPCARD,
    ID_RENAMECARD,
    ID_GAMECLEARCARD,
    ID_YEARVIP_PACKAGE,
    ID_MONTHVIP_PACKAGE
]

# 初始化列表
INIT_LIST = [
    ID_MONEY,
    ID_COIN,
    ID_EXPCARD,
    ID_RENAMECARD,
    ID_GAMECLEARCARD,
    ID_YEARVIP_PACKAGE,
    ID_MONTHVIP_PACKAGE
]


# 商城配置
SHOP_CFG = {
    ID_MONEY: {  # 货币道具-铜钱
        "pid": ID_MONEY, "ename": "money", "name": "铜钱",
        "type": TYPE_USE, "paytype": [TYPE_PAY_COIN, TYPE_PAY_RMB], "discount": 1,
        "inventory": NO_INVENTORY, "iconid": 1000, "version": 10000,
        "buylimittype": BUYLIMITTYPE_INVALID, "buylimitnum": -1, "initnum": 10000,
        "pay": {TYPE_PAY_RMB: 1, TYPE_PAY_COIN: 1, TYPE_PAY_MONEY: -1, },
        "proplist": [{"pid": ID_MONEY, "num": 1}]
    },
    ID_COIN: {  # 货币道具-金币
        "pid": ID_COIN, "ename": "coin", "name": "金币",
        "type": TYPE_USE, "paytype": [TYPE_PAY_RMB],  "discount": 1,
        "inventory": NO_INVENTORY, "iconid": 1001, "version": 10000,
        "buylimittype": BUYLIMITTYPE_INVALID, "buylimitnum": -1, "initnum": 10,
        "pay": {TYPE_PAY_RMB: 1, TYPE_PAY_COIN: -1, TYPE_PAY_MONEY: -1, },
        "proplist": [{"pid": ID_COIN, "num": 1}]
    },
    ID_EXPCARD: {  # 卡牌道具-双倍经验卡
        "pid": ID_EXPCARD, "ename": "expcard", "name": "双倍经验卡",
        "type": TYPE_TIME, "paytype": [TYPE_PAY_MONEY], "discount": 1,
        "inventory": 100, "iconid": 1002, "version": 10000,
        "buylimittype": BUYLIMITTYPE_INVALID, "buylimitnum": -1, "initnum": 0,
        "pay": {TYPE_PAY_RMB: -1, TYPE_PAY_COIN: -1, TYPE_PAY_MONEY: 100, },
        "proplist": [{"pid": ID_EXPCARD, "num": 1}]
    },
    ID_RENAMECARD: {  # 卡牌道具-改名卡
        "pid": ID_RENAMECARD, "ename": "renamecard", "name": "改名卡",
        "type": TYPE_USE, "paytype": [TYPE_PAY_MONEY], "discount": 1,
        "inventory": NO_INVENTORY,  "iconid": 1003, "version": 10000,
        "buylimittype": BUYLIMITTYPE_INVALID, "buylimitnum": -1, "initnum": 0,
        "pay": {TYPE_PAY_RMB: -1, TYPE_PAY_COIN: -1, TYPE_PAY_MONEY: 1000, },
        "proplist": [{"pid": ID_RENAMECARD, "num": 1}]
    },
    ID_GAMECLEARCARD: {  # 卡牌道具-战绩清零卡
        "pid": ID_GAMECLEARCARD, "ename": "gameclearcard", "name": "战绩清零卡",
        "type": TYPE_USE, "paytype": [TYPE_PAY_MONEY], "discount": 1,
        "inventory": NO_INVENTORY, "iconid": 1004, "version": 10000,
        "buylimittype": BUYLIMITTYPE_INVALID, "buylimitnum": -1, "initnum": 0,
        "pay": {TYPE_PAY_RMB: -1, TYPE_PAY_COIN: -1, TYPE_PAY_MONEY: 1000, },
        "proplist": [{"pid": ID_GAMECLEARCARD, "num": 1}]
    },
    ID_MONTHVIP_PACKAGE: {  # 礼包道具-月会员大礼包
        "pid": ID_MONTHVIP_PACKAGE, "ename": "monthvip", "name": "月会员大礼包",
        "type": TYPE_USE, "paytype": [TYPE_PAY_RMB], "discount": 1,
        "inventory": NO_INVENTORY, "iconid": 1006, "version": 10000,
        "buylimittype": BUYLIMITTYPE_INVALID, "buylimitnum": -1, "initnum": 0,
        "pay": {TYPE_PAY_RMB: 50, TYPE_PAY_COIN: -1, TYPE_PAY_MONEY: -1, },
        "proplist": [{"pid": ID_EXPCARD, "num": 2},
                     {"pid": ID_RENAMECARD, "num": 2},
                     {"pid": ID_MONTHVIP, "num": 1}]
    },
    ID_YEARVIP_PACKAGE: {  # 礼包道具-年会员大礼包
        "pid": ID_YEARVIP_PACKAGE, "ename": "yearvip", "name": "年会员大礼包",
        "type": TYPE_USE, "paytype": [TYPE_PAY_RMB], "discount": 1,
        "inventory": NO_INVENTORY, "iconid": 1005, "version": 10000,
        "buylimittype": BUYLIMITTYPE_INVALID, "buylimitnum": -1, "initnum": 0,
        "pay": {TYPE_PAY_RMB: 100, TYPE_PAY_COIN: -1, TYPE_PAY_MONEY: -1, },
        "proplist": [{"pid": ID_EXPCARD, "num": 30},
                     {"pid": ID_RENAMECARD, "num": 30},
                     {"pid": ID_YEARVIP, "num": 1}]
    },
}
