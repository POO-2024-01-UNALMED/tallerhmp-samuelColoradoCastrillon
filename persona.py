class Persona:
    #Constructor
    def __init__(self, nombre, edad, altura, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__sexo = sexo

    #Metodos
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getEdad(self):
        return self.__edad
    def setEdad(self, edad):
        self.__edad = edad
    def getAltura(self):
        return self.__altura
    def setAltura(self, altura):
        self.__altura = altura
    def getSexo(self):
        return self.__sexo
    def setSexo(self, sexo):
            self.__sexo = sexo