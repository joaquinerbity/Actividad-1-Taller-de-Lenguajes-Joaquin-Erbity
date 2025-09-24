"""
Las funciones de este módulo permiten evaluar y determinar quién fue el mejor equipo
de cada ronda.
"""

def calcular_puntaje(datos_equipo: dict):
    puntaje = datos_equipo['innovacion']*3 + datos_equipo['presentacion']*1 + ( -1 if datos_equipo['errores'] else 0)
    return puntaje

#Entrada: diccionario acum con innovacion,presentacion,errores
#Salida: puntaje (int)

def resultados_equipo(equipo:dict) ->dict:
    equipo['puntaje'] = calcular_puntaje(equipo)        #agrego el puntaje
    return equipo


def mejor_equipo_ronda(nombre: str, equipo: dict, mejor_puntaje: int, mejor_nombre: str) -> tuple:
    if equipo["puntaje"] > mejor_puntaje:
        mejor_puntaje = equipo["puntaje"]
        mejor_nombre = nombre
    return mejor_nombre, mejor_puntaje

    
#Entrada: diccionario de todos los equipos en una ronda
#Salida: una tupla [str, int] que seria: [nombre_equipo,puntaje]