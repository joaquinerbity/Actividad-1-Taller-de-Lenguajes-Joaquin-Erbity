"""
Las funciones de este módulo permiten inicializar y actualizar los acumulados por equipo.
"""

#Crea un diccionario base con los campos:
#{"innovacion": 0, "presentacion": 0, "errores": 0, "mejores": 0, "total": 0}.
def resetear_valores():
    return {"innovacion": 0, "presentacion": 0, "errores": 0, "mejores": 0, "puntaje": 0}

#Utilicé lambda y map únicamente para ya asegurarnos de usarlos en algun lado,
#no es lo más eficiente, preguntar si lo hacemos así o con dict comprehension
def inicializar_acumulados(evaluaciones):   
    equipos = evaluaciones[0].keys()
    acumulados = dict(map(lambda equipo: (equipo, resetear_valores()), equipos))    #map recorre la lista de equipos(nombres), lambda recibe el argumento del nombre del equipo,
    return acumulados                                                               #y con el diccionario reseteado por la función, crea una tupla ("Nombre Equipo",{"innovacion":0,"errores":0,...}), luego esa lista de tuplas es dict()                 

#En el programa principal se puede probar así:
#(recordar(import pprint) para imprimir lindo el diccionario)
#acum = inicializar_acumulados(evaluaciones)
#pprint.porint(acum)

#Suma innovacion,presentacion,errores,totales.
#Incrementa el contador de mejores equipos si corresponde
#O sea, en una sola pasada tiene que tocar todos los campos del acumulado.

def actualizar_acumulados(acum: dict, equipo: dict, nom_equipo) -> None:    #escribí none porque no devuelve nada, solo actualiza acumulados
    acum[nom_equipo]["innovacion"] += equipo["innovacion"]
    acum[nom_equipo]["presentacion"] += equipo["presentacion"]

    acum[nom_equipo]["puntaje"] += equipo["puntaje"]

    if equipo["errores"]:
        acum[nom_equipo]["errores"] += 1
        acum[nom_equipo]["puntaje"] -= 1


# Actualizar la info "mejores" de acumulados se hace aparte para hacer solo un bucle
def marcar_mejor_equipo(acum: dict, nombre: str):
    acum[nombre]["mejores"] += 1

# Ranking actividad 4, para puntos por innovacion
def ranking_innovacion(acumulados):
    return sorted(
        acumulados.items(),
        key=lambda item: item[1]['innovacion'],
        reverse=True
    )