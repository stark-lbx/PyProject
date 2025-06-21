
from myConfig import TaskCfg, MessageCfg, ActionCfg
import Config
import Common
import Action
import json
import datetime
from proto.general_pb2 import *


def InitTaskCfg(userid, dateStr):
    strKey = TaskCfg.KEY_TASK.format(userid=userid, date=dateStr)
    taskinfo = {}
    for id in TaskCfg.TASK_LIST:
        if id not in TaskCfg.TASK_CFG:
            continue
        cfg = TaskCfg.TASK_CFG[id]
        taskinfo['count_'+str(id)] = 0
        taskinfo['total_'+str(id)] = cfg['total']
        taskinfo['state_'+str(id)] = TaskCfg.STATE_NOT_FINISH
        taskinfo['reward_'+str(id)] = json.dumps(cfg['rewards'])
    Config.grds.hset(strKey, mapping=taskinfo)
    # Config.grds.expire(strKey,7*24*60*60)


def GetTaskDateStr(type, today):
    datestr = today.strftime("%Y_%m_%d")
    if type == TaskCfg.TYPE_WEEK:
        datestr = Common.GetMonday(today)
    elif type == TaskCfg.TYPE_MONTH:
        datestr = str(today.year)+'_'+str(today.month)+"_01"
    elif type == TaskCfg.TYPE_YEAR:
        datestr = str(today.year)+"_01_01"
    return datestr


def GetTaskCfg(userid, version):
    task = TaskCfg.TASK_LIST
    tasklist = []
    now = datetime.date.today()
    dateStr = now.strftime("%Y_%m_%d")
    strKey = TaskCfg.KEY_TASK.format(userid=userid, date=dateStr)
    if not Config.grds.exists(strKey):
        InitTaskCfg(userid, dateStr)

    for id in task:
        if id not in TaskCfg.TASK_CFG:
            continue
        cfg = TaskCfg.TASK_CFG[id]
        if int(version) < int(cfg['version']):
            continue
        taskdict = {
            'tid': cfg['tid'], 'name': cfg['name'], 'desc': cfg['desc'],
            'type': cfg['type'], 'series': cfg['series'],
            'count': cfg['count'], 'total': cfg['total'], 'state': TaskCfg.STATE_INVALID,
            'iconid': cfg['iconid'], 'version': cfg['version'],
            'action': cfg['action'], 'rewards': cfg['rewards']
        }
        # 获取存放该任务缓存信息的日期
        dateStr = GetTaskDateStr(cfg['type'], now)
        strKey = TaskCfg.KEY_TASK.format(userid=userid, date=dateStr)
        if not Config.grds.exists(strKey):
            tasklist.append(taskdict)
            continue

        countfield = 'count_' + str(id)
        statefield = 'state_' + str(id)
        rewardfield = 'reward_' + str(id)
        taskinfo = Config.grds.hmget(
            strKey, countfield, statefield, rewardfield)
        taskdict['count'] = taskinfo[0].decode() if taskinfo[0] else 0
        taskdict['state'] = taskinfo[1].decode(
        ) if taskinfo[1] else TaskCfg.STATE_INVALID
        taskdict['rewards'] = json.loads(
            taskinfo[2].decode()) if taskinfo[2] else []
        tasklist.append(taskdict)
    return tasklist


def UserSign(userid, signtype, date):
    '''
    判断签到类型
        签到：获取时间
        补签：捕获检测

    获取签到缓存的key
    设置签到信息
    通知签到事件
    '''
    if signtype == TaskCfg.SIGN_TYPE_TODAY:
        date = datetime.datetime.today()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")

    day = date.day
    month_first = datetime.datetime(date.year, date.month, 1)
    date = date.strftime("%Y_%m_%d")
    month_first = month_first.strftime("%Y_%m_%d")
    strKey = TaskCfg.KEY_SIGN.format(userid=userid, date=month_first)

    # 签到
    # 使用位图存储签到数据 setbit用于操作字符串的位 day表示偏移位 1为该位置置1表示签到
    Config.grds.setbit(strKey, day, 1)

    # 签到的proto（消息的格式）
    signproto = Sign()
    signproto.userid = int(userid)
    signproto.signtype = int(signtype)
    signproto.date = date
    # signproto.action = ActionCfg.ACTION_SIGN
    # signproto.SerializeToString()  # 序列化

    Action.SendAction(userid, MessageCfg.MSGID_SIGN,
                      ActionCfg.ACTION_SIGN, signproto.SerializeToString())
