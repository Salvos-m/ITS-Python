'''
numero=int(input("inserire numero: "))
if numero%1==0 and numero>0:
    fattoriale=1
    i=1
    if i==numero:
        print(f"{numero} è fattoriale")
    else:
        fattoriale*=i
        i+=1
else:
    print("il numero deve essere intero e positivo")
'''
#vome faccio a farli "tornare indietro" e non capisco problema contatore

#numero=int(input("inserire numero: "))

while True:
    numero=int(input("inserire numero: "))

    if numero%1==0 and numero>0:
        break

