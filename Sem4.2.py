# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

str = '12 32 0 15'
lst = [int(i) for i in str.split()]
print(min(lst))
print(max(lst))

# n= '3 5 1 7 9 2 5'
# min=int(n[0])
# max=int(n[0])
# for i in n.split(sep= ' '):
#     if int(i)<min:       
#         min=int(i)
#     if int(i)>max:
#         max=int(i)
# print (min,max)


# list = [8, 2, 3, 4, 5]
# min_num = 1
# max_num = 0
# for i in list:
#     if i <= min_num:
#         min_num = i
#     if i >= max_num:
#         max_num = i        
# print(min_num, max_num)


# my_list = [1, 3, 2, 4, 3, 5, -2]
# print(max(my_list), min(my_list))


# print(my_list, '->', max(my_list), min(my_list))



