lista = [5,10,3,12,10,6]
print('lista', lista)

for i in range(1,len(lista)):
    aux = lista[i]
    print('aux:', aux)
    j = i - 1
    print('j', j)
    while j >= 0 and aux < lista[j]:
        print('aux dentro del ciclo:', aux)
        print('lista[j] dentro del ciclo:', lista[j])
        lista[j+1] = lista[j]
        print('lista[j+1]:',lista[j+1])
        lista[j] = aux
        print('lista[j]:',lista[j])
        j -= 1 # para poder comparar elementos a la izq
        print('j:',j)

print(lista)

