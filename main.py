import os
from background import keep_alive 
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time
from telebot import types

bot= telebot.TeleBot('6207441183:AAHtInN2yb7ZbF3IWAeY2pZyrOvTz9Bpzz4')

cnt=0
cntlimit=0

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет тест!')

@bot.message_handler(commands=['countinfo'])
def main(message):
    bot.send_message(message.chat.id, f"current cnt: {cnt}")
    bot.send_message(message.chat.id, f"current limit: {cntlimit}")

@bot.message_handler(commands=['setcounterlimit'])
def handle_limit(message):
    global cntlimit
    bot.send_message(message.chat.id, f"current limit {cntlimit}")
    bot.send_message(message.chat.id,f"set counter limit:")
    bot.register_next_step_handler(message,set_limit)

def set_limit(message):
    global cntlimit
    new_limit=int(message.text)
    cntlimit=new_limit
    bot.send_message(message.chat.id, f"set limit on: {cntlimit}")

@bot.message_handler(commands=['inccnt'])

def incrby(message):
    bot.send_message(message.chat.id, "inc by: ")
    bot.register_next_step_handler(message,incbyfunc)
def incbyfunc(message):
    global cnt
    new_value=int(message.text)
    cnt += new_value

keep_alive()
bot.polling(non_stop=True, interval=0) 