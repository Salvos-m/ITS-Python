'''Write a function called city_country() that takes in the name of 
a city and its country. The function should return a string formatted 
like this: "Santiago, Chile". Call your function with at least three city-country pairs, 
and print the values that are returned.'''

# def city_country(**kwards):
#     for k, v in kwards.items():
#         print (f"{k} , {v}")

# print(city_country(roma="italy", porto="Portugal"))

# #da rivedere
# def city_country(city,cauntry):
#     for k, v in kwards.items():
#         return f"{k} , {v}"

# print(city_country(roma="italy", porto="Portugal"))

'''------------------------------------------'''

'def city_country(**kwargs): '#con i kwargs metto dizionari, quindi uso kay e value
    
#     eturn f"{kay},{value}"
#           "non vanno bene perchè nn li trova come valore quindi usare irerazione for"
# print(city_country(roma="italia",parigi="francia"))


    # for k,v in kwargs:      "non va bene perche è un dizionario e non ho usato .items"
    #     return f"{k},{v}"
    
'''    for k,v in kwargs.items():
        return f"{k},{v}"

print(city_country(roma="italy", porto="Portugal"))'''
#mi printa solo roma="italia, perchè?

'''------------------------------------------'''

def city_country(**kwargs):
  
  #while True:
      
    for k,v in kwargs.items():
        print(f"{k},{v}")
        return f"{k},{v}"
    

print(city_country(catania="sicilia",roma="lazio"))