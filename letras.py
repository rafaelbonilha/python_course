from __future__ import print_function, division

import turtle

from polygon import circle, arc


# Definição das direções: fd, bk, lt, rt, pu, pd

def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()


# Definição dos movimentos

def fdlt(t, n, angle=90):
    """frente e esquerda"""
    fd(t, n)
    lt(t, angle)

def fdbk(t, n):
    """frente e para trás, voltando para a posição original"""
    fd(t, n)
    bk(t, n)

def skip(t, n):
    """move o cursor"""
    pu(t)
    fd(t, n)
    pd(t)

def stump(t, n, angle=90):
    """cria a linha vertical e move a tartaruga"""
    lt(t)
    fd(t, n)
    rt(t, angle)

def hollow(t, n):
    """move o cursor na vertical"""
    lt(t)
    skip(t, n)
    rt(t)


# Definição da localização e da direção, volta o cursor sempre para a posição original


def post(t, n):
    """Cria a linha vertical e volta para a posição original"""
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """Cria a linha horizontal e volta para posição original"""
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

def hangman(t, n, height):
    """Faz uma linha vertical para a altura especificada e uma linha horizontal
     na altura especificada e depois retorne.
     Isso é eficiente de implementar e acaba sendo útil, mas
     não é tão semanticamente limpo."""
    stump(t, n * height)
    fdbk(t, n)
    lt(t)
    bk(t, n*height)
    rt(t)

def diagonal(t, x, y):
    """Cria uma linha na digital e volta para o ponto original"""
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

def bump(t, n, height):
    """ Para criação do radiano
    """
    stump(t, n*height)
    arc(t, n/2.0, 180)
    lt(t)
    fdlt(t, n*height+n)


"""
Criando as letras do alfabeto usando o cursor do turtle

"""

def draw_a(t, n):
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)

def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_c(t, n):
    hangman(t, n, 2)
    fd(t, n)

def draw_d(t, n):
    bump(t, 2*n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    fd(t, n)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    fd(t, n/2)
    beam(t, n/2, 2)
    fd(t, n/2)
    post(t, n)

def draw_h(t, n):
    post(t, 2*n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2*n)

def draw_i(t, n):
    beam(t, n, 2)
    fd(t, n/2)
    post(t, 2*n)
    fd(t, n/2)

def draw_j(t, n):
    beam(t, n, 2)
    arc(t, n/2, 90)
    fd(t, 3*n/2)
    skip(t, -2*n)
    rt(t)
    skip(t, n/2)

def draw_k(t, n):
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2*n)
    fd(t, n)

def draw_n(t, n):
    post(t, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)
    post(t, 2*n)

def draw_m(t, n):
    post(t, 2*n)
    draw_v(t, n)
    post(t, 2*n)

def draw_o(t, n):
    skip(t, n)
    circle(t, n)
    skip(t, n)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n/2)

def draw_q(t, n):
    draw_o(t, n)
    diagonal(t, -n/2, n)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n/2, n)

def draw_s(t, n):
    fd(t, n/2)
    arc(t, n/2, 180)
    arc(t, n/2, -180)
    fdlt(t, n/2, -90)
    skip(t, 2*n)
    lt(t)

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_u(t, n):
    post(t, 2*n)
    fd(t, n)
    post(t, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    diagonal(t, -n/2, 2*n)
    diagonal(t, n/2, 2*n)
    skip(t, n/2)

def draw_y(t, n):
    skip(t, n/2)
    stump(t, n)
    vshape(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n/2)

def draw_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    fd(t, n)

def draw_(t, n):
    # Para gerar um espaço entre uma palavra ou letra
    skip(t, n)

if __name__ == '__main__':

    # Cria a posição e o tamanho do turtle
    size = 8
    bob = turtle.Turtle()

    for f in [draw_o, draw_i, draw_, draw_m, draw_e, draw_u, draw_, draw_a, draw_m, draw_o, draw_r, draw_,
              draw_j, draw_a, draw_, draw_d, draw_i, draw_s, draw_s, draw_e, draw_, draw_q, draw_u, draw_e,
              draw_, draw_t, draw_e, draw_, draw_a, draw_m, draw_o, draw_, draw_h, draw_o, draw_j, draw_e]:
        f(bob, size)
        skip(bob, size)

    turtle.mainloop()
