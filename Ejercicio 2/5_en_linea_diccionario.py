import gamelib
CRUZ = 'X'
CIRCULO = 'O'
DIMENSION = 10
ANCHO, ALTO = 300, [50,350]
PIXEL = 30
MITAD = 30 // 2

def juego_crear():
    """Inicializar el estado del juego"""
    grilla = {}
    for fila in range(DIMENSION):
        for columna in range(DIMENSION):
            grilla[(fila, columna)] = grilla.get((fila, columna), ' ')
    return grilla


def verificar_pocision_valida(x, y):
    '''Verifica si la pocision donde clickea es valido para jugar'''
    if x < ANCHO and ALTO[0] < y < ALTO[1]:
        return True
    return False

def buscar_indices(x, y):
    '''Devuelve los indices para no salir fuera de rango'''
    fila, columna = x // PIXEL, (y - ALTO[0]) // PIXEL
    return fila, columna

def juego_actualizar(juego, x, y, contador):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    fila, columna = buscar_indices(x, y)

    if not verificar_pocision_valida(x,y) or juego[(fila, columna)] != ' ':
        return juego, contador

    if contador % 2 == 0:
        juego[(fila,columna)] = CIRCULO

    else:
        juego[(fila,columna)] = CRUZ
    return juego, contador + 1

def mostrar_turno(contador):
    '''Muestra informacion sobre el turno'''
    if contador % 2 == 0:
        gamelib.draw_text(f'Turno de {CIRCULO}', 50, 30)
    else:
        gamelib.draw_text(f'Turno de {CRUZ}', 50, 30)

def dibujar_contenido_grilla(juego):
    '''Dibuja el simbolo de cada celda, segun el turno'''
    for posicion, elemento in juego.items():
        if elemento == CIRCULO:
            gamelib.draw_text(CIRCULO, posicion[0] * PIXEL + MITAD, posicion[1] * PIXEL + ALTO[0] + MITAD)
        elif elemento == CRUZ:
            gamelib.draw_text(CRUZ, posicion[0] * PIXEL + MITAD, posicion[1] * PIXEL + ALTO[0] + MITAD)

def dibujar_tablero():
    '''La funcion dibuja las lineas'''
    for x in range(0, ANCHO , PIXEL):
        gamelib.draw_line(x, ALTO[0], x, ALTO[1])
    for y in range(ALTO[0], ALTO[1], PIXEL):   
        gamelib.draw_line(0, y, ANCHO, y)

def juego_mostrar(juego, contador):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 15)
    dibujar_tablero()
    mostrar_turno(contador)
    dibujar_contenido_grilla(juego)    

def main():
    juego = juego_crear()
    contador = 0

    gamelib.resize(300, 350)

    while gamelib.is_alive():
        gamelib.draw_begin()
        juego_mostrar(juego, contador)
        gamelib.draw_end()

        ev = gamelib.wait()

        if not ev:
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break

        if ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y 
            juego, contador = juego_actualizar(juego, x, y, contador)

gamelib.init(main)