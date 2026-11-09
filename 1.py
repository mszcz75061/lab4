Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print("Początkowa lista:", Moja_lista)
print("Pierwszy element listy:", Moja_lista[0])
print("Ostatni element listy:", Moja_lista[-1])
print("Długość listy:", len(Moja_lista))
print("Największa wartość w liście:", max(Moja_lista))
print("Najmniejsza wartość w liście:", min(Moja_lista))
print("Suma elementów listy:", sum(Moja_lista))
print("Posortowana lista (funkcja sorted):", sorted(Moja_lista))

Moja_lista.append(6)
print("Po dodaniu elementu 6 na koniec (append):", Moja_lista)

Moja_lista.insert(2, 5)
print("Po wstawieniu elementu 5 na indeks 2 (insert):", Moja_lista)

usuniety = Moja_lista.pop()
print("Po usunięciu ostatniego elementu (pop):", Moja_lista)

Moja_lista.reverse()
print("Po odwróceniu kolejności (reverse):", Moja_lista)

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
listaŁ = lista1 + lista2
print("Połączenie dwóch list (lista1 + lista2):", listaŁ)

listaM = lista1 * 5
print("Pięciokrotne powtórzenie listy1:", listaM)

print("Wycinek od początku do n ([:2]):", listaŁ[:2])
print("Wycinek od indeksu m do końca ([1:]):", listaŁ[1:])
print("Wycinek z krokiem ([0:4:2]):", listaŁ[0:4:2])
print("Odwrócenie listy za pomocą wycinka ([::-1]):", listaŁ[::-1])

tekst = "Ala ma kota, a kot ma Alę."
nowy_tekst = tekst.replace("Ala", "Ola")
print("Tekst po zamianie (replace):", nowy_tekst)

nowy_tekst_ograniczony = tekst.replace("ma", "posiada", 1)
print("Tekst po ograniczonej zamianie (max=1):", nowy_tekst_ograniczony)

tekst_split = "jabłko,banan,gruszka,śliwka"
owoce_split = tekst_split.split(",")
print("Tekst podzielony na listę (split):", owoce_split)

tekst1 = "qwerty"
tekst2 = "QWERTY"
tekst1 = tekst1.upper()
tekst2 = tekst2.lower()
print("Tekst1 po zmianie na duże litery (upper):", tekst1)
print("Tekst2 po zmianie na małe litery (lower):", tekst2)