import os
import cv2
import numpy as np


def ejercicio_analitico():
    puntos = [(2,4),(8,2),(10,7),(3,9)]
    xs = [p[0] for p in puntos]
    ys = [p[1] for p in puntos]
    xmin, ymin, xmax, ymax = min(xs), min(ys), max(xs), max(ys)
    print("Xmin, Ymin, Xmax, Ymax:", xmin, ymin, xmax, ymax)
    print("Ancho:", xmax-xmin, "Alto:", ymax-ymin)


def crear_demo():
    img = np.full((400,600), 255, dtype=np.uint8)
    cv2.circle(img, (120,200), 35, 0, -1)
    cv2.circle(img, (300,200), 70, 0, -1)
    cv2.rectangle(img, (430,120), (550,300), 0, -1)
    return img


def main():
    ejercicio_analitico()
    gris = crear_demo()
    _, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((3,3), np.uint8)
    limpia = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)
    contornos, _ = cv2.findContours(limpia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    salida = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)
    X = 8000
    for i, cnt in enumerate(contornos, 1):
        area = cv2.contourArea(cnt)
        perimetro = cv2.arcLength(cnt, True)
        x,y,w,h = cv2.boundingRect(cnt)
        momentos = cv2.moments(cnt)
        cx = int(momentos['m10']/momentos['m00']) if momentos['m00'] else 0
        cy = int(momentos['m01']/momentos['m00']) if momentos['m00'] else 0
        grande = area > X
        color = (255,0,0) if grande else (0,0,255)  # BGR: azul grande, rojo pequeno
        cv2.rectangle(salida, (x,y), (x+w,y+h), color, 2)
        print(f"Objeto {i}: area={area:.2f}, perimetro={perimetro:.2f}, centro=({cx},{cy}), tipo={'grande' if grande else 'pequeno'}")
    os.makedirs("resultados", exist_ok=True)
    cv2.imwrite("resultados/guia6_binaria.png", binaria)
    cv2.imwrite("resultados/guia6_contornos.png", salida)
    print("Resultados guardados en resultados/")


if __name__ == "__main__":
    main()
