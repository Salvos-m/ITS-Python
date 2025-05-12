
#iterazione
'''
def sum_in_range(a:int,b:int):
    if a>b:
        temp:int=a
        a=b=temp
    
    sum:int=0
    while b>=a:
        sum=sum+b
        b=b-1
    
    return int(sum)
'''
#recursione

#caso semplice 
def sum_in_ramge(a:int,b:int)->int:
    if a>b:
        temp:int=a
        a=b=temp
        #a,b=b,a (un altro modo di scriverlo)

    if b == a:        #non uso elif per separle (per me a livello logico)
        return int(a)

    else:
        return int(b + sum_in_ramge(a, b-1))

print(sum_in_ramge(4,6))