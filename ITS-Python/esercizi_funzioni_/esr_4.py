'''Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.'''

lista=[1,2,3,4,5,6,7,]

def check_list(lista):
    for x in lista:
        if x>5:
          print("il numero è maggiore di 5")
        elif x==5:
          print("il numero è uguale a 5")
        else:
          print("il numero è minore di 5")

#lista=[1,2,3,4,5,6,7,]

print(check_list(lista))
