import string


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

print("La matrix : ")

for elem in liste:
    chaine="".join(elem)
    print(chaine)
print("****************************\n")

chaine = ["7","t","h","i","s","$","#","^","i","s","%"," ","M","a","t","r","3","i","x","#"," "," ","%","!"]  


i = 0 
j = len(chaine)-1
while(i < j ):
    if((chaine[i].isalpha() == False) and chaine[i] != " " ):
        
        if( (chaine[i+1].isalpha()) and chaine[i+1] != " "):
            del chaine[i] 
            i = 0 
            j = len(chaine)-1
          
        else:
            chaine[i]=" " 
            i = i + 1
    else:
        i = i+1
    
if(chaine[len(chaine)-1].isalpha): 
    chaine[len(chaine)-1] = " "
    
 
i = 0 
j = len(chaine)-1
while(i < j ):
    if(chaine[i] == " "  and chaine[i+1] == " " ): 
        del chaine[i] 
        i = 0  
        j = len(chaine)-1
    else:
        i = i + 1 

mot = "".join(chaine)

print("Apres decriptage de la matrice le resultat obtenu est le suivant : ",mot)





