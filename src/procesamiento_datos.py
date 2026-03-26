def filtrar_por_participante(datos: list, id_participante: int) -> list:
    """
    Devuelve los registros correspondientes a un participante específico.

    Parámetros:
    datos (list): lista de registros.
    id_participante (int): ID del participante a filtrar.

    Retorna:
    list: lista de registros del participante.
    """

    filtrados = []

    for registro in datos:
        if registro["id_participante"] == id_participante:
            filtrados.append(registro)

    return filtrados
