# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

print("Данная программа из N элементов, заполненных числами из промежутка [-N, N], выводит\n\
произведение элементов на указанных позициях, которые хранятся в файле file.txt.")

n = int(input('Введите число N: '))
print(f"Список от -N до N: ")
print(*range(-n, n + 1), sep=', ')
object = 'file.txt'
object_2 = 'file_2.txt'

from random import randint

def get_numbers(n):
    return [randint(-n/2, n) for i in range(-n, n + 1)]

def get_data_from_file(object):
    data = open(object, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def writing_file(k: int, n: int):
   with open('../../Other/file_2.txt', 'w') as position:
       for i in range(k):
           position.write(f'{random.randint(-n, n-1)}\n')

def get_data_from_file_2(object_2):
    data = open(object_2, 'r')
    dlist_2 = [int(line.strip()) for line in data]
    data.close()
    return dlist_2


def print_position():
   path = '../../Other/file_2.txt'
   position = open(path, 'r')
   pos_element = []
   for line in position:
    pos_element.append(int(line))
   print(f'Список элементов в указанных позициях: {pos_element}')
   position.close()
   return pos_element

def get_mult(num, datalist):
    mult = 1
    for i in datalist:
        mult *= num[i]
    return mult


datalist = get_data_from_file(object)
datalist_2 = get_data_from_file_2(object_2)
numbers = get_numbers(n)

print(f"Список случайных чисел в промежутке от -N до N: {numbers}")
print(f"Список из файла: {datalist}")
print(f"Список позиций: {numbers}")
print(f"Список элементов из файла № 2 с получившимися позициями: {datalist_2}")
print_position()
# print(get_mult(numbers, datalist))
print()
print("Не могу полностью решить эту задачу! Очень устала!\n\
Задача трудная, не хватает опыта в программировании!")
