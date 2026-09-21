# Taller I de Inteligencia Artificial

Repositorio de ejercicios prácticos desarrollados en Python para estudiar fundamentos de álgebra lineal, procesamiento digital de imágenes, visión por computador, aprendizaje automático y redes neuronales.

Los ejercicios son demostraciones autocontenidas: los datos de prueba y las imágenes de ejemplo se generan dentro de los scripts, por lo que no se necesita un dataset externo para ejecutarlos.

## Contenido del proyecto

### Guías de procesamiento de imágenes

| Archivo | Tema | Actividades principales |
| --- | --- | --- |
| [`guia1.py`](guia1.py) | Python y álgebra lineal | Manipulación de matrices, acceso a posiciones, generación de una matriz identidad, cálculo de dimensiones de una imagen RGB y producto de Hadamard con un filtro. |
| [`guia2.py`](guia2.py) | Imágenes y canales de color | Creación o carga de una imagen, separación de canales BGR, conversión a escala de grises, cálculo del canal dominante y generación de histogramas. |
| [`guia3.py`](guia3.py) | Umbralización y morfología | Binarización con umbral, eliminación de ruido mediante apertura y cierre morfológico. |
| [`guia4.py`](guia4.py) | Filtros de suavizado | Aplicación de filtros de media, Gaussiano y mediana sobre una imagen con ruido sal y pimienta. |
| [`guia5.py`](guia5.py) | Detección de bordes | Cálculo de gradientes con Sobel y comparación de Canny usando distintos umbrales. |
| [`guia6.py`](guia6.py) | Contornos y análisis de objetos | Detección de contornos, cálculo de área, perímetro, centroide y caja delimitadora, además de clasificación por tamaño. |

### Talleres de aprendizaje automático y redes neuronales

| Archivo | Tema | Actividades principales |
| --- | --- | --- |
| [`taller 9.py`](taller%209.py) | K vecinos más cercanos (KNN) | Predicción de compra de un cliente a partir de edad, salario y número de hijos. Compara los resultados con `K=1` y `K=5`. |
| [`taller 10.py`](taller%2010.py) | Máquinas de vectores de soporte (SVM) | Clasificación de puntos con un SVM de kernel RBF, consulta de los vectores de soporte y predicción de un punto nuevo. |
| [`taller 11.py`](taller%2011.py) | Perceptrón | Implementación desde cero de una neurona con función de activación escalón para resolver la compuerta lógica OR. |
| [`taller 12.py`](taller%2012.py) | Red neuronal multicapa | Cálculo manual de una capa oculta y una capa de salida con activación sigmoide para obtener probabilidades de dos clientes. |

## Requisitos

- Python 3.9 o superior.
- NumPy.
- OpenCV (`opencv-python`).
- Matplotlib.
- scikit-learn, utilizado en los talleres 9 y 10.

## Instalación

Desde la carpeta raíz del proyecto, se recomienda crear y activar un entorno virtual:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Instala las dependencias declaradas y la dependencia adicional de los talleres de clasificación:

```bash
python -m pip install -r requirements.txt scikit-learn
```

También se pueden instalar directamente:

```bash
python -m pip install numpy opencv-python matplotlib scikit-learn
```

## Ejecución

Todos los archivos pueden ejecutarse de forma independiente desde la raíz del proyecto.

### Ejecutar las guías

```bash
python guia1.py
python guia2.py
python guia3.py
python guia4.py
python guia5.py
python guia6.py
```

### Ejecutar los talleres

Los nombres de estos archivos contienen espacios, por lo que deben escribirse entre comillas:

```bash
python "taller 9.py"
python "taller 10.py"
python "taller 11.py"
python "taller 12.py"
```

## Resultados generados

Al ejecutar las guías 2 a 6 se crea automáticamente la carpeta `resultados/` con imágenes de salida:

- `guia2`: canales BGR, imagen en escala de grises e histogramas.
- `guia3`: imagen binarizada, resultado de apertura y resultado de cierre.
- `guia4`: imagen con ruido y resultados de los tres filtros.
- `guia5`: bordes Sobel y bordes Canny con tres pares de umbrales.
- `guia6`: imagen binaria y objetos delimitados por sus contornos.

La guía 2 también crea `imagenes/guia2.jpg` cuando no existe una imagen de entrada, usando una imagen sintética de demostración. Las guías 1 y los talleres 9 a 12 muestran sus resultados directamente en la terminal.

## Objetivos de aprendizaje

- Representar imágenes y datos mediante matrices de NumPy.
- Comprender canales de color, escala de grises e histogramas.
- Aplicar umbralización, operaciones morfológicas y filtros de reducción de ruido.
- Detectar bordes y analizar sus efectos al variar los umbrales.
- Extraer características geométricas de objetos mediante contornos.
- Comprender la clasificación basada en vecinos cercanos y vectores de soporte.
- Relacionar pesos, sesgo, combinación lineal y función de activación en una neurona.
- Seguir el flujo de datos a través de las capas de una red neuronal multicapa.

## Observaciones

- Las imágenes de prueba son sintéticas y se generan automáticamente; no se incluyen imágenes externas en el repositorio.
- OpenCV utiliza el orden de canales BGR, mientras que muchas explicaciones de color utilizan RGB.
- KNN y SVM se ejecutan con scikit-learn.
- El perceptrón y la red neuronal multicapa se calculan manualmente con NumPy; no realizan entrenamiento automático ni actualización de pesos.
- Las carpetas `imagenes/` y `resultados/` se crean al ejecutar los scripts que las necesitan.
