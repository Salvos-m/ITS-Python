
# def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
#     for keys,values in dizionario.items():
#         if values==valore:
#             return keys
#         # else:
#         #     return "None"
        



# print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
# print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 300))
# print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))



# def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
#     counter=0

#     for keys,values in da_rimuovere.items():        
#         if keys in lista:
#             while counter<values:
#                 lista.remove(keys)
#                 counter+=1
#     return lista
        

# print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))






#da rivedere ex n4 collection pasq
'''
Scrivi una funzione che prenda in input una lista di dizionari che 
rappresentano voti di studenti e aggrega i voti per studente in un 
nuovo dizionario.
'''

# def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
#     for keys,values in voti:
#         return voti['nome'] 

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    risultato={}
    for x in voti:
        nome= voto["voto"]
         



# print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))


'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e 
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo 
superiore a 20, ma scontati del 10%.
'''

# def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
#     counter=0
#     lung=len(prodotti)
#     prod_scont:dict={}
#     vuoto:dict={}

#     while counter<lung:

#         for keys,values in prodotti.items():
#             if values>20:
#                 counter+=1
#                 prod_scont[keys]=values
                
#     for keys,values in prod_scont.items():
#         scontato=values-(values*10/100)
#         prod_scont[keys]=scontato
#     return prod_scont  


''' 
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    counter=0
    lung=len(prodotti)
    prod_scont:dict={}
    contenitore=0
    print(lung)
    
    

    while counter<lung:

        for keys,values in prodotti.items():
            if values>20:
                print(f"{values} ..")
                counter+=1
                prod_scont[keys]=values
            elif values<=20:
                contenitore+=1
                print(contenitore)
                print(values)
                if contenitore==lung:
                    prodotti.clear()
                    return prodotti

            
    
    for keys,values in prod_scont.items():
        scontato=values-(values*10/100)
        prod_scont[keys]=scontato
    return prod_scont   
    



# print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
# print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
print(filtra_e_mappa({'Lampada': 35.0, 'Libro': 19.0}))
# print(filtra_e_mappa({'zappa': 22.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
'''



'''

PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, 
e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe 
restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, 
il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da 
aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

'''

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    dizionario:dict={}
    dizionario["profille"]=name
    dizionario["email"]=email
    dizionario["telefono"]=telefono
    return dizionario


def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    
    if name==None:
        pass
    else:
        dictionary["profille"]=name 

    if email==None:
        pass
    else:
        dictionary["email"]=email

    if telefono==None:
        pass
    else:
        dictionary["telefono"]=telefono

    for keys,values in dictionary.items():
        dictionary.update({keys:values})
        return dictionary


contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))