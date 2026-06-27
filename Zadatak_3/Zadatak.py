#Podatke iz datoteke rezultati.csv učitati kao listu ntorki oblika (ime, prezime, bodovi).
#Iterirati kroz sve studente i ispisati samo one koji su položili ispit (br. bodova veci od 49)


datoteka = open("rezultati.csv", "r", encoding="utf-8")

studenti = []

for linija in datoteka:

    linija = linija.strip()
    podaci = linija.split(",")
    
    ime = podaci[0]
    prezime = podaci[1]
    bodovi = int(podaci[2])
    
    student_ntorka = (ime, prezime, bodovi)
    studenti.append(student_ntorka)

datoteka.close()


print("Studenti koji su položili ispit:")

for student in studenti:
    ime_studenta = student[0]
    prezime_studenta = student[1]
    bodovi_studenta = student[2]
    
    if bodovi_studenta > 49:
        print(ime_studenta, prezime_studenta, "-", bodovi_studenta, "bodova")
