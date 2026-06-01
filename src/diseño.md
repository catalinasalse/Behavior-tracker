# Diseño del Dashboard - Behavior Tracker

## Objetivo general

El objetivo del dashboard es permitir que un usuario cargue un archivo CSV con datos de uso de aplicaciones y pueda visualizar métricas generales, métricas por participante y gráficos de forma interactiva.

## Flujo de usuario

1. El usuario ingresa a la interfaz web.
2. El sistema muestra un cargador de archivos CSV.
3. El usuario sube el archivo de datos.
4. El sistema carga y valida el archivo.
5. Si hay errores, se muestra un mensaje con st.error y se detiene el avance.
6. Si los datos son válidos, se muestran indicadores clave mediante st.metric.
7. El usuario puede seleccionar un participante.
8. El sistema muestra métricas específicas del participante.
9. El sistema genera y muestra gráficos del comportamiento de uso.

## Datos esperados

El archivo CSV debe contener las siguientes columnas:

- id_participante
- fecha
- app
- cantidad_uso
- tiempo_uso

## Validaciones

El sistema debe validar:

- Que el archivo no esté vacío.
- Que tenga las columnas esperadas.
- Que no existan valores vacíos.
- Que el ID del participante sea positivo.
- Que cantidad_uso no sea negativa.
- Que tiempo_uso no sea negativo.
- Que tiempo_uso no supere 1440 minutos.
- Que la aplicación pertenezca a las apps válidas.
- Que la fecha tenga formato correcto.

## Métricas principales

El dashboard debe mostrar:

- Cantidad total de registros.
- Cantidad de participantes.
- Tiempo total de uso.
- Promedio general de uso.
- Tiempo total por participante.
- Promedio de uso por participante.
- Uso por aplicación.

## Gráficos

El dashboard debe mostrar los gráficos generados por el módulo de gráficos:

- Uso por aplicación.
- Evolución temporal del tiempo de uso.
- Distribución del tiempo de uso.

## Archivos conectados

La interfaz web se conecta con los módulos existentes del proyecto:

- src/carga_datos.py
- src/validacion_datos.py
- src/procesamiento_datos.py
- src/metricas.py
- src/graficos.py

## Decisiones de diseño

Se mantiene la estructura original del repositorio. La interfaz web se agrega como un archivo independiente llamado app.py en la raíz del proyecto. El programa main.py se conserva como orquestador por consola.
