#Exercise 3 : Dogs Domesticated
"""
import random
from  Exercise_XP  import Dog as mp
class PetDog(mp):
    def __init__(self,name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        print(self.bark())
        self.trained = True
    def play(self, *args):
        liste=[]
        for dog in args:
            liste.append(dog.name)
        liste=" ".join(liste)
        liste=liste.replace(" ",",")
        print(f"{liste} all play together")#A revoir
    def do_a_trick(self):
        if self.trained==True:
            liste = [self.name+" "+"does a barrel roll", self.name+" "+"stands on his back legs", self.name+" "+"shakes your hand", self.name+" "+"plays dead"]
            random.shuffle(liste)
            sortons = random.choice(liste)
            print(sortons)
        else:
            print("This dog is not trained")
"""