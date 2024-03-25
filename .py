import random
import os
import time


def print_board(board, flag):
    if flag != 1:
        os.system('cls')
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]


def computer_move(board):
    available_moves = get_available_moves(board)
    for move in available_moves:
        board_copy = [row[:] for row in board]
        board_copy[move[0]][move[1]] = "X"
        if check_win(board_copy, "X"):
            return move
    return random.choice(available_moves)


def animation(turn):
    if turn == 'X':
        turn_name = 'Компьютер'
    else:
        turn_name = 'Вы'
    for x in range(8):
        if turn_name == 'Компьютер':
            turn_name = 'Вы'
        else:
            turn_name = 'Компьютер'

        os.system('cls')
        print('\n\n\t\t\tКто же будет первым???\n\t\t\tДавайте подбросим монетку!')
        print(f'\n\n\n\t\t\t    --> {turn_name} <--')

        time.sleep(0.75)

    print('\t\tНажмите любую клавишу, чтобы продолжить...')
    input()
    os.system('cls')


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = random.choice(players)
    animation(turn)
    # print("Монетка показывает, что первым ходит", "компьютер" if turn == "X" else "вы")
    print_board(board, 1)

    while True:
        # os.system("cls")
        if turn == "X":
            print("Ход компьютера:")
            move = computer_move(board)
            board[move[0]][move[1]] = turn
        else:
            print("Ход пользователя (введите номер ячейки от 1 до 9):")
            try:
                move = int(input()) - 1
            except:
                f = True
                while f == True:
                    try:
                        move = int(input())
                        f = False
                    except:
                        pass
            row = move // 3
            col = move % 3
            if board[row][col] != " ":
                print("Эта ячейка уже занята. Попробуйте еще раз.")
                continue
            board[row][col] = turn

        print_board(board, 0)

        if check_win(board, turn):
            print("Выиграл", "компьютер" if turn == "X" else "вы")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print("Ничья!")
            break

        turn = "X" if turn == "O" else "O"


if __name__ == '__main__':
    main()
            
