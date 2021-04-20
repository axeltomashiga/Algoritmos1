import gamelib
CRUZ = 'X'
CIRCULO = 'O'
DIMENSION = 10
ANCHO, ALTO = 300, [50,350]
PIXEL = 30

def juego_crear():
    """Inicializar el estado del juego"""
    grilla = []
    for fila in range(DIMENSION):
        grilla.append([])
        for _ in range(DIMENSION):
            grilla[fila].append(' ')
    return grilla

def verificar_turno(juego):
    '''La función verifica de quien es el turno, devolviendo True si es del primer jugador y False en caso de que sea 
    del segundo'''
    contador = 0
    for fila in range(len(juego)):
        for columna in juego[fila]:
            if columna in 'XO':
                contador += 1
    if contador % 2 == 0:
        return True
    return False

def verificar_pocision_valida(x, y):
    '''Verifica si la pocision donde clickea es valido para jugar'''
    if x < ANCHO and ALTO[0] < y < ALTO[1]:
        return True
    return False

def buscar_indices(x, y):
    '''Devuelve los indices para no salir fuera de rango'''
    fila, columna = x // PIXEL, (y - ALTO[0]) // PIXEL
    return fila, columna

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    
    if not verificar_pocision_valida(x,y):
        return juego
    else:
        fila, columna = buscar_indices(x, y)
        if juego[fila][columna] != ' ':
            return juego
        if verificar_turno(juego):
            juego[fila][columna] = CIRCULO
        else:
            juego[fila][columna] = CRUZ
        return juego

def mostrar_turno(turno):
    '''Muestra informacion sobre el turno'''
    if turno:
        gamelib.draw_text(f'Turno de {CIRCULO}', 50, 30)
    else:
        gamelib.draw_text(f'Turno de {CRUZ}', 50, 30)

def dibujar_contenido_grilla(juego):
    '''Dibuja el simbolo de cada celda, segun el turno'''
    for fila in range(len(juego)):
        for columna in range(len(juego[fila])):
            x, y = (PIXEL * fila + PIXEL//2), (PIXEL * columna + PIXEL//2 + ALTO[0])
            if juego[fila][columna] == CIRCULO:
                gamelib.draw_text(CIRCULO, x, y)
            elif juego[fila][columna] == CRUZ:
                gamelib.draw_text(CRUZ, x, y)

def dibujar_grilla():
    '''La funcion dibuja las lineas'''
    for x in range(0, ANCHO , PIXEL):
        gamelib.draw_line(x, ALTO[0], x, ALTO[1])
    for y in range(ALTO[0], ALTO[1], PIXEL):   
        gamelib.draw_line(0, y, ANCHO, y)

def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 15)
    dibujar_grilla()
    mostrar_turno(verificar_turno(juego))
    dibujar_contenido_grilla(juego)    

def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(300, 350)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)