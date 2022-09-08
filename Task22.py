# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
# # Тесты
# print(to_dict([1, 2, 3, 4]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))

# list_string = [1, 2, 3, 4]
# dict_list = {}
# for k in list_string:
#     #dict_list.update(list_string[k]=list_string[k])
#     dict_list = dict{[1, 2, 3, 4]}
# print(dict_list)    

def to_dict(lst):
    return {element: element for element in lst}
print(to_dict([1, 2, 3, 4]))
print(to_dict(['grey', (2, 17), 3.11, -4]))

