my_list = [1, 2]
for v in range(2):
    my_list.insert(-1, my_list[v])
print(my_list)
# solución: [1, 1, 1, 2]


def func(a, b):
    return b ** a
#print(func(b=2, 2))
# solucion: ERROR

z = 0
y = 10
x = y < z and z > y or y < z and z < y
print(x)
# solucion: False

#print = 34
# solucion: for y in


my_list =  [x * x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(my_list))
# Borramos list[4] que es el número 16
# solucion: [0, 1, 4, 9]


x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)
# solucion: 1, 1, 2


a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
# solucion: 0, 1


def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
print(fun(fun(2)))
# solucion: 2


nums = [1, 2, 3]
vals = nums
del vals[:]
print(nums)
print(vals)
# solucion: Tienen la misma longitud


x = 3 #int(input())
y = 2 #int(input())
x = x % y
x = x % y
y = y % x
print(y)
# solucion: 0


print("a", "b", "c", sep="sep")
# solucion: asepbsepc


x = 1 // 5 + 1 / 5
print(x)
# solucion: 0.2


my_tuple = (1, 2)
#my_tuple[1] = my_tuple[1] + my_tuple[0]
print(my_tuple)
# solucion: ERROR, tuple no admite asignación por índice.


x = 2.0 #float(input())
y = 4.0 #float(input())
print(y ** (1 / x))
# solucion: 2.0


dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']
for k in range(len(dct)):
    v = dct[v]
print(v)
# solucion: one


lst = [i for i in range(-1, -2)]
print(lst)
# solucion: lst contiene 0 elementos ya que no 'avanza' al revés.


def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
print(fun(0, 3))
# solución: 0


#i = 0
#while i < i + 2 :
#    i += 1
#    print("*")
#else:
#    print("*")
# solución: bucle INFINITO de '*'


tup = (1, 2, 4, 8)
tup = tup[-2:-1]
#print(type(tup))
tup = tup[-1]
#print(type(tup))
print(tup)
# solución: 4 ya que al quedar un solo elemento deja de ser tupla y se convierte en int.


dd = {"1": "0", "0": "1"}
#for x in dd.vals():
#    print(x, end="")
# solución: ERROR ya que el método vals no existe, el correcto es values.


dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)
for x in dct.keys():
    print(dct[x][1], end="")
# solución: 21


def fun(inp=2, out=3):
    return inp * out
print('\n',fun(out=2))
# solución: 4


lst = [[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
# solución: 3


try:
    value = '0'
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")
# solución: 0.0 ya que lo convertimos a int y al dividirlo entre 1 da 0.0 pues
#           se convierte en float.


#try:
#    print(5/0)
#    break
#except:
#    print("Lo siento, algo salió mal...")
#except (ValueError, ZeroDivisionError):
#    print("Mala suerte...")
# solución: Sintax Error ya que hay en break fuera de un bucle.


foo = (1, 2, 3)
foo.index(0)
# solución: Value Error ya que 0 no se encuentra en la tupla.


#print(¡Hola, Mundo!)
# solución: Sintax Error


"""

¿Qué contiene el examen?
El examen abarca los temas que has aprendido a lo largo del curso:

Sección 1:
- Programación de Computadoras y Fundamentos de Python (18%)
- Términos y definiciones fundamentales, incluyendo interpretación,
compilación, léxico, sintaxis y semántica.
- La lógica y estructura de Python, incluyendo palabras clave,
instrucciones, sangría y comentarios.
- La introducción de literales, variables, sistemas numéricos y convenciones 
de nomenclatura que has estudiado en el curso.

Sección 2:
- Flujo de Control - Bloques Condicionales y Bucles (29%)
- Aplicación de la toma de decisiones y diversas estructuras condicionales que 
has explorado en el curso.
- Diferentes tipos de iteraciones y control de bucles que has practicado en el 
curso.

Sección 3:
- Colecciones de Datos - Tuplas, Diccionarios, Listas y Cadenas (25%)
- Recopilación y manipulación de datos utilizando listas, tuplas, diccionarios 
y cadenas, como has cubierto en el curso.

Sección 4:
- Funciones y Excepciones (28%)
- Descomposición de código con funciones y manejo de excepciones, conceptos 
que has explorado durante el curso.

"""