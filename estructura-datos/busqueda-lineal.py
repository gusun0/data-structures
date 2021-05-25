def busqueda_lineal(dato):
    for x in range(len(lista)):
        if lista[x] == dato:
            return x
    return None


def buscar(dato):
    if busqueda_lineal(dato) == None:
        return "El dato %d no se encontro"%(dato)
    else:
        return "El dato %d se encontro en el indice: %d"%(dato, busqueda_lineal(dato))

    


lista = [12,34,5,9,7,3,12,5345,65,432,1,6,567,8,5,65 ]

for i in range(len(lista)):
    print("indice[%d] el valor es %d"%(i, lista[i]))

busqueda_lineal(7)
print(buscar(7))
