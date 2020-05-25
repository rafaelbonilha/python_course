from __future__ import print_function, division


def triplo_dobro(word):
    """Testa se contém três letras duplas consecutivas.
    
    word: string

    retorna: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count
            count = 0
    return False


def find_triplo_dobro():
    """Lê a lista de palavras em busca de palavras com 3 letras duplas consecutivas"""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if triplo_dobro(word):
            print(word)


print('Aqui estão todas as palavras na lista que possuem')
print('três letras duplas consecutivas.')
find_triplo_dobro()
print('')


