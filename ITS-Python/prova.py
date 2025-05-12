#1-10 20-37 45-59
'''
sum:int = 0
for i in range(1, 11):
    sum+=1
    print("la somma e'" sum)'''

'''
def somma(a:int,b:int):
    sum:int=0
    for i in range(a,b+1):
        sum+=1
    return sum

print(f"la somma dei numeri tra a e b è {somma(1,10)}")
'''

def sottrazione(a:int,b:int):
    sot=0
    if a>b:
        sot==a-b
    else:
        sot==b-a
    return sot

print(f"il risultato è {sottrazione(int(input("inserisci:")),int(input("inserisci:")))}")

#doppio risultato
# define a function returning multiple values(returning a tuple)
def operations(a: int, b: int) -> tuple[int, int]:
 sum_result:int = a + b
 diff_result:int = a – b
  # Returns a tuple with two values
 return sum_result, diff_result

# Assigns values to two variables
sum_value, diff_value = operations(10, 5)
print("Sum:", sum_value) # Output: Sum: 15
print("Difference:", diff_value) # Output: Difference: 5
print(type(operations(10,5)))


ciao= "domodossola" \
      2.34 

print(ciao)