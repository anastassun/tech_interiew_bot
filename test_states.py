from telegram.ext import MessageHandler, Filters
from anketa import  name, discussion, quest, num_qestion, final

NAME, DISCUSSION, QUESTION, NUMQUESTION, CONTACT, FINAL = range(6)

statess={
            NAME: [MessageHandler(Filters.text, name)],
            DISCUSSION: [MessageHandler(Filters.text, discussion)],
            QUESTION: [MessageHandler(Filters.text, quest)],
            NUMQUESTION: [MessageHandler(Filters.text, num_qestion)],
            #CONTACT: [
                #MessageHandler(Filters.location, location),
                #CommandHandler('skip', skip_location),
            #],
            FINAL: [MessageHandler(Filters.text & ~Filters.command, final)]
        }