from random import randrange
from datetime import timedelta
from datetime import datetime


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def start(x):
    d1 = datetime.strptime('1/1/1945', '%m/%d/%Y')
    d2 = datetime.strptime('1/1/2005', '%m/%d/%Y')

    birthdays = []

    for i in range(x):
        birthdays.append(random_date(d1, d2).strftime("%Y-%m-%d"))

    with open("files/Birthdays.txt", "w", encoding="utf-8") as file:
        for i in range(len(birthdays)):
            file.write(birthdays[i])
            file.write("\n")
        file.close()

    if __name__ == "__main__":
        print(birthdays)
