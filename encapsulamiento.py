class Persona():
    def __init__(self):
        self.__nombre = None
        self.__edad = None

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre


p = Persona()
p.setNombre('gusun0')
print(p.getNombre())





