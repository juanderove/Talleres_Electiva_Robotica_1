"""4. Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de
la temperatura."""

# Cálculo de resistencia de una RTD PT100
# ecuación IEC 60751

# Constantes del sensor PT100
R0 = 100  # Ohmios a 0°C
A = 3.9083e-3
B = -5.775e-7


# Temperatura previamente definida (°C)
T = 75  #Grados que inluyo


# Cálculo de la resistencia
R = R0 * (1 + A*T + B*(T**2))


# Resultado
print("Temperatura:", T, "°C")
print("Resistencia de la PT100:", round(R, 4), "Ohmios")