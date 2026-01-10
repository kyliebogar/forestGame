#builder 
#Shows user character options
#gabriela: base code
#kylie:fixing it to fit other file 

def picker():
    print(" a. (.-.) b. (._.) c. (o o) d. (* *) e. (: :) f. (-_-)")
    print("    (   )     / \\     /( )\\     /|\\     /[ ]\\    /[ ]\\")
    print("     L L      | |       !        ^        +       ( )")

    playerinput =""

    ans = ["a","b","c","d","e","f","A","B","C","D","E","F"]
    correct = False
    while correct==False:
        playerinput =input("Please Select Your Character:")
        if playerinput in ans:
            correct = True
        else:
            print("No, stop that. Try again.")
            

    #Prints character when user selects one
    if playerinput == "a":
        lst = ["(.-.)\n(   )\n L L", "LeFou"]
        print(lst[0])
        print("You selected: LeFou")
        return lst
    

    elif playerinput == "b":
        lst=["(._.)\n / \\\n | |","Madame Shenzi"]
        print(lst[0])
        print("You selected: Madame Shenzi")
        return lst

    elif playerinput == "c":
        lst=["(o o)\n/( )\\ \n  !", "Oogie Boogie"]
        print(lst[0])
        print("You selected: Oogie Boogie")
        return lst
        

    elif playerinput == "d":
        lst =["(* *)\n /|\\\n  ^ ", "Professor Morgana"]
        print(lst[0])
        print("You selected: Professor Morgana")
        return lst


    elif playerinput == "e":
        lst = ["(: :)\n/[ ]\\\n  + ", "Uncle Ugo"]
        print(lst[0])
        print("You selected: Uncle Ugo")
        return lst

        
    elif playerinput == "f":
        lst = ["(-_-)\n/[ ]\\\n ( ) ", "Sir Randall"]
        print(lst[0])
        print("You selected: Sir Randall")
        return lst


#Random number generator to assign character's weakness
import random
def setWeakness():
    lst = ["smell", "asthma","allergy"]
    a=random.randint(0,2)
    return(lst[a])


def setStrength():
    a=random.randint(1,50)
    return(a)

###calls function and prints it on the screen for user
##print("Your Strength is:")
##print(setStrength())

###calls function and prints it on the screen for user
##print("Your weakness is:")
##print(setWeakness())
##
##lst = picker()
##print(lst)
