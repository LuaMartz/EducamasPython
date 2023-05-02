 # Preguntar si desea café
opcionC = input("¿Desea café? (S/N): ")

 # Establecer la variable café
if opcionC.upper() == "S":
    caffe = True

        # Preparando café
    print("Preparando café...")
    print("")

    # Llenando la cafetera con agua
    print("Llenando la cafetera con agua...")
    print("")

    # Encendiendo la cafetera
    print("Encendiendo la cafetera...")
    print("")

    # Agregando el café molido a la canasta de la cafetera
    print("Agregando el café molido a la canasta de la cafetera...")
    print("")

    # Esperando mientras el agua se filtra a través del café
    print("Esperando mientras el agua se filtra a través del café...")
    print("")

    # Colocando el café en una taza
    print("Colocando el café en una taza...")
    print("")

    # Preguntar si desea su café con azúcar
    opcion = input("¿Desea su café con azúcar? (S/N): ")

    # Establecer la variable azucar
    if opcion.upper() == "S":
        azucar = True
    else:
        azucar = False

    # Establecer la variable cafe
    cafe = "Café"
    if azucar:
        cafe += " con azúcar"

        # Agregando el café molido a la canasta de la cafetera
        print("")
        print("Agregando azúcar al café...")
        print("")


    else:
        cafe += " sin azúcar"

    # Imprimir el resultado
    print("")
    print(f"Su {cafe} está listo. ¡Disfrútelo!")
    print("")

else:
    caffe = False
     # Fin resultado
    print("")
    print("Te esperamos en otra ocasion")
    print("")