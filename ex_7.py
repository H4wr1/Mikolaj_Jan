# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

def wykres(wykres) -> bool:
    x1, y1 = wykres[0]
    x2, y2 = wykres[1]
    x3, y3 = wykres[2]
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        return True
    else:
        return False

