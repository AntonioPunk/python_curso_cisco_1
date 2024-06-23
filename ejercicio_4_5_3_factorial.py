"""4.5.3 Ejemplos de funciones: Factoriales
La siguiente función a definir calcula factoriales.
¿Recuerdas cómo se calcula un factorial?

0! = 1 (¡Si!, es verdad)
1! = 1
2! = 1 * 2
3! = 1 * 2 * 3
4! = 1 * 2 * 3 * 4
:
:
n! = 1 * 2 * 3 * 4 * ... * n-1 * n

Se expresa con un signo de exclamación,
y es igual al producto de todos los números naturales
previos al argumento o número dado. 

La fórmula es n! = n*(n-1)!

"""

def factorial(number):
    """ Calculamos el factorial de 'number' sin recursividad. """
    producto = 1
    if number < 2:
        return 1
    for n in range(2, number+1):
        producto *= n
    return producto

print("Sin recursividad:")
for i in range(6):
    print(i, factorial(i))


def fac_rec(number):
    """ Calculamos el factorial de 'number' con recursividad: n!=n(n-1)! """
    if number < 2:  # Caso base
        return 1
    return number * (fac_rec(number - 1))

print("Con recursividad:")
for i in range(6):
    print(i, fac_rec(i))
