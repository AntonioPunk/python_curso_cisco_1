import random

def display_board(board):
    board_deco = [
        "+-------+-------+-------+",
        "|       |       |       |",
        f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |",
        "|       |       |       |",
        "+-------+-------+-------+",
        "|       |       |       |",
        f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |",
        "|       |       |       |",
        "+-------+-------+-------+",
        "|       |       |       |",
        f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |",
        "|       |       |       |",
        "+-------+-------+-------+"
    ]
    for line in board_deco:
        print(line)

def enter_move(board):
    while True:
        try:
            user_movement = int(input("Ingresa tu movimiento (1-9): "))
            if user_movement not in range(1, 10):
                raise ValueError
            row, colm = divmod(user_movement - 1, 3)
            if board[row][colm] not in ["O", "X"]:
                board[row][colm] = "O"
                break
            else:
                print("La casilla ya está ocupada. Intenta de nuevo.")
        except ValueError:
            print("Debe introducir un número entero de 1 a 9.")

def make_list_of_free_fields(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ["X", "O"]]

def victory_for(board, sign):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]
    for combination in winning_combinations:
        if all(board[r][c] == sign for r, c in combination):
            return "human" if sign == "O" else "machine"
    return None

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, colm = random.choice(free_fields)
        print(f"La máquina ha elegido el número: {board[row][colm]}")
        board[row][colm] = "X"

def main():
    board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
    display_board(board)

    while True:
        if not make_list_of_free_fields(board):
            print("¡Empate!")
            break

        enter_move(board)
        display_board(board)
        if victory_for(board, "O") == "human":
            print("¡Has ganado!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, "X") == "machine":
            print("¡Te he ganado!")
            break

if __name__ == "__main__":
    main()
