'''Creare una classe Animale che abbia gli attributi 
“nome” e “specie”. Aggiungi un metodo “emetti_suono” che stampi 
un suono specifico per ogni specie. Ad esempio, se l’animale è un 
gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.
'''

class animale:

    def __init__(self,nome,spece):
        self.nome=nome
        self.spece=spece
    
    def emetti_suono(self):
        
        match self.spece:

            case "cane":
                print("bau")
            case "gatto":
                print("miaoo")
            case "mucca":
                print("muuu")
            case _:
                print("suono sconosciuto")

              
a=animale("rex","cane")
b=animale("tigo","gatto")
c=animale("geltrude","mucca")
d=animale("coco","coccodrillo")
a.emetti_suono()
b.emetti_suono()
c.emetti_suono()
d.emetti_suono()