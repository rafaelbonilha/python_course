from __future__ import print_function, division
from datetime import datetime

def diaduplo_calc(b1, b2):

    assert b1 > b2
    delta = b1 - b2
    ddia = b1 + delta
    return ddia

def diaduplo():
    # verifica as datas de aniversário de duas pessoas e retorna o dia duplo delas
    b1 = datetime(1985, 5, 5)
    b2 = datetime(1981, 12, 27)
    print('Dia Duplo: ', end=' ')
    print(diaduplo_calc(b1, b2))
