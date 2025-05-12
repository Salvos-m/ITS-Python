3.3
''' Your Own List: Think of your favorite mode of transportation, 
such as a motorcycle or a car, and make a list that stores several 
examples. Use your list to print a series of statements about 
these items, such as “I would like to own a Honda motorcycle.”'''

#da rivedere (soluzione palt. pro.)
'''
veicle=["moto","auto","bici"]
messages: list = ["Come {v} vorrei una Yamaha R1", "L' {v} è comoda d'inverno", "La {v} mi porta a quando andavo alle elementari"]

for index in range(0, len(veicle), 2): 

    print(messages[index].format(v=veicle[index]))
'''

#mia soluzione
'''
 for n in veicle:
     if n==(veicle[0]):
         print(f"come {n} vorrei una yamaha r1")

     elif n==(veicle[1]):
         print(f"L'{n} è comoda d'inverno")
    
     else:
         print(f"la {veicle[2]} mi riporta a qunado andavo all'elementari" )
'''

