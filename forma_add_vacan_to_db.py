from db import db, get_or_create_job

# Ручное добавление данных в базу.

def name_vacan_and_company():
    vacancy = str(input("Введите название вакансии: ")).strip()
    if not vacancy:
        print("Нужно ввести название")
        return name_vacan_and_company
    company = str(input("Введите название компании: ")).strip()
    if not company:
        print("Нужно ввести название")
        return name_vacan_and_company
    else:
        return vacancy, company

def slot_quest():
    blank_forms = input("Введите количество вопросов: ")
    check_res = slot_in_company(blank_forms)
    if check_res == "+":
        return slot()
    else:
        return int(blank_forms)

def slot():
    blank_forms = input("Введите количество вакансий для этой компании: ")
    check_res = slot_in_company(blank_forms)
    if check_res == "+":
        return slot()
    else:
        return int(blank_forms)

def slot_in_company(num):
    if num:
        try:
            good_num = abs(int(num))
        except (TypeError, ValueError):
            print("Введите целое число")
            return "+"
        return '-'

def info_job():
    key = input('Введите код документа: ')
    try:
        vacancy, company = name_vacan_and_company()
    except TypeError:
        return info_job()
    job_info = {'secret_key': key, 'vacancy': vacancy, 'company': company, 'blank_form': dict()}
    num = slot()
    requireds = dict()
    for _ in range(num):
        required = str(input("Введите название специальности: ")).strip()
        if not required:
            print("Ошибка, название не введено, начнем заного.")
            return info_job()
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
    file = info_job()
    job = get_or_create_job(db, file)

