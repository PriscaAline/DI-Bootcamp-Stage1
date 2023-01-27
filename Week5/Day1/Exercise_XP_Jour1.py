import copy

#Exercise 1 : Cats
"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Milou",12)
cat2 = Cat("Rek",23)
cat3 = Cat( "Mome",10)

def ancien_chat(args):
    i = args[0].name
    ancien=args[0].age
    for value in args:
        if value.age>ancien:
            ancien=value.age
            i=value.name
    return i,ancien
liste=[cat1,cat2,cat3]
nom,age=ancien_chat(liste)
print(f"The oldest cat is {nom} and is {age} years old")
"""
#Exercise 2 : Dogs
"""
class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm de high!") 

davids_dog = Dog("Rex",50)
print(f"THis dog's name is {davids_dog.name} and his height is {davids_dog.height }cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"His dog's name is {sarahs_dog.name} and his height is {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height>sarahs_dog.height:
    print(f"The biggest dog is {davids_dog.name}")
else:
    print(f"The biggest dog is {sarahs_dog.name}")
"""
    
#Exercise 3 : Who's The Song Producer?
"""
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for element in self.lyrics:
            print(element)
            
stairway = Song(["There's a lady who's sure", "all that glitter is gold", "and she's buying a stairway to heaven"])

Song.sing_me_a_song(stairway)
"""

#Exercise 4 : Afternoon At The Zoo
"""
class Zoo():
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.liste_global = {}
    def add_animal(self, new_animal):
        while not new_animal in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        for animal in self.animals:
            print(animal)
        print("***************************************")
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            pass
    def sort_animals(self):
        self.animals.sort()
        liste_global = {}
        for i in self.animals:
            if i[0] in self.liste_global.keys():
                self.liste_global[i[0]].append(i)
            else:
               self.liste_global[i[0]]=[i]
        for val in self.liste_global.values():
            if len(val)==1:
                val=" ".join(val)
    def get_groups(self):
        travail=self.liste_global
        for value in travail.values():
            value=" ".join(value)
            value=value.replace(" ",",")
            print(value)     

ramat_gan_safari = Zoo("La decouverte")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Emu")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
"""