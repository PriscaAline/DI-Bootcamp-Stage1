"""with open("secret.txt","a+") as fichier:
fichier.write("Sia \n")
fichier.write("Aline")
"""
f = open("secret.txt","r")
#print(f.read())
print(f.readline(4))

f.close()