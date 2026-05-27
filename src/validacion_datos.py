from datetime import datetime

def validar_registro(registro: dict) -> bool:
    """
    Verifica que un registro tenga tipos correctos y valores válidos.

    Parámetros:
    registro (dict): registro a validar.

    Retorna:
    bool: True si el registro es válido, False en caso contrario.
    """
    apps_validas = ["instagram", "whatsapp", "youtube", "tiktok"]


    if type(registro["id_participante"]) != int:
        return False

    if type(registro["fecha"]) != str:
        return False

    if type(registro["app"]) != str:
        return False

    if type(registro["cantidad_uso"]) != int:
        return False

    if type(registro["tiempo_uso"]) != float:
        return False

    if registro["cantidad_uso"] < 0:
        return False

    if registro["tiempo_uso"] < 0:
        return False

    if registro["tiempo_uso"] > 1440:
        return False

    if registro["app"] not in apps_validas:
        return False

    try:
        datetime.strptime(registro["fecha"], "%d/%m/%Y")
    except ValueError:
        return False

    return True
    
def validar_datos(df: pd.DataFrame) -> bool:
    """
    Valida todos los datos del DataFrame usando operaciones vectorizadas de Pandas.

    Args:
        df (pd.DataFrame): DataFrame con los registros de uso de aplicaciones.

    Returns:
        bool: True si todos los datos son válidos.

    Raises:
        ValueError: Si faltan columnas obligatorias.
        ValueError: Si existen campos vacíos o valores nulos.
        ValueError: Si hay valores negativos.
        ValueError: Si el tiempo de uso supera los límites permitidos.
        ValueError: Si hay aplicaciones no válidas.
        ValueError: Si hay fechas con formato incorrecto.
    """
    apps_validas = ["instagram", "whatsapp", "youtube", "tiktok"]

    columnas_obligatorias = [
        "id_participante",
        "fecha",
        "app",
        "cantidad_uso",
        "tiempo_uso"
    ]

    if not set(columnas_obligatorias).issubset(df.columns):
        raise ValueError("Faltan columnas obligatorias en el archivo CSV.")

    if df[columnas_obligatorias].isna().any().any():
        raise ValueError("El archivo contiene campos vacíos o valores nulos.")

    if not pd.api.types.is_numeric_dtype(df["id_participante"]):
        raise ValueError("La columna id_participante debe ser numérica.")

    if not pd.api.types.is_numeric_dtype(df["cantidad_uso"]):
        raise ValueError("La columna cantidad_uso debe ser numérica.")

    if not pd.api.types.is_numeric_dtype(df["tiempo_uso"]):
        raise ValueError("La columna tiempo_uso debe ser numérica.")

    if (df["id_participante"] <= 0).any():
        raise ValueError("Los ID de participantes deben ser positivos.")

    if (df["cantidad_uso"] < 0).any():
        raise ValueError("La cantidad de uso no puede ser negativa.")

    if (df["tiempo_uso"] < 0).any():
        raise ValueError("El tiempo de uso no puede ser negativo.")

    if not df["tiempo_uso"].between(0, 1440).all():
        raise ValueError("El tiempo de uso debe estar entre 0 y 1440 minutos.")

    if not df["app"].astype(str).str.lower().isin(apps_validas).all():
        raise ValueError("El archivo contiene aplicaciones no válidas.")

    fechas_convertidas = pd.to_datetime(
        df["fecha"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    if fechas_convertidas.isna().any():
        raise ValueError("Hay fechas con formato incorrecto. Usar dd/mm/aaaa.")

    return True
