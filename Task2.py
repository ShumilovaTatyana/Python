# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

num = [int(i) for i in input().split()] # split - пробел еще вариант - mlist = list(map(int, input().split()[:n]))
max_number = num[0]
for i in range(len(num)):
    if num[i] > max_number:
        max_number = num[i]
print(num)
print(max_number)

# Вариант 2
# num = [int(i) for i in input().split()]
# max_num = num[0]
# for i in range(len(num)):
#     if num[i] > max_num:
#         max_num = num[i]
# print(num)
# print(max_num)

# Вариант 3
# print(max([int(i) for i in input().split()]))