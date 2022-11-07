from random import randint


def start(x):
    with open("files/FirstNamesF.txt", encoding="utf-8") as file:
        firstnames = file.read().split()
        file.close()

    with open("files/LastNamesF.txt", encoding="utf-8") as file:
        lastnames = file.read().split()
        file.close()

    with open("files/MiddleNamesF.txt", encoding="utf-8") as file:
        midnames = file.read().split()
        file.close()

    fullnames = []

    for i in range(0, x):
        fullname_str = f"{lastnames[randint(0, len(lastnames) - 1)]} " \
                       f"{firstnames[randint(0, len(firstnames) - 1)]} " \
                       f"{midnames[randint(0, len(midnames) - 1)]}"
        fullnames.append(fullname_str)

    with open("files/Fmen_full_names.txt", "w", encoding="utf-8") as file:
        for i in range(len(fullnames)):
            file.write(fullnames[i])
            file.write("\n")
        file.close()

    if __name__ == "__main__":
        print(firstnames)
        print(lastnames)
        print(midnames)
        print(fullnames)
