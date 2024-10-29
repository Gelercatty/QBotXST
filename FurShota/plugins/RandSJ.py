from nonebot import on_command,get_bot
from nonebot.rule import to_me
from nonebot import on_message
from nonebot.adapters import Bot



CM_test = on_command("test",to_me,aliases={"测试","试试","试试看"},priority=5,block = True)
CM_GetJingHua = on_command("SJ",to_me,aliases={"圣经","典"},priority=3,block = True)


@CM_test.handle()
async def func_test():
    print("[MSG|Request] test")
    await CM_test.send("test")
    
   
   


    
@CM_GetJingHua.handle()
async def func_GetJingHua(bot: Bot):
    result = await bot.call_api("get_essence_msg_list",group_id=669607474)
    # result = await bot.call_api("get_group_list")
    # result = await bot.call_api("get_group_member_list",group_id=589648813)

    print("[MSG|Request] SJ")
    print(result)