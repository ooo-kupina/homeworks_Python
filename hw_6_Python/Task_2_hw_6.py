# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

print("Данная программа выводит случайную исходную последовательность,\n\
получает список её уникальных элементов, список повторяемых и убирает из неё дубликаты.\n\
Размер исходной последовательности задаёт пользователь.")

import random

n = int(input("Введитe размер исходной последовательности: "))
lst = []
for i in range(n):
    lst.append(random.randint(1, 10))
print(f"Исходная последовательность: {lst}")

numbers = lst
undub = list(set(numbers))
dub = []
unique = []

[unique.append(i) for i in numbers if numbers.count(i) < 2]
[dub.append(i) for i in numbers if numbers.count(i) > 1 and i not in dub]

print(f"Уникальные элементы: {unique}")
print(f"Дубликаты в последовательности: {dub}")
print(f"Последовательность без дублирования элементов: {undub}")