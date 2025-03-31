#percorso
percorso:list=["quadrato 1"]
x=len(percorso)
#controllo valore x
#print(x)
while x <=70:
    n=x
    y=f"quadrato {n}"
    percorso.append(y)
    x+=1 #serve per incrementare x, pensavo che leggesee la lunghezza ma è da chiesere
print(percorso) #ottenuto percorso


#mosse animali
import random

numero_t=random.randint(1, 10)

def moss_tar(numero_t):
    match numero_t:
        case numero_t if numero_t <= 5:
            return "passo veloce"
        case

