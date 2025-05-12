'''
Creare in Python una lista vuota chiamata 'oggetti'. 
Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per 
classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

Expected Output:

['casa', 'hotel', 'b&b']
Categoria sconosciuta

--------------------------

['penna', 'matita', 'quaderno']
Materiale scolastico
'''

#oggetti=["gomma","righello","stilo"]
oggetti=[] 

while len(oggetti) <3:
    oggeto1=input("inserisci un oggeto: ")
    oggetti.append(oggeto1)

    match oggetti:
        case ["penna", "matita", "quaderno"]
        