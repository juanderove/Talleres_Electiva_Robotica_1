"""3. Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual
deben consultar sobre el uso de funciones trigonométricas en Python. """

import math

# Coordenadas rectangulares 
x = 3
y = 4
z = 5

# CONVERSIÓN A CILÍNDRICAS

r = math.sqrt(x**2 + y**2)
theta = math.atan2(y, x)  # en radianes
theta_grados = math.degrees(theta)

# CONVERSIÓN A ESFÉRICAS

rho = math.sqrt(x**2 + y**2 + z**2)
phi = math.acos(z / rho)  # en radianes
phi_grados = math.degrees(phi)


# RESULTADOS

print("Coordenadas Rectangulares:")
print(f"(x, y, z) = ({x}, {y}, {z})")

print("\nCoordenadas Cilíndricas:")
print(f"(r, θ, z) = ({r:.3f}, {theta_grados:.3f}°, {z})")

print("\nCoordenadas Esféricas:")
print(f"(ρ, θ, φ) = ({rho:.3f}, {theta_grados:.3f}°, {phi_grados:.3f}°)")