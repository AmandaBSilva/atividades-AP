def celkel(temp):
    return temp + 273.15

def kelcel(temp):
    return temp - 273.15

def celfar(temp):
    return temp * 9 / 5 + 32

def farcel(temp):
    return (temp - 32)* 5/9

dicio = {
    0: exit,
    1: celker,
    2: celfar,
    3: kelcel,
    4: lambda t: celfar(kelcel(t)),
    5: farcel,
    6: lambda t; celkel(farcel(t))
}
