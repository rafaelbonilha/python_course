
from __future__ import print_function, division

"""
Este módulo fornece uma função, structshape (), que leva
um objeto de qualquer tipo e retorna uma sequência que resume a
"forma" da estrutura de dados; isto é, o tipo, tamanho e
composição.
"""

def structshape(ds):
    """Retorna uma string que descreve a forma de uma estrutura de dados.

    ds: qualquer objeto Python

    Returna: string
    """
    typename = type(ds).__name__

    # lidar com sequências
    sequence = (list, tuple, set, type(iter('')))
    if isinstance(ds, sequence):
        t = []
        for i, x in enumerate(ds):
            t.append(structshape(x))
        rep = '%s of %s' % (typename, listrep(t))
        return rep

    # lidar com dicionários
    elif isinstance(ds, dict):
        keys = set()
        vals = set()
        for k, v in ds.items():
            keys.add(structshape(k))
            vals.add(structshape(v))
        rep = '%s of %d %s->%s' % (typename, len(ds), 
                                   setrep(keys), setrep(vals))
        return rep

    # lidar com outros tipos
    else:
        if hasattr(ds, '__class__'):
            return ds.__class__.__name__
        else:
            return typename


def listrep(t):
    """Retorna uma representação de string de uma lista de strings de tipo.

    t: lista de strings

    Retorna: string
    """
    current = t[0]
    count = 0
    res = []
    for x in t:
        if x == current:
            count += 1
        else:
            append(res, current, count)
            current = x
            count = 1
    append(res, current, count)
    return setrep(res)


def setrep(s):
    """Retorna uma representação de sequência de um conjunto de seqüências de caracteres.

    s: conjunto de strings

    Retorna: string
    """
    rep = ', '.join(s)
    if len(s) == 1:
        return rep
    else:
        return '(' + rep + ')'
    return 


def append(res, typestr, count):
    """Adiciona um novo elemento a uma lista de seqüências de caracteres de tipo.

    Modifica res.

    res: lista de tipos de strings
    typestr: novo tipo de string
    count: conta quantos novos tipos foram criados

    Retorna: None
    """
    if count == 1:
        rep = typestr
    else:
        rep = '%d %s' % (count, typestr)
    res.append(rep)


if __name__ == '__main__':

    t = [1, 2, 3]
    print(structshape(t))

    t2 = [[1, 2], [3, 4], [5, 6]]
    print(structshape(t2))

    t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
    print(structshape(t3))

    class Point:
        """tipo trivial de objeto"""

    t4 = [Point(), Point()]
    print(structshape(t4))

    s = set('abc')
    print(structshape(s))

    lt = zip(t, s)
    print(structshape(lt))

    d = dict(lt)        
    print(structshape(d))

    it = iter('abc')
    print(structshape(it))
