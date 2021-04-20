from math import sqrt
from vectores import diferencia, producto_vectorial, norma


def calcular_area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """La funcion va a calcular el área de un triángulo con tres puntos en R3
    utilizando las funciones anteriores de norma, producto vectorial y diferencia"""
    dif_1, dif_2, dif_3 = diferencia(x1, y1, z1, x2, y2, z2)
    dif_4, dif_5, dif_6 = diferencia(x1, y1, z1, x3, y3, z3)
    prod_vec1, prod_vec2, prod_vec3 = producto_vectorial(dif_1, dif_2, dif_3, dif_4, dif_5, dif_6)
    norma_1 = norma(prod_vec1, prod_vec2, prod_vec3)
    area_triangulo = norma_1 / 2
    return area_triangulo

assert calcular_area_triangulo(0, 0, 0, 0, 0, 0, 0, 0, 0) == 0
assert calcular_area_triangulo(0, 0, -3, 4, 2, 0, 3, 3, 1) == sqrt(86) / 2
assert calcular_area_triangulo(1, 2, 3, 2, 2, 2, -4, 1, -3) == sqrt(123) / 2
assert calcular_area_triangulo(1, -1, 2, 1, 5, -3, 0, 3, 1) == sqrt(257) / 2