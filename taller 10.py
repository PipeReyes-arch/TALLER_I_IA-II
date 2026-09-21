import numpy as np
from sklearn.svm import SVC

# 1. Crear el dataset inicial con el punto adicional [5, 5] agregado a la Clase A (0)
X = np.array([
    [2, 2], 
    [3, 3], 
    [4, 2], 
    [6, 6], 
    [7, 8], 
    [8, 7],
    [5, 5]  # Punto añadido en el laboratorio
])

Y = np.array([0, 0, 0, 1, 1, 1, 0])

# 2. Inicializar SVM con Kernel RBF para manejar fronteras no lineales complejas
modelo_svm = SVC(kernel='rbf')

# 3. Entrenar el modelo
modelo_svm.fit(X, Y)

# 4. Extraer los Vectores de Soporte descubiertos por la IA
vectores = modelo_svm.support_vectors_
print("Los Vectores de Soporte con RBF son:\n", vectores)

# 5. Predicción para un nuevo punto
nuevo_punto = np.array([[5, 4]])
pred = modelo_svm.predict(nuevo_punto)
print("El punto [5,4] pertenece a la clase:", pred[0])