from telegram import ReplyKeyboardMarkup

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
