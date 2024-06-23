""" Saber si con tres lados se pude formar un triángulo,
    si ese triángulo es "rectángulo" y su área."""


def is_triangle(a2, b2, c2):
    """Si se puede formar un triángulo con 'a', 'b' y 'c' devuelve 'True'."""
    return a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2


def hypothenusa(a1, b1, c1):
    """ Determinamos la hipotenusa y los 2 catetos. """
    if a1 > b1 and a1 > c1:
        hypo = a1
        cat1 = b1
        cat2 = c1
        return hypo, cat1, cat2
    if b1 > a1 and b1 > c1:
        hypo = b1
        cat1 = a1
        cat2 = c1
        return hypo, cat1, cat2
    if c1 > a1 and c1 > b1:
        hypo = c1
        cat1 = a1
        cat2 = b1
        return hypo, cat1, cat2
    else:
        return a1, b1, c1


def is_right_triangle(a3, b3, c3):
    """ Si cumple el teorema de Pitágoras (es triángulo rectángulo) devuelve 'True'. """

    hypo2, cat_a, cat_b = hypothenusa(a3, b3, c3)

    return hypo2**2 == (cat_a**2 + cat_b**2)

def area(a5, b5, c5):
    """ Calculamos el área del triángulo con la fórmula de Heron. """
    s = (a5 + b5 + c5) / 2
    return (s * (s - a5) * (s - b5) * (s - c5)) ** 0.5




a = float(input("Introduzca los cm. del lado 'a': "))
b = float(input("Introduzca los cm. del lado 'b': "))
c = float(input("Introduzca los cm. del lado 'c': "))

if is_triangle(a, b, c):
    print(f"Con las medidas {a}, {b} y {c} SÍ se puede formar un triángulo.")
    if is_right_triangle(a, b, c):
        print("El triángulo ES rectángulo.")
    else:
        print("El triángulo NO ES rectángulo.")
    print(f"El área del triángulo es de: {area(a, b, c)}cm2.")
else:
    print(f"Con las medidas {a}, {b} y {c} NO se puede formar un triángulo.")
