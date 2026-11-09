imie = input("Podaj imię: ")
print("Witaj", imie)

wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

pelne_dane = input("Podaj imię i nazwisko: ")
czesci = pelne_dane.split()
inicjaly = czesci[0][0].upper() + "." + czesci[1][0].upper() + "."
print("Inicjały:", inicjaly)

lancuch = input("Podaj łańcuch znaków: ")
print("Łańcuch wyświetlony 5 razy:", lancuch * 5)

l1 = input("Podaj pierwszy łańcuch: ")
l2 = input("Podaj drugi łańcuch: ")
l3 = l1 + l2
print("Trzeci łańcuch jako połączenie dwóch:", l3)

t1 = input("Podaj pierwszy łańcuch do podziału: ")
t2 = input("Podaj drugi łańcuch do podziału: ")
trzeci = t1[:len(t1)//2] + t2[len(t2)//2:]
print("Trzeci łańcuch z połówek:", trzeci)