import numpy as np

# Función de Activación: Sigmoide (devuelve un valor entre 0 y 1)
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# 1. ENTRADA (X): 2 clientes con 3 características cada uno (Matriz de 2x3)
X = np.array([
    [0.5, 0.8, 0.2],
    [0.1, 0.9, 0.9]
])

# 2. CAPA OCULTA (4 Neuronas)
# Matriz W1 de (3 entradas x 4 neuronas)
W1 = np.array([
    [0.1,  0.2,  0.3,  0.4],
    [-0.5, 0.6,  0.7, -0.8],
    [0.9, -0.1,  0.2,  0.3]
])
b1 = np.array([0.1, 0.2, 0.3, 0.4])  # 4 Sesgos

# PROCESO CAPA OCULTA (Multiplicación matricial en lote)
Z1 = np.dot(X, W1) + b1
A1 = sigmoide(Z1)  # Salida de la capa oculta para ambos clientes

# 3. CAPA DE SALIDA (1 Neurona)
# Matriz W2 de (4 entradas ocultas x 1 neurona final)
W2 = np.array([0.5, 0.6, 0.7, 0.8])
b2 = np.array([-0.1])

# PROCESO CAPA FINAL
Z2 = np.dot(A1, W2) + b2
Salida_Final = sigmoide(Z2)

# Resultados impresos
print("Valores de Z1 (Capa Oculta):\n", Z1)
print("\nValores de A1 (Activación Sigmoide Oculta):\n", A1)
print("\nPredicción de la Red (Probabilidades para los 2 clientes):", np.round(Salida_Final, 4))