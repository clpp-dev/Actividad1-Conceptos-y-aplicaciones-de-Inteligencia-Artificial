# Actividad1 Conceptos y aplicaciones de Inteligencia Artificial
Actividad 1 - Conceptos y aplicaciones de Inteligencia Artificial

## Integrantes de grupo
- Santiago Tobar Useche
- Cristian Leandro Pérez Peláez

## Curso
- Inteligencia artificial (JOAQUIN SANCHEZ 23022026_C1_202631)

## Descripción

Este proyecto contiene un programa de ejemplo que demuestra el uso de **NumPy** y **Matplotlib**, dos librerías fundamentales en Python para el desarrollo de aplicaciones de Inteligencia Artificial.

El programa visualiza las funciones de activación más comunes utilizadas en Redes Neuronales:
- **Sigmoid**: Función que mapea valores a un rango entre 0 y 1
- **Tanh**: Función tangente hiperbólica que mapea valores entre -1 y 1
- **ReLU** (Rectified Linear Unit): Función que devuelve el máximo entre 0 y x

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar o descargar el proyecto

Si aún no tienes el proyecto, descárgalo o clónalo en tu máquina local.

```bash
git clone https://github.com/clpp-dev/Actividad1-Conceptos-y-aplicaciones-de-Inteligencia-Artificial.git
```

### 2. Crear un entorno virtual (recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Esto instalará:
- **NumPy**: Para cálculos numéricos y operaciones con matrices
- **Matplotlib**: Para crear visualizaciones y gráficas

## 4. Ejecución del Programa

**Para ejecutar el programa, usa el siguiente comando:**

```bash
python funciones_activacion.py
```

### ¿Qué hace el programa?

1. Utiliza **NumPy** para:
   - Generar un rango de valores numéricos
   - Calcular las funciones matemáticas (sigmoid, tanh, ReLU)

2. Utiliza **Matplotlib** para:
   - Crear tres gráficas que muestran cada función de activación
   - Guardar la visualización como imagen PNG
   - Mostrar las gráficas en una ventana interactiva

3. El programa generará un archivo `funciones_activacion.png` con las visualizaciones.

## Archivos del Proyecto

- `funciones_activacion.py`: Programa principal
- `requirements.txt`: Lista de dependencias del proyecto
- `README.md`: Este archivo de documentación

## Librerías Utilizadas

### NumPy
NumPy es la librería fundamental para computación científica en Python. En IA se utiliza para:
- Operaciones con matrices y tensores
- Cálculos matemáticos eficientes
- Procesamiento de datos numéricos

### Matplotlib
Matplotlib es la librería principal para crear visualizaciones en Python. En IA se utiliza para:
- Visualizar datos de entrenamiento
- Graficar métricas de rendimiento
- Analizar resultados de modelos
