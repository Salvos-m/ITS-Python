#2.3
'''Personal Message: Use a variable to represent a person’s name, 
and print a message to that person. Your message should be simple, 
such as, “Hello Eric, would you like to learn some Python today?”'''

'''
nome="Antonio"
print(f"Ciao {nome}, sei pronto a studiare python?")
'''

#2.4
''' Name Cases: Use a variable to represent a person’s name, 
and then print that person’s name in lowercase, uppercase, 
and title case.'''

'''
nome="Antonio"
print(nome.upper())
print(nome.lower())
print(nome.title())
'''

#2.5
''' Famous Quote: Find a quote from a famous person you admire. 
Print the quote and the name of its author. Your output should 
look something like the following, including the 
quotation marks: Albert Einstein once said, “A person who never 
made a mistake never tried anything new.”'''

'''
quote="be water my frend"
name="bruce lee"

print(f"{name} disse \"{quote}")
'''

#2.6
''' Famous Quote 2: Repeat Exercise 2-5, but this time, represent 
the famous person’s name using a variable called famous_person. 
Then compose your message and represent it with a new variable 
called message. Print your message. '''

'''
quote="be water my frend"
famous_person="bruce lee"
message = f"{name} disse \"{quote}"

print(message)
'''

#3.1
'''Names: Store the names of a few of your friends in a list 
called names. Print each person’s name by accessing each 
element in the list, one at a time.'''

'''
names=["Leonardo","Marco","Gabriele"]

print(names)
print(names[0])
print(names[1])
print(names[2])
print(f"{names[0]},{names[1]},{names[2]}")

for n in names:
    print(n)
'''

#3.2
''' Greetings: Start with the list you used in Exercise 3-1, 
but instead of just printing each person’s name, print a 
message to them. The text of each message should be the same, 
but each message should be personalized with the person’s name.'''

'''
names=["Leonardo","Marco","Gabriele"]

for n in names:
    print(f"{n} sei fortissimo!!")
'''

#3.3
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


