import random


            return move
    return random.choice(available_moves)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = random.choice(players)
    print("Монетка показывает, что первым ходит", "компьютер" if turn == "X" else "вы")
    print_board(board)

    while True:
        if turn == "X":
            print("Ход компьютера:")
            move = computer_move(board)
            board[move[0]][move[1]] = turn
        else:
            print("Ход пользователя (введите номер ячейки от 1 до 9):")
            move = int(input()) - 1
            row = move // 3
            col = move % 3
            if board[row][col] != " ":
                print("Эта ячейка уже занята. Попробуйте еще раз.")
                continue
            board[row][col] = turn

        print_board(board)

        if check_win(board, turn):
            print("Выиграл", "компьютер" if turn == "X" else "вы")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print("Ничья!")
            break

        turn = "X" if turn == "O" else "O"

if __name__ == "__main__":
    main()
