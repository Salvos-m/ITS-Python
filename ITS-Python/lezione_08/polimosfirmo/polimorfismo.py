from per_2 import Persona
from alieno import Alieno 

# creare un oggetto p della classe Persona
p:Persona=Persona("salvatore","mancuso", 20)

# visualizzare info sulla persona
# print(p)

# oggetto Alieno
et:Alieno=Alieno("andromeda")

#info su Alieno et
print(et)

#invoca metodo speak() da p
p.speak()

#invoca metodo speak() da et
et.speak()
