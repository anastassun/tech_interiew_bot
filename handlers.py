import os
import constants

from utils import info_bot, main_keyboard, vacansies_keyboard
from db import db, get_or_create_user

def decor_func_registration(func):
    def wrapper(*args, **kwargs):
        update, context = args
        user = get_or_create_user(db, update)
        func(update, context, user)
    return wrapper

def info_view(update, context):
    info_bots = info_bot()
    update.message.reply_text(f'{info_bots}',reply_markup=main_keyboard())

@decor_func_registration
def talk_bot(update, context, user):
    text = 'Загружаю кнопки'
    update.message.reply_text(f'{text}',reply_markup=main_keyboard())

def vacansies_list(update, context):
    text = 'Выберите вакансию, которую рассматриваете'
    update.message.reply_text(f'{text}',reply_markup= vacansies_keyboard())

@decor_func_registration
def save_document(update, context, user):
    update.message.reply_text('Обрабатываем фaйл')
    file_name = os.path.join('donwloads', f"{update.message.caption}.txt")
    if user['role'] == constants.ADMIN:
        os.makedirs('donwloads', exist_ok=True)
        document_file = context.bot.getFile(update.message.document.file_id)
        document_file.download(file_name)
        update.message.reply_text(f'Администратор, файл сохранен под именем {update.message.caption}.txt')
    else:
        update.message.reply_text('Ошибка доступа')