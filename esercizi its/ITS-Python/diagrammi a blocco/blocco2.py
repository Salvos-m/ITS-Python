#numero=input("numero: ")
counter=0
n_max=0

while counter<4:
    numero=int(input("numero: "))
    counter+=1
    if numero>n_max:
        n_max=numero
    

print(n_max)