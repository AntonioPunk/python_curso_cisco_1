""" Pregunta 4: Escribe un programa que "una" los dos
    diccionarios (d1 y d2) para crear uno nuevo (d3). """

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
#-----------------------
    d3.update(item)
#-----------------------

print(d3)



""" Pregunta 5: Escribe un programa que convierta la lista my
    list en una tupla. """

my_list = ["car", "Ford", "flower", "Tulip"]
#-----------------
t = tuple(my_list)
#-----------------
print(t)



""" Pregunta 6: Escribe un programa que convierta la tupla
    colors en un diccionario. """

colors = (("green", "#008000"), ("blue", "#0000FF"))
#-------------------------------
colors_dictionary = dict(colors)
#-------------------------------
print(colors_dictionary)



""" Pregunta 7: ¿Que ocurrirá cuando se ejecute el siguiente código? """

# Devuelve: {"A": 1, "B": 2} ya que copiamos un diccionario
# a otro y solo borramos el contenido del primero.

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)



""" Pregunta 8: ¿Cuál es la salida del siguiente programa? """

# La salida es:
#    blanco : (255, 255, 255)
#    gris : (128, 128, 128)
#    rojo : (255, 0, 0)
#    verde : (0, 128, 0)

colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)
