# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# https://ru.wikipedia.org/wiki/Негафибоначчи#:~:text=В%20математике%2C%20числа%20негафибоначчи%20—%20отрицательно%20индексированные%20элементы%20последовательности%20чисел%20Фибоначчи.)



# f1 = 1
# f2 = 1
# n = (int(input('Введите число n: ')))
# print(f1,f2,end=' ')
# while n>2:
#     f1, f2 = f2, f1+f2
#     print(f2, end=' ')
#     n -=1
# while n<2:
#     f1, f2 = f2, f1-f2
#     print(f2, end=' ')
#     n +=1 

# a = int(input('Enter the number: '))
# print(a)
# negofibonacci = [1,-1]
# fibonacci = [1,1]

# for i in range(2,a):
#     list = fibonacci[i-1]+fibonacci[i-2]
#     fibonacci.append(list)
#     list_nego = negofibonacci[i-2] - negofibonacci[i-1]
#     negofibonacci.append(list_nego)

# negofibonacci.reverse()
# negofibonacci.append(0)

# print(f' for a = {a} =>{negofibonacci+fibonacci}')

# n = int(input('Введите число: '))
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# set1 = [0]
# set2 = []
# for i in range(1, 10):
#     set1.append(fib(i))
#     set2.append(fib(i)*-1)
# for i in range(len(set2)):
#     if i%2==0:
#         set2[i]= -set2[i]
# set3 = set2[::-1]
# print(set3+set1)



def lst_fibonacci_num():
    num = int(input('Введите любое натуральное число: '))
    fib = []
    a, b = 1, 1
    for i in range(num):
        fib.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for j in range(num + 1):
        fib.insert(0, a)
        a, b = b, a - b
    print(f'Список чисел Фибоначчи для {num}: {fib}')
lst_fibonacci_num()


# fib = int(input('5# введите число for fib = '))
# res_5 = []
# for i in range(fib+1):
#     if i==0:
#         res_5.append(i)
#     elif i==1:
#         res_5.append(i)
#         res_5.insert(0, i)
#     else:
#         res_5.append(res_5[len(res_5)-1]+res_5[len(res_5)-2])
#         res_5.insert(0, (-1)**(i-1)*res_5[len(res_5)-1])
# print(res_5)








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
