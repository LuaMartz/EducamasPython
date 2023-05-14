class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")
    
    def presentarse(self):
        print(f"Me llamo {self.nombre}, tengo {self.edad} años y soy {self.profesion}.")

# Creación de objetos de la clase "Persona"
juan = Persona("Juan", 30, "abogado")
maria = Persona("María", 25, "doctora")
pedro = Persona("Pedro", 40, "ingeniero")

# Llamada a los métodos definidos para cada objeto
juan.saludar()
maria.presentarse()
pedro.saludar()

class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, carrera, matricula):
        super().__init__(nombre, edad, profesion)
        self.carrera = carrera
        self.__matricula = matricula # Atributo privado
    def presentarse(self):
        print(f"Me llamo {self.nombre}, tengo {self.edad} años y estudio {self.carrera}.")
    def obtener_matricula(self):
        return self.__matricula
    def asignar_matricula(self, nueva_matricula):
        self.__matricula = nueva_matricula
 
 # Creación de objetos de la clase "Estudiante"
ana = Estudiante("Ana", 22, "estudiante", "ingeniería", "12345")
luis = Estudiante("Luis", 20, "estudiante", "medicina", "67890")
 
 # Llamada a los métodos definidos para cada objeto
ana.presentarse()
luis.asignar_matricula("13579")
print(luis.obtener_matricula())