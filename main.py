import os
import telebot
from env import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['info']) # команда /info
def handle_info(message):
    bot.reply_to(message, 'about created by me 30.11.2023')
if __name__ == "__main__":
    bot.polling(none_stop=True)