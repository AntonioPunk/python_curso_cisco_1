def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

years = [2023, 2024, 2020, 1977, 2024, -5, 2024, 2024]
months = [12, 12, 2, 8, 2, 3, 13, 2]
days = [31, 31, 30, 25, 29, 15, 15, -34]

for n in range(len(years)):
    print(f"El número de día del año de la fecha {days[n]}/{months[n]}/{years[n]} es: {day_of_year(years[n], months[n], days[n])}")
    n += 1