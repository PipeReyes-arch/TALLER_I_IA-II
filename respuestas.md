# Respuestas - Inteligencia Artificial II

Este archivo reúne las preguntas abiertas y los cálculos solicitados en las 6 guías originales.

---

# GUÍA 1 - Refuerzo Python y Álgebra Lineal

## 1. Valor de A[2,3]
Usando índice base 0, la fila 2 es `[255, 0, 128, 0, 255]`. Por lo tanto:

**A[2,3] = 0**.

Visualmente representa un píxel negro o de intensidad mínima.

## 2. Tensor RGB 1080 x 1920 x 3

1080 × 1920 × 3 = **6.220.800 valores**.

Si cada valor ocupa 1 byte, la imagen ocupa aproximadamente **6.220.800 bytes**, es decir, cerca de **5,93 MB** sin compresión.

## 3. Transpuesta de la identidad 4x4

La matriz identidad transpuesta sigue siendo exactamente igual:

```text
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
```

Geométricamente no cambia porque sus elementos diferentes de cero están sobre la diagonal principal y la transposición intercambia filas por columnas sin mover esa diagonal.

## 4. Flatten de una imagen RGB (200,200,3)

200 × 200 × 3 = **120.000 valores**.

La capa de entrada necesita **120.000 neuronas** para recibir el vector completo.

## 5. Kernel de realce

Con la matriz de imagen:

```text
100 100 100
100 200 100
100 100 100
```

Y el kernel:

```text
 0 -1  0
-1  5 -1
 0 -1  0
```

El producto y suma dan:

**1000 - 400 = 600**.

El valor central calculado es **600** antes de cualquier clipping a 8 bits.

---

# GUÍA 2 - Tensor de Color y Análisis Estadístico

## 1. Shape del recorte

La instrucción:

```python
recorte = imagen[100:200, 300:400, 1]
```

produce una matriz de shape **(100, 100)** porque se seleccionan 100 filas, 100 columnas y un único canal.

En OpenCV el canal 1 corresponde al **verde** en el orden BGR.

## 2. ¿Por qué slicing es más eficiente?

El slicing usa operaciones vectorizadas implementadas internamente en NumPy y accede a bloques de memoria sin ejecutar instrucciones Python por cada píxel. Dos ciclos `for` realizan una gran cantidad de iteraciones individuales y agregan sobrecarga.

## 3. Gris de un amarillo puro BGR [0,255,255]

Usando pesos BGR `[0.114, 0.587, 0.299]`:

0×0.114 + 255×0.587 + 255×0.299 = **225.93 ≈ 226**.

Por lo tanto, el amarillo puro genera aproximadamente una intensidad gris de **226**.

## 4. Color dominante

El script calcula el promedio de cada canal y muestra automáticamente cuál es dominante. La respuesta depende de la imagen utilizada. Para una entrega con fotografía propia, ejecute `guia2.py` y copie el resultado obtenido.

---

# GUÍA 3 - Segmentación

## 1. Umbralización con T = 135

Regla: valores mayores a 135 se convierten en 255. Los demás en 0.

Matriz original:

```text
80  120 140
90  200 210
50  130 250
```

Resultado:

```text
0   0   255
0   255 255
0   0   255
```

## 2. Error al elegir T = 135 si se querían aislar valores mayores a 100

Los valores entre **101 y 135** quedan eliminados aunque pertenecían al objeto según el objetivo original. Visualmente el objeto perdería partes y podría aparecer fragmentado o incompleto.

## 3. Apertura vs Cierre

La **apertura** elimina principalmente pequeños puntos blancos aislados y ayuda a limpiar ruido de sal.

El **cierre** rellena pequeños huecos negros y conecta regiones cercanas.

La operación más efectiva depende del ruido presente en la imagen. El programa guarda los tres resultados para compararlos.

---

# GUÍA 4 - Convolución y Filtrado

## 1. Nuevo valor del píxel central

Suma de los valores:

10 + 20 + 30 + 15 + 250 + 15 + 20 + 10 + 20 = **390**.

Con filtro de media 3x3:

390 / 9 = **43.33**.

El nuevo valor aproximado es **43** si se almacena como entero.

## 2. ¿Por qué suaviza la imagen?

El valor extremo 250 se mezcla con sus vecinos de valores bajos. Por eso disminuye a aproximadamente 43. El filtro reduce diferencias bruscas, pero también puede suavizar bordes reales.

## 3. ¿Por qué la mediana funciona mejor con sal y pimienta?

La mediana ordena los valores y selecciona el valor central, por lo que los valores extremos aislados como 0 y 255 tienen poca influencia. El filtro de media incluye todos los valores en el promedio y puede crear manchas grises alrededor del ruido.

---

# GUÍA 5 - Gradientes y Detección de Bordes

## 1. Sobel X

Imagen:

```text
0   0   255
0   0   255
0   0   255
```

Kernel Sobel X:

```text
-1 0 1
-2 0 2
-1 0 1
```

Resultado:

255 + 510 + 255 = **1020**.

Por lo tanto, **Gx = 1020**. Es un gradiente fuerte que indica un borde vertical.

## 2. Sobel Y

Kernel Sobel Y:

```text
-1 -2 -1
 0  0  0
 1  2  1
```

Las contribuciones superior e inferior se compensan y el resultado es:

**Gy = 0**.

Esto indica que no hay cambio importante en la dirección vertical. El borde detectado es vertical.

## 3. Umbrales de Canny

El programa compara:

- 10 y 50: detecta más bordes, incluyendo detalles débiles y posible ruido.
- 100 y 200: resultado intermedio.
- 200 y 250: conserva principalmente cambios muy fuertes.

Los umbrales óptimos dependen de la imagen. El script permite comparar los tres resultados.

---

# GUÍA 6 - Extracción de Características y Contornos

## 1. Coordenadas extremas

Puntos:

A(2,4), B(8,2), C(10,7), D(3,9)

- Xmin = **2**
- Ymin = **2**
- Xmax = **10**
- Ymax = **9**

## 2. Ancho y alto del Bounding Box

Ancho:

10 - 2 = **8**

Alto:

9 - 2 = **7**

## 3. Pipeline integrador

El programa realiza:

1. Conversión a escala de grises.
2. Umbralización.
3. Limpieza morfológica.
4. Detección de contornos.
5. Cálculo del área.
6. Cálculo del perímetro.
7. Cálculo del centroide.
8. Bounding Box.
9. Clasificación por área.

La lógica empresarial utiliza un valor `X = 8000` píxeles:

- Área mayor a X: objeto grande y Bounding Box azul.
- Área menor o igual a X: objeto pequeño y Bounding Box rojo.

Este valor puede modificarse según los tamaños de la imagen utilizada.
