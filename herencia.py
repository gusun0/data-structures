class Padre(object):
    def __init__(self):
        self.apellido = 'flamenco'
        self.color_ojos = 'cafe'
        self.cabello = 'ondulado'

    def obtenerApellido(self):
        return self.apellido

    def obtenerColorOjos(self):
        return self.color_ojos

    def obtenerCabello(self):
        return self.cabello

class Hija1(Padre):
    pass

class Hija2(Hija1):
    pass


p = Padre()
#print(p.apellido)
h = Hija1()
#print(h.apellido)
#print(h.obtenerCabello())
h2 = Hija2()
print(h2.apellido)





