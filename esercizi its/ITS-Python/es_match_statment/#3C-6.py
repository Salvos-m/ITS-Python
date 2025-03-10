'''
Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere 
un codice python che consenta all'utente di inserire il nome di un 
animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica 
l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli 
o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria 
in una variabile animal_type. Se l'animale inserito non è classificabile in una 
delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso
appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene 
possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa 
effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono 
vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.

Expected Output:

Digita il nome di un animale: leone
Digita l'habitat in cui vive l'animale leone: terra
Output:
Leone appartiene alla categoria dei Mammiferi!
L'animale leone è uno dei mammiferi che può vivere sulla terra!
'''


'''
mammiferi=["cane", "gatto", "cavallo", "elefante", "leone"]
rettili= ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli= ["aquila", "pappagallo", "gufo", "falco"]
pesci= ["squalo", "trota", "salmone", "carpa"]
tutti=[mammiferi,rettili,uccelli,pesci]
animal_type=

acqua=[pesci,mammiferi[-1]]
terra=[mammiferi,rettili,uccelli]
aria=[uccelli]

animale=input("inserisci un animale:")
habitat=input("inserisci il suo habitat:")

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
'''

animale:str=(input("inserisci l'animale "))
mammiferi:list=["cane","gatto","cavallo","elefante","leone","balena","delfino"]
rettili:list=["serpente","lucertola","tartaruga","coccodrillo"]
uccelli:list=["aquila","pappagallo","gufo","falco","cigno","anatra","tacchino"]
pesci:list=["squalo","trota","salmone","carpa"]
animali:list=[mammiferi,rettili,pesci,uccelli]
habitat:list=["aria","acqua","terra"]

match animale:
  case animale if animale in mammiferi and animale in (mammiferi[0:4]):
   print(f"{animale} vive nella {habitat[2]}")
  case animale if animale in mammiferi and animale in (mammiferi[5:7]):
   print(f"{animale} vive nel {habitat[1]}")
  case animale if animale in rettili and animale in (rettili[0:2]):
   print(f"{animale} vive sulla{habitat[2]} ferma")
  case animale if animale in rettili and animale in (rettili[2:4]):
   print(f"{animale} vive sull {habitat[1]} e sulla {habitat[2]} ferma")
  case animale if animale in uccelli and animale in (uccelli[0:3]):
   print(f"{animale} vive nel {habitat[0]}")
  case animale if animale in uccelli and animale in (uccelli[4:6]):
   print(f"{animale} vive nel {habitat[1]}")
  case animale if animale in uccelli and animale in uccelli[7]:
   print(f"{animale} vive nel {habitat[2]}")
  case animale if animale in pesci:
   print(f"{animale} vive in {habitat[1]}")
  case _:
   print(f"sconosciuto")



