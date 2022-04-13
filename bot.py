import logging.config
import settings

from logging_config import LOGGING_CONFIG
from test_states import statess
from read_questios_from_file import open_file
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from handlers import info_view, talk_bot, vacansies_list, save_document
from anketa import start, anketa_dontknow

def main():
    mybot = Updater(settings.BOT_API, use_context=True)
    
    dp = mybot.dispatcher

    anketa = ConversationHandler(
        entry_points=[MessageHandler(
        Filters.regex("^(QA Automation|Java Developer|Java 2 Developer|Android Developer|IOS developer|SQL Developer)$"), 
        start)], 
        states=statess,
        fallbacks=[MessageHandler(Filters.video | Filters.photo | Filters.document
          | Filters.location, anketa_dontknow)]
    )

    dp.add_handler(anketa)
    dp.add_handler(CommandHandler('info', info_view))
    dp.add_handler(CommandHandler('openfile', open_file))
    dp.add_handler(MessageHandler(Filters.regex('^(Информация о боте)$'), info_view))
    dp.add_handler(MessageHandler(Filters.regex('^(Начать беседу)$'), vacansies_list))
    dp.add_handler(MessageHandler(Filters.document, save_document))
    dp.add_handler(MessageHandler(Filters.text, talk_bot))

    logging.config.dictConfig(LOGGING_CONFIG)

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()