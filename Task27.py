# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]
# min_num = 1
# max_num = 0
# for i in list:
#     if (i - int(i)) <= min_num:
#         min_num = i - int(i)
#     if (i - int(i)) >= max_num:
#         max_num = i - int(i)        
# print(round(max_num - min_num, 2))

# import math
# list1 = [1.1, 1.2, 3.1, 5, 10.01]
# list2 = []
# for i in range(len(list1)):
#     a = round(list1[i]*10 % 10, 2)
#     if a > 0:
#         list2.append(a)
# b = round(float((max(list2)-min(list2))*10/100), 2)
# print(b)

# from unittest import result
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in my_list:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)  
# print('%.2f' % (max-min))

# list = [1.1, 1.2, 3.1, 10.01]
# mix_list = []

# for i in list:
#     mix_list.append(round(i-int(i), 2))

# print(list, end=' => ')
# print(max(mix_list) - min(mix_list))


# print('задача 3#')
# c = [1.3, 1.4, 20.1, 100.9, 3.001]
# print(c)
# list_c = list(round(c[i]%1, len(c[i])) for i in range(len(c)))
# result_3 = max(list_c)-min(list_c)
# print(f'разница между нецелой частью = {result_3}')

list = [1.1, 1.2, 3.1, 10.01]
min = list[0] % 1
max = list[0] % 1
for i in list:
    item = i % 1    
    if item < min: min = item
    if item > max: max = item
print ('{} min = {} max = {} => {}'.format(list, round(min,2), round(max,2), round(max - min, 2)))

print('задача 3#')
c = [1.3, 1.4, 20.1, 100.9, 3.001]
print(c)
list_c = list(round(c[i]%1, len(str(c[i]))) for i in range(len(c)))
result_3 = max(list_c)-min(list_c)
print(f'разница между нецелой частью = {result_3}')







