def iloczyn_wektorowy(xa, ya, xb, yb, xc, yc):
    # Obliczanie iloczynu wektorowego AB x AC
    return (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)

def po_przeciwnych(xa, ya, xb, yb, xc, yc, xd, yd):
    # Sprawdzanie, czy punkty C i D są po przeciwnych stronach odcinka AB
    iloczyn1 = iloczyn_wektorowy(xa, ya, xb, yb, xc, yc)
    iloczyn2 = iloczyn_wektorowy(xa, ya, xb, yb, xd, yd)
    return iloczyn1 * iloczyn2 < 0

def czy_przecinaja(xa, ya, xb, yb, xc, yc, xd, yd):
    # Sprawdzanie, czy odcinki AB i CD się przecinają
    if (po_przeciwnych(xa, ya, xb, yb, xc, yc, xd, yd) and
        po_przeciwnych(xc, yc, xd, yd, xa, ya, xb, yb)):
        return True
    return False

# Wprowadzenie danych
xa = float(input("Podaj współrzędną xa punktu A: "))
ya = float(input("Podaj współrzędną ya punktu A: "))
xb = float(input("Podaj współrzędną xb punktu B: "))
yb = float(input("Podaj współrzędną yb punktu B: "))
xc = float(input("Podaj współrzędną xc punktu C: "))
yc = float(input("Podaj współrzędną yc punktu C: "))
xd = float(input("Podaj współrzędną xd punktu D: "))
yd = float(input("Podaj współrzędną yd punktu D: "))

# Sprawdzanie, czy odcinki AB i CD się przecinają
if czy_przecinaja(xa, ya, xb, yb, xc, yc, xd, yd):
    print("Odcinki AB i CD się przecinają.")
else:
    print("Odcinki AB i CD się nie przecinają.")