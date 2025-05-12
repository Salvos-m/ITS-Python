#sbagliato non capisco dove
'''
Si scriva un programma in python che computi la statistica di otto 
 lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è 
 uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale 
 dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa"
mentre inserisci "c" o "C" se e' uscito "croce".

Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%

Totale "croce": 3
Percentuale "croce": 37.50%
'''

print("Per ciascun lancio della moneta inserisci \"t\" o \"T\" se e' uscito \"testa\"")
print("mentre inserisci \"c\" o \"C\" se e' uscito \"croce\".")

counter=1
croce=0
testa=0

while counter<=8:
    lancio=input(f"Lancio {counter}: ")
    #counter+=1

    match lancio:
      case "c" | "C":
          croce+=1
          
          counter+=1
      case lancio if lancio== "t" or "T":
          testa+=1
        
          counter+=1
'''case lancio if lancio!="C" or "c" or "T" or "t":
           counter+=0'''

#print(f"{testa} e {croce}")
croceperc=(croce/8)*100
testaperc=(testa/8)*100

print(f"totale \"testa\":{testa}")
print(f"percentuale \"testa\":{testaperc:.2f}%")

print(f"totale \"croce\":{croce}")
print(f"percentuale \"croce\":{croceperc:.2f}%")

