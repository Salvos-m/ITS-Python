'''Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5'''

def check_value(number):
    if number>5:
        print("il numero è maggiore di 5")
    elif number==5:
        print("il numero è uguale a 5")
    else:
        print("il numero è minore di 5")