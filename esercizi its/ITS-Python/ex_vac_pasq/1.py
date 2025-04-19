'''

Scrivere il frammento di codice che cambi il valore intero memorizzato 
nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

'''

# def transform(x: int) -> int:
#     if x%2==0:
#         print(int(x/2))
#     else:
#         print(int(x*3-1))
    
# transform(4)
# transform(5)
# transform(-5)

# def transform(x: int) -> int:
#     if x%2==0:
#         return int(x/2)
#     else:
#         return int(x*3-1)
    
# print (transform(4))
# print (transform(5))
# print (transform(-5))



'''
Sviluppare una funzione in Python per calcolare lo stipendio lordo di 
ciascuno dei diversi impiegati. L'azienda paga 10 dollari all'ora per le 
prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte 
le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato 
durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare 
e stampare lo stipendio lordo.
'''

# def calcola_stipendio(ore_lavorate: int) -> float:
#     if ore_lavorate <=40:
#         return ore_lavorate*10
#     else:
#         x=ore_lavorate-40
#         return 400+ x*15

# print(calcola_stipendio(10))
# print(calcola_stipendio(0))
# print(calcola_stipendio(40))
# print(calcola_stipendio(50))


'''

Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51

'''

# def print_seq(valore:str):
#     # valore=valore.lower

#     match valore:
#         case "a":
#             for x in range(7):
#                 return x 
            
# print(print_seq(0))




# def print_seq(): 
    
#     print("Sequenza a):")
#     for x in range(1,8):
#             print(x)
#     print(" ")
#     print("Sequenza b):")
#     for x in range(3,28,5):
#             print(x)
#     print(" ")
#     print("Sequenza c):")
#     for x in range(20,-16,-6):
#             print(x)
#     print(" ")
#     print("Sequenza d):")
#     for x in range(19,59,8):
#             print(x)
    

# print_seq()


'''
Scrivere una funzione chiamata integerPower che, dati in input una base 
e un esponente, restituisca il risultato della potenza base^exponent. 
Supporre che base sia un numero intero e che l'esponente sia un valore 
intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!
'''

# def integerPower(base:int,esponente:int)->int:
#     if esponente <=0:
#         return
    
#     risultato=base**(esponente)
#     integerPower(base,esponente-1)
#     return risultato

# print(integerPower(3, 4))



'''
Definire una funzione chiamata hypotenuse che calcoli la lunghezza 
dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere 
due argomenti di tipo float (corrispondenti ai due lati del triangolo) 
e restituire l'ipotenusa come un float.


Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora
'''