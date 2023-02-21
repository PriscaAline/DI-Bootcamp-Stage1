#Exercise : Pets
"""
class Pets():
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass

cat1=Bengal("Tipso",5)
cat2=Chartreux("Rex",5)
cat3=Siamese("Milou",3)
all_cats =[cat1, cat2, cat3]
sara_pets = Pets(all_cats)
sara_pets.walk()
"""
#Exercise 2 : Dogs
"""
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight   
    def bark(self):
        return f"{self.name} barks"
    def run_speed(self):
        return self.weight/(self.age*10)
    def fight(self, other_dog ):
        if (self.run_speed()*self.age) > (other_dog.run_speed()*other_dog.age):
            return f"The winning dog is : {self.name}"
        elif (self.run_speed()*self.age) < (other_dog.run_speed()*other_dog.age):
            return f"The winning dog is : {other_dog.name}"
        else:
            return f"The two dogs are equal"     

dog1=Dog("Milou", 10, 50)
dog2=Dog("Bobe", 10, 10)
dog3=Dog("Tapse", 6, 25)

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())
print(dog1.fight(dog2))
"""
#Exercise 3 :
"""Voir Exercise3.py"""
