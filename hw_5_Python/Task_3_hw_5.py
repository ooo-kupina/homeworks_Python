# Создайте программу для игры в ""Крестики-нолики"".

print("Данная программа - это игра в ""Крестики-нолики"".\n\
Игрок № 1 ходит ""крестиками"", а Игрок № 2 ходит ""ноликами"".\n\
Вводить надо номер ячейки от 1 до 9, в которую игрок хочет поставить свой знак.\n")



players_turns = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "
}

turns = 1

def land():
    print(f"  {players_turns[1]}  |  {players_turns[2]}  |  {players_turns[3]}  ")
    print(f"-----|-----|-----")
    print(f"  {players_turns[4]}  |  {players_turns[5]}  |  {players_turns[6]}  ")
    print("-----|-----|-----")
    print(f"  {players_turns[7]}  |  {players_turns[8]}  |  {players_turns[9]}  ")

print("Это поле:")
land()

while turns <= 9:
    print(f"Ход № {turns}")
    player_one = int(input("Игрок 1: "))
    players_turns[player_one] = "X"
    land()
    if (players_turns[1] == players_turns[2] == players_turns[3] == "X") or \
            (players_turns[4] == players_turns[5] == players_turns[6] == "X") or \
            (players_turns[7] == players_turns[8] == players_turns[9] == "X") or \
            (players_turns[1] == players_turns[4] == players_turns[7] == "X") or \
            (players_turns[2] == players_turns[5] == players_turns[8] == "X") or \
            (players_turns[3] == players_turns[6] == players_turns[9] == "X") or \
            (players_turns[1] == players_turns[5] == players_turns[9] == "X") or \
            (players_turns[3] == players_turns[5] == players_turns[7] == "X"):
        print("Игрок 1 выиграл.")
        break
    if turns == 9:
        print("Ничья")
        break
    turns += 1
    print(f"Ход № {turns}")
    player_two = int(input("Игрок 2: "))
    players_turns[player_two] = "O"
    land()
    if (players_turns[1] == players_turns[2] == players_turns[3] == "O") or \
            (players_turns[4] == players_turns[5] == players_turns[6] == "O") or \
            (players_turns[7] == players_turns[8] == players_turns[9] == "O") or \
            (players_turns[1] == players_turns[4] == players_turns[7] == "O") or \
            (players_turns[2] == players_turns[5] == players_turns[8] == "O") or \
            (players_turns[3] == players_turns[6] == players_turns[9] == "O") or \
            (players_turns[1] == players_turns[5] == players_turns[9] == "O") or \
            (players_turns[3] == players_turns[5] == players_turns[7] == "O"):
        print("Игрок 2 выиграл.")
        break
    turns += 1
