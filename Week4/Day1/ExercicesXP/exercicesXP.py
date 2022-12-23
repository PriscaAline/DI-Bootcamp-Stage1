#Exercise 1: Hello world
print("Hello world\nHello world\nHello world\nHello world\n")


#Exercise 2: Some Math
puissance = (99**3)*8
print(puissance)


#Exercise 3: What Is The Output?
print("Predisons le resultat des extraits de code suivants :")
>>> 5<3 
False

>>> 3==3 
True

>>> 3=='3' 
False

>>> '3'>3 
Erreur

>>> 'Hello'=='hello'
False



#Exercise 4 : Your Computer Brand
computer_brand ="HP"
print(f"I have a {computer_brand} computer")


#Exercise 5 : Your Information
name = "Aline Prisca Sia"
age = 23
shoe_size = 38
info =f"Je me nome {name} j'ai' {age} ans, ma pointure est le {shoe_size}"
print(info)


#Exercise 6 : A & B
a = 72
b = 34
if a>b:
    print("Hello world\nHello world\nHello world\nHello world\n")


#Exercise 7 : Odd Or Even
valeur = int(input("Entrez un nombre :"))
if valeur%2==0:
    print("Le nombre saisi est un nombre pair")
else:
    print("Le nombre saisi est impair")


#Exercise 8: What Your Name?
nom = "aline prisca"
user = input("Entrez votre prénom(s) svp :")
if nom == user.lower():
    print("Je suis toute heureuse vous êtes mon homonyme je m'appelle également Aline Prisca. Enchanté de faire votre connaissance")
else:
    print("Dommage vous portez pas le même prénom(s) que moi, neamoins Vous avez un tres beau prenom(s). Bisous a la prochaine ")


#Exercise 9 : Tall Enough To Ride A Roller Coaster
pouces =float(input("Entrez votre taile en pouces : "))
pouces = pouces*(2.54)
if pouces>145:
    print("Vous êtes assez grand pour rouler")
else:
    print("Vous devrez grandir un peu plus pour rouler")