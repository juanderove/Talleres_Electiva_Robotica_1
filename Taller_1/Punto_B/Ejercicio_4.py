"""4. Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico,
donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee."""

while True:
    print("Escoja la opción con el robot que desea obtener la información:\n")
    print("1 Robot Cilindrico")
    print("2 Robot Cartesiano")
    print("3 Robot Esferico")
    
    opcion = int(input("Seleccione la opcion: "))
    if(opcion == 1):
        print("Robot Cilindrico")
        print("Tipo de articulaciones: Prismáticas (P)")
        print("Configuración: PPP")
        print("Número de articulaciones: 3")
        print("Movimiento en ejes: X, Y, Z")
        break
        
    elif(opcion == 2):
        print("Robot Cartesiano")
        print("Configuración: RPP")
        print("1 articulación rotacional (R)")
        print("2 articulaciones prismáticas (P)")
        print("Total: 3 articulaciones")
        break
        
    elif(opcion == 3):
        print("Robot Esferico")
        print("Configuración: RRP")
        print("2 articulaciones rotacionales (R)")
        print("1 articulación prismática (P)")
        print("Total: 3 articulaciones")
        break
        
    else:
        print("Opción Invalida, intente nuevamente!")