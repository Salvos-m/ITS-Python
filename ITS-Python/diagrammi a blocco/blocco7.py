pari=0
dispari=0
count=0

while count<10:
    numero=int(input("inserisci numero:"))
    if numero%2==0:
        pari+=1
        count+=1
    else:
        dispari+=1
        count+=1

print(pari)
print(dispari)