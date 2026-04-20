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
