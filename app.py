import os
import tempfile

import pandas as pd
import streamlit as st

from src.carga_datos import cargar_datos
from src.validacion_datos import validar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (
    calcular_tiempo_total,
    calcular_promedio_uso,
    calcular_uso_por_app,
)
from src.graficos import (
    asegurar_carpeta_graficos,
    graficar_uso_por_app,
    graficar_evolucion_temporal,
    graficar_distribucion_tiempo,
)


st.set_page_config(
    page_title="Behavior Tracker",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Behavior Tracker")
st.write("Dashboard interactivo para analizar el uso de aplicaciones por participante.")


def cargar_archivo_subido(archivo_subido):
    """
    Guarda temporalmente el archivo subido por Streamlit y lo carga usando
    la función cargar_datos del backend.

    Parámetros:
    archivo_subido: archivo CSV cargado desde st.file_uploader.

    Retorna:
    pd.DataFrame: DataFrame validado con los datos del archivo.
    """

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as archivo_temporal:
        archivo_temporal.write(archivo_subido.getvalue())
        ruta_temporal = archivo_temporal.name

    df = cargar_datos(ruta_temporal)
    validar_datos(df)

    return df


def generar_y_mostrar_graficos(df):
    """
    Genera los gráficos usando el módulo src/graficos.py y los muestra
    en la interfaz con st.image.
    """

    asegurar_carpeta_graficos("graficos")
    graficar_uso_por_app(df, "graficos")
    graficar_evolucion_temporal(df, "graficos")
    graficar_distribucion_tiempo(df, "graficos")

    st.subheader("Visualizaciones")

    col1, col2 = st.columns(2)

    with col1:
        st.image("graficos/uso_por_app.png", caption="Uso total por aplicación")

    with col2:
        st.image("graficos/evolucion_temporal.png", caption="Evolución temporal del uso")

    st.image("graficos/distribucion_tiempo.png", caption="Distribución del tiempo de uso")


archivo = st.file_uploader(
    "Subí el archivo CSV del laboratorio",
    type=["csv"]
)

if archivo is None:
    st.info("Para comenzar, subí un archivo CSV.")
else:
    try:
        df = cargar_archivo_subido(archivo)

    except ValueError as error:
        st.error(f"Error de validación: {error}")
        st.stop()

    except FileNotFoundError as error:
        st.error(f"Error de archivo: {error}")
        st.stop()

    except Exception as error:
        st.error(f"Ocurrió un error no previsto: {error}")
        st.stop()

    st.success("Archivo cargado y validado correctamente.")

    st.subheader("Vista previa de los datos")
    st.dataframe(df.head())

    st.subheader("Indicadores generales")

    cantidad_registros = len(df)
    cantidad_participantes = df["id_participante"].nunique()
    tiempo_total = calcular_tiempo_total(df)
    promedio_general = calcular_promedio_uso(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Registros", cantidad_registros)
    col2.metric("Participantes", cantidad_participantes)
    col3.metric("Tiempo total", round(tiempo_total, 2))
    col4.metric("Promedio de uso", round(promedio_general, 2))

    st.subheader("Análisis por participante")

    participantes = sorted(df["id_participante"].unique())
    id_seleccionado = st.selectbox(
        "Seleccioná un participante",
        participantes
    )

    df_participante = filtrar_por_participante(df, id_seleccionado)

    tiempo_participante = calcular_tiempo_total(df_participante)
    promedio_participante = calcular_promedio_uso(df_participante)
    uso_por_app = calcular_uso_por_app(df_participante)

    col5, col6, col7 = st.columns(3)

    col5.metric("ID participante", id_seleccionado)
    col6.metric("Tiempo total", round(tiempo_participante, 2))
    col7.metric("Promedio de uso", round(promedio_participante, 2))

    st.write("Uso por aplicación:")
    st.dataframe(uso_por_app)

    generar_y_mostrar_graficos(df)
