##Gabriela, Bernie, Kylie
#Feb 12 2024
#Final Project 
#this file holds most of the fuctions that run the game

## imports
import time
import graphicsfunctions
import random

## answer keys
answer_yes = ["Yes","yes","y","Y"]
answer_no = ["No","no","N","n"]
ansLeft =["Left","left","L","l"]
ansRight =["Right","right", "r","R"]
ansYodel = ["Yodel","yodel","y","Y"]
ansRun =["run","Run","r","R"]
ansHide = ["hide","Hide","h","H"]
ansSword = ["sword", "Sword", "S", "s"]
ansPerf = ["perfume","Perfume" ,"P","p"]
ansRiddle = ["riddle","Riddle","R","r"]
ansFlower = ["Flower","flower","f","F"]
ansCan = ["Can","can","C","c"]
ansWalk = ["Walk","walk","w","W"]
ansClimb =["climb","Climb","C","c"]
ansMoo = ["Moo","moo","m","M"]
ansHello = ["Hello","hello","H","h"]

## fighting function, takes person obj, and the enemies hp+attack and the phrases said when hit 
def fight(person, eHP, eAttack, enemy1,enemy2):
    hp = person.getHealth()
    attack = person.getStrength()

    while hp > 0 and eHP > 0:
        hp -= eAttack
        print(enemy1)
        time.sleep(2)
        eHP -= attack
        print(enemy2)
        time.sleep(2)
    #you win 
    if hp > 0:
        person.setHealth(hp)
        return False
    #you lose
    else: 
        return True

    
###############################################################################################    
##                                      input checks                                         ##      
###############################################################################################    
def helloYodelMoo():
    ans = input("Hello, moo, or yodel: ")
    if ans in ansMoo:
        return "moo"
    elif ans in ansHello:
        return "hello"
    elif ans in ansYodel:
        return "yodel"
    print("That was actually not an option!! Try again.")
    return helloYodelMoo()

    
def climbOrWalk():
    ans = input("... ")
    if ans in ansClimb:
        return "climb"
    elif ans in ansWalk:
        return "walk"
    print("That was actually not an option!! Try again.")
    return climbOrWalk()


def flowerOrCan(person):
    ans = input("Give the flower or trash? (trash/flower) ")
    if ans in ansCan:
        print("You fed them the trash.")
        person.removeObj("trash")
    elif ans in ansFlower:
        print("You fed them the flower.")
        flowergraphic()
        person.removeObj("flower")
    else:
        print("That was not an option!! Try again.")
        return flowerOrCan(person)
    
def flowerOrRiddle(person):
    ans = input("Give the flower or answer the riddle? (riddle/flower) ")
    if ans in ansRiddle:
        return "riddle"
    elif ans in ansFlower:
        graphicsfunctions.flowergraphic()
        person.removeObj("flower")
        return "rizz"
    else:
        print("That was not an option!! Try again.")
        return flowerOrRiddle(person)
    
def numChoice(num):
    ans = input("Please type the number of the option you would like: ")
    try:
        ans = int(ans)
    except:
        print("Please enter a number from 1 to " +str(num)+".")
        return numChoice(num)
    found = False 
    for x in range(num):
        if x+1 == ans:
            found = True
    if found:
        return ans
    print("That was actually not an option!! Try again.")
    return numChoice(num)
    
def runHideYodel():
    ans = input("What do you do: run, hide, or yodel? ")
    if ans in ansYodel:
        return "yodel"
    elif ans in ansRun:
        return "run"
    elif ans in ansHide:
        return "hide"
    print("That was actually not an option!! Try again.")
    return runHideYodel()

def leftOrRight():
    ans = input("Right or Left? ")
    if ans in ansLeft:
        return "left"
    elif ans in ansRight:
        return "right"
    print("That was actually not an option!! Try again.")
    return leftOrRight()

def swordOrPerf(person):
    ans = input("Will you take the sword or the perfume? ")
    if ans in ansSword:
        person.addObj("sword")
        person.changeStrength(10)
    elif ans in ansPerf:
        person.addObj("perfume")
    else:
        print("That was not an option!! Try again.")
        return swordOrPerf()

def yesOrNo():
    ans = input("Yes or no? ")
    if ans in answer_yes:
        return "yes"
    elif ans in answer_no:
        return "no"
    print("That was not an option!! Try again.")
    return yesOrNo()



###############################################################################################    
##                                      end games                                            ##      
###############################################################################################
def gameOver():
    print("You died! Try again??")
    if yesOrNo() =="no":
        print("Too bad. You play until you win :)")
    print("\n\n Here are your stats:\n(any changes that happened during the game will be reset)\n")
    return False

def topMtn(person):
    print("\nYou have reached the top of the mountain! You find the chest and open it. It is a participation trophy!!!!!!!!"
          +"Thanks for participating!!!!!!!")
    graphicsfunctions.trophygraphic()
    return True

###############################################################################################    
##                                      Event Start                                         ##      
###############################################################################################

def intro(person):
    print("\nYour adventure starts in the forest. There are two paths in "
            +"front of you. You look down the path to your left; it is thick "
            +"with trees but you can see something shiny on the ground ahead. Yo"
            +"u look down the path to your right; there are very few trees, and"
            +"beyond them, you can see bright colors. Which path do you take?")
    choice = leftOrRight()
    if choice == "left":
        graphicsfunctions.treesgraphic()
        return bear(person)
    else:
        graphicsfunctions.fieldgraphic()
        return flowerfield(person)

###############################################################################################    
##                                      Scary Path                                          ##      
###############################################################################################

#run, hide, yodel with the bear 
def bear(person):
    print("\n\nYou start walking down the path to your left…")
    time.sleep(2)
    print("\nYou realize the shiny item on the ground is a bear trap. "
        + "Oh no! You take a few more steps before hearing a growl behind "
        + "you. A bear!")
    time.sleep(2)
    graphicsfunctions.beargraphic()
    time.sleep(1)
    choice = runHideYodel()

    #if statements 
    if choice == "run":
        print("You start running, but not fast enough. The bear catches up to you "
              + "and eats you. Womp womp.")
        return gameOver()

    #start hide statemnets
    elif choice == "hide":
        print("\nYou look around for places to hide. You see 1. a bush, 2. a hol"
              +"low log, 3. a climbable tree, and 4. a cave. Where do you go?")
        choice = numChoice(4)

        #hide in a bush
        if choice == 1:
            if person.getWeakness() == "allergy":
                print("\nYou chose to hide in the bush. Unfortunately, due to"
                      +" your allergies, this causes a very"
                      +" uncomfortable death.")
                return gameOver()
            else:
                print("\nYou chose to hide in the bush. The bear did not find "
                      +"you, so after a few minutes, you get up and keep wal"
                      +"king down the path. You are so happy you got away th"
                      +"at you start yodeling as you walk")
                time.sleep(2)
                return NPC(person)

        #hollow log
        elif choice == 2:
            print("\nYou chose to hide inside the hollow log. You stuck your "
                  +"head inside and were immediately met by an "
                  +"angry family of raccoons. You die of rabies. Womp womp.")
            return gameOver()
        #a tree 
        elif choice == 3:
            print("\nYou choose to hide up the climbable tree. You cli"
                  +"mb and climb and climb until you ultima"
                  +"tely reach a beehive. They start swarming and yo"
                  +"u fall backward out of the tree.")
            return gameOver()
        #cave 
        else:
            time.sleep(1)
            return cave(person)
    #end hide if statemnts
        
    else:
        print("\nYou turn around to face the bear. You don’t know what"
             +" else to do, so you start yodeling. Surprisingly, the"
             +" bear enjoys your music so much he falls asleep to it!"
             +" Once he starts snoring, you feel safe to keep walking.")
        time.sleep(2)
        return NPC(person)


#just dialog with the cheese wizard 
def NPC(person):
    print("\nSuddenly, a wizard pops out from the trees!")
    time.sleep(2)
    graphicsfunctions.yodelergraphic()
    print("\nDave the Cheese Wizard (Yodeling Connoisseur): Wow! Your yodeling is spectacular!")
    time.sleep(3)
    print("\nYou: Thank you Dave the Cheese Wizard! Do you live in this forest?")
    time.sleep(3)
    print("\nDave the Cheese Wizard (Yodeling Connoisseur): Follow me!")
    time.sleep(3)
    print("\nYou follow Dave the Cheese Wizard (Yodeling Connoisseur)."
          +" You eventually exit the forest and come across a giant cheese wheel"
          +" at the bottom of the tallest mountain you’ve ever seen. He takes you inside and shows you a map…")      
    time.sleep(3)
    print("\nDave the Cheese Wizard (Yodeling Connoisseur): Yodeling is only a side"
          +" hustle. My real job is to guide travelers to the secret treasure at"
          +" the top of this mountain. Will you complete the quest?")
    time.sleep(3)
    input("\nYou look at the map and agree. Press enter to continue")
    time.sleep(5)
    return mountain(person)


#dragon and cave event 
def cave(person):
    print("\nYou choose to hide in the cave. You enter cautiously…")
    time.sleep(2)
    graphicsfunctions.itemsgraphic()
    print("\nDeep inside the cave, you see two items on the ground:"
          +" a sword and a bottle of perfume. Will you pick one?")
    print("pick item?")
    choice = yesOrNo()
   
    if choice =="yes":
        swordOrPerf(person)
        print("\nYou keep walking deeper into the cave. Suddenly you encounter "
              +"Gloomkins the Dragon! It sees you, so there is no running. "
              +"What will you do?")
        graphicsfunctions.dragongraphic()
        time.sleep(2)

    if choice =="no":
        print("\nYou keep walking deeper into the cave. Suddenly you encounter"
              +" Gloomkins the Dragon! It sees you, so there is no running."
              +" You'll have to fight using your item!")
        graphicsfunctions.dragongraphic()
        print("\nUnfortunately, since you didn’t grab an item, you can’t do anything. "
        +"Gloomkins eats you. Womp womp.")
        return gameOver()

    elif person.findObj("sword"):
        ded = fight(person, 90, 15, "\nYou whacked the dragon! Gloomkins has an owie","Gloomkins sneezed on you! You have an owie")
        if ded:
            print( "\nYou lost to the dragon! Looks like that sword didn’t help much…"
              +"Womp womp.")
            return gameOver()
        else:
            print("\nYou defeated Gloomkins! You exit the cave and keep walking...")

            print("You are so proud of yourself you have a celebratory yodel!")
            time.sleep(5)
            return NPC(person)
    else:
        if person.getWeakness() == "smell":
            print("\nYou choose to fight the dragon using your perfume."
              +" Clearly, you forgot about your weakness."
              +" The smell kills you instantly. Womp womp.")
            return gameOver()
        else:
            print("\nYou choose to fight the dragon using your perfume… "
              +"You spray it once, and he is literally seduced! "
              +"You have made a new friend :) He lets you climb on his back, "
              +"and you find yourself flying… You eventually land on the top "
              +"of a mountain.")
            person.addFriend("Gloomkins")
            time.sleep(4)
            return topMtn(person)

        
###############################################################################################    
##                                      Cute Path                                            ##      
###############################################################################################
        

def flowerfield(person):
    print("You start walking down the path to your right...")
    time.sleep(2)
    print("\nAfter walking through the trees, you find yourself in "
          +"a field of flowers. So cute!")
    graphicsfunctions.fieldgraphic()
    if person.getWeakness() == "allergy":
        print("\nUnfortunately, you are super allergic to the flowers and "
              +"have a deadly reaction upon contact. Womp womp.")
        return gameOver()
    else:
        print("\nYou skip through the field of flowers while singing "
              +"a little song.")
        time.sleep(2)
        print("\nWill you stop to pick a flower?")
        choice = yesOrNo()
        if choice == "yes":
            print("\nYou pick a flower and take it with you on your journey.")
            graphicsfunctions.flowergraphic()
            person.addObj("flower")
        else:
            print("\nYou reach the end of the field and keep walking.")
        time.sleep(2)
        return troll(person)


def troll(person):
    print("\nYou see a glittery pink river ahead and start wondering how"
          +" you'll get across... As you get closer, you see a bridge. Yay!"
          +" But when you reach the bridge, a goblin stops you.")
    graphicsfunctions.egggoblingraphic()
    time.sleep(2)
    print("\nEgg Goblin: 'Halt! I am Egg Goblin. You must answer this"
          +" riddle to cross my river: I hide under bridges, but I'm not"
          +" shy. With a joke up my sleeve, I'm quite the sly guy. Who am"
          +" I, making travelers sigh?'")
    time.sleep(4)
    print("\nOptions:"
          +" 1) Fred"
          +" 2) A bridge Goblin"
          +" 3) An Egg Goblin"
          +" 4) A Dragon\n")
    time.sleep(2)
    choice = "riddle"
    if person.findObj("flower"):
        choice = flowerOrRiddle(person)
    #rizz coming from the word "charisma" is a gen z slang word for flirting. 
    if choice == "rizz":
        print("\nYou are most definitely not a riddle person, so you try"
              +" giving the Egg Goblin the flower you picked earlier."
              +" The Egg Goblin is flattered! Not only does it let you"
              +" cross the bridge, but it tells you about a secret treasure"
              +" just ahead. You say goodbye to the Egg Goblin, and start your"
              +" journey to the treasure... It cries when you leave :(")
        person.addFriend("egg goblin <3")
        person.marriage()
        time.sleep(6)
        return mountain(person)
        
    else:
        #riddle
        count = 1
        userinput = 7
        #3 chances to get it right 
        while userinput!= 3 and count <=3:
            userinput = numChoice(3)
            if userinput!= 3:
                print("\nYou answered incorrectly. Luckily, the Egg"
                      +" Goblin gives 3 chances. You have "
                      + str(3-count) + " remaining")
                person.takeFinger()
                count+=1

        if userinput!= 3:
            print("\nYou answered incorrectly 3 times. As punishment,"
                  +" the Egg Goblin turns you into an egg and eats you."
                  +" Womp womp.")
            return gameOver()

        else:
            print("\nYou answered correctly! You befriend the Egg Goblin"
                  +" and it allows you to cross. It also lets you in on a"
                  +" secret. There's a treasure on top of a mountain"
                  +" nearby!")
            time.sleep(3)
            person.addFriend("egg goblin")
            return mountain(person)    
        

###############################################################################################    
##                                       Paths Converge                                     ##      
###############################################################################################        
        
def mountain(person):
    graphicsfunctions.mtnbasegraphic()
    print("\nAfter a short walk, you reach the mountain."
          +" It’s massive, and you know you have to climb it. Scary!"
          +" But time to go get that treasure!")
    time.sleep(5)
    print("\nAt the bottom of the mountain, there is a pile of items. "
          +"You should probably take one for your journey… Will you take "
          +"(1) the bag of trash, (2) the rope, (3) the small bag containing"
          +" 2 dubloons, (4) the inhaler, (5) the umbrella, or (6) the pink "
          +"plush pony?")
    choice = numChoice(6)
    print("\nGood choice! You start your journey up the mountain...\n")
    if choice == 1:
        person.addObj("trash")
    elif choice == 2:
        person.addObj("rope")
    elif choice == 3:
        person.addObj("2 dubloons")
    elif choice == 4:
        person.addObj("inhaler")
    elif choice == 5:
        person.addObj("umbrella")
    else:
        person.addObj("pink plush pony")

    ##goats event  
    graphicsfunctions.goatsgraphic()
    time.sleep(2)
    print("\nYou walk for a while before encountering a herd of wild "
          +"mountain goats. They look hungry! Hopefully you have something "
          +"to feed them...")
    time.sleep(4)
    flow = person.findObj("flower")
    can = person.findObj("trash")
    if flow == True or can == True:
        print("\nYou have an item to use! Do you want to feed them?")
        if yesOrNo() == "yes":
            if can == True and flow == True:
                print ("\nDo you want to feed it the flower or the trash?")
            elif can == True:
                print("\nYou throw them the bag of trash and they DEVOUR it."
                      +" They are so happy that they allow you to ride them"
                      +" up the mountain for a while!")
                time.sleep(3)
                person.removeObj("trash")
            else:
                print("\nYou throw them the flower and they DEVOUR it."
                      +" They are so happy that they allow you to ride them"
                      +" up the mountain for a while!")
                time.sleep(3)
                person.removeObj("flower")
            return village(person, True)
        time.sleep(2)
    print("\nYou have nothing to feed the goats (or you do and you're just mean)."
          +" You keep walking and leave the sad sad goats behind.")
    time.sleep(3)

    ## path choice
            
    time.sleep(2)
    print("\nYou walk a little farther and see two potential paths up the mountain."
          +" With a rope, you could scale the cliffside. Without a rope, you'll "
          +"have to walk the winding mountain path. Which path will you take? "
          +"(climb/walk)")

    choice = climbOrWalk()
    if choice == "walk" or person.findObj("rope")==False:
        print("\nNo rope? Start walking...")
        return village(person, False)
    else:
        print("\nThank goodness you grabbed the rope. You will scale the cliffside.")
        if person.getWeakness() == "asthma" and person.findObj("inhaler") == False:
            print("\nBUT, you have asthma and no inhaler! You have climbed"
                  +" up too high and can no longer breathe. You pass out"
                  +" and fall off the cliff. Womp womp.")
            return gameOver()
        elif person.getWeakness() == "asthma" and person.findObj("inhaler") == True:
            print("rutroh you have asthma!! but good thing you grabbed the inhaler!!")
        
        ## break event
        
        print("\nOnce you've climbed for a bit, you realize you are about"
                +" halfway up the mountain. Do you want to take a break?")
        choice = yesOrNo()
        if choice == "yes":
            print("\nYou chose to take a break. Unfortunately, you dangle there a"
                  +" little too long and your rope snaps. Womp womp.")
            return gameOver()
        else:
            print("\nYou chose to keep going. You lost a bit of health, but"
                  +" you're still climbing.")
            person.setHealth(person.getHealth()-10)
            return fairy(person)


## fairy event
def fairy(person):
    graphicsfunctions.fairygraphic()
    print("\nAs you're climbing, you're suddenly swarmed by fairies!"
          +" They are speaking but you can't understand them. Do you"
          +" try to speak to them?")
    choice = yesOrNo()
    if choice == "no":
        print("\nYou choose to ignore them. They take this very personally"
              +" and magically cut your rope, causing you to fall to your"
              +" death. Womp womp.")
        return gameOver()
    print("\nYou decide you want to speak to them. What do you want to say?"
          +" ('hello', 'moo', or 'yodel')")
    choice = helloYodelMoo()
    if choice == "moo" or choice == "yodel":
        print("\nWhy did you think "+choice+"ing at the fairies would be a"
              +" good idea? They are mortified. They use their magic to"
              +" send you back to the bottom of the mountain. Maybe try"
              +" something else next time!")
        person.addEnemy("fairies")
        return smacked(person)
    print("\nYou choose to say hello to the fairies. They think you are"
          +" polite and befriend you. They even use their magic to get"
          +" you to the top of the mountain.")
    person.addFriend("fairies")
    time.sleep(4)
    return topMtn(person)
    
## village event
def village(person, fedGoat):
    time.sleep(2)
    print("\nYou walk and walk and walk up the winding path...")
    
    ## goats event 2
    if fedGoat == False:
        print("\nYou hear a sound behind you. You turn and realize"
              +" the goats are back. It must be because you didn't feed"
              +" them...")
        time.sleep(3)
        graphicsfunctions.goatsgraphic()
        flow = person.findObj("flower")
        can = person.findObj("trash")
        if flow == True or can == True:
            print("Will you feed them now?")
            if yesOrNo() == "yes":
                if can == True and flow == True:
                    print ("Do you want to feed them the flower or the trash?")
                elif can == True:
                    print("\nYou chose to feed the goats. They are much"
                          +" happier now and will leave you alone. You"
                          +" keep heading up the mountain.")
                    time.sleep(2)
                    person.removeObj("trash")
                else:
                    print("\nYou chose to feed the goats. They are much"
                          +" happier now and will leave you alone. You"
                          +" keep heading up the mountain.")
                    time.sleep(2)
                    person.removeObj("flower")
                return rain(person)
            
        print("\nYou still won't feed them? Shame on you. Since"
                  +" you chose to run away, the goats leave, but they"
                  +" are now your enemies. And they're still sad.")
        time.sleep(3)
        person.addEnemy("the goats.")
        if person.weakness == "asthma":
            if person.findObj("inhaler") == False:
                print("\nYou didn' feed them? Shame on you. Since"
                  +" you did not, you have to run away, the goats leave, but you"
                  +" are out of breath from all that running. Don't forget"
                  +" your weakness! You'll have to return to the"
                  +" bottom of the mountain to catch your breath.")
                time.sleep(3)
                return smacked(person)
            print("You have asthma, but you also have an inhaler,"
                  +" which really saved you. You can keep going.")
            time.sleep(3)
        #end goat feed
    
    return rain(person)


## rain event
def rain(person):
    print("\nAs you walk higher up the mountain, it starts to rain."
          +" Will you take a break?")
    choice = yesOrNo()
    if choice == "no":
        print("\nYou choose to keep going and quickly realize this was not a smart call."
              +" You slip and fall, ending up back at the bottom of the mountain."
              +" Maybe be more careful next time...")
        time.sleep(3)
        return smacked(person)
    
    if person.findObj("umbrella") == False:
        print("\nYou choose to take a break, but since you have no umbrella, it's not"
              +" a very pleasant break. You lose some health, and a finger to"
              +" hypothermia, but you are able to keep going once the rain stops.")
        time.sleep(3)
        person.setHealth(person.getHealth()-10)
        person.takeFinger()
    else:
        print("\nYou choose to take a break. Since you have an umbrella, you"
              +"stay warm and dry. You're ready to keep going!")
        time.sleep(3)

    return fred(person)


def fred(person):
    print("\nAfter even more climbing, you encounter Fred. Fred is not happy to see you."
          +" What will you do to get past him? (1) Tickle (2) Battle (3) Bribe")
    time.sleep(2)
    choice = numChoice(3)

    #luck based tickling 
    if choice == 1:
        luck = random.randint(0,1)
        if luck == 1:
            print("\nFred is not amused. He is understandably upset because he did"
                  +"not consent to that. He slaps you right off the mountain. Womp womp.")
            time.sleep(2)
            return gameOver()
        print("\nIt worked! Turns out Fred is VERY ticklish."
            +" You are able to pass him while he is busy laughing.")
        time.sleep(2)
        
    #fight 
    elif choice == 2:
        if fight(person, 95, 15, "you whack fred","fred whacks you"):
            print("\nYou lose to Fred and are dramatically thrown off the mountain. Womp womp.")
            time.sleep(2)
            return gameOver()
        print("\nYou defeat Fred! You keep moving up the mountain.")
        time.sleep(2)

    #bribe
    else:
        print("\nYou choose to bribe Fred… What item will you give him?")
        time.sleep(2)
        coun = 1
        for x in person.obj:
            print(str(coun) +". "+x)
            coun+=1
        choice = numChoice(len(person.obj))
        if person.obj[choice-1] != "pink plush pony":
            print("\nHe did not appreciate your little gift. He slaps you right off the mountain. Womp womp.")
            time.sleep(2)
            return gameOver()
        print("\nHe liked your item! He allows you to live and keep going.")
    return bridge(person)
            
        
        
def bridge(person):
    print("\nYou encounter a bridge. It doesn’t look sturdy, and you can tell if you step on it in the wrong place,"
          +"it will break. You need to start stepping, so do you step on the left side of the bridge or the right?")
    time.sleep(2)
    if leftOrRight() == "right" :
        print("\nYou took a wrong step, and the bridge broke, causing you to take a tumble. Womp womp.")
        return gameOver()
    print("\nYou are still alive! Time to take another step.")
        
    if leftOrRight() == "right" :
        print("\nYou took a wrong step, and the bridge broke, causing you to take a tumble. Womp womp.")
        return gameOver()
    print("\nYou are still alive! Time to take another step.")
    if leftOrRight() == "left" :
        print("\nYou took a wrong step, and the bridge broke, causing you to take a tumble. Womp womp.")
        return gameOver()
    print("\nYou are still alive! Time to take another step.")
    print("\nYou have successfully crossed the bridge!"
          +"The top of the mountain is in sight! Keep going :)")
    return topMtn(person)
    
    

def smacked(person):
    person.removeObj("trash")
    person.removeObj("rope")
    person.removeObj("2 dubloons")
    person.removeObj("inhaler")
    person.removeObj("umbrella")
    person.removeObj("pink plush pony")
    person.setHealth(person.getHealth()-10)
    person.takeFinger()
    if person.getHealth() <= 0:
        print("Sorry! You have no more health and you died")
        return gameOver()
    return mountain(person)
    




                
