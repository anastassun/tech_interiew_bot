# tech_interiew_bot
Чат-бот: проведение тех интервью - чат-бота для Telegram, который проводит тех интервью по списку вопросов на разные должности с заранее фиксированным временем на ответ

Ключевые возможности:
1. При старте бот выводит информацию об правилах прохождения опроса.
2. Далее запускает процесс вопрос-ответ и запускает таймер отсчета времени на ответ
3. За 10 секунд до окончания времени информирует пользователя об этом событии
4. В конце благодарит за прохождение опроса
5. Записывает ответы респодента в файл ворд, который высылает на заданный адрес электронной почты

## <br><b>Установка</b>

### <br><b>Откройте консоль</b>

<b>Выполните в консоле</b>             
    <details><summary> Команды: </summary>
```
git clone https://github.com/anastassun/tech_interiew_bot.git
pip install -r requirments.txt
```
</details>

### <br><b>Настройка</b>

<b>Создайте файл *settings.py* и добавьте туда следующие параметры</b>
    <details>
    <summary> Параметры: </summary></b>
```
BOT_API = 'Ключ от BotFather'
ADMIN = (telegram_id,)
MONGO_LINK = 'адрес базы данных'
MONGO_DB = 'название базы данных'
LOGIN_MAIL = 'адрес отправителя'
PASSWORD_MAIL = 'пароль для приложений от почты'
SEND_MAIL = 'адрес получателя'
SERVER_MAIL = 'сервер вашей почты SMTP'
```
</details>

### <br><b>Наполнение базы данных</b>

<b>Отправьте боту файл в формате .txt или .docx</b>
    <details>
    <summary> Оформление файла: </summary>
```
Название вакансии '*' - указывается около вакансии.
Вопрос
```
</details>

### <br><b>Запуск</b>
<b>Чтобы запустить бота, выполните в консоле</b>
    <details>
    <summary> Команда запуска: </summary>
```
python bot.py
```
</details>

