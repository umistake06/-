import telebot
import config
import db
import handlers

bot = telebot.TeleBot(config.TOKEN)

def main():
    print("Проверка базы данных...")
    db.init_db()  
    
    print("Регистрация хэндлеров...")
    handlers.register_handlers(bot)
    
    print("Бот успешно запущен и готов к работе!")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
