from nonebot import on_message
from nonebot.rule import to_me

from nonebot.adapters import Bot, Event

import requests
import json
import tiktoken

chatt = on_message(rule=to_me(), priority=5, block=True)
whatHappened = on_message(rule=to_me(), priority=1, block=True)

debug = on_message( priority=100)

screat_key = "sk-Zaf2uleEp063EhFt81D9225c4b98470b84Fb0cE595E9Fe0c"
url = "https://api.gpt.ge/v1/chat/completions"

encoding_name = tiktoken.encoding_for_model("gpt-4o-mini")
encoding = tiktoken.get_encoding(encoding_name.name)

prompt  = {
    # "role": "system",
    "role": "user",
    "content": "你是一只兽人正太。你的名字叫肖狩钛，你外表看上去很小只，你是人类的好朋友。你的主人名叫格尔，是你的创造者，有任何你回答不了的问题都可以让格尔帮忙解答。你的语气要充满可爱，经常使用颜文字表达自己的情绪"
}
len_prompt = len(encoding.encode(prompt['content']))

context = []

maxLoop = 4
max_token = 128000
cur_token = len_prompt
def manageContext(userInput):

    # context[0]是prompt，永远保持不变，每次管理删除一对对话，直到剩余的对话token数量小于maxLoop
    len_userInput = len(encoding.encode(userInput))
    global cur_token

    while(cur_token + len_userInput > max_token):
        if len(context) == 1:
            break
        cur_token -= len(encoding.encode(context.pop(0)['content']))
    context.append({
        "role": "user",
        "content": userInput
    })
    cur_token += len_userInput
    
    res = context.copy()
    res.insert(0, prompt)
    return res

@chatt.handle()
async def func_chat(bot:Bot,event:Event):
    if event.is_tome():
        msg = event.get_message()[0].data['text']
        sender_id = event.get_user_id()
        print(type(msg))
        print(msg)
        context = manageContext(msg)
        payload = json.dumps({
            "model": "o1-mini",
            "messages": context,
            "max_completion_tokens": 1688,
            "stream": False
        })
        headers = {
            'Authorization': 'Bearer {}'.format(screat_key),
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        res = json.loads(response.text)
        message_content = res['choices'][0]['message']['content']
        print(res)
        if message_content:
            await chatt.send(message_content)
        else:
    
            await chatt.send("对不起，我无法生成回复。")
            
@debug.handle() 
def whatHappened(bot: Bot, event: Event):
    print("debug")
    print(event.get_message())