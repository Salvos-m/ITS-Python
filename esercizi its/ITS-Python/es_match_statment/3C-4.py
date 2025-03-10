'''
Scrivere un programma in Python che permetta all'utente di inserire 
il nome di un animale e, utilizzando un match statement, identifichi 
a quale categoria esso appartiene. L'animale deve essere classificato 
in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,  
mostrare un messaggio indicante che il programma non è in grado di 
classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie.

Expected Output:

Digita il nome di un animale: cane
Output: cane appartiene alla categoria dei Mammiferi!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: coccodrillo
Output: coccodrillo appartiene alla categoria dei Rettili!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: pappagallo
Output: pappagallo appartiene alla categoria degli Uccelli!
''' 

mammiferi=["cane", "gatto", "cavallo", "elefante", "leone"]
rettili= ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli= ["aquila", "pappagallo", "gufo", "falco"]
pesci= ["squalo", "trota", "salmone", "carpa"]
tutti=[mammiferi,rettili,uccelli,pesci]

animale=input("inserisci un animale:")

match animale:
    case animale if animale in mammiferi:
        print(f"{animale} appartiene alla categoria dei mammiferi")
    case animale if animale in rettili:
        print(f"{animale} appartiene alla categoria dei rettili")
    case animale if animale in uccelli:
        print(f"{animale} appartiene alla categoria dei ucceli")
    case animale if animale in pesci:
        print(f"{animale} appartiene alla categoria dei pesci")
    case animale if animale not in tutti:
        print(f"{animale} non appartiene a nessuna delle categorie")