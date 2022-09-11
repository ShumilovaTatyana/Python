# (ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

# a = []
# n = int(input("Ведите N: ")) 
# x = -n 
# for i in range(x, n+1):
#      a.append(i)
# print(a)


N = 5
list1 = []
for n in range(-N, N+1):
     list1.append(n)
print(f"Заданный список = {list1}")

def read_file():
     with open('file18.txt', 'r') as data:
          positions = list1(map(int, data.readlines()))
          print(f"Индексы из файла = {positions}")
     return positions

f = read_file()
composition = 1
for i in range(len(f)):
     composition *= list1[f[i]] 
print(f"Произведение элементов = {composition}") 


