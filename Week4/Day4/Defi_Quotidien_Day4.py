import string

alphabet = list(string.ascii_lowercase)

liste = [["7", "i", "3"],
         ["T", "S", "i"],
         ["h", "%", "x"],
         ["i", " ", "#"],
         ["s", "M", " "],
         ["$", "a", " "],
         ["#", "t", "%"],
         ["^", "r", "!"]
        ]

print("****************************\n")

for elem in liste:
    chaine="".join(elem)
    print(chaine)
print("****************************\n")
stocke=[]
liste1=[]
liste2=[]
liste3=[]

for i in range(3):
    for j in range(8):
        liste1.append(liste[j][i])
    """liste1.append(liste[i][0])
    if not liste1 in stocke:
        stocke.append(liste1)
    liste2.append(liste[i][1])
    if not liste2 in stocke:
        stocke.append(liste2)
    liste3.append(liste[i][2])
    if not liste3 in stocke:
        stocke.append(liste3)"""

print(liste1)
print("********************************************************\n")
result=[]
for i in range(len(stocke)):
    servir=stocke[i]
    for val in servir:
        result.append(val)
        
print(result)
print("********************************************************\n")

chaine1="".join(result)
print(chaine1)

"""while i<len(chaine1):
    if not chaine[i] in alphabet and chaine[i+1] in alphabet:
        chaine.remove(chaine[i])
    elif not chaine[i] in alphabet and not chaine[i+1] in alphabet:
  """
""" 
for i in range(len(result)):
    if not result[i] in alphabet and result[i+1] in alphabet:
        result.remove(result[i])
    elif result[i-1] in alphabet and result[i+1] in alphabet:
        result.remove(result[i])

print(result)"""
            