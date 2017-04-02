import turtle

def drawRhombus(someTurtle):
    for i in range(0,2):
        someTurtle.forward(100)
        someTurtle.right(45)
        someTurtle.forward(100)
        someTurtle.right(135)

def drawArt():
    window = turtle.Screen()
    window.bgcolor("black")
    
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed(10)

    for i in range(0,36):
        drawRhombus(brad)
        brad.right(10)

    brad.right(90)
    brad.forward(150)

    window.exitonclick
drawArt()
        
