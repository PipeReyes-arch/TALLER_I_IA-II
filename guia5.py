import os
import cv2
import numpy as np


def ejercicio_analitico():
    I = np.array([[0,0,255],[0,0,255],[0,0,255]])
    gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    gy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    Gx = int(np.sum(I * gx))
    Gy = int(np.sum(I * gy))
    print("Gradiente Gx:", Gx)
    print("Gradiente Gy:", Gy)
    print("Magnitud:", (Gx**2 + Gy**2)**0.5)


def crear_demo():
    img = np.zeros((400,600), dtype=np.uint8)
    cv2.rectangle(img, (80,80), (250,300), 255, -1)
    cv2.circle(img, (420,200), 100, 180, -1)
    cv2.line(img, (0,350), (600,100), 255, 4)
    return img


def main():
    ejercicio_analitico()
    imagen = crear_demo()
    sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    canny_10_50 = cv2.Canny(imagen, 10, 50)
    canny_100_200 = cv2.Canny(imagen, 100, 200)
    canny_200_250 = cv2.Canny(imagen, 200, 250)
    os.makedirs("resultados", exist_ok=True)
    for nombre, img in [("sobel_x",sobel_x),("sobel_y",sobel_y),("canny_10_50",canny_10_50),("canny_100_200",canny_100_200),("canny_200_250",canny_200_250)]:
        cv2.imwrite(f"resultados/guia5_{nombre}.png", img)
        print(nombre, "pixeles de borde:", np.count_nonzero(img))
    print("Resultados guardados en resultados/")


if __name__ == "__main__":
    main()
