#Exercise 1 : Cats
"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Premier chat",12)
print(cat1.name)

cat2 = Cat("Deuxieme chat",23)
print(cat2.name)

cat3 = Cat( "Troisieme chat",10)
print(cat3.name)

def ancien_chat(chat1, chat2, chat3):
    dico_chat = {chat1.name:chat1.age, chat2.name:chat2.age, chat3.name:chat3.age}
    i = 0
    for key,value in dico_chat.items():
        if value>i:
            i=value
    print(f"Le chat le plus age est : {key}, et age est : {i}")

ancien_chat (cat1, cat2, cat3)
"""

#Exercise 2 : Dogs

class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(self.name)

    def jump(self):
        print(f"{self.name} saute {self.height} en cm de haut! .  x is {self.height}*2 ") 

davids_dog = Dog("Rex",50)

print(f"Le nom du chien est  {davids_dog.name} et sa taille  {davids_dog.height }cm")

davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)



