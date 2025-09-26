"""
Las funciones de este módulo permiten evaluar y determinar quién fue el mejor equipo
de cada ronda.
"""

# Recibe el diccionario de los datos de un equipo, y devuelve su puntaje (int)
def calcular_puntaje(datos_equipo):
    puntaje = datos_equipo['innovacion']*3 + datos_equipo['presentacion']*1 + ( -1 if datos_equipo['errores'] else 0)
    return puntaje

# Recibe un equipo y devuelve una tupla del nombre y puntaje actualizados del que al momento es el mejor equipo
def mejor_equipo_ronda(nombre, equipo, mejor_puntaje, mejor_nombre):
    if equipo["puntaje"] > mejor_puntaje:
        mejor_puntaje = equipo["puntaje"]
        mejor_nombre = nombre
    return mejor_nombre, mejor_puntaje