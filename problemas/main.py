from City import City
from Passenger import Passenger
from Ticket import Ticket

origen = City('Norte',6)
destino = City('Norte',5)
pasajero = Passenger('gus', 'un', 5)
    
ticket = Ticket(100,pasajero,origen,destino)

print(ticket.fullPrice())

