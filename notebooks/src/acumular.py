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

def actualizar_acumulados(acum: dict, ronda: dict, mejor: str) -> dict: 
    for nom_equipo, datos_equipo in ronda.items():
        acum[nom_equipo]["innovacion"] += datos_equipo["innovacion"]
        acum[nom_equipo]["presentacion"] += datos_equipo["presentacion"]
        if (nom_equipo == mejor):
            acum[nom_equipo]["mejores"] += 1

        acum[nom_equipo]["puntaje"] += datos_equipo["puntaje"]

        if datos_equipo["errores"]:
            acum[nom_equipo]["errores"] += 1
            acum[nom_equipo]["puntaje"] -= 1