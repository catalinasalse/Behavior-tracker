# Behavior-tracker

Sistema que permite analizar el uso de aplicaciones por participante a partir de datos en un archivo CSV.
El proyecto fue adaptado para la Actividad 7 incorporando **Pandas** para la carga, validación, filtrado y cálculo de métricas, y **Matplotlib** para la generación automática de gráficos en formato `.png`

## Funcionalidades
- Leer datos desde un archivo CSV usando Pandas.
- Validar el dataset antes de procesarlo.
- Detectar errores en los datos.
- Filtrar registros por participante.
- Calcular métricas de uso.
- Calcular el tiempo total de uso.
- Calcular el promedio de uso.
- Calcular el uso por aplicación.
- Generar gráficos con Matplotlib.
- Crear automáticamente una carpeta llamada `graficos/`.
- Guardar los gráficos generados en formato `.png`.

## Estructura
- `src/`: funciones del programa
- `datos/`: BehaviorTracker_mock_data.csv
- `diagramas/`: diagramas de flujo
- `graficos/`: gráficos generados automáticamente
- main.py
- README.md


## Integrantes 
 - Olivia Salmoyraghi
 - Belen Blaksley
 - Maia Uranga 
 - Catalina Salse

## Errores y validaciones 
- El programa utiliza bloques try y except para manejar errores durante la ejecución. Puede detectar errores como:
- Archivo CSV no encontrado.
- Archivo CSV vacío.
- Columnas faltantes o incorrectas.
- Valores vacíos.
- Datos numéricos inválidos.
- Valores negativos.
- Tiempo de uso fuera del rango permitido.
- Aplicaciones no válidas.
- Fechas con formato incorrecto.
- ID de participante inexistente.
- ID ingresado por el usuario con formato incorrecto.
  
## Objetos
Clase: Participante

Atributos:
- id_participante
- registros

Métodos:
- calcular_tiempo_total()
- calcular_promedio()
- calcular_uso_por_app()

Clase: RegistroUso

Atributos:
- fecha
- app
- cantidad_uso
- tiempo_uso

Métodos:
- validar_registro()

Clase: BehaviorTracker

Atributos:
- lista_participantes

Métodos:
- cargar_datos()
- filtrar_participante()
- calcular_metricas()

## Implementación de Pandas para la lectura del dataset

Para esta entrega, el programa fue adaptado para trabajar con Pandas.

El archivo main.py carga los datos usando pd.read_csv(). Esto permite trabajar con los datos en forma de DataFrame, es decir, como una tabla compuesta por filas y columnas.

El uso de Pandas permite reemplazar la lectura manual del archivo CSV y facilita el procesamiento de los datos.

# Métricas calculadas

El programa calcula métricas utilizando funciones de Pandas como .sum(), .mean() y .groupby().

Las métricas principales son:

Tiempo total de uso de un participante.
Promedio de uso de un participante.
Uso total por aplicación.

# Implementación con Matplotlib

El programa utiliza Matplotlib para generar gráficos a partir de los datos procesados.

Los gráficos se guardan automáticamente en la carpeta graficos/, ubicada en la raíz del repositorio.

La carpeta se crea automáticamente desde el código usando os.makedirs("graficos", exist_ok=True). Esto permite que el programa funcione aunque la carpeta todavía no exista.

# Gráficos generados

El programa genera tres gráficos en formato .png:

uso_por_app.png: gráfico de barras que muestra el tiempo total de uso por aplicación.
evolucion_temporal.png: gráfico de líneas que muestra la evolución del tiempo de uso por fecha.
distribucion_tiempo.png: gráfico de caja que muestra la distribución del tiempo de uso.

## Funciones que se deberían modificar

Para implementar Pandas, se deberían modificar principalmente estas funciones:

- `cargar_datos()`: debería usar `pd.read_csv()` para cargar el archivo CSV y devolver un `DataFrame`.
- `validar_registro()` o funciones de validación: para validar columnas completas del `DataFrame`, por ejemplo valores vacíos, tipos de datos y valores negativos.
- `filtrar_por_participante()`: debería filtrar los datos usando la columna `id_participante`
- `calcular_tiempo_total()`: podría usar `.sum()` sobre la columna `tiempo_uso`.

También debería adaptarse el `main.py`, ya que el programa pasaría a trabajar con un `DataFrame` en lugar de listas o diccionarios.

## Instrucciones de uso 
1. Ejecutar el programa

Abrir el proyecto y ejecutar el archivo principal:

```bash
python main.py

2. Esperar la carga de datos

El sistema cargará automáticamente el archivo CSV ubicado en la carpeta datos/.

Luego, validará que los datos estén completos y tengan el formato correcto.

3. Ingresar el ID del participante

El programa pedirá ingresar el ID del participante que se desea consultar.

Ejemplo:

Ingrese el ID del participante: 1

El ID debe ser un número entero positivo.

4. Consultar los resultados

Después de ingresar el ID, el sistema mostrará en pantalla las métricas principales del participante:

Tiempo total de uso de aplicaciones.
Promedio de tiempo de uso.
Uso total por aplicación.

5. Revisar los gráficos generados

Al finalizar la ejecución, el programa generará automáticamente gráficos en formato .png.

Estos gráficos se guardarán dentro de la carpeta:

graficos/

Los gráficos permiten visualizar:

El uso total por aplicación.
La evolución temporal del tiempo de uso.
La distribución general del tiempo de uso.


## Guía de Ejecución de la Interfaz Web

Además del programa por consola, el proyecto cuenta con una interfaz web desarrollada con Streamlit.

Para ejecutar el dashboard, primero se deben instalar las librerías necesarias:

```bash
pip install streamlit pandas matplotlib

