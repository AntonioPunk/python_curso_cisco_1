""" 4.5.4 Números Fibonacci
¿Estás familiarizado con la serie Fibonacci?

Son una secuencia de números enteros los cuales siguen una regla sencilla:

el primer elemento de la secuencia es igual a uno (Fib1 = 1)
el segundo elemento también es igual a uno (Fib2 = 1)
cada número después de ellos son la suman de los dos números
anteriores (Fibi = Fibi-1 + Fibi-2)
Aquí están algunos de los primeros números en la serie Fibonacci:

fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 =
8 fib_7 = 5 + 8 = 13

Debemos seguir esta pauta:

Definimos dos elementos -> elem1 = 1 ; elem2 = 1
Definimos un sumatorio -> sumatorio = 0

    Para num = 0 -> sumatorio = 0
    Para num = 1 -> sumatorio = 1
    Para num < 3 -> sumatorio = 1
    Para num = 3 -> elem1 = 1 ; elem2 = 1 ; sumatorio = elem1 + elem2 = 2 
    Para num = 4 -> elem1 = elem2 = 1 ; elem2 = sumatorio = 2 ; sumatorio = elem1 + elem2 = 3
    Para num = 5 -> elem1 = elem2 = 2 ; elem2 = sumatorio = 3 ; sumatorio = elem1 + elem2 = 5
    (...)

La fórmula de Fibonacci es: Fibi = Fibi-1 + Fibi-2

"""

def fibonacci(num):
    """ Calculamos Fibonacci hasta 'num' sin recursividad. """
    if num == 0:
        return 0
    if num < 3:
        return 1

    elem1 = elem2 = 1
    sumatorio = 0

    for _ in range(3, num + 1):
        sumatorio = elem1 + elem2
        elem1, elem2 = elem2, sumatorio # Intercambiamos valores
    return sumatorio

print("Sin recursividad:")
for n in range(0, 10):
    print(n, "->", fibonacci(n))


def fibo_rec(num):
    """ Calculamos Fibonacci hasta 'num' CON recursividad. """
    if num == 0:
        return 0
    if num < 3:
        return 1
    return fibo_rec(num - 1) + fibo_rec(num - 2)

print("Con recursividad:")
for n in range(0, 10):
    print(n, "->", fibo_rec(n))
