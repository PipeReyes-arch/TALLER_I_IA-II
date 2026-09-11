import os
import cv2
import numpy as np


def ejercicio_analitico():
    I = np.array([[10,20,30],[15,250,15],[20,10,20]])
    nuevo = np.sum(I) / 9
    print("Suma:", np.sum(I))
    print("Nuevo valor central con filtro de media:", nuevo)


def crear_ruido_sal_pimienta():
    imagen = np.full((400,600), 128, dtype=np.uint8)
    cv2.rectangle(imagen, (100,100), (500,300), 200, -1)
    rng = np.random.default_rng(10)
    ruido = rng.random(imagen.shape)
    imagen[ruido < 0.03] = 0
    imagen[ruido > 0.97] = 255
    return imagen


def main():
    ejercicio_analitico()
    imagen = crear_ruido_sal_pimienta()
    media = cv2.blur(imagen, (7,7))
    gaussiano = cv2.GaussianBlur(imagen, (7,7), 0)
    mediana = cv2.medianBlur(imagen, 7)
    os.makedirs("resultados", exist_ok=True)
    cv2.imwrite("resultados/guia4_ruido.png", imagen)
    cv2.imwrite("resultados/guia4_media.png", media)
    cv2.imwrite("resultados/guia4_gaussiano.png", gaussiano)
    cv2.imwrite("resultados/guia4_mediana.png", mediana)
    print("Aplicados: Media, Gaussiano y Mediana con kernel 7x7")
    print("Resultados guardados en resultados/")


if __name__ == "__main__":
    main()
