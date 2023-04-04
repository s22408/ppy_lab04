"""
Zadanie 1. Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli w
danym pomieszczeniu, zakładając prostokątną podłogę i prostokątne panele. Dane wejściowe
to długość i szerokość podłogi, (do powierzchni pomieszczenia należy dodać 10%)
długość i szerokość panela oraz ilość paneli w opakowaniu. (10%)

"""

import math

def function1(xPod, yPod, xPan, yPan, ilOp):
    realX = 1.1 * xPod
    realY = 1.1 * yPod
    xIle = math.floor(realX / xPan) + 1
    yIle = math.floor(realY / yPan) + 1
    potrzebaPaneli = xIle * yIle
    print(potrzebaPaneli)
    potrzebaOpakowan = math.ceil(potrzebaPaneli / ilOp)
    return potrzebaOpakowan
