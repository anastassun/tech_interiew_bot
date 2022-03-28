from db import db, get_or_create_job
from open_console_file import open_file
from func_for_add_to_base import name_vacan_and_company, slot, slot_quest, create_dict_db

def variable():
    quest = (input("В бота загружен файл нужного формата, ответьте ДА или НЕТ: ").strip()).lower()
    if quest == 'да':
        return info_job_file()
    return info_job_arm()

def info_job_file():
    key = input('Введите код документа: ')
    try:
        vacancy, company = name_vacan_and_company()
    except TypeError:
        return info_job_file()
    name_file = input("Введите имя загруженного файла вместе с .txt: ")
    info = open_file(name_file)
    job_info = create_dict_db(key, vacancy, company, info)
    return job_info

def info_job_arm():
    key = input('Введите код документа: ')
    try:
        vacancy, company = name_vacan_and_company()
    except TypeError:
        return info_job_arm()
    job_info = {'secret_key': key, 'vacancy': vacancy, 'company': company, 'blank_form': dict()}
    num = slot()
    requireds = dict()
    for _ in range(num):
        required = str(input("Введите название специальности: ")).strip()
        if not required:
            print("Ошибка, название не введено, начнем заного.")
            return info_job_arm()
        else:
            quest_num = slot_quest()
            quest_list = dict()
            for num in range(1,quest_num+1):
                quest = str(input(f"{num} Введите вопрос: ")).strip()
                quest_list[str(num)] = quest
            requireds[required] = quest_list
        job_info["blank_form"] = requireds
    return job_info

if __name__ == '__main__':
    file = variable()
    get_or_create_job(db, file)