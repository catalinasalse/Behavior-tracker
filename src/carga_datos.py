def parsear_linea(linea: str) -> dict:
    """
    Convierte una línea del archivo CSV en un diccionario.

    Parámetros:
    linea (str): línea con datos separados por comas.

    Retorna:
    dict: diccionario con id_participante, fecha, app,
          cantidad_uso y tiempo_uso.
    """

    partes = linea.strip().split(",")

    registro = {
        "id_participante": int(partes[0]),
        "fecha": partes[1],
        "app": partes[2],
        "cantidad_uso": int(partes[3]),
        "tiempo_uso": float(partes[4])
    }

    return registro


def cargar_datos(ruta: str) -> list:
    """
    Lee un archivo CSV y convierte cada línea en un registro.

    Parámetros:
    ruta (str): ruta del archivo CSV.

    Retorna:
    list: lista de registros (diccionarios).
    """

    datos = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    for linea in lineas[1:]:  # salta encabezado
        registro = parsear_linea(linea)
        datos.append(registro)

    return datos
