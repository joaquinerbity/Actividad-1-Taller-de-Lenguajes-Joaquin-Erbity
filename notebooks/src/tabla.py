"""
Las funciones de este módulo implementan la posibilidad de mostrar los resultados de cada ronda
y luego los acumulados en tablas con los equipos con orden de puntaje descendente
"""

# Recibe una ronda y muestra su tabla
def tabla_ronda(i, dict_ronda):
    #Creo una lista con los nombres de los equipos ya ordenados por puntaje, entonces el primero([0]) será el mejor equipo
    mejor_equipo = list(dict_ronda.keys())[0]
    print(f"\n Ronda {i} : En esta ronda, el mejor equipo fue el {mejor_equipo}")
    print("=" * 50)
    print(f"{'Equipo':<10} {'Innov':<6} {'Pres':<6} {'Errores':<8} {'Puntaje':<8} {'Mejor':<6}")
    print("=" * 50)

    for nombre, datos in dict_ronda.items():
        print(f"{nombre:<10} {datos['innovacion']:<6} {datos['presentacion']:<6} {str(datos['errores']):<8} {datos['puntaje']:<8} {str(datos['mejores']):<6}")

# Habiendo ordenado "acumulados" según su puntaje total, la informa como tabla
def tabla_resultados_finales(acumulados_ordenados):
    print("\n Resultados Finales")
    print("-" * 50)
    print(f"{'Equipo':<10} {'Innov':<6} {'Pres':<6} {'Errores':<8} {'Puntaje':<8} {'Mejores':<6}")
    print("-" * 50)

    for nombre, datos in acumulados_ordenados:
        print(f"{nombre:<10} {datos['innovacion']:<8} {datos['presentacion']:<8} {datos['errores']:<8} {datos['puntaje']:<8} {datos['mejores']:<15}")
    print(f"El ganador fue el {acumulados_ordenados[0][0]}")

# Informa el ranking de puntos de innovacion
def tabla_ranking_innovacion(ranking_innovacion):
    print("\n Ranking Puntos Innovacion Acumulados")
    print("-" * 50)
    print(f"{'Equipo':<10} {'Puntos Innovacion':<8}")
    print("-" * 50)

    for nombre, datos in ranking_innovacion:
        print(f"{nombre:<10} {datos['innovacion']*3:<8}")
