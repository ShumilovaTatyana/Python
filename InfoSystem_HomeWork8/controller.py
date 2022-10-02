from view import (show_menu, print_result, get_search_name,
                  get_search_number, get_new_student, get_file_name)
from model import write_txt, write_csv, read_csv, find_by_name, find_by_number, add_student 

def work_with_data_base():
    choice = show_menu()
    db = read_csv('data_base.csv')


    while (choice != 6):
        if choice == 1:
            print_result(db)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(db, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(db, number)) 
        elif choice == 4:
            user_data = get_new_student()
            add_student(db, user_data) 
            write_csv('data_base.csv', db) 
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, db) 
        choic = show_menu()                  