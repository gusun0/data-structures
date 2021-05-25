lista = [i** 2 for i in range(1,11) if i**2 > 40]
string = ['java','py','go']

lista2 = [ len(i) for i in string ]

print(lista2)

def elevado(n):
    return 2**n

lista = [elevado(i) for i in range(10)]
print(lista)




