soglia=int(input("valore soglia: "))

count=0
while True:
    numero=int(input("valore numero: "))
    if numero>soglia:
        print("il numero è maggiore")
        count+=1
    else:
        count+=1
    
    if count==7:
        break