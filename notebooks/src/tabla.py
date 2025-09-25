"""
Las funciones de este módulo implementan la posibilidad de mostrar los resultados de cada ronda
y luego los acumulados en tablas con los equipos con orden de puntaje descendente
"""

# Recibe una ronda y muestra su tabla:
def tabla_ronda(i, ronda, dict_ronda):
    print(f"\n🏁Ronda {i} : {ronda}")
    print("-" * 50)
    print(f"{'Equipo':<10} {'Innov':<6} {'Pres':<6} {'Errores':<8} {'Puntaje':<8} {'Mejor':<6}")
    print("-" * 50)

    for nombre, datos in dict_ronda.items():
        print(f"{nombre:<10} {datos['innovacion']:<6} {datos['presentacion']:<6} {str(datos['errores']):<8} {datos['puntaje']:<8} {str(datos['mejores']):<6}")


def tabla_resultados_finales(acumulados_ordenados):
    print("\n📊 Resultados Finales")
    print("-" * 50)
    print(f"{'Equipo':<10} {'Puntaje':<8} {'Mejores Rondas':<15}")
    print("-" * 50)
    
    for nombre, datos in acumulados_ordenados:
        print(f"{nombre:<10} {datos['puntaje']:<8} {datos['mejores']:<15}")

