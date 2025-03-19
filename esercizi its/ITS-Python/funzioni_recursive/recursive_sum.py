# metodo iterativo
'''
def sum(n:int)->None:
    if n<0:
        print("errore")
        return None
    else:
        sum=0
        while n:
            sum= sum +n
            n=n-1
        return int(sum)

sum(5)
'''

# metodo ricorsivo

def recur_sum(n:int)->None:
    #casso di interruzione
    if n<0:
        print("errore")
        return None
    
    elif n==0:
        return 0
    
    else:
        return int(n+recur_sum(n-1))

recur_sum(0)