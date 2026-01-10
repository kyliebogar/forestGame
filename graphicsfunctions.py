##Gabriela, Bernie, Kylie
#Feb 12 2024
#Final Project 
### file containing all functions that call graphics
# bernie: functions and txt files
# gabriela: txt files


# fairy
path = "images/"
def fairygraphic():
    a = open(path + "fairies.txt")
    fairy = a.read()
    print(fairy)
    a.close()


# trees (scary path)

def treesgraphic():
    b = open(path + "EnchantedForest.txt")
    forest = b.read()
    print(forest)
    b.close()


# flowers (cutesy path)

def fieldgraphic():
    c = open(path + "Flowerpath.txt")
    field = c.read()
    print(field)
    c.close()


# flower (picked)

def flowergraphic():
    d = open(path + "flower.txt")
    flower = d.read()
    print(flower)
    d.close()


# yodel man

def yodelergraphic():
    e = open(path + "YodelNPC.txt")
    yodeler = e.read()
    print(yodeler)
    e.close()
   

# sword and perfume choice

def itemsgraphic():
    f = open(path + "PerfumeSword.txt")
    items = f.read()
    print(items)
    f.close()


# dragon

def dragongraphic():
    g = open(path + "GloomkinsDragon.txt")
    dragon = g.read()
    print(dragon)
    g.close()



# goats

def goatsgraphic():
    h = open(path + "GoatArmy.txt")
    goats = h.read()
    print(goats)
    h.close()


# bear

def beargraphic():
    i = open(path + "bear.txt")
    bear = i.read()
    print(bear)
    i.close()


# mountain village

def mtnvillagegraphic():
    j = open(path + "village.txt")
    village = j.read()
    print(village)
    j.close()


# egg goblin

def egggoblingraphic():
    k = open("egggoblin.txt")
    goblin = k.read()
    print(goblin)
    k.close()


# base of mtn

def mtnbasegraphic():
    l = open(path + "BaseMountain.txt")
    mtnbase = l.read()
    print(mtnbase)
    l.close()


# game over

def gameovergraphic():
    m = open(path + "GameOver.txt")
    gameover = m.read()
    print(gameover)
    m.close()

# participation trophy

def trophygraphic():
    n = open(path + "TROPHY.txt")
    trophy = n.read()
    print(trophy)
    n.close()
