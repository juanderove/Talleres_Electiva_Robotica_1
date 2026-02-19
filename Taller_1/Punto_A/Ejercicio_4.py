import math

# Constantes PT100 según IEC 60751
R0 = 100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Temperatura
T = 75   # Cambia aquí el valor

# Cálculo según rango
if T >= 0:
    R = R0 * (1 + A*T + B*(T**2))
else:
    R = R0 * (1 + A*T + B*(T**2) + C*(T-100)*(T**3))

print("Temperatura:", T, "°C")
print("Resistencia PT100:", round(R,4), "Ohmios")