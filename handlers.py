from utils import info_bot, main_keyboard, vacansies_keyboard
from  telegram  import KeyboardButton, Update, ReplyKeyboardMarkup


def info_view(update, context):
    info_bots = info_bot()
    update.message.reply_text(f'{info_bots}',reply_markup=main_keyboard())

def start(update: Update, context) -> None:
    keyboard = [
        [
            KeyboardButton("Информация о боте", callback_data='1'),
            KeyboardButton("Начать тест", callback_data='2'),
        ],
        [KeyboardButton("У тебя есть вопросы?", callback_data='3')],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    
def user_contact(update, context):
    contacts = update.message.contact
    update.message.reply_text(f'Ваши контакты {contacts}')

def talk_bot(update, context):
    print(update)
    text = 'Выбирите один из вариантов ответа'
    update.message.reply_text(f'{text}',reply_markup=main_keyboard())
    
def vacansies_list(update, context):
    print(update)
    text = 'Выберите вакансию, которую рассматриваете'
    update.message.reply_text(f'{text}',reply_markup= vacansies_keyboard())
    

