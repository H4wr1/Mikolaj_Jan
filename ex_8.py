# dla podanych dwoch punktow, oblicz, czy funkcja liniowa jest rozsnaca, czy malejaca
# dla niemalejacej zrwoc True
# dla malejacej zwroc False

def funkcja_liniowa(punkty) -> bool:
    x1 = punkty[0][0]
    y1 = punkty[0][1]
    x2 = punkty[1][0]
    y2 = punkty[1][1]
    #if y2-y1==0:
    #    return False
    if (x2-x1>=0 and y2-y1>=0) or (x2-x1<0 and y2-y1<0) :
        return True
    return False



