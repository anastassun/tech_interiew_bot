from db import db, get_or_create_job
from open_console_file import open_file

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

def info_job():
    key = input('Введите код документа: ')
    try:
        vacancy, company = name_vacan_and_company()
    except TypeError:
        return info_job()
    name_file = input("Введите имя загруженного файла вместе с .txt: ")
    info = open_file(name_file)
    job_info = {'secret_key': key, 'vacancy': vacancy, 'company': company, 'blank_form': info}
    return job_info

if __name__ == '__main__':
    file = info_job()
    get_or_create_job(db, file)