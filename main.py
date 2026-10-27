import os
import telebot
from dotenv import load_dotenv

load_dotenv() #загружает в память file .env
BOT_TOKEN = os.getenv("BOT_TOKEN") #загружает из файла переменную BOT_TOKEN

if not BOT_TOKEN:
	print("NO TOKEN PLS STOPE")

bot = telebot.TeleBot(BOT_TOKEN) #объект бота. нельзя изменять

@bot.message_handler(commands = ["start"])
def welcome(message):
	user_name = message.from_user.first_name #берет имя пользователя из его профиля
	bot.reply_to(message, f"Privet, {user_name} \nsasi penes") #отвечает на соо

@bot.message_handler(commands = ["help"])
def help(message):
	bot.reply_to(message, f"I can \n /start \n /echo ur message")

@bot.message_handler(content_types = ["text"])
def echo(message):
	user_text = message.text
	chat_id = message.chat.id #id чата

	bot.send_message(chat_id, user_text) #отправляет соо

if __name__ == "__main__":
	bot.infinity_polling() #запускает бота и заставляет не падать после ответа на одно соо