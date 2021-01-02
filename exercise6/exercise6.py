import random
colors=["pink","yellow","green","orange","red","blue"]

while True:
    color=colors[random.randint(0,len(colors)-1)]
    guess=input("guess the color ,I am thinking:")
    if color==guess:
        break
    else:
        guess=input("nope .try again:")
        print("you guess it ,I was thinking about:",color)
        loop=input("do you want to play this game again,answer in yes or no:")
        if loop.lower()=='no':
            break
print("it was fun thaks for playing")


    
        