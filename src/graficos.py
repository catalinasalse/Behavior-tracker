import os
import pandas as pd
import matplotlib.pyplot as plt


def asegurar_carpeta_graficos(carpeta: str = "graficos") -> None:
    """
    Asegura la existencia de la carpeta donde se guardarán los gráficos.

    Si la carpeta indicada no existe, la crea automáticamente. Esto permite
    que el programa pueda guardar imágenes en formato PNG sin que el usuario
    tenga que crear manualmente la carpeta.

    Args:
        carpeta (str): Nombre o ruta de la carpeta donde se guardarán
        los gráficos. Por defecto es "graficos".

    Returns:
        None
    """
    os.makedirs(carpeta, exist_ok=True)


def graficar_uso_por_app(df: pd.DataFrame, carpeta: str = "graficos") -> None:
    """
    Genera un gráfico de barras con el tiempo total de uso por aplicación.

    Args:
        df (pd.DataFrame): DataFrame con los registros de uso.
        carpeta (str): Carpeta donde se guardará el gráfico generado.

    Returns:
        None
    """
    asegurar_carpeta_graficos(carpeta)

    uso_por_app = df.groupby("app")["tiempo_uso"].sum()

    plt.figure(figsize=(9, 5))
    uso_por_app.plot(kind="bar", edgecolor="black", alpha=0.8)

    plt.title("Tiempo total de uso por aplicación", fontsize=13, fontweight="bold")
    plt.xlabel("Aplicación", fontsize=11)
    plt.ylabel("Tiempo total de uso en minutos", fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.tight_layout()

    plt.savefig(f"{carpeta}/uso_por_app.png", dpi=300)
    plt.close()


def graficar_evolucion_temporal(df: pd.DataFrame, carpeta: str = "graficos") -> None:
    """
    Genera un gráfico de líneas con la evolución del tiempo de uso por fecha.

    Args:
        df (pd.DataFrame): DataFrame con los registros de uso.
        carpeta (str): Carpeta donde se guardará el gráfico generado.

    Returns:
        None
    """
    asegurar_carpeta_graficos(carpeta)

    df_copia = df.copy()
    df_copia["fecha"] = pd.to_datetime(df_copia["fecha"], format="%d/%m/%Y")

    uso_por_fecha = df_copia.groupby("fecha")["tiempo_uso"].sum()

    plt.figure(figsize=(11, 5))
    uso_por_fecha.plot(kind="line", linewidth=1.5)

    plt.title("Evolución temporal del tiempo de uso", fontsize=13, fontweight="bold")
    plt.xlabel("Fecha", fontsize=11)
    plt.ylabel("Tiempo total de uso en minutos", fontsize=11)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()

    plt.savefig(f"{carpeta}/evolucion_temporal.png", dpi=300)
    plt.close()


def graficar_distribucion_tiempo(df: pd.DataFrame, carpeta: str = "graficos") -> None:
    """
    Genera un boxplot para analizar la distribución del tiempo de uso.

    Args:
        df (pd.DataFrame): DataFrame con los registros de uso.
        carpeta (str): Carpeta donde se guardará el gráfico generado.

    Returns:
        None
    """
    asegurar_carpeta_graficos(carpeta)

    plt.figure(figsize=(8, 5))
    df["tiempo_uso"].plot(kind="box")

    plt.title("Distribución del tiempo de uso", fontsize=13, fontweight="bold")
    plt.ylabel("Tiempo de uso en minutos", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.4, axis="y")
    plt.tight_layout()

    plt.savefig(f"{carpeta}/distribucion_tiempo.png", dpi=300)
    plt.close()
