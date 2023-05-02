# Crear un diccionario con los ingredientes y sus cantidades
receta = {
  "harina": 2.5,
  "azúcar": 1,
  "huevo": 3,
  "leche": 1,
  "mantequilla": 0.5,
  "polvo para hornear": 1,
  "sal": 0.5,
  "chocolate": 0.5
}

# Definir una función para calcular la cantidad necesaria de cada ingrediente en base al número de porciones
def calcular_cantidad_porcion(ingrediente, cantidad, porciones):
    cantidad_porcion = cantidad / 4  # Cantidad necesaria por cada cuatro porciones
    cantidad_total = cantidad_porcion * porciones  # Cantidad necesaria para el número de porciones deseado
    return cantidad_total

# Solicitar al usuario el número de porciones y calcular la cantidad de cada ingrediente necesario
porciones = int(input("¿Para cuántas porciones desea hacer la receta? "))
print("Para", porciones, "porciones de la receta se necesitan los siguientes ingredientes:")

for ingrediente, cantidad in receta.items():
    cantidad_necesaria = calcular_cantidad_porcion(ingrediente, cantidad, porciones)
    print(ingrediente + ":", str(cantidad_necesaria) + " unidades")

# Solicitar al usuario la tienda donde realizará la compra
tienda = input("¿En qué tienda realizará la compra? ")

# Simular la compra en línea o en persona
compra_en_linea = input("¿Desea realizar la compra en línea en " + tienda + "? (Sí/No) ")
if compra_en_linea.upper() == "SÍ":
    # Simular compra en línea
    print("Comprando en línea en", tienda, "...")
    print("Compra exitosa.")
else:
    # Simular compra en persona
    print("Dirigirse a", tienda, "para realizar la compra.")