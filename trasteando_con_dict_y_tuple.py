#------------------------------------------

dictionary = {}

for i in range(10):
    name = "nombre" + str(i)
    dictionary.update({name : i})

for names, values in dictionary.items():
    print(f"{names} : {values}")

#-------------------------------------------

for i in dictionary:
    dictionary[i] = i + i

for names, values in dictionary.items():
    print(f"{names} : {values}")

#--------------------------------------------

dictionary = {1 : (1, 2, 3), 2: (4, 5, 6), 3 : (7, 8, 9)}

print(dictionary[2][1]) # Presenta un 5

for i in dictionary:
    print(*(dictionary[i])) # Desempaqueto las tuplas de cada clave para mostrarlas.

lista = list(dictionary.values())

print(lista)
print(*lista)
print(lista[2][1])

dictionary_2 = {4 : (10, 11, 12)}
dictionary.update(dictionary_2)
print(dictionary)

print(dictionary.get(3))
