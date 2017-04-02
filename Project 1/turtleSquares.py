import turtle

def drawSquare(someTurtle):
    someTurtle.right(10)
    for i in range(1,5):
        someTurtle.forward(100)
        someTurtle.right(90)

def drawArt():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.color("cyan")
    brad.shape("turtle")
    brad.speed(5)
    i = 0
    while(i<36):
        drawSquare(brad)
        i=i+1
        

    #angei = turtle.Turtle()
    #angei.shape("arrow")
    #angei.color("yellow")
    #angei.circle(100)

    window.exitonclick()

drawArt()    
