def filtrar_por_participante(datos: list, id_participante: int) -> list:
    """
    Devuelve los registros correspondientes a un participante específico.

    Parámetros:
    datos (list): lista de registros.
    id_participante (int): ID del participante a filtrar.

    Retorna:
    dicc: diccionario del participante o None si no existe
    """


    for participante in datos:
        if participante["id_participante"] == id_participante:
            return participante

    return None
