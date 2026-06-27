'''
Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.

Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 

Nedovoljan
0-49%

Dovoljan
50-65%

Dobar
65-80%

Vrlodobar
80-90%

Izvrstan
90-100%
'''


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


def prezime(student):
    return student[1]

studenti.sort(key=prezime)

print("Studenti sortirani po prezimenima:")
for s in studenti:
    print(s[1], s[0], "-", s[2], "bodova")


ocjene = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlodobar": 0,
    "Odličan": 0
}

for s in studenti:
    broj_bodova = s[2]
    
    if broj_bodova <= 49:
        ocjene["Nedovoljan"] += 1
    elif broj_bodova <= 65:
        ocjene["Dovoljan"] += 1
    elif broj_bodova <= 80:
        ocjene["Dobar"] += 1
    elif broj_bodova <= 90:
        ocjene["Vrlodobar"] += 1
    else:
        ocjene["Izvrstan"] += 1

print("Ostvarane ocjene:")
for ocjena, broj in ocjene.items():
    print(ocjena + ":", broj)
