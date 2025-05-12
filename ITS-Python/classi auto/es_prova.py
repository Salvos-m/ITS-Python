# class person:

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# alice= person("alice", 45)
# bob= person("bob", 36)

'''
Creare una classe Persona che abbia i seguenti attributi: 
nome, età, sesso. Aggiungi un metodo “presentati” che stampi 
una frase di presentazione della persona, ad esempio “Ciao, mi 
chiamo Marco e ho 32 anni”.

'''

class persona:

    def __init__(self,nome,età,sesso):
        self.nome=nome
        self.età=età
        self.sesso=sesso
    
    def presentati(self): #invece che (__init__) scrivere (felf)
        print(f"ciao, mi chiamo {self.nome} e ho {self.età}")

p = persona("Marco", 32, "maschio")
p.presentati()  
x= persona ("salvatore", 20, "maschio")
x.presentati()