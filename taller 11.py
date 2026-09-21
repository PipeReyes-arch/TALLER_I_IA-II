import numpy as np

# 1. Definir la Función de Activación (Escalón)
def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0

# 2. Definir la Estructura de la Neurona
def perceptron(X, W, b):
    # Producto punto (Combinación lineal)
    Z = np.dot(X, W) + b
    # Activación
    salida = funcion_escalon(Z)
    return salida

# 3. Datos del problema (Compuerta Lógica OR)
# Pesos modificados y sesgo ajustado para resolver la compuerta OR
pesos = np.array([1.0, 1.0])  # Vector W
sesgo = -0.5                   # Constante b

# Probando las 4 combinaciones posibles de la compuerta OR:
combinaciones = [
    np.array([0, 0]),
    np.array([1, 0]),
    np.array([0, 1]),
    np.array([1, 1])
]

print("Resultados de la Compuerta OR con el Perceptrón:")
for entradas in combinaciones:
    resultado = perceptron(entradas, pesos, sesgo)
    print(f"Entradas: {entradas} -> El Perceptrón disparó el valor: {resultado}")