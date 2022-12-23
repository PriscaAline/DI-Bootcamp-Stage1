import random
#Premiere partie
chaine = input("Entrez une chaine de 10 caracteres :")
if len(chaine)<10:
    print("Chaine pas assez longue")
elif len(chaine)>10:
    print("Chaine trop longue")


#Deuxieme partie
premier=chaine[0]
second=chaine[-1]
print(f" la première lettre de ta chaine est : <{premier}>, et la dernière lettre est : <{second}>")


#Troisieme partie
for j in range(len(chaine)+1):
    resultat=chaine[0:j]
    print(f"{resultat}")


#Quatrieme partie
ma_Liste=list(chaine)
random.shuffle(ma_Liste)
result= "".join(ma_Liste)
print(f" la chaine melangée est : {result}")