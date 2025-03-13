nome_corso=input("nome del corso: ")
max_posti=100

'''
opzioni=input("opzioni (iscrivi,visualizza,annulla,elimina,esci): ")

match opzioni:

    case "iscrivi":
        if max_posti>0:
            max_posti-=1
        else:
            print("non ci sono posti disponibili")
    
    case "annulla":
        if max_posti<100:
            max_posti+=1
        else:
            print("tutti i posti sono gia disponibili")
    
    case "visualizza":
        print(max_posti)
        print(100-max_posti)
    
    case "elimina":
        #non so come farlo tornare indietro
    
    case "esci":
        break
    # e come farlo stoppare
'''

while True:
    opzioni=input("opzioni (iscrivi,visualizza,annulla,elimina,esci): ")

    match opzioni:

        case "iscrivi":
            if max_posti>0:
                max_posti-=1
            else:
                print("non ci sono posti disponibili")
        
        case "annulla":
            if max_posti<100:
                max_posti+=1
            else:
                print("tutti i posti sono gia disponibili")
        
        case "visualizza":
            print(max_posti)
            print(100-max_posti)
        
        case "elimina":
            pass
                
        case "esci":
            break

