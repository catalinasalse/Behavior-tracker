from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app


def main():
    """
    Programa principal que carga, valida, procesa y muestra resultados
    del uso de aplicaciones por participante.
    """

    datos = cargar_datos("datos/datos_proyecto.csv")

    datos_validos = []

    for registro in datos:
        if validar_registro(registro):
            datos_validos.append(registro)

    id_buscado = int(input("Ingrese el id del participante: "))

    datos_participante = filtrar_por_participante(datos_validos, id_buscado)

    tiempo_total = calcular_tiempo_total(datos_participante)
    promedio_uso = calcular_promedio_uso(datos_participante)
    uso_apps = calcular_uso_por_app(datos_participante)

    print("\n--- RESULTADOS ---")
    print("Participante:", id_buscado)
    print("Cantidad de registros:", len(datos_participante))
    print("Tiempo total de uso:", tiempo_total)
    print("Promedio de uso:", promedio_uso)
    print("Uso por app:", uso_apps)


main()
