#Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.

def rekurzija(tekst):
    if len(tekst) <= 1:
        return tekst
    
    return rekurzija(tekst[1:]) + tekst[0]

