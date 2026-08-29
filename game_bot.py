import os
from flask import Flask
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Flask for Render
app = Flask(__name__)
@app.route('/')
def home(): return "Bot is Live! 24x7"
def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
threading.Thread(target=run_web, daemon=True).start()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Masti Bot Live hai Uday! /game likho")

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Game shuru! Truth/Dare?")

def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN nahi mila!")
        return
    app_bot = Application.builder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CommandHandler("game", game))
    print("Bot chal raha hai...")
    app_bot.run_polling()

if __name__ == "__main__":
    main()
