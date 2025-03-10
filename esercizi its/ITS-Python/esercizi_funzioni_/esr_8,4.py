'''Modify the make_shirt() function so that shirts are large by default 
with a message that reads I love Python. Make a large shirt and a 
medium shirt with the default message, and a shirt of any size with 
a different message.'''

def make_shirt(size:str="large",text:str="i love python"):
    #size=="large" , text=="i love python"
    print(f"la maglietta sarà una taglia {size} con su scritto \"{text}\"")

make_shirt()
make_shirt("mediun")
make_shirt("extrasmall","i love NY")