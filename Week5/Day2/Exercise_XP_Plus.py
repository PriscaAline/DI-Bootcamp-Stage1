#Exercise 1:
"""
class Family():
    def __init__(self, membres = [{'name':'Michael','age':'35','gender':'Male','is_child':False}, {'name':'Sarah','age':'32','gender':'Female','is_child':False}], nom_de_famille = " Zara"):
        self.membres = membres
        self.nom_de_famille = nom_de_famille
    def born(self, **kwargs):
        self.membres.append(kwargs)
        print("Felicitation à la famille")
    def is_18(self, other_name):
        for personne in self.membres:
            if personne['name'] == other_name:
                if personne['age']==18:
                    return True
                else:
                    return False
    def family_presentation(self):
        for elements in self.membres:
            print(f"{self.nom_de_famille}  {elements['name']}")
print("*********************************************************\n")
"""
#Exercise 2 :
"""
class TheIncredibles(Family):
    def __init__(self, membres =  [{'name':'Michael','age':'35','gender':'Male','is_child':False,'power':'fly','incredible_name':'MikeFly'}, {'name':'Sarah','age':'32','gender':'Female','is_child':False,'power':'read minds','incredible_name':'SuperWoman'}], nom_de_famille = " Zara"):
        super().__init__(membres,nom_de_famille)
        self.membres = membres
    def use_power(self):
        try:
            for personne in self.membres:
                if personne['age']>18:
                    print(f"The power of {personne['name']} is {personne['power']}")
        except:
            print(f"{personne['name']} are not over 18 years old")
    def incredible_presentation(self):
        self.family_presentation()
        for individu in self.membres:
            print(f"The power of {individu['name']} is {individu['power']}")

testons = TheIncredibles()
testons.incredible_presentation()
testons.born(name='Jack',age='4',gender='Male',is_child='True',power='Puissance Inconnue',incredible_name='')
testons.incredible_presentation()
"""