class Bebida:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio # Atributo privado
    def obtener_precio(self):
        return self.__precio

class Refresco(Bebida):
    def __init__(self, nombre, precio, sabor):
        super().__init__(nombre, precio)
        self.sabor = sabor

 # Creación de instancias de las clases "Bebida" y "Refresco"
agua = Bebida("Agua", 10.0)
cocacola = Refresco("Coca-Cola", 20.0, "cola")

 # Llamada a los métodos para obtener el precio de cada bebida
print("Valor agua: ", agua.obtener_precio())
print("Valor Coca Cola: ", cocacola.obtener_precio())