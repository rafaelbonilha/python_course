# Funcao map

def dobro(x):
    return x*2

valor = [1,2,3,4,5]

valor_dobrado = list(map(dobro, valor))

print(valor_dobrado)
