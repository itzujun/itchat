# _*_ coding:utf-8 _*_
"""
微信机器人自动聊天
write the code, change the world
"""

__author__ = "open_china"

__time__ = "2018.11.16"

import itchat

from itchat.content import *
import requests

# 机器人KEY
KEY = "5b9956e1704944ae9d832bf51b9e08xxxx"


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,  # 这是要发送出去的信息
        'userid': 'wechat-rebot',  # 这里随意写点什么都行
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get("text")
    except:
        return


@itchat.msg_register(TEXT)
def reply_text(msg):
    # do somethimg as you want
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    print(msg['Text'])
    print("reply:" + reply)
    itchat.send(reply + "(智能回复)", toUserName=msg['FromUserName'])


if __name__ == "__main__":
    itchat.auto_login()
    itchat.run()
