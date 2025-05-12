class Media 

'''
attributi classe Media
self.title:str
self.year: str

'''

#inixializzare un oggetto classe media 
def __init__(self,title,year):
    self.setTitle(title)
    self.setYear(year)

#setter
def setTitle(self,title:str):
    if title:
        self.title=title
    else:
        print("errore")

def setYear(self,year:int):
    if year>1000:
        self.year=year
    else:
        print("error")

def __str__