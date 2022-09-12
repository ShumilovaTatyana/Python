# (ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

import random
list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    list[i], list[index_a] = list[index_a], list[i]
print(list)

# import random
# list = ["Anna", "Alex", 3.14159, 0]
# for i in range(len(list)):
#     index_a = random.randint(0, len(list) - 1)
#     temp = list[i]
#     list[i] = list[index_a]
#     list[index_a] = temp
# print(list)


# from random import shuffle
# some_list = ['a', 'b', 'c', 'd', 'f']
# shuffle(some_list)
# print(some_list)


# from random import randint
# n = int(input('Введите число N - '))
# numbers = []
# for i in range(n):
#     numbers.append(randint(-n, n))
# print(numbers)

# f = open('file181.txt', 'w') # создать файл, если его нет
# while True:
#     s = input('Укажите позицию для вычисления - ')
#     if s == "":
#         break
#     f.write(s+"\n")
# f.close()

# result = 1
# f = open('file181.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)]
# f.close()
# print(result)


# n = int(input('Введите N: '))
# a = []
# for i in range(-n, n+1):
#     a.append(i)
# print(a, sep=',')

# l = []
# with open('file18.txt', 'r') as f:
#     for line in f:
#         l.append(int(line))

# c = l[0]
# d = l[1]
# k = a[c]*a[d]
# print('Произведение элементов на указанных в файле позициях = ', k)


# a = []
# n = int(input("Ведите N: ")) 
# x = -n 
# for i in range(x, n+1):
#      a.append(i)
# print(a)


# N = 5
# list1 = []
# for n in range(-N, N+1):
#      list1.append(n)
# print(f"Заданный список = {list1}")

# def read_file():
#      with open('file18.txt', 'r') as data:
#           positions = list1(map(int, data.readlines()))
#           print(f"Индексы из файла = {positions}")
#      return positions

# f = read_file()
# composition = 1
# for i in range(len(f)):
#      composition *= list1[f[i]] 
# print(f"Произведение элементов = {composition}") 


