import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

CARPETA = "imagenes"
RUTA = os.path.join(CARPETA, "guia2.jpg")


def crear_imagen_demo(ruta):
    imagen = np.zeros((400, 600, 3), dtype=np.uint8)
    imagen[:] = (80, 140, 220)
    cv2.circle(imagen, (180, 200), 100, (255, 80, 30), -1)
    cv2.rectangle(imagen, (350, 100), (550, 300), (30, 220, 80), -1)
    cv2.imwrite(ruta, imagen)
    return imagen


def cargar_imagen():
    os.makedirs(CARPETA, exist_ok=True)
    imagen = cv2.imread(RUTA)
    if imagen is None:
        imagen = crear_imagen_demo(RUTA)
    return imagen


def main():
    # Pregunta teorica: recorte [100:200,300:400,1] -> (100,100)
    # Pregunta matematica: amarillo BGR [0,255,255] -> 226.0
    pixel = np.array([0, 255, 255], dtype=float)
    gris_pixel = np.dot(pixel, [0.114, 0.587, 0.299])
    print("Gris del amarillo puro:", gris_pixel)

    imagen = cargar_imagen()
    azul, verde, rojo = cv2.split(imagen)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    print("Shape imagen:", imagen.shape)
    print("Shape canal azul:", azul.shape)
    print("Promedios BGR:", round(float(azul.mean()),2), round(float(verde.mean()),2), round(float(rojo.mean()),2))

    nombres = ["Azul", "Verde", "Rojo"]
    canales = [azul, verde, rojo]
    dominante = nombres[int(np.argmax([c.mean() for c in canales]))]
    print("Canal dominante promedio:", dominante)

    os.makedirs("resultados", exist_ok=True)
    plt.figure(figsize=(8,4))
    for canal, color, nombre in zip(canales, ["b", "g", "r"], nombres):
        hist = cv2.calcHist([canal], [0], None, [256], [0,256])
        plt.plot(hist, color=color, label=nombre)
    plt.title("Histogramas BGR")
    plt.xlabel("Intensidad")
    plt.ylabel("Pixeles")
    plt.legend()
    plt.tight_layout()
    plt.savefig("resultados/guia2_histogramas.png")
    plt.close()

    cv2.imwrite("resultados/guia2_gris.png", gris)
    cv2.imwrite("resultados/guia2_azul.png", azul)
    cv2.imwrite("resultados/guia2_verde.png", verde)
    cv2.imwrite("resultados/guia2_rojo.png", rojo)
    print("Resultados guardados en resultados/")


if __name__ == "__main__":
    main()
