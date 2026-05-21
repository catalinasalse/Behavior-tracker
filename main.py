from src.carga_datos import cargar_datos
from src.validacion_datos import validar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (
    calcular_tiempo_total,
    calcular_promedio_uso,
    calcular_uso_por_app,
    calcular_promedio_por_app,
    calcular_promedio_por_participante,
)
from src.graficos import (
    asegurar_carpeta_graficos,
    graficar_uso_por_app,
    graficar_evolucion_temporal,
    graficar_distribucion_tiempo,
)


def mostrar_metricas_generales(df):
    """
    Muestra en consola las métricas generales del sistema.

    Args:
        df (pd.DataFrame): DataFrame con todos los registros de uso.

    Returns:
        None
    """
    print("\n--- MÉTRICAS GENERALES ---")

    promedio_por_app = calcular_promedio_por_app(df)
    promedio_por_participante = calcular_promedio_por_participante(df)

    print("\nPromedio de uso por aplicación:")
    print(promedio_por_app)

    print("\nPromedio de uso por participante:")
    print(promedio_por_participante)


def mostrar_metricas_participante(df, id_participante):
    """
    Filtra los datos de un participante y muestra sus métricas principales.

    Args:
        df (pd.DataFrame): DataFrame con todos los registros de uso.
        id_participante (int): ID del participante que se desea consultar.

    Returns:
        None

    Raises:
        ValueError: Si el participante no existe en el DataFrame.
    """
    df_participante = filtrar_por_participante(df, id_participante)

    tiempo_total = calcular_tiempo_total(df_participante)
    promedio_uso = calcular_promedio_uso(df_participante)
    uso_por_app = calcular_uso_por_app(df_participante)

    print("\n--- MÉTRICAS DEL PARTICIPANTE ---")
    print(f"ID del participante: {id_participante}")
    print(f"Cantidad de registros: {len(df_participante)}")
    print(f"Tiempo total de uso: {tiempo_total}")
    print(f"Promedio de uso: {promedio_uso:.2f}")

    print("\nUso total por aplicación:")
    print(uso_por_app)


def generar_graficos(df):
    """
    Genera y guarda automáticamente los gráficos del proyecto.

    Los gráficos se guardan en la carpeta graficos/ en formato PNG.

    Args:
        df (pd.DataFrame): DataFrame con todos los registros de uso.

    Returns:
        None
    """
    asegurar_carpeta_graficos("graficos")

    graficar_uso_por_app(df, "graficos")
    graficar_evolucion_temporal(df, "graficos")
    graficar_distribucion_tiempo(df, "graficos")

    print("\n--- GRÁFICOS GENERADOS ---")
    print("Los gráficos fueron guardados correctamente en la carpeta graficos/.")


def main():
    """
    Ejecuta el flujo principal del sistema Behavior Tracker.

    El programa realiza los siguientes pasos:
    1. Carga el archivo CSV usando Pandas.
    2. Valida los datos de forma vectorizada.
    3. Muestra una vista previa de los datos.
    4. Calcula métricas generales.
    5. Solicita un ID de participante y muestra sus métricas.
    6. Genera gráficos con Matplotlib y los guarda en graficos/.

    Returns:
        None
    """
    try:
        ruta_csv = "datos/BehaviorTracker_mock_data.csv"

        print("--- BEHAVIOR TRACKER ---")
        print("Cargando datos...")

        df = cargar_datos(ruta_csv)

        print("Validando datos...")
        validar_datos(df)

        print("\nDatos cargados y validados correctamente.")

        print("\n--- VISTA PREVIA DEL DATAFRAME ---")
        print(df.head())

        mostrar_metricas_generales(df)

        id_participante = int(input("\nIngrese el ID del participante a consultar: "))

        if id_participante <= 0:
            raise ValueError("El ID del participante debe ser un número entero positivo.")

        mostrar_metricas_participante(df, id_participante)

        generar_graficos(df)

        print("\nEjecución finalizada correctamente.")

    except FileNotFoundError as error:
        print(f"\n[ERROR DE ARCHIVO] {error}")

    except ValueError as error:
        print(f"\n[ERROR DE VALIDACIÓN] {error}")

    except KeyError as error:
        print(f"\n[ERROR DE COLUMNA] No se encontró la columna esperada: {error}")

    except Exception as error:
        print(f"\n[ERROR NO PREVISTO] {error}")


if __name__ == "__main__":
    main()
