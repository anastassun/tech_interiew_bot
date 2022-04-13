from telegram.ext import MessageHandler, Filters, CallbackQueryHandler
from anketa import  name, discussion, quest, num_qestion, final, contact, yes, no

NAME, DISCUSSION, QUESTION, NUMQUESTION, CONTACT, FINAL = range(6)

statess={
            NAME: [MessageHandler(Filters.text, name),
            CallbackQueryHandler(yes, pattern='^' + 'ДА' + '$'),
            CallbackQueryHandler(no, pattern='^' + 'НЕТ' + '$')],
            DISCUSSION: [MessageHandler(Filters.text, discussion)],
            QUESTION: [MessageHandler(Filters.text, quest)],
            NUMQUESTION: [MessageHandler(Filters.text, num_qestion)],
            CONTACT: [MessageHandler(Filters.text, contact),
            CallbackQueryHandler(yes, pattern='^' + 'ДА' + '$'),
            CallbackQueryHandler(no, pattern='^' + 'НЕТ' + '$')],
            FINAL: [MessageHandler(Filters.text & ~Filters.command, final)]
        }