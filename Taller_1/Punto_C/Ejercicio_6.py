"""6. Obtenga las coordenadas X y Y de los contornos de dos logos de automóviles (Chevrolet, Hyundai,
Mazda, etc.), a través de Python."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def obtener_contorno(ruta_imagen, nombre_logo):
    
    # Lee imagen
    img = cv2.imread(ruta_imagen) #Carga la imagen en matriz
    
    if img is None:
        print(f"No se pudo cargar la imagen {nombre_logo}")
        return
    
    # Convierte a escala de grises
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplica detección de bordes (binaria,blanco y negro)
    bordes = cv2.Canny(gris, 80, 180)
    
    # Encuentra contornos,aqui extraemos el contorno
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if len(contornos) == 0:
        print(f"No se encontraron contornos en {nombre_logo}")
        return
    
    # Toma el contorno más grande
    contorno_principal = max(contornos, key=cv2.contourArea)
    
    # Extrae coordenadas X y Y
    x = contorno_principal[:, 0, 0]
    y = contorno_principal[:, 0, 1]
    
    # Mostrar primeras coordenadas
    print(f"\nCoordenadas del logo {nombre_logo}:")
    print("Primeros valores de X:", x[:20])
    print("Primeros valores de Y:", y[:20])
    
    # Graficar contorno
    plt.figure()
    plt.plot(x, -y)  # Se invierte Y para corregir orientación
    plt.title(f"Contorno - {nombre_logo}")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

# -----------------------------
# RUTAS COMPLETAS

obtener_contorno(
r"C:\Users\juand\OneDrive\Documentos\Repositorios\Talleres_Electiva_Robotica_1\Taller_1\Punto_C\Tesla.png",
"Tesla"
)

obtener_contorno(
r"C:\Users\juand\OneDrive\Documentos\Repositorios\Talleres_Electiva_Robotica_1\Taller_1\Punto_C\chevrolet_2.png",
"Chevrolet"
)