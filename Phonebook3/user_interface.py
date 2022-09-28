import data_provider as prov
import logger as log

def name_view(sensor):
    info = prov.get_name(sensor)
    log.name_logger(info)
    return info

def num_view(sensor):
    info = prov.get_num(sensor)
    log.num_logger(info)
    return info

def text_view(sensor):
    info = prov.get_text(sensor)
    log.text_logger(info)
    return info

import data_provider as prov
import logger as log

# def get_data():
#     name = input("Введите имя: ")
#     num = input("Введите номер телефона: ")
#     text = input("Введите описание: ")
    
#     return f'{name}; {num}; {text};'.title()
 
# print(get_data())    