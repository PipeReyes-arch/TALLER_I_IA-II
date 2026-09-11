import os
import cv2
import numpy as np


def ejercicio_analitico():
    matriz = np.array([[80,120,140],[90,200,210],[50,130,250]])
    resultado = np.where(matriz > 135, 255, 0).astype(np.uint8)
    print("Matriz original:\n", matriz)
    print("Umbral T=135:\n", resultado)


def crear_demo():
    imagen = np.full((400, 600), 100, dtype=np.uint8)
    cv2.rectangle(imagen, (150,100), (450,300), 190, -1)
    imagen[40,40] = 255
    imagen[60,80] = 255
    imagen[200,300] = 0
    return imagen


def main():
    ejercicio_analitico()
    imagen = crear_demo()
    _, binaria = cv2.threshold(imagen, 135, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3), np.uint8)
    apertura = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)
    cierre = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, kernel)
    os.makedirs("resultados", exist_ok=True)
    cv2.imwrite("resultados/guia3_original_binarizada.png", binaria)
    cv2.imwrite("resultados/guia3_apertura.png", apertura)
    cv2.imwrite("resultados/guia3_cierre.png", cierre)
    print("Pixeles blancos original:", np.count_nonzero(binaria))
    print("Pixeles blancos apertura:", np.count_nonzero(apertura))
    print("Pixeles blancos cierre:", np.count_nonzero(cierre))
    print("Resultados guardados en resultados/")


if __name__ == "__main__":
    main()
