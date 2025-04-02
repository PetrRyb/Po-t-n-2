číslo1 = int(input("Napiš sem s jakým číslem chceš počítat."))
číslo2 = int(input("Napiš sem druhé číslo s jakým chceš počítat."))
znaménko = str(input("Napiš sem slovem znaménko podle toho co bys chtěl provést za operaci")) 

if znaménko == "plus":
    výsledek = číslo1 + číslo2 
    
elif znaménko == "mínus":
    výsledek =číslo1 - číslo2 

elif znaménko == "děleno":
    výsledek =  číslo1/číslo2 
    
elif znaménko == "krát":
    výsledek = číslo1 * číslo2    
x = len(výsledek)    
výsledek = [1,2,3,4,5,6,7,8,9,10]
opakovat = input("Chcete opakovat program? (ano/ne)")
import random
random.choice (výsledek)