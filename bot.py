from multiprocessing import context
from turtle import update
from telegram.ext import Updater, CommandHandler
def greet_user(update,context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def main():
    mybot = Updater("5262680588:AAHXaXg_gIpLk0ANWwmtKg5xbwCgD2Y0koM", use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    print("bot_online")
    mybot.idle()

main()


    