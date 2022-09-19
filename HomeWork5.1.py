# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = 'Привет, абвгдейка! Как дела? абв'
print(f'Исходный текст: {text}')
def remove_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)
text = remove_words(text)
print(f'Итоговый текст: {text}')


# text = input('Введите исходный текст через пробел: ')
# find_text = "абв"
# list = [i for i in text.split() if find_text not in i]
# print(f'Итоговый текст: {" ".join(list)}')