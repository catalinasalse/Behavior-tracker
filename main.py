from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app


def main():
    """
    Programa principal que carga, valida, procesa y muestra resultados
    del uso de aplicaciones por participante.
    """
    try:
        ruta = "datos/BehaviorTracker_mock_data.csv"

        datos = cargar_datos(ruta)

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
    
    except FileNotFoundError:
        print("Error: el archivo CSV no se encontro en la carpeta datos/")
    except ValueError:
        print("Error: debe ingresar un numero valido para el ID")
    except Exception as error:
        print("Error inesperado:", error)
        
if __name__ == "__main__":
    main()
    
