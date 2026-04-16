# Behavior-tracker

Sistema que permite analizar el uso de aplicaciones por participante a partir de datos en un archivo CSV.

## Funcionalidades
- Lectura de datos
- Validación de registros
- Filtrado por participante
- Cálculo de métricas:
  - Tiempo total
  - Promedio de uso
  - Uso por aplicación
- Detectar errores y validaciones 

## Estructura
- `src/`: funciones del programa
- `datos/`: archivo CSV
- `diagramas/`: diagramas de flujo
- `main.py`: programa principal

## Integrantes 
 - Olivia Salmoyraghi
 - Belen Blaksley
 - Maia Uranga 
 - Catalina Salse

## Errores y validaciones 
- No encontrar el archivo. Esto hace que no pueda correr el programa ya que no hay nada para leer. 
- ID invalido. Si al pedir el ID ingresan letras o un numero no valido como por ejemplo "3.5"
- Lista vacia. Si la lista datos_validos esta vacia puede generar un error a la hora de enocntrar el promedio
- Hay que validar que el ID sea un numero, entero y positivo.
- Hay que validar que si la lista esta vacia, es decir len(datos_validos)==0 muestre que no hay datos para calcular
- Usando el except Exception as error caputramos cualquier error que no hayamos previsto

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

