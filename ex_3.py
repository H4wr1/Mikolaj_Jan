# Policz studentki i studentow i zwroc wynik w formacie: [k, m]
# Przyjmij, ze imie dla kobiety konczy sie na "a"
def policz_studentow_plec(studenci) -> [int, int]:
    k = 0
    m = 0
    for student in studenci:
        if student.split()[0].endswith("a"):
            k += 1
        else:
            m += 1

    return [k, m]
