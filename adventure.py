##Gabriela, Bernie, Kylie
#Feb 12 2024
#Final Project
#driver

## import files needed

import gamePlay
import builder
import time
import graphicsfunctions  
## player class to auto generate new character stats
class Player():
    
    def __init__(self):
        #call characterization file for name, strength, weakness, char
        temp = builder.picker()
        self.name = temp[1] 
        self.strength = builder.setStrength()
        self.weakness = builder.setWeakness()
        self.char = temp[0]
        self.health = 100
        self.obj = []
        self.enemy = []
        self.friend = []
        self.fingies = 20
        self.contract = False
   
    def marriage(self):
        self.contract = True
    def married(self):
        return self.contract
        
    ## enemies   
    def addEnemy(self,name):
        self.enemy.append(name)
    def findEnemy(self,name):
        if name in self.enemy:
            return True
        else:
            return False
    def printEnemy(self):
        if self.enemy == []:
            print("No enemies... for now")
        else:
            print("Enemies:")
            for i in self.enemy:
                print(i)
            print()
    def removeEnemy(self,name): ##be careful not to send a non enemy 
        self.enemy.remove(name)
        

    ## friends   
    def addFriend(self,name):
        self.friend.append(name)
    def findFriend(self,name):
        if name in self.friend:
            return True
        else:
            return False
    def printFriend(self):
        if self.friend == []:
            print( "You have no friends :(")
        else:
            print("Friends:")
            for i in self.friend:
                print(i)
            print()
    def removeFriend(self,name): 
        self.friend.remove(name)


    ## objects in inventory
    def addObj(self,name):
        self.obj.append(name)
        
    def findObj(self,name):
        if name in self.obj:
            return True
        else:
            return False
    def removeObj(self,name):
        try: 
            self.obj.remove(name)
        except:
            return None 
    def inventory(self):
        if self.obj == []:
            print( "There is nothing in your inventory yet...")
        else:
            print("Inventory:")
            for i in self.obj:
                print(i)
            print()
    
    def reset(self):
        self.health = 100
        if "sword" in self.obj:
            self.strength -=10
        self.obj = []
        self.enemy = []
        self.friend = []
        self.fingies = 20
        self.contract = False
        
    ## strengths + weaknesses
                
    def getWeakness(self):
        return self.weakness
    def getStrength(self):
        return self.strength    
    def changeStrength(self, num):
        self.strength += num
    def getHealth(self):
        return self.health
    def setHealth(self,num):
        self.health = num
    def takeFinger(self):
        self.fingies -=1
        
    #print stats 
    def stats(self):
        print(self.char, "\nName:", self.name,"\nStrength: "+str(self.strength))
        print("Weakness: "+self.weakness+"\nFingers and toes: ",str(self.fingies))
        print()
        self.printEnemy()
        print()
        self.printFriend()
        print()
        self.inventory()
        print()
        
## end of player class 

#############################################################################
#                           GAME START                                      #
#############################################################################


restart = "yes"
while restart == "yes" :
    input("Welcome to our game! This is a text-based adventure game."
         +" Please follow directions and use only the given options when answe"
          +"ring questions. Press enter to proceed to character select.\n")

    person = Player()
    playAgain = "yes"
    
    while playAgain == "yes":
        time.sleep(1)
        person.stats()
        print("You have selected your character and received your strength "
          +"and weakness! Are you ready?")
        choice = gamePlay.yesOrNo()
        if choice == "yes":
            print("Lets go!!")
        else:
            print("That's tough. too bad!!")
        time.sleep(1)

        rah = gamePlay.intro(person)
        if rah:
            playAgain = "no"
            print("you won!!")
        else:
            print(person.getHealth())
            person.stats()
            person.reset()
            input("press enter to continue")
    
    #end inner game loop
    if person.married():
        print("\nSuddenly, the Egg Goblin reappears, holding the flower you gave to it!"
              +" It professes its love to you, and you get married on the mountaintop."
              +" Congratulations to the happy couple <3!")
        graphicsfunctions.egggoblingraphic()
        time.sleep(2)
    print("here are your final stats!!")
    person.stats()
    print("Do you want to play again?")  
    restart = gamePlay.yesOrNo()
    
    #end outer game loop
    
print("thanks for playing!")
