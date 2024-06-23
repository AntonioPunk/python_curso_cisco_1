# 4.3.6   LAB   Día del año: escribiendo y usando tus propias funciones.

# Tu tarea es escribir y probar una función que toma tres argumentos
# (un año, un mes y un día del mes) y devuelve el día correspondiente
# del año, o devuelve None si cualquiera de los argumentos no es válido.

# Debes utilizar las funciones previamente escritas y probadas.
# Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.


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
    else:
        return dias_meses[month-1]

def day_of_year(year, month, day):
    if days_in_month(year, month) is None:
        return # Retorna None
    elif day > days_in_month(year, month) or day < 1:
        return # Retorna 'None'
    else:
        sum_dias = 0
        for i in range(1, month):
            sum_dias += days_in_month(year, i)
            i += 1
        sum_dias += day
        return sum_dias

years = [2023, 2024, 2020, 1977, 2024, -5, 2024, 2024]
months = [12, 12, 2, 8, 2, 3, 13, 2]
days = [31, 31, 30, 25, 29, 15, 15, -34]

for n in range(len(years)):
    print(f"El número de día del año de la fecha {days[n]}/{months[n]}/{years[n]} es: {day_of_year(years[n], months[n], days[n])}")
    n += 1