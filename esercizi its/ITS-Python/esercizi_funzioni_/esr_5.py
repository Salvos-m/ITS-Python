'''
Write a function add_one(). It takes an integer as argument. The function adds 1 to the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.

Example:
add_one_to_list([1, 2, 3])
>>> [2, 3, 4]
'''

def add_one(numero:int):
    return numero+1

def add_one_to_list(lista:int):
    new_list=[]
    for item in lista:
        new_list.append(add_one(item))
    return new_list

print(add_one(5))

lista=[1,2,3,4,5]

print(add_one_to_list(lista))

# alternativamente
nuovaLista = add_one_to_list(lista)
print(nuovaLista)
'''
def add_one_to_list(lista:int):
    new_list=[]
    for x in lista:
        new_list.append(add_one)
    print(new_list)
'''

