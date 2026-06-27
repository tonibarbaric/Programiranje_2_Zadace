#Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.

def generator_parnih(broj):
    for i in range(broj):
        if i % 2 == 0:
            yield i

def generator_neparnih(broj):
    for i in range(broj):
        if i % 2 != 0:
            yield i


granica = int(input("Unesite neki broj: "))

print("Parni brojevi manji od", granica, "su:")
for parni_broj in generator_parnih(granica):
    print(parni_broj, end=" ")

print("Neparni brojevi manji od", granica, "su:")
for neparni_broj in generator_neparnih(granica):
    print(neparni_broj, end=" ")
