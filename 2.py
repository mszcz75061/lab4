osoby = ["Anna", "Katarzyna", "Piotr", "Michał"]
osoby.sort()
print("a) Posortowana alfabetycznie lista osób:", osoby)

osoby.append("Jan")
osoby.append("Magda")
pobrana = osoby.pop()
print("b) Pobrana ostatnia osoba za pomocą pop():", pobrana)
print("b) Aktualna lista osób:", osoby)

osoby.insert(2, "Tomasz")
print("c) Po dodaniu osoby na pozycji 3 (indeks 2):", osoby)

osoby.reverse()
osoby_zdublowane = osoby * 2
print("d) Odwrócona i zdublowana lista osób:", osoby_zdublowane)