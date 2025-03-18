'''
Creare una classe Automobile che abbia gli attributi 
“marca”, “modello” e “anno”. Aggiungi un metodo “descrivi” 
che stampi una descrizione dell’automobile, ad esempio 
“Questa è una Toyota Corolla del 2017”.
'''

class automobile:

    def __init__(self,marca,modello,anno):
        self.marca=marca
        self.modello=modello
        self.anno=anno
    
    def descrivi(self):
        print (f"questa è una {self.marca} {self.modello} del {self.anno}")

x= automobile("fiat","panda",2021)
x.descrivi()