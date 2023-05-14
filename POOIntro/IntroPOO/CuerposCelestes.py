class CuerposCelestes:
    def __init__(self, nombre, masa, diametro, distancia):
        self.nombre = nombre
        self.__masa = masa   # atributo encapsulado
        self.__diametro = diametro   # atributo encapsulado
        self.__distancia = distancia  # atributo encapsulado

    def obtener_masa(self):
        return self.__masa

    def obtener_diametro(self):
        return self.__diametro

    def obtener_distancia(self):
        return self.__distancia

class Planetas(CuerposCelestes):
    def __init__(self, nombre, masa, diametro, distancia, gravedad):
        super().__init__(nombre, masa, diametro, distancia)
        self.__gravedad = gravedad   # atributo encapsulado
        self.__temperatura = "no definido"  # atributo encapsulado

    def obtener_gravedad(self):
        return self.__gravedad

    def obtener_temperatura(self):
        return self.__temperatura

class Estrellas(CuerposCelestes):
    def __init__(self, nombre, masa, diametro, distancia, temperatura):
        super().__init__(nombre, masa, diametro, distancia)
        self.__temperatura = temperatura  # atributo encapsulado
        self.__edad = "no definido"  # atributo encapsulado

    def obtener_temperatura(self):
        return self.__temperatura

    def obtener_edad(self):
        return self.__edad

class Cometas(CuerposCelestes):
    def __init__(self, nombre, masa, diametro, distancia, orbita):
        super().__init__(nombre, masa, diametro, distancia)
        self.__orbita = orbita  # atributo encapsulado
        self.__periodo = "no definido"  # atributo encapsulado

    def obtener_orbita(self):
        return self.__orbita

    def obtener_periodo(self):
        return self.__periodo

class Asteroides(CuerposCelestes):
    def __init__(self, nombre, masa, diametro, distancia, material):
        super().__init__(nombre, masa, diametro, distancia)
        self.__material = material  # atributo encapsulado
        self.__composicion = "no definido"  # atributo encapsulado

    def obtener_material(self):
        return self.__material

    def obtener_composicion(self):
        return self.__composicion

class Satelites(CuerposCelestes):
    def __init__(self, nombre, masa, diametro, distancia, planeta):
        super().__init__(nombre, masa, diametro, distancia)
        self.planeta = planeta  # atributo público
        self.__orbita = "no definido"  # atributo encapsulado

    def obtener_orbita(self):
        return self.__orbita

# Creación de instancias
planeta1 = Planetas("Tierra", 5.97, 12742, 149.6, 9.8)
planeta2 = Planetas("Marte", 0.642, 6794, 227.9, 3.7)
planeta3 = Planetas("Júpiter", 1898, 139822, 778.5, 24.8)
estrella1 = Estrellas("Sol", 1.989e30, 1391000, 0, 5778)
estrella2 = Estrellas("Betelgeuse", 15, 1180, 643, 3600)
estrella3 = Estrellas("Sirio A", 2.063, 1675000, 8.6, 9940)
cometa1 = Cometas("Halley", 2.2e14, 11, 35.1, "elíptica")
cometa2 = Cometas("Kohoutek", 2.4e14, 10, 75.3, "hiperbólica")
cometa3 = Cometas("Hale-Bopp", 2.2e15, 60, 3159.6, "parabólica")
asteroide1 = Asteroides("Ceres", 9.4e20, 940, 414, "rocoso")
asteroide2 = Asteroides("Vesta", 2.7e20, 525, 353, "metálico")
asteroide3 = Asteroides("Eros", 6.7e15, 34.4, 218, "rocoso")
satelite1 = Satelites("Luna", 7.342e22, 3474, 384, "Tierra")
satelite2 = Satelites("Fobos", 1.08e16, 22.5, 9380, "Marte")
satelite3 = Satelites("Io", 8.93e22, 3643, 421700, "Júpiter")

# Llamada a los métodos
print("La masa del planeta 1 es:", planeta1.obtener_masa())
print("La temperatura del Planeta 2 es:", planeta2.obtener_temperatura())
print("La distancia de la Estrella 3 es:", estrella3.obtener_distancia())
print("La órbita del satélite 1 es:", satelite1.obtener_orbita())