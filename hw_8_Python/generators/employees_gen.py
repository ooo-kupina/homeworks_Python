from random import randint


def start():
    with open("files/Men_full_names.txt", encoding="utf-8") as file:
        men_full_name = list(file.read().split("\n"))
        men_full_name.remove("")
        file.close()

    with open("files/FMen_full_names.txt", encoding="utf-8") as file:
        fmen_full_name = list(file.read().split("\n"))
        fmen_full_name.remove("")
        file.close()

    employees = men_full_name + fmen_full_name
    employees_exception = []

    while len(employees) != len(employees_exception):
        k = randint(0, len(employees) - 1)
        if employees[k] not in employees_exception:
            employees_exception.append(employees[k])
        if len(employees) == len(employees_exception):
            break

    with open("files/Phones.txt", encoding="utf-8") as file:
        phones = list(file.read().split("\n"))
        phones.remove("")
        file.close()

    phones_exception = []

    while len(phones) != len(phones_exception):
        k = randint(0, len(phones) - 1)
        if phones[k] not in phones_exception:
            phones_exception.append(phones[k])
        if len(phones) == len(phones_exception):
            break

    with open("files/Birthdays.txt", encoding="utf-8") as file:
        birthdays = list(file.read().split("\n"))
        birthdays.remove("")
        file.close()

    birthdays_exception = []

    while len(birthdays) != len(birthdays_exception):
        k = randint(0, len(birthdays) - 1)
        if birthdays[k] not in birthdays_exception:
            birthdays_exception.append(birthdays[k])
        if len(birthdays) == len(birthdays_exception):
            break

    with open("files/Department.txt", encoding="utf-8") as file:
        department = list(file.readlines())
        departments = []
        for i in range(1, len(department)):
            departments.append(department[i][department[i].find(",") + 3:department[i].find("\n") - 1])
        file.close()

    with open("files/Post.txt", encoding="utf-8") as file:
        post = list(file.readlines())
        posts = []
        for i in range(1, len(post)):
            posts.append(post[i][post[i].find(",") + 1:post[i][post[i].find(",") + 1].find(',')])
        file.close()

    post_exception = []
    post_exception.append(f'{employees_exception[0]}, {posts[0]}')  # Дир
    post_exception.append(f'{employees_exception[1]}, {posts[1]}')  # Зам
    post_exception.append(f'{employees_exception[2]}, {posts[2]}')  # Сек
    post_exception.append(f'{employees_exception[3]}, {posts[3]}')  # Гл. Диз
    post_exception.append(f'{employees_exception[4]}, {posts[4]}')  # Диз
    post_exception.append(f'{employees_exception[11]}, {posts[11]}')  # Гл. Бух
    post_exception.append(f'{employees_exception[12]}, {posts[12]}')  # Бух
    post_exception.append(f'{employees_exception[7]}, {posts[7]}')  # Аналитик
    post_exception.append(f'{employees_exception[10]}, {posts[10]}')  # Тестировщик

    s = 0
    # Инженеры
    while s < 2:
        k = randint(0, len(employees_exception) - 1)
        if employees_exception[k][employees_exception[k].find(",")] not in post_exception:
            post_exception.append(f"{employees_exception[k]}, {posts[6]}")
            s += 1

    s = 0

    # Фронтэнд
    while s < 2:
        k = randint(0, len(employees_exception) - 1)
        if employees_exception[k][employees_exception[k].find(",")] not in post_exception:
            post_exception.append(f"{employees_exception[k]}, {posts[8]}")
            s += 1

    s = 0

    # Бекэнд
    while s < 2:
        k = randint(0, len(employees_exception) - 1)
        if employees_exception[k][employees_exception[k].find(",")] not in post_exception:
            post_exception.append(f"{employees_exception[k]}, {posts[9]}")
            s += 1

    while len(employees_exception) != len(post_exception):
        k = randint(0, len(employees_exception) - 1)
        if employees_exception[k][employees_exception[k].find(",")] not in post_exception:
            post_exception.append(f"{employees_exception[k]}, {posts[5]}")
            s += 1

    with open("files/Employees.txt", "w", encoding="utf-8") as file:
        file.write(f'"id", "ФИО", "Дата рождения", "Телефон", "Должность", "Отдел"\n')
        for i in range(len(post_exception)):
            stroka = post_exception[i][len(post_exception[i])::-1]
            # print(stroka)
            file.write(f'"{i}", "{employees_exception[i]}", "{birthdays_exception[i]}", "{phones_exception[i]}"'
                       f'{post_exception[i][post_exception[i].find(","):post_exception[i].find(",", post_exception[i].find(",") + 1)]}, '
                       f'{departments[int(stroka[1])]}\n')
    # if __name__ == "__main__":
    # print(men_full_name, len(men_full_name), sep=" ")
    # print(fmen_full_name, len(fmen_full_name), sep=" ")
    # print(employees, len(employees), sep=" ")
    # print(employees_exception, len(employees_exception), sep=" ")
    # print(phones, len(phones), sep=" ")
    # print(phones_exception, len(phones_exception), sep=" ")
    # print(birthdays, len(birthdays), sep=" ")
    # print(birthdays_exception, len(birthdays_exception), sep=" ")
    # print(department)
    # print(departments)
    # print(post)
    # print(posts)
    # print(post_exception, len(post_exception), sep=' ')
