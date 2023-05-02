# Datos de la reserva
restaurante = "Restaurante 5 Estrellas"
ciudad = "Bogotá"
num_personas = 2
hora_reserva = "8pm"

# Solicitar información del usuario
nombre = input("Ingrese su nombre: ")
telefono = input("Ingrese su número de teléfono: ")
email = input("Ingrese su dirección de correo electrónico: ")

# Confirmación de reserva
print("")
print("\n¡Gracias,", nombre + "! Estamos procesando su reserva en", 
      restaurante, "en", ciudad, "para", num_personas, "personas a las",
        hora_reserva, ".\nLe contactaremos al", telefono,
          "o al correo electrónico", email, 
          ", para confirmar su reserva. ¡Que tenga un buen día!")
print("")