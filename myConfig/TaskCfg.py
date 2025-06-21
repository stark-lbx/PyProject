from myConfig import ActionCfg
from myConfig import ShopCfg

ID_INVALID = -1  # 无效任务id
ID_SIGN = 2001  # 签到
ID_SIGN_SEVENDAYS = 2002  # 签到7天

# 系列任务
ID_PLAY_SERIES_1 = 2003  # 对局3局
ID_PLAY_SERIES_2 = 2004  # 对局5局
ID_PLAY_SERIES_3 = 2005  # 对局10局

# 任务类型
TYPE_DAY = 1001  # 日任务
TYPE_WEEK = 1002  # 周任务
TYPE_MONTH = 1003  # 月任务
TYPE_YEAR = 1004  # 年任务

# 展示的任务列表
TASK_LIST = [
    ID_SIGN,
    ID_SIGN_SEVENDAYS,
    ID_PLAY_SERIES_1,
    ID_PLAY_SERIES_2,
    ID_PLAY_SERIES_3,
]

# 任务状态
STATE_INVALID = -1  # 无效任务
STATE_NOT_FINISH = 1  # 未完成
STATE_FINISH = 2  # 已完成
STATE_AWARDED = 3  # 已领取


# 签到配置
SIGN_TYPE_TODAY = 1
SIGN_TYPE_AGO = 2
KEY_SIGN = "KEY_SIGN_{userid}_{date}"
SIGN_EXPIRE_TIME = 60*24*60*60


# 缓存-键
KEY_TASK = "KEY_TASK_{userid}_{date}"


TASK_CFG = {
    ID_SIGN: {
        'tid': ID_SIGN, 'name': "每日签到", 'desc': "每日签到领取100铜钱",
        'type': TYPE_DAY, 'series': ID_INVALID,
        'count': 0, 'total': 1, 'state': STATE_NOT_FINISH,
        'action': ActionCfg.ACTION_SIGN,
        'iconid': 2001, 'version': 10000,
        'rewards': [
            {'id': ShopCfg.ID_MONEY, 'propnum': 100}
        ]
    },
    ID_SIGN_SEVENDAYS: {
        'tid': ID_SIGN_SEVENDAYS, 'name': "每周签到", 'desc': "签到7日后领取1000铜钱",
        'type': TYPE_WEEK, 'series': ID_INVALID,
        'count': 0, 'total': 7, 'state': STATE_NOT_FINISH,
        'action': ActionCfg.ACTION_SIGN,
        'iconid': 2002, 'version': 10000,
        'rewards': [
            {'id': ShopCfg.ID_MONEY, 'propnum': 1000}
        ]
    },
    ID_PLAY_SERIES_1: {
        'tid': ID_PLAY_SERIES_1, 'name': "对局任务1", 'desc': "单日累计对局3次获得少量铜钱",
        'type': TYPE_DAY, 'series': ID_INVALID,
        'count': 0, 'total': 1, 'state': STATE_NOT_FINISH,
        'action': ActionCfg.ACTION_PLAY,
        'iconid': 2003, 'version': 10000,
        'rewards': [
            {'id': ShopCfg.ID_MONEY, 'propnum': 50}
        ]
    },
    ID_PLAY_SERIES_2: {
        'tid': ID_PLAY_SERIES_2, 'name': "对局任务2", 'desc': "单日累计对局5次获得大量铜钱",
        'type': TYPE_DAY, 'series': ID_PLAY_SERIES_1,
        'count': 0, 'total': 5, 'state': STATE_NOT_FINISH,
        'action': ActionCfg.ACTION_PLAY,
        'iconid': 2004, 'version': 10000,
        'rewards': [
            {'id': ShopCfg.ID_MONEY, 'propnum': 500}
        ]
    },
    ID_PLAY_SERIES_3: {
        'tid': ID_PLAY_SERIES_3, 'name': "对局任务3", 'desc': "单日累计对局10次获得海量铜钱",
        'type': TYPE_DAY, 'series': ID_PLAY_SERIES_2,
        'count': 0, 'total': 10, 'state': STATE_NOT_FINISH,
        'action': ActionCfg.ACTION_PLAY,
        'iconid': 2005, 'version': 10000,
        'rewards': [
            {'id': ShopCfg.ID_MONEY, 'propnum': 3000}
        ]
    }

}
