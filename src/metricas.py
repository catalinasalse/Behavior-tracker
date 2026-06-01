import pandas as pd


def calcular_tiempo_total(df: pd.DataFrame) -> float:
    """
    Calcula el tiempo total de uso.

    Parámetros:
    df (pd.DataFrame): DataFrame con los registros de uso.

    Retorna:
    float: suma total de la columna tiempo_uso.
    """

    return df["tiempo_uso"].sum()


def calcular_promedio_uso(df: pd.DataFrame) -> float:
    """
    Calcula el promedio de tiempo de uso.

    Parámetros:
    df (pd.DataFrame): DataFrame con los registros de uso.

    Retorna:
    float: promedio de la columna tiempo_uso.
    """

    if df.empty:
        return 0.0

    return df["tiempo_uso"].mean()


def calcular_uso_por_app(df: pd.DataFrame) -> pd.Series:
    """
    Calcula el tiempo total de uso agrupado por aplicación.

    Parámetros:
    df (pd.DataFrame): DataFrame con los registros de uso.

    Retorna:
    pd.Series: tiempo total por aplicación.
    """

    return df.groupby("app")["tiempo_uso"].sum()


def calcular_promedio_por_app(df: pd.DataFrame) -> pd.Series:
    """
    Calcula el promedio de uso por aplicación.
    """

    return df.groupby("app")["tiempo_uso"].mean()


def calcular_promedio_por_participante(df: pd.DataFrame) -> pd.Series:
    """
    Calcula el promedio de uso por participante.
    """

    return df.groupby("id_participante")["tiempo_uso"].mean()
