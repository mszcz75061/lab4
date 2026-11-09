stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżancie",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)
ilość_stopnii = len(stopnie)
Major_index = stopnie.index("Major")
Pułkownik_wstepowanie = "Pułkownik" in stopnie
print("Liczba wszystkich stopni wojskowych (ilość_stopnii):", ilość_stopnii)
print("Indeks stopnia 'Major' (Major_index):", Major_index)
print("Czy 'Pułkownik' znajduje się w krotce (Pułkownik_wstepowanie):", Pułkownik_wstepowanie)