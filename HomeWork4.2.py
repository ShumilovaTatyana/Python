# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число N: "))
# i = 2 
# list = []
# number = num
# while i <= num:
#     if num % i == 0:
#         list.append(i)
#         num //= i
#         i = 2
#     else:
#         i = i + 1
# print(f"Простые множители числа {number} = {list}")

n = int(input("Введите число N: "))
i = 2 
list = []

while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители введенного числа указаны в списке: {list}")

