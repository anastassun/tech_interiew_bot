import logging, time

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import info_view, talk_bot, user_contact, test, vacansies_list
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.BOT_API, use_context=True)
    
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CommandHandler('info', info_view))
    dp.add_handler(MessageHandler(Filters.regex('^(Информация о боте)$'), info_view))
    dp.add_handler(MessageHandler(Filters.regex('^(Начать тест)$'), vacansies_list))
    dp.add_handler(MessageHandler(Filters.contact, user_contact))
    dp.add_handler(MessageHandler(Filters.text, talk_bot))
    
    logging.info(f"BOT starting... Date: {time.ctime()}")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()