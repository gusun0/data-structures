class Perro():
  #  *** Varibale de clase ***
    tipo = 'canino'
    def __init__(self, nombre, raza):
  #      *** variable de instancia ***
        self.nombre = nombre
        self.raza = raza

perro1 = Perro('madonna','pitbull')
perro2 = Perro('borkc','pastor')
perro3 = Perro('toby','chihuahua')


print(perro1.nombre)
print(perro2.nombre)
print(perro1.tipo)
print(perro2.tipo)
print(Perro.tipo)


