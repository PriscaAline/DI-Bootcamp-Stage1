import copy
"""class Farm():
    liste = []
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.height = 0
        self.animal = "" 
        print(f"{farm_name}'s farm\n")
    def add_animal(self, animal_name, nombre = 2):
        if not animal_name in self.liste:
            self.animal = animal_name
            self.height = nombre
            self.liste.append(self.animal)
            print(f"{animal_name} : {self.height}") 
    def get_info(self):
        return f"{' '+' '+' '+'E-I-E-I-O!'}"
    def get_animal_types(self):
        self.liste.sort()
        return self.liste
    def get_short_info(self):
        self.get_animal_types()
        rempl=copy.deepcopy(self.liste)
        rempl=" ".join(rempl)
        rempl=rempl.replace(" ",",")
        print(f"La ferme {self.farm_name} possèdes des : {rempl} ")
        
macdonald = Farm("McDonald")
macdonald.add_animal("cow",5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(f"{macdonald.get_info()}")
print(macdonald.get_animal_types())
macdonald.get_short_info()
"""