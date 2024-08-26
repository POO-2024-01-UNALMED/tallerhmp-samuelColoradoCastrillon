from persona import Persona

class Deportista(Persona):
    #Constructor
    def __init__(self, nombre, edad, altura, sexo, años_practicando, deporte="Futbol"):
        super().__init__(nombre, edad, altura, sexo)
        self.__deporte = deporte
        self.__años_practicando = años_practicando

    #Metodos
    def getDeporte(self):
        return self.__deporte
    def setDeporte(self, deporte):
            self.__deporte = deporte
    def getAñosPracticando(self):
        return self.__años_practicando
    def setAñosPracticando(self, años_practicando):
        self.__años_practicando = años_practicando