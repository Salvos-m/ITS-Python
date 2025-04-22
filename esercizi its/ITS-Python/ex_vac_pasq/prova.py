
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

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    for keys,values in voti:
        return voti['nome'] 
         



print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))