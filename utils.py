from telegram import ReplyKeyboardMarkup
import datetime
import settings

def info_bot():
    with open('bot_info.txt', 'r', encoding='utf8') as f:
        return f.read()

def main_keyboard():
    return ReplyKeyboardMarkup([
        ["Информация о боте",  
        "Начать тест"]
        ])

def vacansies_keyboard():
    return ReplyKeyboardMarkup(
        [ 
        ["Java Developer"], 
        ["Java 2 Developer"] , 
        ["Android Develope"],
        ['QA Automatio'],
        ["IOS developer"],
        ["SQL Developer"]
        ]
    )

def get_current_time(times):
    delta = datetime.timedelta(hours=3, minutes=0)
    current_time = times + delta
    times = datetime.datetime.strftime(current_time, "%d.%m.%y %H:%M")
    return times

def check_role(user_id):
    if user_id in settings.ADMIN:
        return 'ADMIN'
    else:
        return 'users'