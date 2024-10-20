from random import randrange

def display_board(board):
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
    user_movement = 5   # Fijo valor para poder entrar al bucle 'while'.
    row = 1             # Fijo valor para poder entrar al bucle 'while'.
    colm = 1            # Fijo valor para poder entrar al bucle 'while'.
    while user_movement not in range(1, 10) or board[row][colm] in ["O", "X"]:
        try:
            user_movement = int(input("Ingresa tu movimiento: "))
        except:
            print("Debe introducir un número entero de 1 a 9.")
        row = (user_movement-1) // 3 # Obtengo el número de fila.       Ejem: (4-1)//3 = 1 ; (9-1)//3 = 2
        colm = (user_movement-1) % 3 # Obtengo el número de columna.    Ejem: (4-1)%3  = 0 ; (9-1)%3  = 2
    board[row][colm] = "O"

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    list_free_field = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "X" and board[i][j] != "O":
                list_free_field.append((i,j))
    return list_free_field

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if sign == "O":         # Si el símbolo es 'O' jugamos con el humano.
        who = "human"
    elif sign == "X":       # Si el símbolo es 'X' jugamos con la máquina.
        who = "machine"
    else:
        who = None
    cross1 = cross2 = True
    for i in range(len(board)):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign: # Comprobamos filas.
            return who
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign: # Comprobamos columnas.
            return who
        if board[i][i] != sign:     # Comprobamos diagonal: (0, 0), (1, 1), (2, 2)
            cross1 = False
        if board[2-i][i] != sign:   # Comprobamos diagonal: (2, 0), (1, 1), (0, 2)
            cross2 = False
    if cross1 or cross2:
        return who
    return None           

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    control = len(list_free_field)
    if control > 0:                                     # Si la lista de posiciones libres no está vacía:
        machine_movement = randrange(control)           # obtengo una posición aleatoria dentro de esa lista.
        row, colm = list_free_field[machine_movement]   # Asignamos los valores de la tupla elegida a 'row' y 'colm'.
        print("Yo he elegido el número: ", board[row][colm])
        board[row][colm] = "X"

""" MAIN ------------------------------------------------------------------- """

board = [[1, 2, 3], [4, "X", 6,], [7, 8, 9]]            # Creamos el contenido del tablero e iniciamos la posición
                                                        # central con una 'X'.
cont = 0                                                # Creamos un contador para saber cuándo se ha
                                                        # producido un empate. (cont == 5)

display_board(board)                                    # Mostramos el tablero de inicio.

while True:                                             # Bucle principal del programa, salimos de él (break)
    cont += 1                                           # si se produce una victoria o llegamos al empate.
    if cont == 5:
        print("Empate !!!")
        break   
    list_free_field = make_list_of_free_fields(board)
    enter_move(board)
    display_board(board)
    if victory_for(board, "O") == "human":
        print("Has ganado !!!")
        break    
    list_free_field = make_list_of_free_fields(board)
    draw_move(board)
    display_board(board)
    if victory_for(board, "X") == "machine":
        print("Te he ganado, pringao !!!")
        break
