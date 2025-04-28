from forma_generica import Formagenerica

class Rettangolo(Formagenerica):

    #inizializzare un oggetto della classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape("rettangolo")

    def draw(self)-> None:

        print(f"\n{self.getShape()}\n")
        #outed for
        for i in range(5):
            #inner for
            for j in range(5*2):

                #lato a , d
                if i==0 or i==5-1:
                    print("*", end=" ")

                #lato b, c
                elif j==0 or j==(5*2)-1:
                    print("*", end=" ")
                
                #spazzi biachi
                else:
                    print(" ", end=" ")
            print("\n", end=" ")
