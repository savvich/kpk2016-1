from drawman import *
from random import randint
from math import cos, sin, pi
"""
Рисование фрактала КРУГИ ЛЕБЕДЕВА
Количество потомков определяется переменной m
Радиус круга-потомка меньше родителя в m/2 раза.
    Возможны вариации, например, радиус всегда в два раза меньше,
    получаются интересные узоры при количестве потомков 4, 6, 8
Входные параметры:
    Глубина рекурсии - количество поколений. (Не стоит указывать слишком большой количество)
    Количество потомков - количество кругов расположенных на круге родителя
"""
cur_color=''
r=20 # Начальный радиус - радиус основного родителя
x0=0 # Положение основного родителя
y0=0 # Положение основного родителя
n=int(input('Какая глубина рекурсии?:'))
m=int(input('Сколько потомков в каждом поколении?:'))
_cos=list(range(0, 360, 360//m))
_sin=list()
_sin[:]=[sin(x*pi/180) for x in _cos]
_cos[:]=[cos(x*pi/180) for x in _cos]

def Ring(x, y, r, n):
    """
    Рисует окружность родителя
    :param x: положение родителя
    :param y: положение родителя
    :param r: радиус родителя
    :param n: уровень потомка
    """
    if n==1:
        circle(x, y, r, random_color())
    else:
        Rings(x, y, r, n)
        circle(x, y, r, random_color())

def Rings(x, y, r, n):
    """
    Вызывает рекурсивное выполнение с обновлёнными параметрами
    :param x: положение родителя
    :param y: положение родителя
    :param r: радиус родителя
    :param n: уровень потомка
    """
    for rx, ry in zip(_cos,_sin):
        Ring(x+rx*r, y+ry*r, r/m*2, n-1)


def random_color():
    """
    Задаёт случайный цвет круга из RGB схемы
    :return: цвет круга (строка типа #rrggbb)
    """
    global cur_color
    cur_color='#'
    for i in range(3):
        rgb=str(hex(randint(16, 255)))
        cur_color+=rgb[2::]
    return cur_color


Ring(x0, y0, r, n)
input('Для завершения нажмите ВВОД')