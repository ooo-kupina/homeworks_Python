from generators import fmen_name_gen, men_name_gen, birthdays_gen, phones_gen, employees_gen
import subprocess


def rewrite(a, x):
    file = open("files/Employees.txt", "r", encoding="utf-8")
    file_read_list = file.read().split("\n")
    file_read_list[x] = f'{a[0]}, {a[1]}, ' \
                        f'{a[2]}, {a[3]}, ' \
                        f'{a[4]}, {a[5]}'
    file.close()

    file = open("files/Employees.txt", "w", encoding="utf-8")
    for i in range(len(file_read_list)):
        file.write(f"{file_read_list[i]}\n")
    file.close()


def gen_bd():
    men_name_gen.start(men_num)
    fmen_name_gen.start(fmen_num)
    birthdays_gen.start(fmen_men_num)
    phones_gen.start(fmen_men_num)
    employees_gen.start()
    print("База данных сгенерирована.")


def edit_main_tab(x):
    with open("files/Post.txt", encoding="utf-8") as file:
        post = list(file.readlines())
        posts = []
        for i in range(1, len(post)):
            posts.append(post[i][post[i].find(",") + 1:post[i][post[i].find(",") + 1].find(',')])
        file.close()

    with open("files/Department.txt", encoding="utf-8") as file:
        department = list(file.readlines())
        departments = []
        for i in range(1, len(department)):
            departments.append(department[i][department[i].find(",") + 3:department[i].find("\n") - 1])
        file.close()

    with open("files/Employees.txt", "r", encoding="utf-8") as file:
        flag = False
        selected_string = list(file.readlines()[x].strip().split(", "))
        print(selected_string)
        selected_field = input("Что поменять: имя, дату рождения, телефон, должность?: ").strip().lower()
        if selected_field == "имя":
            selected_string[1] = input("Введите новое имя: ")
            selected_string[1] = f'"{selected_string[1]}"'
            print(selected_string)
            rewrite(selected_string, x)
        elif selected_field == "дату рождения":
            selected_string[2] = input("Введите новую дату рождения: ")
            selected_string[2] = f'"{selected_string[2]}"'
            print(selected_string)
            rewrite(selected_string, x)
        elif selected_field == "телефон":
            selected_string[3] = input("Введите новый телефон: ")
            selected_string[3] = f'"{selected_string[3]}"'
            print(selected_string)
            rewrite(selected_string, x)
        elif selected_field == "должность":
            selected_string[4] = input("Введите новую должность: ").capitalize()
            selected_string[4] = f'"{selected_string[4]}"'
            for i in range(len(posts)):
                if selected_string[4] in posts[i]:
                    department_change = posts[i][len(posts[i]) - 2:len(posts[i]) - 1]
                    selected_string[5] = departments[int(department_change)]
                    flag = True

            if flag == True:
                print(selected_string)
                rewrite(selected_string, x)

            elif flag == False:
                print("Такой должности не существует.")

        else:
            print("Названия команд: имя, дату рождения, телефон или должность введите правильно.")

        file.close()


def open_main_tab_in_notepad():
    subprocess.Popen("notepad files/Employees.txt")
    subprocess.Popen("notepad files/Post.txt")
    subprocess.Popen("notepad files/Department.txt")


def add_in_main_tab():
    with open("files/Post.txt", encoding="utf-8") as file:
        post = list(file.readlines())
        posts = []
        for i in range(1, len(post)):
            posts.append(post[i][post[i].find(",") + 2:post[i][post[i].find(",") + 1].find(',')])
        file.close()

    with open("files/Department.txt", encoding="utf-8") as file:
        department = list(file.readlines())
        departments = []
        for i in range(1, len(department)):
            departments.append(department[i][department[i].find(",") + 3:department[i].find("\n") - 1])
        file.close()

    with open("files/Employees.txt", "r", encoding="utf-8") as file:
        full_tab = file.read().strip().split("\n")
        index_tab = []
        for i in range(1, len(full_tab)):
            start_index = 1
            end_intdex = full_tab[i][start_index:].find('"') + 1
            index_tab.append(int(full_tab[i][start_index:end_intdex]))
        file.close()
    with open("files/Employees.txt", "a", encoding="utf-8") as file:
        flag_employee = False
        flag = False
        name_emp = input("Введите имя: ").title()
        birthday_emp = input("Введите дату рождения: ")
        phone_emp = input("Введите телефон: ")
        post_emp = f'"{input("Введите должность: ").capitalize().strip()}"'
        for i in range(len(index_tab) + 1):
            if i not in index_tab:
                index_tab.append(i)
                break

        for j in range(len(posts)):
            if post_emp in posts[j]:
                department_emp = departments[int(posts[j][len(posts[j]) - 2:len(posts[j]) - 1])]
                flag = True
                if flag == True:
                    new_employee = f'"{i}", "{name_emp}", "{birthday_emp}", ' \
                                   f'"{phone_emp}", {post_emp}, "{department_emp}"\n'
                    file.writelines(new_employee)
                    flag_employee = True
                    print("Запись о сотруднике создана.")
                    if flag_employee == True:
                        break
            else:
                print("Вы ввели должность, которой не существует.")
                break


def delete_in_main_tab(x):
    with open("files/Employees.txt", "r", encoding="utf=8") as file:
        employees = list(file.read().split("\n"))
        file.close()
    with open("files/Employees.txt", "w", encoding="utf-8") as file:
        for i in range(0, x):
            file.write(f'{employees[i]}\n')
        for i in range(x + 1, len(employees)):
            file.write(f'{employees[i]}\n')
        file.close()
    print(f"Строка удалена {x}.")


men_num = 10
fmen_num = 11

fmen_men_num = men_num + fmen_num

command_gen_bd = "0"
command_edit_main_tab = "1"
command_add_in_main_tab = "2"
command_delete_in_main_tab = "3"
command_open_main_tab_in_notepad = "4"
command_close = "5"

while True:
    print(f'''База данных компании "IT-комплект".
                Чтобы сгенерировать БД введите команду: {command_gen_bd}.
                Для редактирования главной таблицы введите команду: {command_edit_main_tab}.
                Для добавления данных в главную таблицу введите команду: {command_add_in_main_tab}.
                Для удаления данных из главной таблицы введите команду: {command_delete_in_main_tab}.
                Для открытия всех таблиц в блокноте введите команду: {command_open_main_tab_in_notepad}
                Чтобы прервать выполнение введите команду: {command_close}''')

    command = input("Введите команду: ")

    if command == command_gen_bd:
        gen_bd()

    elif command == command_edit_main_tab:
        edited_string = int(input("Какую строчку вы хотите изменить?: "))
        with open("files/Employees.txt", "r", encoding="utf-8") as file:
            file_count = list(file.read().split("\n"))
            file_count = len(file_count) - 1
            file.close()
        if edited_string == 0:
            print("Нельзя поменять 0 строку")
        elif 0 < edited_string < file_count:
            edit_main_tab(edited_string)
        else:
            print("Такой строки нет.")

    elif command == command_add_in_main_tab:
        print("Происходит дозапись в файл.")
        add_in_main_tab()

    elif command == command_delete_in_main_tab:
        deleted_string = int(input("Какую строчку вы хотите Удалить?: "))
        with open("files/Employees.txt", "r", encoding="utf-8") as file:
            file_count = list(file.read().split("\n"))
            file_count = len(file_count) - 1
            file.close()
        if deleted_string == 0:
            print("Нельзя поменять 0 строку")
        elif 0 < deleted_string < file_count:
            delete_in_main_tab(deleted_string)
        else:
            print("Такой строки нет.")

    elif command == command_open_main_tab_in_notepad:
        open_main_tab_in_notepad()

    elif command == command_close:
        break

    else:
        print("Такой команды нет.")
