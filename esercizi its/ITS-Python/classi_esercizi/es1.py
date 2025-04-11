'''
9-1. Restaurant: Make a class called Restaurant. 
The __init__() method for Restaurant should store two attributes: 
a restaurant_name and a cuisine_type. Make a method called 
describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating 
that the restaurant is open. Make an instance called restaurant from 
your class. Print the two attributes individually, 
and then call both methods.
'''

class Restaurant:
    def __init__(self,restaurant_name:str,cuisine_type:str,booleano:bool):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.booleano=booleano
    
    def describe_restaurant(self):
        print(f"il {self.restaurant_name} è un ristorante storico, \n situato al centro che serve cucina {self.cuisine_type}")

    def open_restaurant(self):
        if self.booleano==True:
            print ("il ristorante è aperto")
        else:
            print("il ristorante è chiuso")

    #def reviews(self):




Ristorante_1=Restaurant("Da Giggi","italiana",True)
print(Ristorante_1.describe_restaurant())
print(Ristorante_1.open_restaurant())

print("----------------")

Ristorante_2=Restaurant("Idilili","Indiana",False)
print(Ristorante_2.describe_restaurant())
print(Ristorante_2.open_restaurant())

print("----------------")

Ristorante_3=Restaurant("Oldy","Americana",False)
print(Ristorante_3.describe_restaurant())
print(Ristorante_3.open_restaurant())