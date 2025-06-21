from myConfig import ActionCfg, MessageCfg
import Config
from proto.message_pb2 import Message


def DistributeAction(actiontype, actionmsg):
    for strKey in ActionCfg.ACTION_MAPPING[actiontype]:
        # print(actiontype)
        # print("rpush msg to: " + strKey)
        Config.grds.rpush(strKey, actionmsg)


def ActionMointor():
    while True:
        # blpop()返回的对象 里面存的：一个[0]是键名、一个[1]是消息
        res = Config.grds.blpop(ActionCfg.KEY_ACTION_LIST)[1]
        print("--------------start--------------")
        msg = Message()
        msg.ParseFromString(res)
        msgid = int(msg.msgid) & MessageCfg.MSGID
        actiontype = int(msg.actiontype)

        # print("msgid: "+str(msgid))
        if msgid == MessageCfg.MSGID_SIGN:
            DistributeAction(actiontype, res)
        elif msgid == MessageCfg.MSGID_LOGIN:
            DistributeAction(actiontype, res)

        print("---------------end---------------")


if __name__ == "__main__":
    ActionMointor()
