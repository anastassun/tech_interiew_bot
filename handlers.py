import os

from utils import info_bot, main_keyboard, vacansies_keyboard
from test_question import list_quest, dict_answer
from db import db, get_or_create_user

def info_view(update, context):
    print(update)
    info_bots = info_bot()
    update.message.reply_text(f'{info_bots}',reply_markup=main_keyboard())
    user = get_or_create_user(db, update)

def talk_bot(update, context):
    
    text = 'Загружаю кнопки'
    update.message.reply_text(f'{text}',reply_markup=main_keyboard())

def user_contact(update, context):
    contacts = update.message.contact
    update.message.reply_text(f'Ваши контакты {contacts}')

def test(update, context):
    for index,key in enumerate(list_quest):
        questions = list_quest[index]
        answer = dict_answer[key]
        message = context.bot.send_poll(
            update.effective_chat.id, questions, answer, 
            is_anonymous=True, allows_multiple_answers=True,
        )
        payload = {
            message.poll.id: {
                "questions": questions,
                "message_id": message.message_id,
                "chat_id": update.effective_chat.id,
                "answers": 0,
            }
        }
    context.bot_data.update(payload)

def vacansies_list(update, context):
    text = 'Выберите вакансию, которую рассматриваете'
    update.message.reply_text(f'{text}',reply_markup= vacansies_keyboard())

def save_document(update, context):
    user = db.users.find_one({"user_id" : update.effective_user.id})
    update.message.reply_text('Обрабатываем фaйл')
    file_name = os.path.join('donwloads', f"{update.message.caption}.txt")
    if user['role'] == 'ADMIN':
        os.makedirs('donwloads', exist_ok=True)
        document_file = context.bot.getFile(update.message.document.file_id)
        document_file.download(file_name)
        update.message.reply_text(f'Администратор, файл сохранен под именем {update.message.caption}.txt')
    else:
        update.message.reply_text('Ошибка доступа')