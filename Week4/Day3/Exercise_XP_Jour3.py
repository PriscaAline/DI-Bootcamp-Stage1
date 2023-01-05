#Exercise 1 : Convert Lists Into Dictionaries
"""
keys=["Ten", "Twenty","Thirty"]
values=[10, 20, 30]
dictionnaire={}
for item in zip(keys,values):
    dictionnaire.update({item[0]:item[1]})
"""

#Exercise 2 : Cinemax
"""
family = {"rick": 43, "beth": 13, "morty": 5, "summer":8}
som=0
for key,value in family.items():
    if value<3:
        som+=0
        print(f"{key} pour vous c'est gratuit")
    elif 3<=value<=12:
        prix=10
        som+=10
        print(f"{key} vous payez {prix}$")
    elif value>12:
        prix=15
        som+=15
        print(f"{key} vous payez {prix}$")

print("Le prix total pour la familles est : ", som)

print("\n*****************************************************\n")
family_dico = {}
nombre = int(input("Entrez le nombre de personnes : "))
for i in range(1, nombre+1):
    nom = input(f"Entrez le {i} nom : ")
    age = int(input("Entrez son age : "))
    family_dico[nom.lower()] = age

print("\n", family_dico)
"""

#Exercise 3 : Zara
"""
brand = {"name": "Zara", "creation_date": 1975, "creator_name": "Amancio Ortega Gaona", "type_of_clothes": ["men", "women", "children", "home"], "international_competitors": ["Gap", "H&M", "Benetton"], "numbers_stores": 7000, "major_color":{"France": "blue", "Spain": "red", "US": ["pink", "green"]}}

brand["numbers_stores"]=2

print("\n")
print("Les clients de Zara sont : ")
for elem in brand["type_of_clothes"]:
    print(elem)

brand.update({"country_creation": "Spain"})

if "international_competitors" in brand.keys():
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]


print("Le dernier concurant internationnal est : ", brand["international_competitors"][-1])

print("\n")

print("Les principales couleurs aux US sont : ")
for val in brand["major_color"]["US"]:
    print(val)

print("\n")

print("La longueur du dictionnaire est : ", len(brand))

print("\n")

print("Les cles du dictionnaire sont : ")
for key in brand.keys():
    print(key)


more_one_zara = {"creation_date": 1975, "numbers_stores": 10000}

brand.update(more_one_zara)

print("\n")

print("La valeur de la clé number_stores est : ", brand["numbers_stores"])
"""

# Exercise 4 : Disney Characters
"""
print("\n")
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A ={}
disney_users_B ={}
disney_users_C ={}

for elem in zip(users, range(len(users))):
    disney_users_A[elem[0]] = elem[1]
print(disney_users_A)

print("\n************************************************** \n")
for elem in zip(range(len(users)), users):
    disney_users_B[elem[0]] = elem[1]
print(disney_users_B)

print("\n*******************************************\n")

users.sort()
for elem in zip(users, range(len(users))):
    disney_users_C[elem[0]] = elem[1]
print(disney_users_C)
print("\n**************************************************************\n")

disney_users_A2 = {} 
liste=[]
for elem in users :
    if not "i" in elem:
        pass
    else:
        liste.append(elem)

for val in zip(liste, range(len(liste))):
    disney_users_A2[val[0]] = val[1]

print(disney_users_A2)

print("\n**************************************************************\n")

disney_users_A3 = {}       
liste2=[]
for elem in users :
    elem=elem.lower()
    if "m" in elem:
        liste2.append(elem)
    elif "p" in elem:
        liste2.append(elem)

for val in zip(liste2, range(len(liste2))):
    disney_users_A3[val[0]] = val[1]

print(disney_users_A3)
"""
