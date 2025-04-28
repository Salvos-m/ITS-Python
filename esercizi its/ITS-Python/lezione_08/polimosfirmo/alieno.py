class Alieno:

    '''
    ci serve sapere la galassia di provenienza:
    self-galaxy:str
    '''
    #inizializzare oggetto classe alieno
    def __init__(self,galaxy:str):

        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy:str)-> None:
        if galaxy:
            self.galaxy=galaxy
        else:
            print("errore la galassia non ce")

    def getGalaxy(self)->str:
        return self.galaxy
    
    def speak(self)->None:
        print("jnjbgvnbirbngfikn")

    def __str__(self):
        return f"\n Allieno viene da {self.galaxy}"