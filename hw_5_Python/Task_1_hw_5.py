# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print("Данная программа удаляет все слова, содержащие 'абв'")

text = list(input("Введите текст: ").split())
print("Итоговый текст: ")
[print(text[i], end=' ') for i in range(len(text)) if 'абв' not in text[i]]
