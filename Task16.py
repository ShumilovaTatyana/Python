# (ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input())
res = [1]
for i in range(2, n + 1):
    res.append(res[-1] * i)
print(res)

# num = int(input())
# f = 1
# for i in range(1, num + 1):
#         f = f * i
#         print(f, end=' ')


# num = int(input("Введите число N:"))
# proizved = 1
# for i in range(1, num + 1):
#     proizved = proizved * i
#     print(proizved, end=' ')

 