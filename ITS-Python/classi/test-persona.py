'''
#dal file persona.py importa la classe Persona
from persona import Persona

#creare un oggetto di tipo persona
sm:Persona=Persona("Salvatore","mancuso", 20)

print(sm)

print(sm.nome,sm.cognome,sm.eta)'
'''

#dal file persona2.py importa la classe Persona
from persona2 import Persona

sm:Persona=Persona()

#vogli richiamare la funzione display_data 
sm.display_data()

# impostare nome della persona sm
sm.setName("salvatore")

print("-----------")
sm.display_data()

