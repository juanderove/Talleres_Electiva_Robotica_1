"""5. Escribir un programa que realice la pregunta ¿Desea continuar Si/No? y que no deje de hacerla
hasta que el usuario teclee No."""

respuesta = ""

while respuesta != "No":
    respuesta = input("¿Desea continuar? Si/No: ")

print("Programa finalizado.")