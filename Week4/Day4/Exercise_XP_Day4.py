from random import *

#Exercise 1 : What Are You Learning?
"""
def display_message():
    print("J'apprends la partie sur les fonctions en python ")

display_message()"""


#Exercise 2 : What's Your Favorite Book
"""
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Les frasque d'Ebinto")
"""

#Exercise 3 : Some Geographie
"""
def describe_city(Ville,pays="Burkina Faso"):
    print(f"{Ville} is in {pays}")

describe_city("Bobo")
"""
#Exercise 4 : Random
"""
def aleatoire(nombre):
    a = randint(1,100)
    if nombre not in range(1,101):
        print("Vous devez appeler la fonction avec un nombre compris entre 1 et 100")
    elif a==nombre:
        print("Succès")
    else:
        print(f"Echec: Le nombre saisi est {nombre} et le nombre aleatoire est {a}")
"""

#Exercise 5 :

#Premiere et Deuxieme question
"""def make_shirt(size,text):
    print(f"The size of the shirt is {size} and the text is {text}")

#Troisieme question
make_shirt("M","Court")
"""
"""
#Quatrieme question
def make_shirt(size="XXL",text="J'aime Python"):
    print(f"The size of the shirt is {size} and the text is {text}")

#Cinquieme question
make_shirt("XL")

#Sixieme question
make_shirt("L")

#Septieme question
make_shirt("S","Taille quelconque")
"""

#Question huit
"""
def make_shirt(**kwargs):
    for key,value in kwargs.items():
        print(f"The size of the shirt is {key} and the text is {value}")
make_shirt(M="La meilleure taille")
"""
#Exercise 6 : Magicians...
"""
magicians = ["Harry Houdini", "David Blaine", "Criss Angel"]
print("Voici la liste des magiciens : \n")
def show_magicians(listes):
    for i in listes:
        print(i)

show_magicians(magicians)

print("\n*****************************************\n")

def make_great(liste_modifie):
    for i in range(len(liste_modifie)):
        liste_modifie[i]=liste_modifie[i] +" "+ "The Great"

make_great(magicians)
print("La liste modifier donne : \n")
show_magicians(magicians)
"""

#Exercise 7 : Temperature Advice
"""
def  gret_random_temp():
    a = randint(-10,40)
    print(a)

gret_random_temp()

def main():
    val=gret_random_temp()
    print(f"La temperature actuelle est : {val}")
    if val<0:
        print("Brr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    elif 0<=val<16:
        print("Assez froid ! N'oubliez pas votre manteau")
    elif 16<=val<=23:
        print("Moyenne,N'oubliez pas votre manteau")
    elif 24<=val<32:
        print("Pas mal ! Il se peut que vous n'aillez pas besoin de votre manteu aujourd'hui")
    elif 32<=val<=40:
        print("Vous devrez sortir sans votre manteau")
main()
"""
"""
#Question 4:
def gret_random_temp(saison):
    if saison=="hiver":
        print("La temperature est : ",randint(17,36))
    elif saison=="printemps":
        print("La temperature est : ",randint(24,40))
    elif saison=="automne":
        print("La temperature est : ",randint(20,36))
    elif saison=="été" or saison=="ete":
        print("La temperature est : ",randint(23,35))

saison1 = input("Entrez une saison : \n")
saison1=saison1.lower()

gret_random_temp(saison1)

#Question 5

print("La temperature actuelle sous forme de float est : ", float(randint(-10,40)))

print("\n**********************************************\n")

#Question 6 
mois=int(input("Entrez le numero du mois de l'année : \n"))

if mois==9 or mois==10 or mois==11:
     print("Nous sommes en AUTOMNE")
elif mois==12 or mois ==1:
    print("Nous sommes en HIVER")
elif mois==3 or mois ==4 or mois==5:
    print("Nous sommes en PRINTEMPS")
elif mois==6 or mois ==7 or mois==8:
    print("Nous sommes en ETE")
"""