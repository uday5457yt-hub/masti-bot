import os
import telebot
from flask import Flask
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Masti Bot Live Hai!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_web, daemon=True).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔥 Masti Bot Live hai Uday! /game likho")

@bot.message_handler(commands=['game'])
def game(m):
    bot.reply_to(m, "🎮 Game shuru! Truth ya Dare?")

print("Bot chal raha hai...")
bot.infinity_polling()
