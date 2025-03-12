n_tudor=10
attesa=0
studente=input("nome studente: ")


if n_tudor>0:
    n_tudor-=1
    print("tutor assegnato con successo")

else:
    attesa+=1
    print("studente in attesa")

if n_tudor==0 and attesa>50:
    #fine
else:
    #torna a studente