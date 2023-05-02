# Pedir al usuario su información
nombre = input("Ingrese su nombre: ")
direccion = input("Ingrese su dirección: ")
correo = input("Ingrese su correo electrónico: ")
telefono = input("Ingrese su número de teléfono: ")

# Pedir información sobre el gato
nombre_gato = input("Ingrese el nombre del gato que desea adoptar: ")
edad_gato = input("Ingrese la edad del gato: ")
raza_gato = input("Ingrese la raza del gato: ")
color_gato = input("Ingrese el color del gato: ")

# Preparar el espacio para el gato
print("Preparando el espacio para el gato...")
print("1. Comprar una caja de arena y arena para gatos.")
print("2. Comprar una cama y un rascador.")
print("3. Comprar comederos y bebederos para gatos.")
print("4. Limpiar el espacio donde el gato vivirá.")
print("5. Preparar juguetes para que el gato se entretenga.")

# Pedir una cita con el veterinario para el gato
print("Pidiendo cita con el veterinario para el gato...")
nombre_veterinario = input("Ingrese el nombre del veterinario: ")
fecha_cita = input("Ingrese la fecha y hora para la cita (formato: DD/MM/AAAA HH:MM): ")
print("Cita agendada con", nombre_veterinario, "para el", fecha_cita)

# Confirmar la adopción del gato
print("Estimado", nombre + ", ha solicitado la adopción del gato", nombre_gato + ".")
print("Nos pondremos en contacto con usted para informarle si su solicitud ha sido aprobada.")
print("Gracias por considerar adoptar una mascota.")