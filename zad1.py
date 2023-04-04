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
