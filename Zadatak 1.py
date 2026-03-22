# Napisati program koji generira kvadratnu matricu dimenzija 7x7.
# Elementi su nasumični brojevi od 1 do 9.
# Zatim napisati program koji računa zbroj elemenata na rubovima matrice.

import random

r = 7
s = 7

matrica = []

for i in range(r):
    red = []
    for j in range(s):
        unos = random.randint(1,9)
        red.append(unos)
    matrica.append(red)

print("----Matrica----")
for red in matrica:
    print(red)

zbroj = 0

for i in range (r):
    for j in range(s):
        if i == 6 or i == 0 or j == 0 or j == 6:
            zbroj += matrica[i][j]

print("Zbroj elemenata na rubovima matrica iznosi: ",zbroj)
        
