'''
Scrivi una funzione che determina se un numero è 'magico'. 
Un numero è considerato magico se è divisibile per 4 ma non per 6.
'''

# def numero_magico(num: int) -> bool:
#     if num % 4==0 and num % 6!=0:
#         return True
#     else:
#         return False

# print(numero_magico(8))



'''
Scrivi una funzione che prenda un dizionario e un valore, e 
ritorni la prima chiave che corrisponde a quel valore, o None 
se il valore non è presente.
'''
        
# def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
#     for keys,values in dizionario.items():
#         if values==valore:
#             return keys
        # else:
        #     return "None"



#print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))



'''
Scrivi una funzione che elimini dalla lista dati certi elementi 
specificati in un dizionario. Il dizionario contiene elementi da 
rimuovere come chiavi e il numero di volte che devono essere
rimossi come valori
'''

# def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
#     for keys,values in da_rimuovere.items():
#         while True:
#             k_num=keys in lista
#             if k_num==0:
#                 break          
#             if keys in lista:
#                 lista.remove(keys)
#                 return lista
            
#             # return keys
#             #if da_rimuovere.keys() in lista:
        
'definitivo'
# def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
#     counter=0

#     for keys,values in da_rimuovere.items():        
#         if keys in lista:
#             while counter<values:
#                 lista.remove(keys)
#                 counter+=1
#     return lista
        

# print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))







                                # '''
                                # Scrivi una funzione che prenda in input una lista di dizionari che 
                                # rappresentano voti di studenti e aggrega i voti per studente in un 
                                # nuovo dizionario.
                                # '''

                                # def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
                                #     for keys,values in voti:
                                #         return voti['nome'] 
                                        



                                # print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))















# '''
# Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e 
# restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo 
# superiore a 20, ma scontati del 10%.
# '''

# def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
#     counter=0
#     lung=len(prodotti)
#     print(lung)
    
#     while counter<lung:
#         for keys,values in prodotti.items():
        
#             if values>20:
#                 counter+=1
#         return values


# def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
#     counter=0
#     lung=len(prodotti)
#     prod_scont:dict={}
    

#     while counter<lung:

#         for keys,values in prodotti.items():
#             if values>20:
#                 counter+=1
#                 prod_scont[keys]=values
           
    
#     for keys,values in prod_scont.items():
#         scontato=values-(values*10/100)
#         prod_scont[keys]=scontato
#     return prod_scont   

# print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))






    
# def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
#     counter=0
#     lung=len(prodotti)
#     prod_scont:dict={}
#     contenitore=0
    

#     while counter<lung:

#         for keys,values in prodotti.items():
#             if values>20:
#                 counter+=1
#                 prod_scont[keys]=values
#             else:
#                 contenitore+=1
#                 if contenitore==lung:
#                     prodotti.clear()
#                     return prodotti

            
    
#     for keys,values in prod_scont.items():
#         scontato=values-(values*10/100)
#         prod_scont[keys]=scontato
#     return prod_scont   


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