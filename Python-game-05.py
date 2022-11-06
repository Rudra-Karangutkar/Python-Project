import random
from xml.etree.ElementTree import TreeBuilder
def game(comp, you):
    if comp == you :
        return None
    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False
    elif comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True
    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False

ran = random.randint(1, 3)
#print(ran)
if ran == 1:
    comp = "r"
elif ran == 2:
    comp = "p"
elif ran == 3:
    comp = "s"
you = input("Your Turn: Rock(r) , Paper(p) and Scissor(s):\n")

a = game(comp, you)
print(f"computer choose {comp}")
print(F"You choose {you}")
if a == None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")