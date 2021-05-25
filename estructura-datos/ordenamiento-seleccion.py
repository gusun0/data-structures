lista = [4,2,6,8,5,7,8]
for i in range(len(lista)):
    minimo = i
    print('minimo: ', minimo)
    for x in range(i,len(lista)):
        print('x', x)
        print('i', i)
        if lista[x] < lista[minimo]:
            print('lista[x] - lista[minimo]: ', lista[x],lista[minimo])
            minimo = x
            print('minimo', minimo)
    aux = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux
    print(lista)


         
