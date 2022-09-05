# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# a = 'pyt'
# b = 'pythonpythonpython'
# count = 0
# for i in range(0, len(b) - len(a)):
#     if b[i:i + len(a)] == a:
#         count += 1 
# print(count)

string_1 = input('Введите строку 1: ')
string_2 = input('Введите строку 2: ')
if string_1 > string_2:
    print(string_1.count(string_2))
else:
    print(string_2.count(string_1))

