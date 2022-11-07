# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

print("Данная программа вычисляет арифметическое выражение, заданного строкой.\n\
Например, выражение 2*(5+2)/7 даст результат 2.\n\
Строковое выражение вводит пользователь.")

import os

expression = input("Введите арифметическое выражение: ")

file = open("Python_help_me.py", "w")

file.write(f"print({expression})")

file.close()

# os.system("Python_help_me.py")

from subprocess import Popen, PIPE

out, err = Popen('python3 Python_help_me.py', shell=True, stdout=PIPE).communicate()
result = str(out, 'utf-8')
# print(str(out, 'utf-8')) # или var = str(out, 'utf-8')
print(f"Результат: {expression} = {result}")
