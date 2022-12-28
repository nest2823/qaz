# Игра в 'крестики - нолики'.


# Определим игровое поле в виде словаря. Заполним его таким образом, что бы игрок понял куда он может поставить свой знак.
Part = {'1': '1', '2': '2', '3': '3',
        '4': '4', '5': '5', '6': '6',
        '7': '7', '8': '8', '9': '9'}

part_keys = []

for key in Part:
    part_keys.append(key)


# Выведем игровое поле на экран в виде функции.
def printPart(part):
    print("     |     |")
    print("  " + part['1'] + "  |  " + part['2'] + "  |  " + part['3'])
    print("_____|_____|_____\n     |     |")
    print("  " + part['4'] + "  |  " + part['5'] + "  |  " + part['6'])
    print("_____|_____|_____\n     |     |")
    print("  " + part['7'] + "  |  " + part['8'] + "  |  " + part['9'])
    print("     |     |\n________________")


# Напишем функцию, содержащую игровой процесс.
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printPart(Part)
        print("Ходит знак " + turn + ".")

        move = input()

        if Part[move] == ' ' or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            Part[move] = turn
            count += 1
        else:
            print("Место занято, выбери другое.")
            continue

        # После пяти ходов, может плявиться победная комбмнация у X или O. Опишем эти комбинации.
        if count >= 5:
            if Part['7'] == Part['8'] == Part['9'] != ' ':
                printPart(Part)
                print("Игра окончена")
                print("Победил знак " + turn)
                break
            elif Part['4'] == Part['5'] == Part['6'] != ' ':
                printPart(Part)
                print("Игра окончена")
                print("Победил знак " + turn)
                break
            elif Part['1'] == Part['2'] == Part['3'] != ' ':
                printPart(Part)
                print("Игра окончена")
                print("Победил знак " + turn)
                break
            elif Part['1'] == Part['4'] == Part['7'] != ' ':
                printPart(Part)
                print("Игра окончена")
                print("Победил знак " + turn)
                break
            elif Part['2'] == Part['5'] == Part['8'] != ' ':
                printPart(Part)
                print("Игра окончена")
                print("Победил знак " + turn)
                break
            elif Part['3'] == Part['6'] == Part['9'] != ' ':
                printPart(Part)
                print("Игра окончена")
                print("Победил знак " + turn)
                break
            elif Part['7'] == Part['5'] == Part['3'] != ' ':
                printPart(Part)
                print("Игра окончена")
                print("Победил знак " + turn)
                break
            elif Part['1'] == Part['5'] == Part['9'] != ' ':
                printPart(Part)
                print("Игра окончена")
                print("Победил знак " + turn)
                break

            # Если победная комбинация не была найдена, а количество знаков на игровом поле стало равно 9, объявим о ничьей.
        if count == 9:
            print("Игра окончена" "\n" "Ничья")

        # Каждый ход меняем игроков.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        # Спросим игрока,хочет ли он играть снова после окончания игры.
    restart = input("Играете снова? (д/н)")
    if restart == "д" or restart == "Д":
        for key in part_keys:
            Part[key] = " "

        game()


if __name__ == "__main__":
    game()