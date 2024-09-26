while True:
    try:
        number = int(input('Introduzca un número: '))
        print(f'El recíproco de {number} es : {1 / number}')
        break
    except ValueError:
        print('El valor introducido no es válido.')
    except ZeroDivisionError:
        print('El "0" no es un número válido')
    except:
        print('Se ha producido un ERROR INESPERADO')

print('El programa ha finalizado con éxito')
