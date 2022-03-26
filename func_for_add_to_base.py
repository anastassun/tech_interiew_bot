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

def create_dict_db(key, vacancy, company, blank):
    db_dict = {'secret_key': key, 'vacancy': vacancy, 'company': company, 'blank_form': blank}
    return db_dict
    
