from datetime import datetime

def parsear_linea(linea: str) -> dict:
    """
    Convierte una línea del archivo CSV en un diccionario.

    Parámetros:
    linea (str): línea con datos separados por comas.

    Retorna:
    dict: diccionario con id_participante, fecha, app,
          cantidad_uso y tiempo_uso.
    """

    if linea.strip() == "":
        raise ValueError("La linea está vacia")
    
    partes = linea.strip().split(",")
    
    if len(partes) != 5:
        raise ValueError("La linea no tiene la cantidad correcta de columnas")
    for parte in partes:
        if parte.strip() == "":
            raise ValueError("Hay campos vacios en la linea")
    try:
        registro = {
            "id_participante": int(partes[0]),
            "fecha": partes[1],
            "app": partes[2],
            "cantidad_uso": int(partes[3]),
            "tiempo_uso": float(partes[4])
            }
    
    except ValueError:
        raise ValueError("Hay datos con tipo incorrecto")

    if registro["id_participante"] <= 0:
        raise ValueError("El ID del participante debe ser un entero positivo")

    if registro["cantidad_uso"] < 0:
        raise ValueError("La cantidad de uso no puede ser negativa")

    if registro["tiempo_uso"] < 0:
        raise ValueError("El tiempo de uso no puede ser negativo")

    if registro["tiempo_uso"] > 1440:
        raise ValueError("El tiempo de uso está fuera de rango")

    apps_validas = ["instagram", "whatsapp", "youtube", "tiktok"]

    if registro["app"] not in apps_validas:
        raise ValueError("La app no es válida")

    try:
        datetime.strptime(registro["fecha"], "%d/%m/%Y")
    except ValueError:
        raise ValueError("La fecha no tiene un formato válido")
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
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró el archivo")

    if len(lineas) == 0:
        raise ValueError("El archivo está vacío")

    if len(lineas) == 1:
        raise ValueError("El archivo solo contiene encabezado")

    for numero_linea, linea in enumerate(lineas[1:], start=2):
        registro = parsear_linea(linea)

        id_participante = registro["id_participante"]

        participante_encontrado = None

        for participante in datos:
            if participante["id_participante"] == id_participante:
                participante_encontrado = participante
                break

        registro_sin_id = {
            "fecha": registro["fecha"],
            "app": registro["app"],
            "cantidad_uso": registro["cantidad_uso"],
            "tiempo_uso": registro["tiempo_uso"]
        }

        if participante_encontrado is None:
            nuevo_participante = {
                "id_participante": id_participante,
                "registros": [registro_sin_id]
            }
            datos.append(nuevo_participante)
        else:
            ultima_fecha = participante_encontrado["registros"][-1]["fecha"]
            fecha_actual = registro["fecha"]

            fecha_1 = datetime.strptime(ultima_fecha, "%d/%m/%Y")
            fecha_2 = datetime.strptime(fecha_actual, "%d/%m/%Y")

            if fecha_2 < fecha_1:
                raise ValueError(
                    f"Línea {numero_linea}: las fechas del participante no están en orden creciente"
                )

            participante_encontrado["registros"].append(registro_sin_id)

    if len(datos) == 0:
        raise ValueError("La base de datos está vacía")

    return datos
    
    
