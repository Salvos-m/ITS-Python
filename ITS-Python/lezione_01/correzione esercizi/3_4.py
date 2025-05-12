
#3.4
'''Guest List: If you could invite anyone, living or deceased, to dinner, 
who would you invite? Make a list that includes at least three people 
you’d like to invite to dinner. Then use your list to print a message 
to each person, inviting them to dinner.'''


#da rivedere (soluzione palt. pro.)
'''
veicle=["moto","auto","bici"]
messages: list = ["Come {v} vorrei una Yamaha R1", "L' {v} è comoda d'inverno", "La {v} mi porta a quando andavo alle elementari"]

for index in range(0, len(veicle), 2): 

    print(messages[index].format(v=veicle[index]))
'''
guest:list=["Bruce Lee","Lady D","Frank Sinatra"]
messages:list=["Sarei onorato di avere a cena il maestro {g}","Buongiono {g} gradirei il piacere di ospitarla a cena", "Grande {g} venerdi sera da me?"]

for t in range(len(guest)):
    print(messages[t].format(g=guest[t]))

#for t in range(len(guest)):

