# Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
# Prebrojati u rječnik koliko ima kojih ocjena.
# Izračunati postotak prolaznosti. (sve ocjene veće od 1)

import random

imena = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", "Magdalena", "Ivana",
         "Stipe", "Emanuel", "Petar", "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana",
         "Marija", "Nikolina", "Andrija", "Slaven", "Sebastian", "Marko", "Frano", "Stipan", "Eugen",
         "Toni", "Dražan", "Matej", "Nives", "Nemanja", "Sara", "Ružica", "Gabrijel", "Darian", "Ivana",
         "Ivan Stjepan", "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante", "Josip",
         "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko", "Sergej", "Matej",
         "Marin", "Sara", "Josip", "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko",
         "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", "Petar", "Emanuel", "Helena", "Antonio", "Petar"]

ocjene = {}
prolaz = 0

for ime in imena:
    ocjena = random.randint(1, 5)

    if ocjena in ocjene:
        ocjene[ocjena] += 1
    else:
        ocjene[ocjena] = 1

    if ocjena > 1:
        prolaz += 1

print("Broj ocjena:")
for ocjena in ocjene:
    print(ocjena, ":", ocjene[ocjena])

ukupno = len(imena)
postotak = (prolaz / ukupno) * 100

print("Prolaznost:", round(postotak, 2), "%")





