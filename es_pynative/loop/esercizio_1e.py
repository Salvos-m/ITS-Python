'''
Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python code to 
return their product only if the product is equal to 
or lower than 1000. Otherwise, return their sum.
'''


#n1=int(input("inaerisci numero:"))
#n2=int(input("inaerisci numero:"))

#def calcoli(n1:int,n2:int): #-> int
#    numeri=(n1,n2)
 #   match numeri:
  #      case numeri if n1*n2<=1000:
   #         print("il risultato e'" + (n1*n2))
    #    case numeri if n1*n2>1000:
     #       print("il risultato e'"+(n1+n2) )
      #return calcoli
#non va bene, e' troppo lunga e l'ho resa piu' complicata 
# penso che sia proprio scritta male se come funzione

#versione normale
'''
n1=int(input("inaerisci numero:"))
n2=int(input("inaerisci numero:"))

numeri=(n1,n2)
match numeri:
 case numeri if n1*n2<=1000:
  moltiplicazione=n1*n2
  print(f"il risultato {moltiplicazione}")
 case numeri if n1*n2>1000:
  somma=n1+n2
  print(f"il risultato {somma}")
'''

#versine con funzione
'''
def multiply_or_sum(a, b):
    product = a * b
    if product <= 1000:
        return product
    else:
        return a + b
print(f"il risultato e' {multiply_or_sum(20, 30)}")
print(f"il risultato e' {multiply_or_sum(50, 30)}")
'''
 #invece che il print nele funzioni usare il return per tutti i valori da voler "salvare"


#con valore input
'''
def multiply_or_sum(a, b):
    product = a * b
    if product <= 1000:
        return product
    else:
        return a + b

#questi vanno fuori dalla funzione,  
# Get user input                           
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

#creo il valore delle variabili e poi chiamo la funzione

# Call the function and print the result
result = multiply_or_sum(a, b)
print(f"The result is: {result}")
'''
#soluzione sito 
def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)