# 4.3.8   LAB   Conversión del consumo de combustible.

# El consumo de combustible de un automóvil se puede expresar
# de muchas maneras diferentes. Por ejemplo, en Europa, se 
# muestra como la cantidad de combustible consumido por cada 100 kilómetros.

# En los EE. UU., se muestra como la cantidad de millas recorridas
# por un automóvil con un galón de combustible.

# Tu tarea es escribir un par de funciones que conviertan l/100km
# a mpg (milas por galón), y viceversa.

# Las funciones:

# - se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km
# respectivamente;
# toman un argumento (el valor correspondiente a sus nombres)
# Complementa el código en el editor y ejecuta tu código y verifica
# si tu salida es la misma que la nuestra.

# Aquí hay información para ayudarte:

# 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.
# Salida esperada:

# 60.31143162393162
# 31.36194444444444
# 23.52145833333333
# 3.9007393587617467
# 7.490910297239916
# 10.009131205673757


CONS1 = 3.785411784 # Litros en 1 galón.
CONS2 = 1.609344    # Km. en una milla. 

def liters_100km_to_miles_gallon(liters):
    galons = liters / CONS1                 # Pasamos los litros a galones.
    miles = 100 / CONS2                     # Pasamos los 100km a millas.
    return miles / galons                   # Retornamos las millas por galón.

def miles_gallon_to_liters_100km(miles):
    km = miles * CONS2                      # Pasamos las millas a kilómetros.
    liters = 1 * CONS1                      # Pasamos el galón a litros.
    return (liters / km) * 100              # Retornamos los litros por cada 100 kilómetros.


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
