'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''

def check_length(frase):
    if len(frase)>10:
        print(f"la lunghezza di {frase} è maggiore di 10")
    elif len(frase)==10:
        print(f"la lunghezza di {frase} è uguale a 10")
    else:
        print(f"la lunghezza di {frase} è minore di 10")