import soko
from pila import Pila
MOVIMIENTOS = (1,0),(-1,0),(0,1),(0,-1)

def buscar_solucion(estado_inicial):
    '''Inicializa el estado del 'backtracking' utilizando un diccionario'''
    visitados = set()
    return pista(estado_inicial, visitados)

def convertir_estado_cadena(estado):
    '''Tranforma el estado, de lista a cadena, para volverlo un tipo de dato inmutable'''
    resultado = ''
    for i in range(len(estado)):
        resultado += ''.join(estado[i]) + ','
    return resultado

def pista(estado, visitados):
    '''Busca una solucion posible al estado del juego'''
    estado_actual = convertir_estado_cadena(estado)
    visitados.add(estado_actual)
    if soko.juego_ganado(estado):
        return True, []
    for movimiento in MOVIMIENTOS:
        nuevo_estado = soko.mover(estado, movimiento)
        if convertir_estado_cadena(nuevo_estado) in visitados:
            continue
        solucion_encontrada, acciones = pista(nuevo_estado, visitados)
        if solucion_encontrada:
            return True, acciones + [movimiento]
    return False, {}

def movimientos_pista(estado):
    '''Apila los movimientos de la solucion'''
    pistas = Pila()
    try:
        resuelto, solucion = buscar_solucion(estado)
    except:
        return pistas
    if resuelto:
        for movimiento in solucion:
            pistas.apilar(movimiento)
    return pistas