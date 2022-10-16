# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.20

print("Данная программа найдёт разницу между максимальным и минимальным \n\
значением дробной части элементов случайного списка вещественных чисел.\n\
Размер списка задаёт пользователь.")
import random
N = int(input('Задайте размер списка N: '))
list = []
for i in range(N):
    list.append(round(random.uniform(0, 10), 4))
min = list[0]-int(list[0])
max = list[0]-int(list[0])

for item in list:
    if item-int(item) <= min:
        min = round(item-int(item), 4)
    if item-int(item) >= max:
        max = round(item-int(item), 4)
res = 0
res = round(max-min, 4)
print(f'Сгенерированный список {list} \nМакс и мин дробная часть списка {max} и {min} \nИх разница {res}')
