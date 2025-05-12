sum=0
count=0
while True:
    #count<5
    numero=int(input("numero:"))
    if numero>0:
      sum+=numero
      count+=1
    elif numero<0:
       count+=1
    

print(sum)