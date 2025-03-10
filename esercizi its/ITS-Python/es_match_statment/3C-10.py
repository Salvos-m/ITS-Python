'''
Scrivere un programma in Python che permetta all'utente di inserire una data 
(giorno e mese espressi in forma numerica), salvi la data in una tupla e 
utilizzi un match statement per verificare se la data corrisponde a una 
festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.
'''

giorno=int(input("inserisci il giorno: "))
mese=int(input("inserisci il mese: "))

data:tuple=(giorno,mese)

capodanno:tuple=(1,1)
san_valentino:tuple=(14,2)
ferragosto:tuple=(15,8) 
halloween:tuple=(31,10)
natale:tuple= (25,12)
lista:list=[capodanno,san_valentino,ferragosto,halloween,natale]

match data:
    case data if data == capodanno:
        print("il 1/1 e' capodanno")
    case data if data==san_valentino:
        print("il 14/12 e' San Valentino")
    case data if data==ferragosto:
        print("il 15/8 e' Ferragosto")
    case data if data ==halloween:
        print("il 31/10 e' Halloween")
    case data if data==natale:
        print("il 25/12 e' Natale")
    case data if mese==7:
        print("Festa della Repubblica Italiana")
    case data if data!=lista:
        print("Nessuna festività importante in questa data.")