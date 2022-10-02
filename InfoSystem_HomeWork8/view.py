def show_menu() -> int:
    print('\nВыберите наобходимое действие:\n'
        "1. Отобразить весь список студентов\n"
        "2. Найти студента по фамилии\n"
        "3. Найти студента по номеру телефона\n"
        "4. Добавить студента в базу данных\n"
        "5. Сохранить базу данных в текстовом формате\n"
        "6. Закончить работу\n")
    choice = int(input())
    return choice

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)

def get_search_name() -> str:
    return input("Введите фамилию для поиска")

def get_search_number() -> str:
    return input("Введите номер телефона для поиска") 

def get_new_student() -> str:
    last_name = input("Введите фамилию студента: ")
    first_name = input("Ввдеите имя студента: ")
    phone_number = input("Введите номер телефона студента: ")
    specialty = input("Введите специальность студента: ") 
    return f'{last_name}, {first_name}, {phone_number}, {specialty}'

def get_file_name() -> str:
    return input("Введите название файла для сохраниения: ")
