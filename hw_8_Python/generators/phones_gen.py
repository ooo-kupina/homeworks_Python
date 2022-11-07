from random import randint


def start(x):
    opers = ["+7 (915)", "+7 (962)"]

    phones = []

    for i in range(0, x):
        phones.append(f"{opers[randint(0, len(opers) - 1)]} {randint(202, 999)}-"
                      f"{randint(0, 9)}{randint(0, 9)}-"
                      f"{randint(0, 9)}{randint(0, 9)}")

    with open("files/Phones.txt", "w", encoding="utf-8") as file:
        for i in range(len(phones)):
            file.write(f"{phones[i]}\n")

    if __name__ == "__main__":
        print(phones)
