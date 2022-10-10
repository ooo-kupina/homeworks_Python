# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

print("Данная программа составит список простых множителей числа N,\n\
которое задаёт пользователь.")
number = int(input('Введитe натуральное число N: '))
N = number
multipliers = []
for i in range(2, int(number ** 0.5) + 2):
    while number % i == 0:
        multipliers.append(i)
        number //= i
if number != 1:
    multipliers.append(number)
print(f"Список простых множителей числа {N}: {multipliers}")
