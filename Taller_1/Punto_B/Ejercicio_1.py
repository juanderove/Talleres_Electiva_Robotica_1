"""1. Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el
valor de corriente y voltaje."""

print("Calculo de la Potencia Electrica: \n")
corriente = float(input("Ingese el valor de corriente: "))
voltaje = float(input("Ingese el valor de voltaje: "))

# -> Calculo de Potencia:
potencia = corriente * voltaje

print(f"La Potencia es: {potencia} w")