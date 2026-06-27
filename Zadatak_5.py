#Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
#Nakon toga napisati regex za provjeru eduId koji mora biti formata ime.prezimeX@sum.ba 
#X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo ime.prezime@sum.ba).
#Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.

import re

email = input("Unesite e-mail (ime.prezime@fpmoz.sum.ba): ")
eduid = input("Unesite eduID (ime.prezimeX@sum.ba): ")


regex = "^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"

regex2 = "^[a-zA-Z]+\.[a-zA-Z]+[0-9]*@sum\.ba$"

if re.search(regex, email):
    print("E-mail je ispravan.")
else:
    print("E-mail nije ispravan")

if re.search(regex2, eduid):
    print("eduID je ispravan.")
else:
    print("eduID nije ispravan")
