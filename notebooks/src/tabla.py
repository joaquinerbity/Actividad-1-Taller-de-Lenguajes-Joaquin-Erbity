"""
Las funciones de este módulo implementan la posibilidad de mostrar los resultados de cada ronda
y luego los acumulados en tablas con los equipos con orden de puntaje descendente
"""




#recibe una ronda y el mejor ya evaluado
def mostrar_ronda(ronda:dict, mejor:tuple) -> dict : 
    lista = []
    for equipo in ronda:
        
     