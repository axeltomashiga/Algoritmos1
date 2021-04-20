def crear_grilla(desc):
    '''Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador

    Ejemplo:

    >>> crear_grilla([
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
    ])
    '''
    grilla = []
    for fila in range(len(desc)):
        grilla.append([])
        for columna in desc[fila]:
            grilla[fila].append(columna)
    return grilla

def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    filas = len(grilla)
    columnas = len(grilla[0])
    return columnas, filas
    
def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return grilla[f][c] == '#'

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return grilla[f][c] == '.' or grilla[f][c] == '*' or grilla[f][c] == '+'

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return grilla[f][c] == '$' or grilla[f][c] == '*'

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return grilla[f][c] == '@' or grilla[f][c] == '+'

def hay_espacio(grilla, c, f):
    '''Devuelve True hay una celda en blanco en la columna y fila (c, f).'''
    return grilla[f][c] == ' '

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for fila in grilla:
        if '.' in fila or '+' in fila:
            return False
    return True

def obtener_posicion_jugador(grilla):
    '''Obtiene la posicion de jugador'''
    
    for fila in range(len(grilla)):
        for columna in range(len(grilla[fila])):
            if hay_jugador(grilla, columna, fila):
                return fila, columna
    return None

def mover_caja(grilla, c, f, direccion):
    '''Mueve la caja a la direccion que que indica si es valido'''
    if hay_espacio(grilla, c + direccion[0], f + direccion[1]):
        grilla[f + direccion[1]][c + direccion[0]] = '$'
        if grilla[f][c] == '*':
            grilla[f][c] = '.'
            return grilla
        grilla[f][c] = ' '
    elif hay_objetivo(grilla, c + direccion[0], f + direccion[1]) and not hay_caja(grilla, c + direccion[0], f + direccion[1]):
        grilla[f + direccion[1]][c + direccion[0]] = '*'
        if grilla[f][c] == '*':
            grilla[f][c] = '.'
        else:
            grilla[f][c] = ' '
    return grilla
    
def mover_jugador(grilla, c, f, direccion):
    '''Mueve el jugador a la direccion que que indica si es valido'''
    if hay_espacio(grilla, c + direccion[0], f + direccion[1]):
        grilla[f + direccion[1]][c + direccion[0]] = '@'
        if grilla[f][c] == '+':
            grilla[f][c] = '.'
            return grilla
        grilla[f][c] = ' '
    elif hay_objetivo(grilla, c + direccion[0], f + direccion[1]) and not hay_caja(grilla, c + direccion[0], f + direccion[1]):
        grilla[f + direccion[1]][c + direccion[0]] = '+'
        if grilla[f][c] == '+':
            grilla[f][c] = '.'
        else:
            grilla[f][c] = ' '
    return grilla
    
def copiar_grilla(grilla):
    nueva_grilla = []
    for fila in grilla:
        nueva_grilla.append(fila[:])
    return nueva_grilla
    
def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.

    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:

    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur

    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.
    '''
    nueva_grilla = copiar_grilla(grilla)
    fila_jugador, columna_jugador = obtener_posicion_jugador(grilla)

    if hay_pared(nueva_grilla, columna_jugador + direccion[0], fila_jugador + direccion[1]):
        return grilla
    if hay_caja(nueva_grilla, columna_jugador + direccion[0], fila_jugador + direccion[1]):
        nueva_grilla = mover_caja(nueva_grilla, columna_jugador + direccion[0], fila_jugador + direccion[1], direccion)
        nueva_grilla = mover_jugador(nueva_grilla, columna_jugador, fila_jugador, direccion)
    elif hay_espacio(nueva_grilla, columna_jugador + direccion[0], fila_jugador + direccion[1]) or hay_objetivo(nueva_grilla, columna_jugador + direccion[0], fila_jugador + direccion[1]):
        nueva_grilla = mover_jugador(nueva_grilla, columna_jugador, fila_jugador, direccion)
    return nueva_grilla