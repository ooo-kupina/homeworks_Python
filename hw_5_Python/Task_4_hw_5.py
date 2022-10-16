# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# RRRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUYYYYYYYYYYYYYYYSSSSSSSSSSSSSSSSS
# Выходные данные:
# 22R1U15U1Y15Y1S

print("Данная программа реализует модуль сжатия и восстановления данных.\n\
Входные и выходные данные хранятся в отдельных текстовых файлах file_decode.txt и file_encode.txt\n\
Пример на сжатие:\n\
Входные данные:\n\
RRRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUYYYYYYYYYYYYYYYSSSSSSSSSSSSSSSSS\n\
Выходные данные:\n\
2R1U15U1Y15Y1S\n")


with open('file_encode.txt', 'w') as data:
    data.write('RRRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUYYYYYYYYYYYYYYYSSSSSSSSSSSSSSSSS')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Строка № 1 сжимаемая: \t' + decoded_string)
print(f"Длина строки № 1: \t{len(decoded_string)}")
print('Строка № 2 сжатая: \t' + rle_encode(decoded_string))
print(f"Длина строки № 2: \t{len(encoded_string)}")
print("Степень сжатия: ")
enc_on_dec = len(encoded_string) / len(decoded_string)
percentage1 = "{:.2%}".format(enc_on_dec)  # Отношение размера сжатой строки к несжатой
print(f'Отношение размера сжатой строки к несжатой: \t{percentage1}')
dec_on_enc = len(decoded_string) / len(encoded_string) # Во сколько раз несжатая строка превосходит сжатую
size = round(dec_on_enc, 1)  # Отношение размера несжатой строки к сжатой
print(f'Во сколько раз несжатая строка превосходит сжатую: \t{size}')
