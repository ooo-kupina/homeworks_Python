# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


print("Данная программа создаёт содержимое двух файлов poly_1.txt и poly_2.txt,\n\
в которых сохраняются записи многочленов, сгенерированных случайным образом в интервале\n\
от 0 до 100, и формирует файл sum_poly.txt, содержащий сумму этих многочленов.\n\
Степени k1 многочлена №1 и k2 многочлена №2 задаёт пользователь.")

import numpy.polynomial
from numpy.polynomial import Polynomial as P
import os
from random import randint
k1 = int(input('Введите степень многочлена №1 k1: '))
k2 = int(input('Введите степень многочлена №2 k2: '))
set1 = [randint(0, 100) for i in range(k1 + 1)]
set2 = [randint(0, 100) for j in range(k2 + 1)]
print(f"Список коэффициентов многочлена №1: {set1}")
print(f"Список коэффициентов многочлена №2: {set2}")

p1 = P(set1)
p2 = P(set2)
print(f"Многочлен №1 = {p1}")
print(f"Многочлен №2 = {p2}")
s = p1 + p2
print(f"Сумма многочленов №1 и №2 = {s}")

result_dir = 'files'

# if not os.path.exists(result_dir):	# если данная директория не существует,
#     os.mkdir(result_dir) # то ее необходимо создать
# Хотела сделать, чтобы файлы создавались в директории files
# но у меня почему-то не получилось.

with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write(f"{p1}")
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write(f"{p2}")

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

sum_poly = p1 + p2
print(f'Записан файл sum_poly.txt с содержимым ({p1}) + ({p2}) = {sum_poly}')

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'({p1}) + ({p2}) = {sum_poly}')
