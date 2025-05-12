max_posti=int(input("posti tot: "))

liberi=max_posti
# occupati=max_posti-liberi

#opzione=input("opzione(ingresso,uscita,stato): ").lower

while True:
    
    opzione=input("opzione(ingresso,uscita,stato): ")

    match opzione:

        case "prenota":
            if liberi>0:
                liberi-=1
            else:
                print("non ci sono posti disponibili")
    
        case "uscita":
            if liberi<max_posti:
                liberi+=1
            else:
                print("tutti i posti sono gia disponibili")

        case "stato":
            occupati=max_posti-liberi

            print(f"posi liberi: {liberi}, posti occupati: {occupati}")

        case "esci":            
                break

#devo aggiungere più versatilità su input(opzione) 