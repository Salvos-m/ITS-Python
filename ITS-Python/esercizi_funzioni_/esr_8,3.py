'''Write a function called make_shirt() that accepts a size and the text of a message 
that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and 
the message printed on it.

Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.'''

def make_shirt(size:int,text:str):
    print(f"la maglietta sarà una taglia {size} con su scritto \"{text}\"")

make_shirt(5,"i love NY")
make_shirt(text="i love NY",size=5)
 