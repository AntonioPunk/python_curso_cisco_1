# Cálculo del Índice de Masa Corporal.

def inch_to_m(inch):
    return inch * 0.0254

def lb_to_kg(lb):
    return lb * 0.4535923

def metric_system():
    weight = float(input("Introduzca el peso en kilogramos: "))
    height = float(input("Introduzca la altura en metros: "))
    print(f"IMC = {round(bmi(weight, height), 2)}")

def imperial_system():
    weight = float(input("Introduzca el peso en libras: "))
    height = float(input("Introduzca la altura en pulgadas: "))
    print(f"IMC = {round(bmi(weight = lb_to_kg(weight), \
                             height = inch_to_m(height)), 2)}")

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2



print("------------- CÁLCULO DEL IMC ---------------\n")

metric_or_imperial = "x"
while metric_or_imperial not in ("m", "i"):
    metric_or_imperial = input("Introduzca el sistema de medidas, Métrico (M) / Inglés (I): ")
    metric_or_imperial = metric_or_imperial.lower()

if metric_or_imperial == "m":
    metric_system()
else:
    imperial_system()
