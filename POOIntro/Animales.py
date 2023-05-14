class Animales:
    def __init__(self, nombre, especie, habitat):
        self.nombre = nombre
        self.__especie = especie   # atributo encapsulado
        self.__habitat = habitat   # atributo encapsulado

    def obtener_especie(self):
        return self.__especie

    def obtener_habitat(self):
        return self.__habitat
    
class Mamiferos(Animales):
    def __init__(self, nombre, especie, habitat, alimentacion):
        super().__init__(nombre, especie, habitat)
        self.__alimentacion = alimentacion    # atributo encapsulado
    def obtener_alimentacion(self):
        return self.__alimentacion
    
class Aves(Animales):
    def __init__(self, nombre, especie, habitat, altura_maxima):
        super().__init__(nombre, especie, habitat)
        self.altura_maxima = altura_maxima    # atributo público
        self.__color_plumaje = "no definido"  # atributo encapsulado
    def obtener_color_plumaje(self):
        return self.__color_plumaje
    
class Reptiles(Animales):
    def __init__(self, nombre, especie, habitat, temperatura_corporal):
        super().__init__(nombre, especie, habitat)
        self.__temperatura_corporal = temperatura_corporal    # atributo encapsulado
        self.__venenoso = False   # atributo encapsulado
    def es_venenoso(self):
        return self.__venenoso
    
class Peces(Animales):
    def __init__(self, nombre, especie, habitat, temperatura_agua):
        super().__init__(nombre, especie, habitat)
        self.__temperatura_agua = temperatura_agua    # atributo encapsulado
        self.color = "no definido"   # atributo público
    def obtener_temperatura_agua(self):
        return self.__temperatura_agua
    
class Insectos(Animales):
    def __init__(self, nombre, especie, habitat, tipo):
        super().__init__(nombre, especie, habitat)
        self.tipo = tipo    # atributo público
        self.__num_patas = 6   # atributo encapsulado
    def obtener_num_patas(self):
        return self.__num_patas
    
 # Creación de instancias
mamifero1 = Mamiferos("León", "Panthera leo", "Savannah", "Carnívoro")
mamifero2 = Mamiferos("Perro", "Canis lupus familiaris", "Doméstico", "Omnívoro")
ave1 = Aves("Águila", "Aquila chrysaetos", "Montañas", 3000)
ave2 = Aves("Loro", "Psittacidae", "Bosques Tropicales", 1000)
reptil1 = Reptiles("Serpiente", "Viperidae", "Desiertos", "Variable")
reptil2 = Reptiles("Tortuga", "Testudines", "Aquático", "Variable")
pez1 = Peces("Tiburón", "Carcharodon carcharias", "Océanos", "Variable")
pez2 = Peces("Trucha", "Salmo trutta", "Ríos", "Variable")
insecto1 = Insectos("Abeja", "Apis mellifera", "Colmenas", "Polinizador")
insecto2 = Insectos("Hormiga", "Formicidae", "Hormigueros", "Sociales")
 
 # Llamada a los métodos
print("La alimentación del mamífero 1 es:", mamifero1.obtener_alimentacion())
print("El color de plumaje del ave 2 es:", ave2.obtener_color_plumaje())
print("El número de patas del insecto 1 es:", insecto1.obtener_num_patas())
print("La temperatura del agua del pez 2 es:", pez2.obtener_temperatura_agua())