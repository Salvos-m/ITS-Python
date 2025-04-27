# def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
#     counter=0
#     lung=len(prodotti)
#     prod_scont:dict={}
#     contenitore=0
#     print(lung)
    
    

#     while counter<lung:

#         for keys,values in prodotti.items():
#             if values>20:
#                 print(f"{values} ..")
#                 counter+=1
#                 prod_scont[keys]=values
#             elif values<=20:
#                 contenitore+=1
#                 print(contenitore)
#                 print(values)
#                 if contenitore==lung:
#                     prodotti.clear()
#                     return prodotti

            
    
#     for keys,values in prod_scont.items():
#         scontato=values-(values*10/100)
#         prod_scont[keys]=scontato
#     return prod_scont   
    



# print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
# print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) #print(filtra_e_mappa({'Lampada': 35.0, 'Libro': 19.0}))
# print(filtra_e_mappa({'zappa': 22.0, 'Zaino': 50.0, 'Quaderno': 22.0}))


def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    counter=0
    lung=len(prodotti)
    print(f"{lung} n. elementi nel dict prodotti")
    prod_scont:dict={}
    contenitore=0

    while counter<lung:

        #visione prezzi
        for keys,values in prodotti.items():
            print(f"{values} valore entrato")

            if values>20:
                print(f"{values} valore entrato >")
                counter+=1
                prod_scont[keys]=values #aggiungo item in prod_scont:dict
            
            elif values<=20:
                print(f"{values} valore entrato <")
                counter+=1
                contenitore+=1
                # va qui?
                if contenitore==lung:
                    prodotti.clear()
                    return prodotti

    #sconto
    for keys,values in prod_scont.items():
        scontato=values-(values*10/100)
        prod_scont[keys]=scontato
    return prod_scont   

print(filtra_e_mappa({'Lampada': 35.0, 'Libro': 19.0}))

