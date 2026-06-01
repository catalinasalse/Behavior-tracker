import pandas as pd


def validar_datos(df: pd.DataFrame) -> None:
    """
    Valida que el DataFrame tenga las columnas, tipos y valores esperados.

    Parámetros:
    df (pd.DataFrame): DataFrame con los datos de uso de aplicaciones.

    Retorna:
    None

    Raises:
    ValueError: Si el DataFrame no cumple alguna regla de validación.
    """

    columnas_esperadas = [
        "id_participante",
        "fecha",
        "app",
        "cantidad_uso",
        "tiempo_uso"
    ]

    apps_validas = ["instagram", "whatsapp", "youtube", "tiktok"]

    if df.empty:
        raise ValueError("El archivo está vacío.")

    for columna in columnas_esperadas:
        if columna not in df.columns:
            raise ValueError(f"Falta la columna obligatoria: {columna}")

    if df[columnas_esperadas].isnull().any().any():
        raise ValueError("El archivo contiene valores vacíos.")

    try:
        df["id_participante"] = df["id_participante"].astype(int)
        df["cantidad_uso"] = df["cantidad_uso"].astype(int)
        df["tiempo_uso"] = df["tiempo_uso"].astype(float)
    except ValueError:
        raise ValueError("Hay columnas numéricas con valores inválidos.")

    if (df["id_participante"] <= 0).any():
        raise ValueError("El ID del participante debe ser positivo.")

    if (df["cantidad_uso"] < 0).any():
        raise ValueError("La cantidad de uso no puede ser negativa.")

    if (df["tiempo_uso"] < 0).any():
        raise ValueError("El tiempo de uso no puede ser negativo.")

    if (df["tiempo_uso"] > 1440).any():
        raise ValueError("El tiempo de uso no puede superar 1440 minutos.")

    if not df["app"].isin(apps_validas).all():
        raise ValueError("Hay aplicaciones no válidas.")

    try:
        pd.to_datetime(df["fecha"], format="%d/%m/%Y")
    except ValueError:
        raise ValueError("Hay fechas con formato incorrecto. El formato debe ser dd/mm/aaaa.")
