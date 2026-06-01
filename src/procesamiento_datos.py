import pandas as pd


def filtrar_por_participante(df: pd.DataFrame, id_participante: int) -> pd.DataFrame:
    """
    Filtra los registros de un participante específico.

    Parámetros:
    df (pd.DataFrame): DataFrame con todos los registros.
    id_participante (int): ID del participante a filtrar.

    Retorna:
    pd.DataFrame: DataFrame con los registros del participante.

    Raises:
    ValueError: Si el participante no existe.
    """

    df_filtrado = df[df["id_participante"] == id_participante]

    if df_filtrado.empty:
        raise ValueError("No existe un participante con ese ID.")

    return df_filtrado
