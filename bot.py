from multiprocessing import context
from turtle import update
from telegram.ext import Updater, CommandHandler

from token import TOKEN
def greet_user(update,context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def main():
    mybot = Updater(TOKEN, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    print("bot_online")
    mybot.idle()

main(
    