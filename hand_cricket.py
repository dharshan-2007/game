import random
def cricket():
    add=0
    while True:
        res=int(input("Enter the number:"))
        if(res>6):
            print("Not applicable:")
            exit()
        sc=random.randint(1,6)
        print("computers number:",sc)
        if(sc==res):
            return add
        else:
            add+=res
        

print("1. head")
print("2. Tails")
ch=int(input("Choose Head or Tails (1 or 2):"))
if(not(1,2)):
    print("Not valid option")
    exit()
a=(ch==random.randint(1,2))
if(a):
    print("You have won the toss")
    print("1. Batting")
    print("2. Bowling")
    role=int(input("Enter the choice (1 or 2):"))
    choice=(role-1)
else:
    print("You have lost the toss")
    choice=random.randint(0,1)
    if(choice==0):
        print("Computer has chosen bowling")
    else:
        print("Computer has chosen batting")
if (choice==0):
    print("\t\t----Batting----")
    print("Enter number 1 to 6")
    bat=cricket()
    print("Your total:",bat)
    print("\t\t----Bowling----")
    print("Enter number 1 to 6")
    bowl=cricket()
    print("Computer's total:",bowl)
    if(bat<bowl):
        print(f"you have lost by {bowl-bat} runs")
    elif(bat==bowl):
        print("Match has been drawn")
    else:
        print(f"you have won by {bat-bowl} runs")

else:
    print("\t\t----Bowling----")
    print("Enter number 1 to 6")
    bat=cricket()
    print("Computer's total:",bat)
    print("\t\t----Batting----")
    print("Enter number 1 to 6")
    bowl=cricket()
    print("Your total:",bowl)
    if(bat<bowl):
        print(f"you have won by {bowl-bat} runs")
    elif(bat==bowl):
        print("Match has been drawn")
    else:
        print(f"you have lost by {bat-bowl} runs")

