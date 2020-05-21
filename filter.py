# Função Filter

def pares(i):
    if i % 2 == 0:
        return i
lista = [1,2,3, 4,5,6,7,8,9,10]

list_pares = filter(pares, lista)
print(list(list_pares))
