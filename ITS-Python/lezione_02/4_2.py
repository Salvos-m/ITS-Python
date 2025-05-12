#4.2
'''
Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such a
  s A dog would make a great pet.
• Add a line at the end of your program, stating what these animals 
  have in common. You could print a sentence, such as Any of these animals would make a great pet!
'''

#
dizionario:dict={"cane": "il {} è il migliore amico dell'uomo", 
                 "Gatto": "al {} piace stare per i fatti suoi", 
                 "Furetto": "il {} è un animale domenstico insolito"}

for animale, frase in dizionario.items():
    frase_completa = frase.format(animale)
    print(frase_completa)

