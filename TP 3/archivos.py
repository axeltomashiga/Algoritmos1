import csv
def ajustar_grilla(grilla, cantidad_de_coumnas):
    '''
    La funcion hace que cada linea del nivel se ajuste a la cantidad de columnas que haya para que sea rectangular
    '''
    grilla_nueva = []
    for fila in grilla:
        if len(fila) < cantidad_de_coumnas:
            cantidad_espacios = cantidad_de_coumnas - len(fila)
            fila += ' ' * cantidad_espacios
        grilla_nueva.append(fila)
    return grilla_nueva

def cargar_niveles(ruta_niveles):
    '''El metodo crea una lista de listas con todos los niveles a partir del archivo 'niveles.txt' para que se pueda crear la grilla, 
    teniendo en cuenta que el archivo de niveles tenga el formato de nivel, nombre, y grilla
    uno abajo del otro, que el numero de nivel y nombre no empieze por '#' o espacio y que cada nivel 
    completo este separado por un salto de linea '''
    niveles = []
    nivel = []
    cantidad_columnas = 0
    with open(ruta_niveles, 'r') as archivo_niveles:
        for linea in archivo_niveles:
            if linea == '\n':
                nivel = ajustar_grilla(nivel, cantidad_columnas)
                niveles.append(nivel)
                nivel = []
                cantidad_columnas = 0
                continue
            if linea[0] not in ('#', ' '):
                continue
            nivel.append(linea.rstrip('\n'))
            if cantidad_columnas < len(linea.rstrip('\n')):
                cantidad_columnas = len(linea.rstrip('\n'))
        nivel = ajustar_grilla(nivel, cantidad_columnas)
        niveles.append(nivel)
    return niveles

def cargar_accion_de_tecla(ruta_teclado):
    '''Devuelve que accion hace la tecla que preciona el usuario, mediante el uso de DictReader
    que crea un diccionario por cada fila leida de clave tecla y accion, con valor sus respectivas asignaciones'''
    acciones = {}
    with open(ruta_teclado, 'r') as archivo:
        acciones_teclado = csv.reader(archivo, delimiter = '=')
        for fila in acciones_teclado:
            if not fila:
                continue
            tecla, accion = fila[0], fila[1]
            acciones[tecla] = acciones.get(tecla, accion)
    return acciones
