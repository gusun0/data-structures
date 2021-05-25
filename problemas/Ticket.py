class Ticket():
    def __init__(self, id = None, passenger = None, origin = None, destination = None):
        self.id = id
        self.passenger = passenger
        self.origin = origin
        self.destination = destination

    def getId(self):
        return self.id

    def getPassenger(self):
        return self.passenger.getFullName

    def getOrigin(self):
        return self.origin.getName()

    def getDestino(self):
        return self.destination.getName()

    def fullPrice(self):
        if self.origin.getRegion() > 4 or self.destination.getRegion() > 4:
            return "Esos destinos no existen"
        else:
            lista = [[1000,1500,2000,3000],[1500,1000,1500,2000],[2000,1500,1000,1500],[3000,2000,1500,1000]]
            total = lista[self.origin.getRegion() - 1][self.destination.getRegion() - 1]
            return total

    def discount(self):
        descuento = 0
        if self.passenger.isChild():
            descuento = self.fullPrice * 0.20
            return descuento
        if self.passenger.isSenior():
            descuento = self.fullPrice * 0.25
            return descuento
        return descuento

    def finalPrice(self):
        total = self.fullPrice() - self.discount()
        return total















