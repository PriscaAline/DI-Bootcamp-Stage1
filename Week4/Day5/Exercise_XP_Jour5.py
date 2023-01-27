def display_board(liste):
    a11 = liste[0][0]
    a12 = liste[0][1]
    a13 = liste[0][2]
    a21 = liste[1][0]
    a22 = liste[1][1]
    a23 = liste[1][2]
    a31 = liste[2][0]
    a32 = liste[2][1]
    a33 = liste[2][2]

    print(" *********************************** ")
    print(" *     "+a11+"   |      "+a12+"     |     "+a13+"    * ")
    print(" *   ------|------------|------    * ")
    print(" *     "+a21+"   |      "+a22+"     |     "+a23+"    * ")
    print(" *   ------|------------|------    * ")
    print(" *     "+a31+"   |      "+a32+"     |     "+a33+"    * ")
    print(" *********************************** ")
    
def player_input(liste, player1, player2):
    player = player1
    b = False 
    compteur = 1
    while compteur<=9 and b == False:
        print(f"{player}'s turn")
        row = int(input(" Enter the row :"))
        coloumn = int(input(" Enter the column:"))
        position = list(range(1,4))
        if not row in position or not coloumn in position:
            compteur=compteur
            print("Row or coloumn does not exist\n")
            player=player
            pass
        else:
            row-=1
            coloumn-=1 
            if compteur%2!=0:
                if liste[row][coloumn]!= " ":
                    compteur=compteur
                    print("Impossible: position already occupied \n")
                    player=player
                else:
                    liste[row][coloumn]="x"
                    display_board(liste)
                    print("\n")
                    b = check_win(liste,compteur,player)
                    compteur+=1   
                    player=player2    
            else:
                if liste[row][coloumn]!= " ":
                    compteur=compteur
                    print("Impossible: position already occupied\n")
                    player=player
                else:
                    liste[row][coloumn]="o"
                    display_board(liste)
                    print("\n")
                    b = check_win(liste,compteur,player)
                    compteur+=1
                    player=player1        
def check_win(liste, n, player):
    if n >= 5 and n <= 9 :
        if liste[0][0]==liste[0][1] and liste[0][0]==liste[0][2]:
            if liste[0][0]=="x" or  liste[0][0]=="o" :
                print(f"The winner is {player}")
                return True
            else:
                return False
        elif liste[1][0]==liste[1][1] and liste[1][0]==liste[1][2]:
            if liste[1][0]=="x" or  liste[1][0]=="o":
                print(f"The winner is {player}")
                return True
            else:
                return False
        elif liste[2][0]==liste[2][1] and liste[2][0]==liste[2][2]:
            if liste[2][0]=="x" or  liste[2][0]=="o":
                print(f"The winner is {player}")
                return True
            else:
                return False
        elif liste[0][0]==liste[1][1] and liste[0][0]==liste[2][2]:
            if liste[0][0]=="x" or  liste[0][0]=="o":
                print(f"The winner is {player}")
                return True
            else:
                return False
        elif liste[0][2]==liste[1][1] and liste[0][2]==liste[2][0]:
            if liste[0][2]=="x" or  liste[0][2]=="o":
                print(f"The winner is {player}")
                return True
            else:
                return False
        elif liste[0][0]==liste[1][0] and liste[0][0]==liste[2][0]:
            if liste[0][0]=="x" or  liste[0][0]=="o":
                print(f"The winner is {player}")
                return True
            else:
                return False
        elif liste[0][1]==liste[1][1] and liste[0][1]==liste[2][1]:
            if liste[0][1]=="x" or  liste[0][1]=="o":
                print(f"The winner is {player}")
                return True
            else:
                return False
        elif liste[0][2]==liste[1][2] and liste[0][2]==liste[2][2]:
            if liste[0][2]=="x" or  liste[0][2]=="o":
                print(f"The winner is {player}")
                return True
            else:
                return False
        else:
            if n==9 :
                print("No winner : both players are tied ")
                return False 
            else:
                return False
    else:
        return False
def play():
    liste = [[" "," "," "],[" "," "," "],[" "," "," "]]
    player1 = input("\nPlayer n°1 please enter your name : ")
    player2 = input("Player n°2 please enter your name  : ")
    print("\n")
    display_board(liste)
    player_input(liste, player1.lower(), player2.lower())       

play()