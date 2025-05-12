'''
Creare una classe Impiegato che abbia gli attributi 
“nome”, “cognome”, “matricola” e “stipendio”. Aggiungere un metodo 
“aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% 
e un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, 
ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.
'''

class impiegato:

    def __init__(self,nome,cognome,matricola,stipendio):
        self.nome=nome
        self.cognome=cognome
        self.matricola=matricola
        self.stipendio=stipendio

    def aumenta_stipendio(self):
        self.stipendio+= (self.stipendio/10)
    
    def stampa_dettagli(self):
        print(f"Impiegato: {self.nome} {self.cognome},matricola: {self.matricola}, stipendio: {self.stipendio}")
        print(self.stipendio)

x=impiegato("salvatore","mancuso", 646454, 100000)
x.aumenta_stipendio()
x.stampa_dettagli()

y=impiegato("salvatore","mancuso", 646454, 100000)
# y.aumenta_stipendio()
y.stampa_dettagli()

