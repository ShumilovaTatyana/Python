# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# text = 'Привет, абвгдейка! Как дела? абв'
# print(f'Исходный текст: {text}')
# def remove_words(text):
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return ' '.join(text)
# text = remove_words(text)
# print(f'Итоговый текст: {text}')

# lst = ['впк', 'ыуапку', 'вапабв', 'фкак', 'абв']
# print(*filter(lambda x:not 'абв' in x, lst))


# text = input('Введите исходный текст через пробел: ')
# find_text = "абв"
# list = [i for i in text.split() if find_text not in i]
# print(f'Итоговый текст: {" ".join(list)}')

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
