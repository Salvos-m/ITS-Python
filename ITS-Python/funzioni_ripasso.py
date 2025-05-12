class Libro:
    def __init__(self):
        self.titolo:str=""
        self.autore:str=""
        self.genere:list[str]=[]
    
    #per dare valore
    def set_autore(self,nome_autore:str):
        self.autore=nome_autore

    def set_titolo(self,nome_autore:str):
        self.titolo=nomtitolo

    def set_autore(self,nome_autore:str):
        self.titolo=nome_autore

    def 

    class Biblioteca:
        def __init__(self):
            self.libri:list[Libro]=[]

        def set_libro(self, libro:Libro):
            self.libri.append(libro)
        
        def get_libro_òtitolo(self)->str:
            for item in self.libri:
                return item.get_titolo()

piccolo_principe:Libro=Libro()
piccolo_principe.set_titolo("piccolo principe")
