from utils import info_bot, main_keyboard, vacansies_keyboard
from test_question import list_quest, dict_answer

def info_view(update, context):
    info_bots = info_bot()
    update.message.reply_text(f'{info_bots}',reply_markup=main_keyboard())

def talk_bot(update, context):
    print(update)
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
    print(update)
    text = 'Выберите вакансию, которую рассматриваете'
    update.message.reply_text(f'{text}',reply_markup= vacansies_keyboard())
