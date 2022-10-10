# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


print("Данная программа сформирует случайным образом список коэффициентов\n\
(значения от 0 до 100) многочлена и запишет в файл многочлен степени k.\n\
Степень k задаёт пользователь.")
import os
from random import randint
k = int(input('Введите степень многочлена k: '))
set = [randint(0, 100) for i in range(k + 1)]
print(f"Список коэффициентов многочлена: {set}")

terms = []
for coeff in set:
    if coeff:
        coeff = coeff if k == 0 else '' if coeff == 1 else coeff
        ability = 'x' if k == 1 else '' if k == 0 else f'x^{k}'
        term = f'{coeff}{ability}'
        terms.append(term)

    k -= 1
polynom = ' + '.join(terms) + ' = O'
print(f"Многочлен: {polynom}")

result_dir = 'files'

if not os.path.exists(result_dir):	# если данная директория не существует,
    os.mkdir(result_dir) # то ее необходимо создать

with open(f'{result_dir}\\{"_".join(map(str, set))}.txt', 'w', encoding='utf-8') as file:
    file.write(polynom)

name = (f'{"_".join(map(str, set))}.txt')
print(f"Создан файл с именем {name} в директории {result_dir}")
