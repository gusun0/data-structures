class Clase1(object):
    def __init__(self):
        self.atributo_clase1 = 'Soy de la clase 1'

    def metodo_clase_1(self):
        print('Soy de la clase 1')


class Clase2(object):
    def __init__(self):
        self.atributo_clase2 = 'Soy de la clase 2'

    def metodo_clase_2(self):
        print('Soy de la clase 2')


# herencia multiple

class Clase3(Clase1,Clase2):
    pass

#c3 = Clase3()
#c3.metodo_clase_1()
#c3.metodo_clase_2()


class Animal(object):
    def __init__(self, patas):
        self.patas = patas
        self.orejas = 2

class Mamifero(object):
    def __init__(self):
        self.tipo = 'Mamifero'

class Perro(Animal, Mamifero):
    def __init__(self, nombre, edad):
        super(Perro,self).__init__()
        self.nombre = nombre 
        self.edad = edad

    def getNombre(self):
         print(self.nombre)

    def getEdad(self):
        print(self.edad)


p = Perro('borck', 23)
p.getNombre()
print(p.patas)
print(Animal.patas)


    




    


