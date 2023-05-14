class Materiales:
    def __init__(self, nombre, precio, peso):
        self.nombre = nombre
        self.__precio = precio   # atributo encapsulado
        self.__peso = peso       # atributo encapsulado
    def obtener_precio(self):
        return self.__precio
    def obtener_peso(self):
        return self.__peso
    
class Metal(Materiales):
    def __init__(self, nombre, precio, peso, tipo):
        super().__init__(nombre, precio, peso)
        self.__tipo = tipo      # atributo encapsulado
    def obtener_tipo(self):
        return self.__tipo
    
class Plastico(Materiales):
    def __init__(self, nombre, precio, peso, color):
        super().__init__(nombre, precio, peso)
        self.__color = color   # atributo encapsulado
    def obtener_color(self):
        return self.__color
    
class Vidrio(Materiales):
    def __init__(self, nombre, precio, peso, resistencia):
        super().__init__(nombre, precio, peso)
        self.__resistencia = resistencia    # atributo encapsulado
    def obtener_resistencia(self):
        return self.__resistencia
    
class Papel(Materiales):
    def __init__(self, nombre, precio, peso, tamaño):
        super().__init__(nombre, precio, peso)
        self.__tamaño = tamaño   # atributo encapsulado
    def obtener_tamaño(self):
        return self.__tamaño

# Creación de instancias
metal1 = Metal("Hierro", 200, 20, "Férreo")
metal2 = Metal("Aluminio", 150, 10, "Ligero")

plastico1 = Plastico("Polietileno", 50, 5, "Transparente")
plastico2 = Plastico("PVC", 100, 8, "Blanco")

vidrio1 = Vidrio("Cristal", 500, 15, "Alta")
vidrio2 = Vidrio("Vidrio Templado", 800, 12, "Muy Alta")

papel1 = Papel("Papel de Carta", 10, 2, "A4")
papel2 = Papel("Papel de Periódico", 5, 1, "Tabloide")

# Llamada a los métodos
print("El precio del metal 1 es: ",metal1.obtener_precio())
print("El peso del vidrio 2 es: ",vidrio2.obtener_peso())
print("El color del plástico 1 es: ",plastico1.obtener_color())
print("El tamaño del papel 2 es: ",papel2.obtener_tamaño())