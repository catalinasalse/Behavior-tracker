import os
import pandas as pd
import matplotlib.pyplot as plt


def cargar_datos(ruta_csv: str) -> pd.DataFrame:
    """
    Carga los datos del archivo CSV usando Pandas.

    Args:
        ruta_csv (str): Ruta del archivo CSV que contiene los datos del proyecto.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el archivo está vacío.
    """
    if not os.path.exists(ruta_csv):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")

    df = pd.read_csv(ruta_csv)

    if df.empty:
        raise ValueError("El archivo CSV está vacío.")

    return df


def validar_datos(df: pd.DataFrame) -> bool:
    """
    Valida el DataFrame completo usando operaciones vectorizadas de Pandas.

    Controla que no haya valores vacíos, que existan las columnas esperadas,
    que los valores numéricos sean válidos y que las aplicaciones pertenezcan
    a las categorías permitidas.

    Args:
        df (pd.DataFrame): DataFrame con los datos del archivo CSV.

    Returns:
        bool: True si los datos son válidos.

    Raises:
        TypeError: Si el dato recibido no es un DataFrame.
        ValueError: Si hay columnas faltantes, valores vacíos o datos inválidos.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("El dato recibido debe ser un DataFrame de Pandas.")

    columnas_esperadas = [
        "id_participante",
        "fecha",
        "app",
        "cantidad_uso",
        "tiempo_uso"
    ]

    if list(df.columns) != columnas_esperadas:
        raise ValueError(
            "El CSV debe tener estas columnas: "
            "id_participante, fecha, app, cantidad_uso, tiempo_uso"
        )

    if df.isna().any().any():
        raise ValueError("El archivo contiene campos vacíos o valores NaN.")

    if not pd.api.types.is_integer_dtype(df["id_participante"]):
        raise ValueError("La columna id_participante debe contener números enteros.")

    if not pd.api.types.is_integer_dtype(df["cantidad_uso"]):
        raise ValueError("La columna cantidad_uso debe contener números enteros.")

    if not pd.api.types.is_numeric_dtype(df["tiempo_uso"]):
        raise ValueError("La columna tiempo_uso debe contener valores numéricos.")

    if (df["id_participante"] <= 0).any():
        raise ValueError("Los ID de participantes deben ser números positivos.")

    if (df["cantidad_uso"] < 0).any():
        raise ValueError("La cantidad de uso no puede ser negativa.")

    if (df["tiempo_uso"] < 0).any():
        raise ValueError("El tiempo de uso no puede ser negativo.")

    if not df["tiempo_uso"].between(0, 1440).all():
        raise ValueError("El tiempo de uso debe estar entre 0 y 1440 minutos.")

    apps_validas = ["instagram", "whatsapp", "youtube", "tiktok"]

    if not df["app"].str.lower().isin(apps_validas).all():
        raise ValueError("Hay aplicaciones no válidas en el archivo.")

    fechas = pd.to_datetime(df["fecha"], format="%d/%m/%Y", errors="coerce")

    if fechas.isna().any():
        raise ValueError("Las fechas deben tener formato dd/mm/aaaa.")

    return True


def filtrar_por_participante(df: pd.DataFrame, id_participante: int) -> pd.DataFrame:
    """
    Filtra los registros de un participante específico usando Pandas.

    Args:
        df (pd.DataFrame): DataFrame con todos los registros.
        id_participante (int): ID del participante que se desea consultar.

    Returns:
        pd.DataFrame: DataFrame filtrado con los registros del participante.

    Raises:
        ValueError: Si no existen registros para ese participante.
    """
    df_filtrado = df[df["id_participante"] == id_participante]

    if df_filtrado.empty:
        raise ValueError(f"No se encontraron datos para el participante {id_participante}.")

    return df_filtrado


def calcular_tiempo_total(df: pd.DataFrame) -> float:
    """
    Calcula el tiempo total de uso.

    Args:
        df (pd.DataFrame): DataFrame con registros de uso.

    Returns:
        float: Suma total de la columna tiempo_uso.
    """
    return df["tiempo_uso"].sum()


def calcular_promedio_uso(df: pd.DataFrame) -> float:
    """
    Calcula el promedio de tiempo de uso.

    Args:
        df (pd.DataFrame): DataFrame con registros de uso.

    Returns:
        float: Promedio de la columna tiempo_uso.
    """
    return df["tiempo_uso"].mean()


def calcular_uso_por_app(df: pd.DataFrame) -> pd.Series:
    """
    Calcula el tiempo total de uso por aplicación usando groupby.

    Args:
        df (pd.DataFrame): DataFrame con registros de uso.

    Returns:
        pd.Series: Serie con el tiempo total de uso agrupado por aplicación.
    """
    return df.groupby("app")["tiempo_uso"].sum()


def asegurar_carpeta_graficos(nombre_carpeta: str = "graficos") -> None:
    """
    Crea automáticamente la carpeta donde se guardarán los gráficos.

    Args:
        nombre_carpeta (str): Nombre de la carpeta que se desea crear.

    Returns:
        None
    """
    os.makedirs(nombre_carpeta, exist_ok=True)


def graficar_uso_por_app(df: pd.DataFrame) -> None:
    """
    Genera un gráfico de barras con el tiempo total de uso por aplicación.

    El gráfico se guarda automáticamente en la carpeta graficos/
    con formato PNG.

    Args:
        df (pd.DataFrame): DataFrame con registros de uso.

    Returns:
        None
    """
    asegurar_carpeta_graficos()

    uso_por_app = df.groupby("app")["tiempo_uso"].sum()

    plt.figure(figsize=(9, 5))
    uso_por_app.plot(kind="bar", edgecolor="black", alpha=0.8)

    plt.title("Tiempo total de uso por aplicación")
    plt.xlabel("Aplicación")
    plt.ylabel("Tiempo total de uso en minutos")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.tight_layout()

    plt.savefig("graficos/uso_por_app.png", dpi=300)
    plt.close()


def graficar_evolucion_temporal(df: pd.DataFrame) -> None:
    """
    Genera un gráfico de líneas con la evolución del tiempo de uso por fecha.

    El gráfico se guarda automáticamente en la carpeta graficos/
    con formato PNG.

    Args:
        df (pd.DataFrame): DataFrame con registros de uso.

    Returns:
        None
    """
    asegurar_carpeta_graficos()

    df_copia = df.copy()
    df_copia["fecha"] = pd.to_datetime(df_copia["fecha"], format="%d/%m/%Y")

    uso_por_fecha = df_copia.groupby("fecha")["tiempo_uso"].sum()

    plt.figure(figsize=(10, 5))
    uso_por_fecha.plot(kind="line", marker="o", linewidth=1.5)

    plt.title("Evolución temporal del tiempo de uso")
    plt.xlabel("Fecha")
    plt.ylabel("Tiempo total de uso en minutos")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()

    plt.savefig("graficos/evolucion_temporal.png", dpi=300)
    plt.close()


def graficar_distribucion_tiempo(df: pd.DataFrame) -> None:
    """
    Genera un boxplot para observar la distribución del tiempo de uso.

    El gráfico se guarda automáticamente en la carpeta graficos/
    con formato PNG.

    Args:
        df (pd.DataFrame): DataFrame con registros de uso.

    Returns:
        None
    """
    asegurar_carpeta_graficos()

    plt.figure(figsize=(8, 5))
    df["tiempo_uso"].plot(kind="box")

    plt.title("Distribución del tiempo de uso")
    plt.ylabel("Tiempo de uso en minutos")
    plt.grid(True, linestyle="--", alpha=0.4, axis="y")
    plt.tight_layout()

    plt.savefig("graficos/distribucion_tiempo.png", dpi=300)
    plt.close()


def mostrar_metricas(df: pd.DataFrame, id_participante: int) -> None:
    """
    Muestra en consola las métricas principales de un participante.

    Args:
        df (pd.DataFrame): DataFrame con todos los datos.
        id_participante (int): ID del participante elegido.

    Returns:
        None
    """
    df_participante = filtrar_por_participante(df, id_participante)

    tiempo_total = calcular_tiempo_total(df_participante)
    promedio_uso = calcular_promedio_uso(df_participante)
    uso_por_app = calcular_uso_por_app(df_participante)

    print("\n--- MÉTRICAS DEL PARTICIPANTE ---")
    print(f"ID participante: {id_participante}")
    print(f"Tiempo total de uso: {tiempo_total:.2f} minutos")
    print(f"Promedio de uso: {promedio_uso:.2f} minutos")

    print("\nUso por aplicación:")
    print(uso_por_app)


def main() -> None:
    """
    Ejecuta el programa principal del proyecto Behavior Tracker.

    El programa carga los datos con Pandas, valida el DataFrame completo,
    filtra los datos por participante, calcula métricas y genera gráficos
    con Matplotlib guardados en la carpeta graficos/.

    Returns:
        None
    """
    try:
        ruta_csv = "datos/BehaviorTracker_mock_data.csv"

        print("--- BEHAVIOR TRACKER ---")

        df = cargar_datos(ruta_csv)
        validar_datos(df)

        print("\nDatos cargados y validados correctamente.")
        print("\nVista previa de los datos:")
        print(df.head())

        id_participante = int(input("\nIngrese el ID del participante: "))

        if id_participante <= 0:
            raise ValueError("El ID debe ser un número entero positivo.")

        mostrar_metricas(df, id_participante)

        graficar_uso_por_app(df)
        graficar_evolucion_temporal(df)
        graficar_distribucion_tiempo(df)

        print("\nGráficos generados correctamente en la carpeta graficos/.")
        print("Programa finalizado correctamente.")

    except FileNotFoundError as error:
        print(f"\nError de archivo: {error}")

    except ValueError as error:
        print(f"\nError de validación: {error}")

    except Exception as error:
        print(f"\nError inesperado: {error}")


if __name__ == "__main__":
    main()
  
