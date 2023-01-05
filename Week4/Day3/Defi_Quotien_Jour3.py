#Defi 1
"""mot = input(" Entrez un mot : ")
mot=mot.lower()
liste2=[]
dico={}

for i in range(len(mot)):
    c=mot[i]
    listevar=[]
    if not c in liste2:
        liste2.append(c)
        for j in range(i,len(mot)):
            if c==mot[j]:
                listevar.append(j)
        dico[c]=listevar
print("\n")
print(dico)"""

#Defi 2
"""
liste=[]
articles={
    "Apple": 4,
    "Honey": 3,
    "Fan": 14,
    "Bananas": 4,
    "Pan": 100,
    "Spoon":2
}

wallet = int(input("Entrez la somme que vous poseder : "))

for key,value in articles.items():
    if (wallet>=value):
        liste.append(key)
print(articles)
print(sorted(liste))
"""
