#Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo prezimena.
#String mora sadržavati bar jedan broj između 0 i 5 i razmak.

import re

unos = input("Unesite string za provjeru: ")

regex = "^T.*([0-5].*\s|\s.*[0-5]).*B$"

if re.search(regex, unos):
    print("Unos je ispravan")
else:
    print("Unos nije ispravan")
