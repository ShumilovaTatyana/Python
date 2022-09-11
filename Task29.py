# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# https://ru.wikipedia.org/wiki/Негафибоначчи#:~:text=В%20математике%2C%20числа%20негафибоначчи%20—%20отрицательно%20индексированные%20элементы%20последовательности%20чисел%20Фибоначчи.)



f1 = 1
f2 = 1
n = (int(input('Введите число n: ')))
print(f1,f2,end=' ')
while n>2:
    f1, f2 = f2, f1+f2
    print(f2, end=' ')
    n -=1
while n<2:
    f1, f2 = f2, f1-f2
    print(f2, end=' ')
    n +=1 






# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))
