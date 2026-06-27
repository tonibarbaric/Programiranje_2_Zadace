#Funkciju iz prethodne zadaće učitati kao funkciju modula u novi program
#i pozvati je nakon traženja unosa od korisnika.

from Zadatak_7 import rekurzija

unos = input("Unesite tekst: ")

rezultat = rekurzija(unos)

print("Rezultat je:", rezultat)
