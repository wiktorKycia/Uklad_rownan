wsx1 = int(input('Podaj wspóczynnik przy x w pierwszym równaniu: '))
wsy1 = int(input('Podaj wspóczynnik przy y w pierwszym równaniu: '))
wsz1 = int(input('Podaj wspóczynnik przy z w pierwszym równaniu: '))
wynik1 = int(input('Podaj wynik z pierwego równania: '))
print("="*50)
wsx2 = int(input('Podaj wspóczynnik przy x w drugim równaniu: '))
wsy2 = int(input('Podaj wspóczynnik przy y w drugim równaniu: '))
wsz2 = int(input('Podaj wspóczynnik przy z w drugim równaniu: '))
wynik2 = int(input('Podaj wynik z drugiego równania: '))
print("="*50)
wsx3 = int(input('Podaj wspóczynnik przy x w trzecim równaniu: '))
wsy3 = int(input('Podaj wspóczynnik przy y w trzecim równaniu: '))
wsz3 = int(input('Podaj wspóczynnik przy z w trzecim równaniu: '))
wynik3 = int(input('Podaj wynik z trzeciego równania: '))
lista = [
    [wsx1, wsy1, wsz1, wynik1],
    [wsx2, wsy2, wsz2, wynik2],
    [wsx3, wsy3, wsz3, wynik3]
]


def func(lis, tuple1, tuple2, tuple3) -> int:
    return lis[tuple1[0]][tuple1[1]] * lis[tuple2[0]][tuple2[1]] * lis[tuple3[0]][tuple3[1]]


listaw = [
    [wsx1, wsy1, wsz1],
    [wsx2, wsy2, wsz2],
    [wsx3, wsy3, wsz3]
]
listax = [
    [wynik1, wsy1, wsz1],
    [wynik2, wsy2, wsz2],
    [wynik3, wsy3, wsz3]
]
listay = [
    [wsx1, wynik1, wsz1],
    [wsx2, wynik2, wsz2],
    [wsx3, wynik3, wsz3]
]
listaz = [
    [wsx1, wsy1, wynik1],
    [wsx2, wsy2, wynik2],
    [wsx3, wsy3, wynik3]
]
Wyznacznik = func(listaw, (0, 0), (1, 1), (2, 2)) + func(listaw, (0, 1), (1, 2), (2, 0)) + func(listaw, (1, 0), (2, 1), (0, 2)) - func(listaw, (2, 0), (1, 1), (0, 2)) - func(listaw, (0, 0), (1, 2), (2, 1)) - func(listaw, (0, 1), (1, 0), (2, 2))
Wyznacznikx = func(listax, (0, 0), (1, 1), (2, 2)) + func(listax, (0, 1), (1, 2), (2, 0)) + func(listax, (1, 0), (2, 1), (0, 2)) - func(listax, (2, 0), (1, 1), (0, 2)) - func(listax, (0, 0), (1, 2), (2, 1)) - func(listax, (0, 1), (1, 0), (2, 2))
Wyznaczniky = func(listay, (0, 0), (1, 1), (2, 2)) + func(listay, (0, 1), (1, 2), (2, 0)) + func(listay, (1, 0), (2, 1), (0, 2)) - func(listay, (2, 0), (1, 1), (0, 2)) - func(listay, (0, 0), (1, 2), (2, 1)) - func(listay, (0, 1), (1, 0), (2, 2))
Wyznacznikz = func(listaz, (0, 0), (1, 1), (2, 2)) + func(listaz, (0, 1), (1, 2), (2, 0)) + func(listaz, (1, 0), (2, 1), (0, 2)) - func(listaz, (2, 0), (1, 1), (0, 2)) - func(listaz, (0, 0), (1, 2), (2, 1)) - func(listaz, (0, 1), (1, 0), (2, 2))


def podziel_przez_w(liczba) -> int:
    return liczba / Wyznacznik


x = podziel_przez_w(Wyznacznikx)
y = podziel_przez_w(Wyznaczniky)
z = podziel_przez_w(Wyznacznikz)

tuplew = (x, y, z)
for i in tuplew:
    print(i, end=' ')