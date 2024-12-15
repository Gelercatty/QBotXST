from nonebot import on_command,get_bot
from nonebot.rule import to_me
from nonebot import on_message
from nonebot.adapters import Bot,Event
from .db import SJDB
# test_group_id = 727822963
test_group_id = 589648813


sj_db = SJDB()

CM_test = on_command("test",to_me,aliases={"测试","试试","试试看"},priority=5,block = True)
CM_ru_dian = on_command("入典",to_me,aliases={"SJ","sj"},priority=6,block = True)
CM_got_sj_by_id = on_command("看看",aliases={"查看","查看圣经"},priority=7,block = True)

SJ_ID = [664471467,834090819]




def GenerateSJ(msgLIST: list):
    result = []
    for itm in msgLIST:
        result.append(
            {
                "type":"node",
                "data":{
                    "id": "{}".format(itm),
                }
            }
        )
    return result
@CM_test.handle()
async def func_test(bot: Bot):
    print("[MSG|Request] test")
    # await CM_test.send("test")
    result = await bot.call_api("send_group_forward_msg",message=GenerateSJ(SJ_ID),group_id=test_group_id)    
    
   
   

@CM_ru_dian.handle()
async def func_rudian(bot: Bot,event: Event):
    print("[MSG|Request] SJ")
    # result = await b
    msg = event.get_message()
    sender_id = event.get_user_id()

    # sender_nike_name = await bot.call_api("get_stranger_info",group_id = ,user_id = sender_id)
    if event.reply:
        referenced_message_id = event.reply.message_id
        referenced_sender_id = event.reply.sender.user_id
        print(event.reply)
        referenced_gorup_id = event.reply.group_id
        print("入典")
        sj_db.insert_SJ(referenced_sender_id,referenced_message_id,referenced_gorup_id)
        await CM_ru_dian.send("咱已经记住哥哥的小秘密啦，嘻嘻w")
    else:
        await CM_ru_dian.send("咱还不知道要往圣经里面塞什么进去呢❤~QAQ")

# 随机发送这个人的一条圣经
@CM_got_sj_by_id.handle()
async def func_got_sj_by_id(bot: Bot,event: Event):
    print("[MSG|Request] SJ")
    at_ids = []
    group_id = event.group_id
    for segment in event.message:
        if segment.type == "at":
            at_ids.append(segment.data["qq"]) 
    if at_ids:
        print(f"被 @ 的对象的 ID: {at_ids}")
        # sjlists = sj_db.get_SJ_senderid(at_ids[0])
        sjlists = sj_db.get_SJ_senderid_and_group_id(at_ids[0],group_id)
        if not sjlists:
            await CM_got_sj_by_id.send("这个人还没有圣经哦~")
        print(sjlists)  
        readytosend = []
        for itm in sjlists:
            readytosend.append(itm["message_id"])
        print(readytosend)
        await bot.call_api("send_group_forward_msg",messages=GenerateSJ(readytosend),group_id=group_id)      
    else:
        print("没有 @ 的对象")

