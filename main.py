import pgzrun
import random 

#WIDTH and HEIGHT - sys variables - output screen

WIDTH=300
HEIGHT=300
TITLE="square shape"

#draw() - inbuilt function gets called itself. Helps to render animations/shapes/texts...
def draw() :
    screen.fill("black")
    #rectangle width and height
    width=WIDTH
    height=HEIGHT-200
    r= 255
    g= 0
    b=random.randint(100,200)
    for i in range(20) :
        #x,y width,height
        myRect = Rect((0,0),(width,height))
        myRect.center=150,150

        screen.draw.rect(myRect,(r,g,b))
        width=width-10
        height=height+10
        r=r-10
        g=g+5


pgzrun.go()