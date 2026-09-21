# Mini Taller de Inteligencia Artificial

Ejercicios prácticos de introducción al aprendizaje automático y las redes neuronales usando Python.

## Contenido

| Archivo | Tema | Descripción |
| --- | --- | --- |
| `taller 9.py` | K vecinos más cercanos (KNN) | Predice si un cliente realizará una compra usando edad, salario y número de hijos. Compara los resultados con `K=1` y `K=5`. |
| `taller 10.py` | Máquinas de vectores de soporte (SVM) | Clasifica puntos usando un modelo SVM con kernel RBF y muestra sus vectores de soporte. |
| `taller 11.py` | Perceptrón | Implementa desde cero una neurona con función escalón para resolver la compuerta lógica OR. |
| `taller 12.py` | Red neuronal multicapa | Calcula manualmente una capa oculta y una capa de salida usando la función de activación sigmoide. |

## Requisitos

- Python 3.9 o superior
- NumPy
- scikit-learn

## Instalación

Desde la carpeta del proyecto, instala las dependencias con:

```bash
pip install numpy scikit-learn
```

También puedes usar un entorno virtual:

```bash
python -m venv .venv
```

En Windows, actívalo con:

```bash
.venv\Scripts\activate
```

## Ejecución

Ejecuta cada taller por separado:

```bash
python "taller 9.py"
python "taller 10.py"
python "taller 11.py"
python "taller 12.py"
```

## Objetivos de aprendizaje

- Comprender cómo los algoritmos clasifican datos.
- Observar el efecto de cambiar el número de vecinos en KNN.
- Identificar los vectores de soporte en un modelo SVM.
- Entender el cálculo de una neurona: combinación lineal, sesgo y activación.
- Reconocer el flujo de datos entre capas de una red neuronal.

## Notas

- Los datos utilizados son pequeños y están definidos directamente dentro de cada script.
- Los modelos de KNN y SVM utilizan scikit-learn.
- El perceptrón y la red neuronal del último taller se implementan con operaciones de NumPy, sin entrenamiento automático.
