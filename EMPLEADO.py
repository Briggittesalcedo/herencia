class Persona:
    def _init_(self, nombre, direccion, edad, genero):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.genero = genero

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    def _str_(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Edad: {self.edad}, Género: {self.genero}"


persona1 = Persona("Anabel mite", "Calle rosendo aviles", 38,"femenino")
print(persona1)


persona1.nombre = "Fernando Gómez"
persona1.direccion = "Avenida quito"
persona1.edad = 25
persona1.genero = "masculino"
print(persona1)