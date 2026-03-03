"""6. Obtenga las coordenadas X y Y de los contornos de dos logos de automóviles (Chevrolet, Hyundai,
Mazda, etc.), a través de Python."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def obtener_contorno_logo_real(ruta_imagen, nombre_logo):
    # 1. Cargar imagen
    img = cv2.imread(ruta_imagen)
    if img is None:
        print(f"Error cargando la imagen para {nombre_logo}. Verifica la ruta.")
        return

    # Obtener dimensiones para el filtrado posterior
    alto_img, ancho_img = img.shape[:2]
    area_imagen = alto_img * ancho_img

    # 2. Pre-procesamiento: Escala de grises y desenfoque
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(gris, (5, 5), 0)

    # 3. Binarización Robusta (Fondo Blanco)
    _, binaria = cv2.threshold(suave, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 4. Encontrar contornos
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contornos:
        print(f"No se hallaron contornos en la imagen de {nombre_logo}.")
        return

    # 5. Filtrar el contorno del borde de la foto y tomar el más grande real
    contornos_reales = []
    for cnt in contornos:
        area_cnt = cv2.contourArea(cnt)
        if area_cnt > 0.95 * area_imagen:
            continue
        if area_cnt > 100: 
            contornos_reales.append(cnt)

    if not contornos_reales:
        print(f"No se encontraron contornos válidos para {nombre_logo}.")
        return

    # Tomar el contorno más grande de los que quedaron (el logo real)
    contorno_logo = max(contornos_reales, key=cv2.contourArea)
    
    # 6. Aproximación para suavizar
    epsilon = 0.0005 * cv2.arcLength(contorno_logo, True)
    contorno_final = cv2.approxPolyDP(contorno_logo, epsilon, True)

    # 7. Extraer coordenadas X e Y
    x_coords = contorno_final[:, 0, 0]
    y_coords = contorno_final[:, 0, 1]

    # --- CAMBIO CLAVE: CERRAR LA FIGURA ---
    # Creamos una copia de las coordenadas añadiendo el primer punto al final 
    # para que la línea de la gráfica complete el ciclo.
    x_cierre = np.append(x_coords, x_coords[0])
    y_cierre = np.append(y_coords, y_coords[0])

    # --- IMPRESIÓN EN TERMINAL ---
    print("-" * 30)
    print(f" RESULTADOS PARA LOGO: {nombre_logo.upper()}")
    print("-" * 30)
    print(f"Número total de puntos detectados: {len(x_coords)}")
    print("\n")
    
    for i in range(len(x_coords)):
        print(f"Punto {i+1:3}: X={x_coords[i]:4}, Y={y_coords[i]:4}")
    
    print("-" * 30 + "\n")

    # 8. Graficar con la trayectoria cerrada
    plt.figure(figsize=(8, 8))
    
    # Usamos x_cierre y y_cierre para la línea azul
    plt.plot(x_cierre, -y_cierre, 'b-', linewidth=2, label='Trayectoria del Logo (Cerrada)') 
    
    # Usamos las originales para los puntos rojos (no queremos duplicar el punto en el mapa de puntos)
    plt.scatter(x_coords, -y_coords, color='red', s=20, label='Puntos de Coordenadas Reales')
    
    plt.title(f"Puntos de Coordenadas - {nombre_logo}")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y (Invertida)")
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.grid(True)
    
    plt.show(block=False) 

# --- EJECUCIÓN ---
ruta_chevrolet = r"C:\Users\juand\OneDrive\Documentos\Repositorios\Talleres_Electiva_Robotica_1\Taller_1\Punto_C\chevrolet_2.png"
obtener_contorno_logo_real(ruta_chevrolet, "Chevrolet")

ruta_tesla = r"C:\Users\juand\OneDrive\Documentos\Repositorios\Talleres_Electiva_Robotica_1\Taller_1\Punto_C\Tesla.png"
obtener_contorno_logo_real(ruta_tesla, "Tesla")

print("Programa finalizado. Cierra las gráficas para salir.")
plt.show()