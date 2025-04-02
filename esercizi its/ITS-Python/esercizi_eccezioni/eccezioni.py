'''
Safe Square Root: Write a function safe_sqrt(number) that calculates the square root 
of a number using math.sqrt(). Handle ValueError if the input is negative by returning 
an informative message.
'''
import math

def safe_sqrt(number:int):
    try:
        #numero=int(input("inserisci un numero: "))
        radice=math.sqrt(number)
        print(f"la radice quadrata di {number} è {radice}")
    except ValueError as NumeroNegativo:
        print("il numero deve essere positivo")
        #if number<=0:
            # print("ValueError il numero deve essere positivo")

safe_sqrt(10)
safe_sqrt(-10)
safe_sqrt(100)