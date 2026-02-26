"""3. Implemente la ecuación de carga y descarga para un circuito RC. El usuario ingresa por teclado el
valor de voltaje (V), capacitancia (𝜇𝐹) y resistencia (Ω). Posteriormente realice en Python la
gráfica."""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Entrada de datos
V = float(input("Ingresar el voltaje (V): "))
R = float(input("Ingresar la resistencia (Ohmios): "))
C_micro = float(input("Ingrese la capacitancia (microFaradios): "))

# Convertir microFaradios a Faradios
C = C_micro * 1e-6

# Constante de tiempo
tau = R * C

# Vector de tiempo (0 a 5 constantes de tiempo)
t = np.linspace(0, 5*tau, 1000)


# Ecuaciones
Vc_carga = V * (1 - np.exp(-t/tau))
Vc_descarga = V * np.exp(-t/tau)


# Gráfica
plt.plot(t, Vc_carga, label="Carga")
plt.plot(t, Vc_descarga, label="Descarga")

plt.title("Carga y Descarga en Circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje en el capacitor (V)")
plt.legend()
plt.grid()

plt.show()

# Mostrar constante de tiempo
print("\nConstante de tiempo (tau) =", round(tau,6), "segundos")