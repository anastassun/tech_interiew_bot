import logging, time
from tracemalloc import start

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from handlers import info_view, talk_bot, user_contact, vacansies_list, start
import settings
from anketa import anketa_start,anketa_name, anketa_rating, anketa_comment, anketa_skip, anketa_dontknow


logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.BOT_API, use_context=True)
    
    dp = mybot.dispatcher

    anketa = ConversationHandler (
        entry_points = [
            MessageHandler(Filters.regex('^(Заполнить тест)$'), anketa_start)
        ],
        states = {
            "name": [MessageHandler(Filters.text, anketa_name)],
            "rating":[MessageHandler(Filters.regex('^ (1|2|3|4)$'), anketa_rating)],
            "comment": [
                CommandHandler('skip', anketa_skip),
                MessageHandler(Filters.text, anketa_comment)
            ]
        },
        fallbacks=[MessageHandler(Filters.text| Filters.video | Filters.photo | Filters.document
          | Filters.location, anketa_dontknow)]
    )


    dp.add_handler(anketa)
    dp.add_handler(CommandHandler('info', info_view))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex('^(Информация о боте)$'), info_view))
    dp.add_handler(MessageHandler(Filters.regex('^(Начать тест)$'), vacansies_list))
    #dp.add_handler(MessageHandler(Filters.regex('^(На прохождения теста у вас есть 5 минут)$'), android_test))
    dp.add_handler(MessageHandler(Filters.contact, user_contact))
    dp.add_handler(MessageHandler(Filters.text, talk_bot))
    
    logging.info(f"BOT starting... Date: {time.ctime()}")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()