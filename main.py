import os
import telebot
import logging
from dotenv import load_dotenv


load_dotenv()

bot = telebot.TeleBot("6637498364:AAEMtFQ2PAkEQiX0TroW8D0pMr0l5N9U3K8")
print(bot)


@bot.message_handler(commands=["help"], content_types=["new_chat_members", "left_chat_member", "chat_member"])
def send_welcome(message):
	bot.reply_to(message, "howa you")
    

@bot.chat_member_handler(func=None)
def hello(data):
    print("yiiiii")


bot.infinity_polling(logger_level=logging.INFO, allowed_updates= ["util.update_types"])
