"""2. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
matrices previamente inicializadas."""

# Inicializacion de matrices:
m1 = [[25,45,29], 
      [30,75,72],
      [22,36,45]]

m2 = [[5,9,2], 
      [13,14,15],
      [16,17,18]]

print(f"Matriz No. 1: {m1}")
print(f"Matriz No. 2: {m2}")

# Identificacion de la matriz para recorrerla:
filas = len(m1)
columnas = len(m1[0])

# Variables de registro de datos:
suma = []
resta = []
division = []

# -> Operaciones Basicas:
for i in range(filas):
    fila_suma = []
    fila_resta = []
    fila_division = []
    for j in range(columnas):
        # -> Suma:
        fila_suma.append(m1[i][j] + m2[i][j])
        
        # -> Resta:
        fila_resta.append(m1[i][j] - m2[i][j]) 
        
        # -> División:
        if m2[i][j] != 0:
            # -> División:
            operacion = m1[i][j] / m2[i][j]
            # Redondeo:
            valor_final = round(operacion, 2)
        else:
            valor_final = "Error"
            
        fila_division.append(valor_final)

# -> Resultados:       
    suma.append(fila_suma)
    resta.append(fila_resta) 
    division.append(fila_division)
        
# -> Producto Punto:
prod_punto = []

for i in range(filas):
    fila_punto = []
    for j in range(columnas):
        suma_temporal = 0
        for k in range(columnas):
            suma_temporal += m1[i][k] * m2[k][j]
        fila_punto.append(suma_temporal)
    prod_punto.append(fila_punto)
    
# -> Producto Cruz:
prod_cruz = []
for i in range(filas):
    ax, ay, az = m1[i][0], m1[i][1], m1[i][2]
    bx, by, bz = m2[i][0], m2[i][1], m2[i][2] 
    
    # Fórmula del producto cruz
    cx = (ay * bz) - (az * by)
    cy = (az * bx) - (ax * bz)
    cz = (ax * by) - (ay * bx)
    
    prod_cruz.append([cx, cy, cz])    
            
print("\nSuma: ",suma)
print("Resta: ",resta)
print("División: ",division)
print("Producto Punto: ",prod_punto)
print("Producto Cruz: ",prod_cruz)
