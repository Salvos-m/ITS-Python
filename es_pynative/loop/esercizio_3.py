'''
Write a Python code to accept a string from the 
user and display characters present at an even index number.
'''
frase="prisencolinesanciusol"
x=len(frase)

for x in frase:
    if len(frase)%2==0:
        print(frase[x])
