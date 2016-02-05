import random


rndnum = 0
def getrndnum ():




    global rndnum
    rndnum = random.randint(1,20)
    getanswr()

def getanswr ():
    global getnum
    getnum = input("Guess a number between 1-20")

    if getnum == "" :
        print "You have to type a number between 1-20"
        getanswr()
    elif getnum > 20:
        print "You have to type a number between 1-20"
        getanswr()
    elif getnum < 1:
        print "You have to type a number between 1-20"
        getanswr()
    else:
        chkanswr(getnum)

def chkanswr(x):
    if x > rndnum:
        print "your guess is greater than the number I'm thinking of, try again"
        getanswr()
    elif x < rndnum:
        print "your guess is smaller than the number I'm thinking of, try again"
        getanswr()
    else:
        print "You've guesed right, my number was:",rndnum,"!"
        playag = raw_input("Play again? Type yes:")
        if playag == "yes":
            getrndnum()
getrndnum()
