import pandas as pd


def cargar_datos(ruta: str) -> pd.DataFrame:
    """
    Carga los datos desde un archivo CSV usando Pandas.

    Parámetros:
    ruta (str): Ruta del archivo CSV.

    Retorna:
    pd.DataFrame: Datos cargados en formato DataFrame.

    Raises:
    FileNotFoundError: Si no se encuentra el archivo.
    ValueError: Si el archivo está vacío o no puede leerse correctamente.
    """

    try:
        df = pd.read_csv(ruta)
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró el archivo CSV.")
    except pd.errors.EmptyDataError:
        raise ValueError("El archivo CSV está vacío.")
    except Exception:
        raise ValueError("No se pudo leer el archivo CSV.")

    return df
    
    
