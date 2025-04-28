#classe capace di creare forme geometriche

from abc import ABC, abstractmethod

#una classa astratta è astratta se ha almeno un metodo astratto

class Formagenerica(ABC):#cosi dico che la classe generica è astratta
    
    @abstractmethod #decoretor, indica che il metodo è astratto
    def draw(self)->None:
        pass

    def setShape(self, shape:str)-> None:
        if shape:
            self.shape=shape
        else:
            print("Errore, shape non puo essere una stringa vuota")

    def getShape(self)->None:
        return self.shape