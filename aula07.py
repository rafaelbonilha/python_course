n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisao é {:.3f}'.format(s, m, d), end=' ')
print('Divisao inteira {} e a potencia {}'.format(di, e))

