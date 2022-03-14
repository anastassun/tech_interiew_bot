from telegram import ReplyKeyboardMarkup

def info_bot():
    with open('bot_info.txt', 'r', encoding='utf8') as f:
        return f.read()

def start_keyboard():
    return ReplyKeyboardMarkup([
        ["Информация о боте",  
        "Начать тест", "Есть вопросы?"]
        ])

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
        ["Android Developer"],
        ['QA Automatio'],
        ["IOS developer"],
        ["SQL Developer"]
        ]
    )


    