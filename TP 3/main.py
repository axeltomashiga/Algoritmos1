import soko
import gamelib
import archivos
from pila import Pila
import pista

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

def deshacer_movimiento(estados, grilla):
    '''Vuelve al movimiento anterior'''
    if estados.esta_vacia():
        return estados, grilla
    nuevo = estados.desapilar()
    return estados, nuevo

def apilar_estados(estados, grilla):
    '''Guarda los estados del juego'''
    if estados.esta_vacia() or estados.ver_tope() != grilla:
        estados.apilar(grilla)
    return estados

def buscar_pistas(pistas, grilla):
    '''Busca las pistas del backtracking, y las devuelve en una pila'''
    gamelib.draw_begin()
    mostrar_interfaz(grilla)
    gamelib.draw_text('Buscando pista', PIXELES_GIF, PIXELES_GIF//2, size = 12, fill = '#00FF00')
    gamelib.draw_end()
    pistas = pista.movimientos_pista(grilla)
    if pistas.esta_vacia():
        pistas = None
        gamelib.say('No hay pistas')
    return pistas
    
def juego_actualizar(grilla, nivel, niveles, accion, estados, pistas):
    '''Actualiza la grilla dependiendo de la accion que el usuario haga'''
    acciones = {'NORTE':NORTE, 'SUR':SUR, 'ESTE':ESTE ,'OESTE':OESTE}
    if accion == 'REINICIAR':
        grilla = juego_crear(nivel, niveles)
        while not estados.esta_vacia():
            estados.desapilar()

    elif accion == 'VOLVER':
        estados, grilla = deshacer_movimiento(estados, grilla)

    elif accion == 'PISTA':
        if not pistas:
            pistas = buscar_pistas(pistas, grilla)
        else:
            estados = apilar_estados(estados,grilla)
            movimiento = pistas.desapilar()
            grilla = soko.mover(grilla, movimiento)
        return grilla, estados, pistas

    elif accion in acciones:
        estados = apilar_estados(estados, grilla)
        grilla = soko.mover(grilla, acciones[accion])

    elif accion == 'SALIR':
        grilla = None

    pistas = None
    return grilla, estados, pistas

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
    estados = Pila()
    pistas = None

    grilla, nivel = juego_inicializar(niveles)
   
    x, y = soko.dimensiones(grilla)
    gamelib.resize(x * PIXELES_GIF, y * PIXELES_GIF)
    
    while gamelib.is_alive():
        
        gamelib.draw_begin()
        mostrar_interfaz(grilla)
        if pistas != None:
            gamelib.draw_text('Pista encontrada', PIXELES_GIF, PIXELES_GIF//2, size = 12, fill = '#00FF00')
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        accion = procesar_tecla_presionada(tecla, acciones)
        
        grilla, estados, pistas = juego_actualizar(grilla, nivel, niveles, accion, estados, pistas)
        
        if not grilla:
            break
        
        if soko.juego_ganado(grilla):
            while not estados.esta_vacia():
                estados.desapilar()
            pistas = None
            nivel, grilla = juego_pasar_nivel(nivel, niveles)
            if not grilla:
                break
        # Actualizar el estado del juego, según la `tecla` presionada

gamelib.init(main)