def calcular_tiempo_total(datos: list) -> float:
    """
    Calcula el tiempo total de uso sumando todos los registros.

    Parámetros:
    datos (list): lista de registros.

    Retorna:
    float: tiempo total de uso.
    """

    total = 0.0

    for registro in datos:
        total += registro["tiempo_uso"]

    return total


def calcular_promedio_uso(datos: list) -> float:
    """
    Calcula el promedio de tiempo de uso.

    Parámetros:
    datos (list): lista de registros.

    Retorna:
    float: promedio de uso.
    """

    if len(datos) == 0:
        return 0.0

    total = calcular_tiempo_total(datos)
    promedio = total / len(datos)

    return promedio


def calcular_uso_por_app(datos: list) -> dict:
    """
    Calcula el tiempo total de uso por aplicación.

    Parámetros:
    datos (list): lista de registros.

    Retorna:
    dict: diccionario con app como clave y tiempo total como valor.
    """

    uso_por_app = {}

    for registro in datos:
        app = registro["app"]
        tiempo = registro["tiempo_uso"]

        if app in uso_por_app:
            uso_por_app[app] += tiempo
        else:
            uso_por_app[app] = tiempo

    return uso_por_app
