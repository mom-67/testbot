import os
import telebot
from dotenv import load_dotenv

load_dotenv() 
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
	print("NO TOKEN PLS STOPE")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ["start"])
def welcome(message):
	user_name = message.from_user.first_name #берет имя пользователя из его профиля
	bot.reply_to(message, f"Privet, {user_name} \nsasi penes") #отвечает на соо

if __name__ == "__main__":
	bot.infinity_polling()

