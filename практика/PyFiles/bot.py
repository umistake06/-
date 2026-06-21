"""Главный файл запуска Telegram-бота."""
import telebot
import config
import db
import handlers


db.init_db()
db.load_test_data()

telegram_bot = telebot.TeleBot(config.TOKEN)

handlers.register_handlers(telegram_bot)

if __name__ == "__main__":
    telegram_bot.polling()