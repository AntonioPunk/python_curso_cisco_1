from random import randrange


def print_board(board):
    board_deco = [["+-------+-------+-------+"],
            ["|       |       |       |"],
            ["|  ",str(board[0][0]),"  |  ",str(board[0][1]),"  |  ",str(board[0][2]),"  |"],
            ["|       |       |       |"],
            ["+-------+-------+-------+"],
            ["|       |       |       |"],
            ["|  ",str(board[1][0]),"  |  ",str(board[1][1]),"  |  ",str(board[1][2]),"  |"],
            ["|       |       |       |"],
            ["+-------+-------+-------+"],
            ["|       |       |       |"],
            ["|  ",str(board[2][0]),"  |  ",str(board[2][1]),"  |  ",str(board[2][2]),"  |"],
            ["|       |       |       |"],
            ["+-------+-------+-------+"]]
    for i in range(len(board_deco)):
        print(*board_deco[i])

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    user_movement = 5
    position = False
    while user_movement not in range(1, 10) or conversion_dictionary[user_movement] not in list_free_field:
        try:
            user_movement = int(input("Ingresa tu movimiento: "))
        except:
            print("Debe introducir un número entero de 1 a 9.")
    board[conversion_dictionary[user_movement][0]][conversion_dictionary[user_movement][1]] = "O"
    user_list_movements.append((conversion_dictionary[user_movement][0],conversion_dictionary[user_movement][1]))
    return user_list_movements

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    list_free_field = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "X" and board[i][j] != "O":
                list_free_field.append((i,j))
    return list_free_field

def victory_for(board, sign, cont):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == "O":
        sign = 1
        return sign, cont
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == "O":
        sign = 1
        return sign, cont 
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == "O":
        sign = 1
        return sign, cont 
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == "O":
        sign = 1
        return sign, cont
    elif board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == "X":
        sign = 2
        return sign, cont 
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == "X":
        sign = 2
        return sign, cont 
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == "X":
        sign = 2
        return sign, cont
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == "X":
        sign = 2
        return sign, cont 
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] == "X":
        sign = 2
        return sign, cont
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == "X":
        sign = 2
        return sign, cont
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == "X":
        sign = 2
        return sign, cont
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[0][2] == "X":
        sign = 2
        return sign, cont
    else:
        cont += 1
        return sign, cont


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    machine_movement = 5
    while conversion_dictionary[machine_movement] not in list_free_field:
        machine_movement = randrange(1,10)
    board[conversion_dictionary[machine_movement][0]][conversion_dictionary[machine_movement][1]] = "X"
    print("La máquina ha elegido el movimiento: ", machine_movement)
    machine_list_movements.append((conversion_dictionary[machine_movement][0],conversion_dictionary[machine_movement][1]))
    return machine_list_movements


board = [[1, 2, 3], [4, "X", 6,], [7, 8, 9]]
user_list_movements = []
machine_list_movements = [(1, 1)]
conversion_dictionary = {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2)}
sign = 0
cont = 0

print_board(board)

while True:
    if cont == 8:
        print("Habéis empatado")
        break   
    list_free_field = make_list_of_free_fields(board)
    enter_move(board)
    print(user_list_movements)
    print_board(board)
    sign, cont = victory_for(board, sign, cont)
    if sign == 1:
        print("Has ganado!!!")
        break    
    list_free_field = make_list_of_free_fields(board)
    draw_move(board)
    print(machine_list_movements)
    print_board(board)
    sign, cont = victory_for(board, sign, cont)
    if sign == 2:
        print("Te ha ganado la máquina, pringao!!!")
        break
