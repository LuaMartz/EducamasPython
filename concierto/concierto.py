# Precio de los boletos y cantidad disponible
precio = 50
cantidad_disponible = 100

# Datos del comprador
nombre_completo = input("Ingrese su nombre completo: ")
edad = input("Ingrese su edad: ")
email = input("Ingrese su dirección de correo electrónico: ")
telefono = input("Ingrese su número de teléfono: ")

# Compra en línea o en persona
compra_en_linea = input("¿Desea comprar los boletos en línea? (Sí/No): ")

if compra_en_linea == "Sí":
  
  # Opciones de pago en línea
  print("Opciones de pago:")
  print("1. Tarjeta de crédito")
  print("2. PayPal")
  opcion_pago = int(input("Seleccione una opción de pago (1 o 2): "))
  if opcion_pago == 1:

    # Pagar con tarjeta de crédito
    num_tarjeta = input("Ingrese el número de su tarjeta de crédito: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento de su tarjeta (MM/AA): ")
    cvv = input("Ingrese el CVV de su tarjeta: ")

    # Procesar pago
    print("¡Gracias por su compra,", nombre_completo + "! Su pago ha sido procesado exitosamente con tarjeta de crédito.")
  elif opcion_pago == 2:

    # Pagar con PayPal
    correo_paypal = input("Ingrese su dirección de correo electrónico de PayPal: ")
    
    # Procesar pago
    print("¡Gracias por su compra,", nombre_completo + "! Su pago ha sido procesado exitosamente con PayPal.")
  else:
    print("Opción de pago inválida.")
else:
  
  # Comprar en persona
  # Opciones de pago en efectivo o tarjeta
  print("Opciones de pago:")
  print("1. Efectivo")
  print("2. Tarjeta de crédito")
  opcion_pago = int(input("Seleccione una opción de pago (1 o 2): "))
  if opcion_pago == 1:

    # Pagar con efectivo
    monto_pago = float(input("Ingrese el monto de su pago en efectivo: "))
    if monto_pago < precio:
      print("El monto ingresado es insuficiente.")
    else:
      cambio = monto_pago - precio

      # Procesar pago
      print("¡Gracias por su compra,", nombre_completo + "! Su pago ha sido procesado exitosamente con efectivo.")
      print("Su cambio es de $", cambio)
  elif opcion_pago == 2:

    # Pagar con tarjeta de crédito
    num_tarjeta = input("Ingrese el número de su tarjeta de crédito: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento de su tarjeta (MM/AA): ")
    cvv = input("Ingrese el CVV de su tarjeta: ")
    
    # Procesar pago
    print("¡Gracias por su compra,", nombre_completo + "! Su pago ha sido procesado exitosamente con tarjeta de crédito.")
  else:
    print("Opción de pago inválida.")
    
# Actualizar la cantidad de boletos disponibles
cantidad_disponible -= 1
print("Quedan", cantidad_disponible, "boletos disponibles para el concierto.")