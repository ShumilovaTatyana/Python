# Задание
# Формат: На семинаре и в лекциях мы разобрали новые функции, которые позволяют улучшить код прошлых задач.
# Задача: предложить улучшения кода для уже решённых задач(не менее 4 задач нужно улучшить):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) -
#  исходите из уровня группы и студента.

# n = int(input('Введите число N: '))
# num = list(range(-n, n+1))
# print(num)

# def f(x):
#     return x**2
# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)  

string_input = input("введите строку: ")
if string_input == '':
    string_input = "привет абв мир улеабвтел"

# ------ filter()
string_result = string_input.split(' ')
string_result = filter(lambda s: not 'абв' in s , string_result)
print (' '.join(list(string_result)), ' <-- filter()')

# ------ python comrehension
string_result = string_input.split(' ')
string_result = [s for s in string_result if s.find('абв') == -1] # not 'абв' in s | s.find('абв') == -1 (Аналоги)
print (' '.join(list(string_result)), ' <-- python comrehension')

1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0.56 -> 11

# print(sum(map(int, [item for item in input('Введите вещественное число ') if item != '.'])))

Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def fun(x):
#     return 1 if x == 1 else x * fun(x - 1)
# print(list(fun(i) for i in range(1, int(input('Введите натуральное число ')) + 1)))

Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# print(tuple(((not(x and y and z) == (not(x) or not(y) or not(z))) for z in range(2) for y in range(2) for x in range(2))))

Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19


# input = [1.1, 1.2, 3.1, 10.01]
# print(max(map(fract:= lambda x: float(fr:=str(x).split('.')[1])/10**(len(fr)), input)) - min(map(fract, input)))

Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil
input = [2, 3, 4, 5, 6]
print(list(input[i] * input[-i-1] for i in range(ceil(len(input)/2))))
