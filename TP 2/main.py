import soko
import gamelib
import archivos
OESTE = (-1, 0)
ESTE = (1, 0)     
NORTE = (0, -1)
SUR = (0, 1)
PIXELES_GIF = 64

def juego_inicializar(niveles):
    '''Inicializa el estado del juego en el primer nivel'''
    nivel = 0
    grilla = juego_crear(nivel, niveles)
    return grilla, nivel

def juego_crear(nivel, niveles):
    '''Devuelve la grilla dependiendo del nivel, siendo este un numero entero que indicara
    el numero del indice en la lista'''
    return soko.crear_grilla(niveles[nivel])

def juego_pasar_nivel(nivel, niveles):
    '''Prosigue al siguiente nivel, devulve None con respecto a la grilla si supera el ultimo nivel'''
    nivel += 1
    if nivel == len(niveles):
        gamelib.say('Felicidades, compleataste todos los niveles')
        return nivel, None
    grilla = juego_crear(nivel, niveles)
    x, y = soko.dimensiones(grilla)
    gamelib.resize(x * PIXELES_GIF, y * PIXELES_GIF)
    return nivel, grilla

def juego_actualizar(grilla, nivel, niveles, accion):
    '''Actualiza la grilla dependiendo de la accion que el usuario haga'''
    if accion == 'REINICIAR':
        grilla = juego_crear(nivel, niveles)
    elif accion == 'NORTE':
        grilla = soko.mover(grilla, NORTE)
    elif accion == 'SUR':
        grilla = soko.mover(grilla, SUR)    
    elif accion == 'ESTE':
        grilla = soko.mover(grilla, ESTE) 
    elif accion == 'OESTE':
        grilla = soko.mover(grilla, OESTE)
    elif accion == 'SALIR':
        return None
    return grilla

def mostrar_interfaz(grilla):
    '''Muestra la interfaz a partir de la grilla, en su estado actual, dependiendo de su simbolo se mostrara en la interfaz
    el gif correspondiente'''
    columnas, filas = soko.dimensiones(grilla)
    for fila in range(filas):
        for columna in range(columnas):
            gamelib.draw_image('img/ground.gif', columna * PIXELES_GIF , fila * PIXELES_GIF)
            if soko.hay_caja(grilla, columna, fila):
                gamelib.draw_image('img/box.gif', columna * PIXELES_GIF , fila * PIXELES_GIF)
            if soko.hay_objetivo(grilla, columna, fila):
                gamelib.draw_image('img/goal.gif', columna * PIXELES_GIF , fila * PIXELES_GIF )
            if soko.hay_jugador(grilla, columna, fila):
                gamelib.draw_image('img/player.gif', columna * PIXELES_GIF , fila * PIXELES_GIF )
            if soko.hay_pared(grilla, columna, fila):
                gamelib.draw_image('img/wall.gif', columna * PIXELES_GIF , fila * PIXELES_GIF )

def procesar_tecla_presionada(tecla_usuario, acciones):
    '''Devuelve la accion que realiza el usuario, mediante la tecla presionada, y el diccionario que tiene de clave a la tecla 
    y valor la accion'''
    if tecla_usuario not in acciones:
        return None
    return acciones[tecla_usuario]

def main():
    # Inicializar el estado del juego
    niveles = archivos.cargar_niveles('niveles.txt')
    acciones = archivos.cargar_accion_de_tecla('teclas.txt')

    grilla, nivel = juego_inicializar(niveles)
    
    x, y = soko.dimensiones(grilla)
    gamelib.resize(x * PIXELES_GIF, y * PIXELES_GIF)
    
    while gamelib.is_alive():
        
        gamelib.draw_begin()
        mostrar_interfaz(grilla)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        accion = procesar_tecla_presionada(tecla, acciones)
        grilla = juego_actualizar(grilla, nivel, niveles, accion)
        
        if not grilla:
            break

        if soko.juego_ganado(grilla):
            nivel, grilla = juego_pasar_nivel(nivel, niveles)
            if not grilla:
                break
        # Actualizar el estado del juego, según la `tecla` presionada

gamelib.init(main)