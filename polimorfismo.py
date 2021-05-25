class Carro():
    def tipo(self):
        print('Soy un carro automatico')

class Moto(Carro):
    def tipo(self):
        print('Soy una moto estandar')

p = Carro()
m = Moto()
m.tipo()
p.tipo()



