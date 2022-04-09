from telegram.ext import MessageHandler, Filters
from anketa import  name, discussion, quest, num_qestion, final, contact

NAME, DISCUSSION, QUESTION, NUMQUESTION, CONTACT, FINAL = range(6)

statess={
            NAME: [MessageHandler(Filters.text, name)],
            DISCUSSION: [MessageHandler(Filters.text, discussion)],
            QUESTION: [MessageHandler(Filters.text, quest)],
            NUMQUESTION: [MessageHandler(Filters.text, num_qestion)],
            CONTACT: [MessageHandler(Filters.text, contact)],
            FINAL: [MessageHandler(Filters.text & ~Filters.command, final)]
        }