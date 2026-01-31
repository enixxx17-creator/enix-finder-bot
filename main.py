import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет!\n\n"
        "Я бот для поиска одежды по фото.\n"
        "Отправь мне изображение — я попробую найти похожие товары."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ Как пользоваться ботом:\n"
        "1. Отправь фото одежды\n"
        "2. Я покажу похожие товары\n\n"
        "Доступ по инвайту."
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
