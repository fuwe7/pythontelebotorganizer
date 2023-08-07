import telebot

bot= telebot.TeleBot('6207441183:AAHtInN2yb7ZbF3IWAeY2pZyrOvTz9Bpzz4')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.infinity_polling()

