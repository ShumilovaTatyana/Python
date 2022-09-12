# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
min_num = 1
max_num = 0
for i in list:
    if (i - int(i)) <= min_num:
        min_num = i - int(i)
    if (i - int(i)) >= max_num:
        max_num = i - int(i)        
print(round(max_num - min_num, 2))

