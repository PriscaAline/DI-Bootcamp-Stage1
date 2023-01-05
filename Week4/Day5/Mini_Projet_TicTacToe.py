liste1=[
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
]

for elem in liste1:
    for val in elem:
        print("*", end="")
for truc in liste1:
    for fav in truc:
        if val==1:
            print("*")
        elif val==0:
            print("",)