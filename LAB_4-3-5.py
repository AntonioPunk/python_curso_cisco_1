# 4.3.5   LAB   Cuántos días: escribiendo y usando tus propias funciones.
# Tu tarea es escribir y probar una función que toma dos argumentos
# (un año y un mes) y devuelve el número de días del mes/año dado
# (mientras que solo febrero es sensible al valor year, tu función
# debería ser universal).

# La parte inicial de la función está lista. Ahora, haz que la función
# devuelva None si los argumentos no tienen sentido.

# Por supuesto, puedes (y debes) utilizar la función previamente escrita
# y probada (LAB 4.3.1.6). Puede ser muy útil. Te recomendamos que utilices
# una lista con los meses. Puedes crearla dentro de la función - este truco
# acortará significativamente el código.

# Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.

def is_year_leap(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def days_in_month(year, month):
    dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month <= 0 or month > 12 or year <= 0:
        return # Retorna 'None'
    if month == 2 and is_year_leap(year):
        return 29
    return dias_meses[month-1]


test_years = [1900, 2000, 2016, 1987, -12, 2024, 1912]
test_months = [2, 2, 1, 11, 12, 2, 0]
test_results = [28, 29, 31, 30, 30, 29, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    elif result is None:
        print("Dato sin sentido")
    else:
        print("Fallido")
