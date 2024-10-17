""" PREGUNTA 7 """
dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    # Inserta tu código aquí
    print(k[0])
    

""" PREGUNTA 8 """
def func(a, b):
    return a ** a

#print(func(2)) DA ERROR PUES FALTA UN PARÁMETRO

""" PREGUNTA 9 """
def func_1(a):
    return a ** a

def func_2(a):
    return func_1(a) * func_1(a)

print(func_2(2))
# RESULTADO:
# 16

""" PREGUNTA 12 """
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return

#print(fun(fun(2)) + 1) DA ERROR, PUES fun(2) da 1, luego fun(1) retorna None y 
# None no se puede sumar con 1.

""" PREGUNTA 13 """
def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)
# RESULTADO:
# 4

""" PREGUNTA 14 """
def any():
    print(var + 1, end='')

var = 1
any()
print(var)
#RESULTADO:
# 21


""" CONCLUSIONES """

# Las tuplas se pueden recortar mediante slicing y acceder mediante índices.
# Un intento de operación aritmética entre dos str arrojará un error Type Error




