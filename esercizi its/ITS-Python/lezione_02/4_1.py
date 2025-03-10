
#4.1
'''
-Think of at least three kinds of your favorite pizza. 
Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, 
  instead of printing just the name of the pizza. For each pizza, you should 
  have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states 
  how much you like pizza. The output should consist of three or more lines 
  about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
'''

#prima parte
pizze:list=["Rossa", "Margherita", "Boscaiola base rossa", "Parmigiana"]

print("le pizze sono: ")
for x in pizze:
    print(f"Pizza {x} ")

print("\n")

#seconda parte
for x in pizze:
    print(f"La pizza preferita di Luigi è la pizza {x} ")

print("\n")

#terza parte
print("La pizza è uno dei \nmiei piatti preferiti \nAmo la Boscaiola base rossa! ")