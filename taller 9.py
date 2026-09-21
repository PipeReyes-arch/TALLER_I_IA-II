import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 1. Dataset ampliado con 10 puntos y 3 características: [Edad, Salario (miles), Número de Hijos]
X_entrenamiento = np.array([
    [20, 30, 0],
    [40, 50, 2],
    [35, 45, 1],
    [25, 20, 0],
    [50, 80, 3],
    [22, 25, 0],
    [45, 60, 2],
    [38, 55, 1],
    [60, 90, 4],
    [28, 35, 0]
])

# Etiquetas: 0 = NO COMPRA, 1 = COMPRA
Y_entrenamiento = np.array([0, 1, 1, 0, 1, 0, 1, 1, 1, 0])

# Nuevo cliente a evaluar: [Edad, Salario, Hijos]
nuevo_cliente = np.array([[30, 40, 1]])

# Experimento A: K = 1
modelo_knn_1 = KNeighborsClassifier(n_neighbors=1)
modelo_knn_1.fit(X_entrenamiento, Y_entrenamiento)
print("Predicción con K=1:", modelo_knn_1.predict(nuevo_cliente)[0])

# Experimento B: K = 5
modelo_knn_5 = KNeighborsClassifier(n_neighbors=5)
modelo_knn_5.fit(X_entrenamiento, Y_entrenamiento)
print("Predicción con K=5:", modelo_knn_5.predict(nuevo_cliente)[0])