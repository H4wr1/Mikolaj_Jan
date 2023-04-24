# sprawdz, czy nawias ma swoja pare, jesli ma swroc True, jesli nie False

def para_nawiasow(tekst: str) -> bool:
    count = 0
    for i in tekst:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    return count == 0

