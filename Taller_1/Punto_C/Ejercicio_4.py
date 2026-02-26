"""4. Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un vector con coordenadas
ingresadas por el usuario."""

import matplotlib.pyplot as plt # Libreria para graficar 
from mpl_toolkits.mplot3d import Axes3D 

dimensiones = 3
coordenadas = []
nombres = ["X", "Y", "Z"]

# Ingreso de coordenadas:
for i in range(dimensiones):
    x_y_z = float(input(f"Ingrese la coordenada {nombres[i]} del vector a graficar: "))
    coordenadas.append(x_y_z)

print(f"Las coordenadas del vector son: {coordenadas}")

x, y, z = coordenadas

# Configuración de la grafica en 3D:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujamos el vector desde el origen (0,0,0) hasta el punto ingresado
# ax.quiver(origen_x, origen_y, origen_z, x, y, z)
ax.quiver(0, 0, 0, x, y, z, color='blue')

# Configuramos los nombres de los ejes:
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Ajustamos los límites de la vista:
max_val = max(abs(x), abs(y), abs(z), 5)
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

print(f"\nGraficando vector: {coordenadas}")
plt.show()