class Texto:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.__autor = autor # Atributo privado
    def obtener_autor(self):
        return self.__autor
    
class Libro(Texto):
    def __init__(self, titulo, autor, num_paginas, año_publicacion):
        super().__init__(titulo, autor)
        self.__num_paginas = num_paginas # Atributo privado
        self.año_publicacion = año_publicacion
    def obtener_num_paginas(self):
        return self.__num_paginas
    
class Articulo(Texto):
    def __init__(self, titulo, autor, revista, fecha_publicacion):
        super().__init__(titulo, autor)
        self.revista = revista
        self.fecha_publicacion = fecha_publicacion
    def obtener_revista(self):
        return self.revista
    
class Poema(Texto):
    def __init__(self, titulo, autor, estrofas, rima):
        super().__init__(titulo, autor)
        self.estrofas = estrofas
        self.__rima = rima # Atributo privado
    def obtener_rima(self):
        return self.__rima
    
  # Creación de instancias de las clases "Libro", "Artículo" y "Poema"
teatro = Libro("Teatro Completo", "Federico García Lorca", 500, 1936)
periodismo = Articulo("Periodismo", "Gabriel García Márquez", "El Espectador", "1958")
sonetos = Poema("Cien Sonetos de Amor", "Pablo Neruda", 14, "ABBA")
 
  # Llamada a los métodos para obtener los atributos de cada texto
print("Autor: ", teatro.obtener_autor())
print("Revista: ", periodismo.obtener_revista())
print("Rima: ", sonetos.obtener_rima())