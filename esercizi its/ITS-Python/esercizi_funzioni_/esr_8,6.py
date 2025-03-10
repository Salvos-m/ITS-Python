'''Write a function called city_country() that takes in the name of 
a city and its country. The function should return a string formatted 
like this: "Santiago, Chile". Call your function with at least three city-country pairs, 
and print the values that are returned.'''

def city_country(**kwards):
    for k, v in kwards.items():
        print (f"{k} , {v}")

print(city_country(roma="italy", porto="Portugal"))

#da rivedere
def city_country(city,cauntry):
    for k, v in kwards.items():
        return f"{k} , {v}"

print(city_country(roma="italy", porto="Portugal"))