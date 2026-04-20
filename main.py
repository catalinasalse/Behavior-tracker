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

         try:
            id_buscado = int(input("Ingrese el id del participante: "))
        except ValueError:
            raise ValueError("Debe ingresar un número entero para el ID")

        if id_buscado <= 0:
            raise ValueError("El ID debe ser un entero positivo")

        participante = filtrar_por_participante(datos, id_buscado)

        if participante is None:
            raise ValueError("El participante no existe")

        datos_validos = []

        for registro in participante["registros"]:
            if validar_registro(registro):
                datos_validos.append(registro)

        if len(datos_validos) == 0:
            raise ValueError("No hay datos válidos para calcular")

        tiempo_total = calcular_tiempo_total(datos_validos)
        promedio_uso = calcular_promedio_uso(datos_validos)
        uso_apps = calcular_uso_por_app(datos_validos)

        print("\n--- RESULTADOS ---")
        print("Participante:", id_buscado)
        print("Cantidad de registros:", len(datos_validos))
        print("Tiempo total de uso:", tiempo_total)
        print("Promedio de uso:", promedio_uso)
        print("Uso por app:", uso_apps)

    except FileNotFoundError:
        print("[ERROR CRÍTICO] Tipo de error encontrado: No se encontró el archivo | Ubicación: main")
    except ValueError as error:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {error} | Ubicación: main")
    except Exception as error:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {error} | Ubicación: main")


if __name__ == "__main__":
    main()
