'''
Scrivere un programma in Python che memorizzi il nome, il ruolo e 
l'età di un utente in un dizionario. Il nome, il ruolo e l'età devono 
essere inseriti in input dall'utente stesso. Il programma deve determinare 
il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"

Expected Output:

Digitare nome dell'utente: Mario Rossi
Digitare ruolo dell'utente: admin
Digitare l'età dell'utente: 30
Output: Accesso completo a tutte le funzionalità.
'''

nome=input("nome utente:")
ruolo=input("ruolo utente:").strip().lower()
eta=input("età utente")
utente={ruolo:eta}
ruoli=["Admin","Moderatore","Utente","Ospite"]

match utente:
    case utente if utente[ruolo]=="Admin":
        print("Accesso completo a tutte le funzionalità.")
    case utente if utente[ruolo]=="Moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni.")
    case utente if utente[ruolo]=="Utente" and utente[eta]>=18:
        print("Accesso standard a tutti i servizi.")
    case utente if utente[ruolo]=="Utente" and utente[eta]<=18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case utente if utente[ruolo]=="Ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case utente if utente[ruolo] not in ruoli:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")
    
    
