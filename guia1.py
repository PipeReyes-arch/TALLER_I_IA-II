import numpy as np

# GUIA 1: Refuerzo Python y Algebra Lineal

def ejercicio_1():
    A = np.array([
        [0, 255, 255, 255, 0],
        [255, 0, 0, 0, 255],
        [255, 0, 128, 0, 255],
        [255, 0, 0, 0, 255],
        [0, 255, 255, 255, 0]
    ])
    print("Matriz A:\n", A)
    print("A[2, 3] =", A[2, 3])
    print("Valores RGB 1080x1920x3 =", 1080 * 1920 * 3, "bytes")


def ejercicio_2():
    np.random.seed(10)
    original = np.random.randint(200, 255, (5, 5))
    procesada = original * 0.5 - 50
    procesada = np.clip(procesada, 0, 255).astype(np.uint8)
    print("\nOriginal:\n", original)
    print("\nContraste -50% y brillo -50:\n", procesada)


def ejercicio_3():
    identidad = np.eye(4, dtype=int)
    print("\nIdentidad 4x4 transpuesta:\n", identidad.T)
    print("Neurona de entrada para RGB (200,200,3):", 200 * 200 * 3)


def ejercicio_4():
    I = np.array([
        [100, 100, 100],
        [100, 200, 100],
        [100, 100, 100]
    ])
    K = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    resultado = np.sum(I * K)
    print("\nProducto Hadamard:\n", I * K)
    print("Valor central calculado:", resultado)


if __name__ == "__main__":
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
