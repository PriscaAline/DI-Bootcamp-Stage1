#Exercise 1 : Set
"""my_fav_numbers={2,3,4,7,48,56,63}
my_fav_numbers.add(12)
my_fav_numbers.add(72)
my_fav_numbers.remove(63)
friend_fav_numbers={23,67,2,90,56,25}
our_fav_numbers = friend_fav_numbers|my_fav_numbers"""

print("\n\n**********************************************************\n\n")

#Exercise 2 :
"""Il nest pas possible d'ajouter plus d'entier car les elements d'un tuple ne sont 
pas modifiable"""

print("\n\n**********************************************************\n\n")

#Exercise 3 : List
"""basket = ["Banana",      "Apples", "Oranges", "Bleueberries"]
basket.remove("Banana")
basket.remove("Bleueberries")
basket.append("Kiwi")
basket[0]="Apples"
nombr = basket.count("Apples")
basket.clear()"""

print("\n\n**********************************************************\n\n")

#Exercise 4 : Floats

#Première question:
"""Les floats sont des variables de types flotantes

La difference est que les floates sont utilées pour saisie des element a valeur flottantes
par contre les entiers sont utilisés pour des saisie des valeurs entières
"""
"""
ma_Liste = []
for valeur in range(1,6):
    if valeur==1:
        ma_Liste.append(valeur+0.5)
    elif valeur!=1:
        ma_Liste.append(valeur)
        ma_Liste.append(valeur+0.5)
print(ma_Liste)

"""

print("\n\n**********************************************************\n\n")

#Exercise 5 :
"""for elem in range(1,22):
    if (elem-1)%2==0 and (elem-1):
        print(elem)"""

print("\n\n**********************************************************\n\n")

#Exexcise 6 :While Loop Instructions
"""nom="aline prisca"
saisie = input("Entrez votre prénom(s) svp : ")
while nom!=saisie.lower():
    saisie = input("Entrez votre prénom(s) svp : ")"""


#Exercise 7 : Favorite Fruits Instructions
"""print("NB: Si vous avez plusieurs fruits préférés a chaque fruit saisie veuillez laisser un seul espace entre vos fruits\n")

fruit = input("Entrez maintenant tout en tenant compte de nos critère signifier ci dessus votre ou vos fruit(s) préféré(s) : ")
fruit = fruit.lower()
liste_fruit = fruit.split(" ")

print("\n\n")

fruit_second = input("Veullez entrer le nom d'un fruit :")
if fruit_second.lower() in liste_fruit:
    print("\nVous avez choisi l'un de nos fruits préférés !")
else:
    print("\nVous avez choisi un nouveau fruit. J'espere que tu apprécies")"""

print("\n\n**********************************************************\n\n")

#Exercise 8 : Who Ordered A Pizza?
"""liste_graniture=[]
while 1:
    graniture = input("\nVeuillez Entré une serie de granitures de pizza : ")
    
    if graniture=="quitter":
        break

    else:
        print("Nous ajouterons cette graniture à votre pizza")
        liste_graniture.append(graniture)

print("\nLes differentes granitures et leurs prix sont:\n")
for val in liste_graniture:
    print(f"{val} : 10+2.5")"""


#Exercise 9 : Cinemax
"""liste_cine=[]
nombre=int(input("Entrez le nombre de personne qui veulent un billet : "))

for val in range(1,(nombre+1)):
    age=int(input(f"Entrez l'age de la {val} personne : "))

    if age<3:
        liste_cine.append(0)
    elif 3<=age<=12:
        liste_cine.append(10)
    else:
        liste_cine.append(15)

somme=0
for elem in liste_cine:
    somme=somme+elem
print(f"Le coût total de tous les billets de la famille est : {somme}$")"""

print("\n\n**********************************************************\n")
#Question 4
"""liste_nom=[]
liste_age=[]
ado_nombre=int(input("Nombre d'adolescent : " ))

for ado in range(ado_nombre):
    nom=input("Entrez votre nom :")
    nom=nom.lower()
    age=int(input("Entrez votre âge : "))
    if age<16 or age>21:
        pass
    elif 16<=age<=21:
        liste_nom.append(nom)
        liste_age.append(age)

print(f"La liste finale des personnes autorisées pour le film sont :")
for person in liste_nom:
    print(person)"""

print("\n\n**********************************************************\n")

#Exercise 10 : Sandwich Orders
"""sandwich_orders = ["Tuna sandwich", "Avocate sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwich = []
for plat in (sandwich_orders):
    finished_sandwich.append(plat)

for nourit in (finished_sandwich):
    print(f"I made your {nourit}")


#Exercise 11 : Sandwich Orders#2

print("L'épicerie est a court de Pastrami sandwich")
for i in range(4):
    sandwich_orders.append("Pastrami sandwich")

for i in range(len(sandwich_orders)):
    if "Pastrami sandwich" in sandwich_orders:
        sandwich_orders.remove("Pastrami sandwich")

for plat in (sandwich_orders):
    finished_sandwich.append(plat)

print("\n\n******************************************************************")
print("La liste finale des sandwich préparés sont :")
for nour in finished_sandwich:
    if "Pastrami sandwich" in finished_sandwich:
        finished_sandwich.remove("Pastrami sandwich")
    print(nour)
"""