import turtle

robot = turtle.Turtle()
robot.color = "black"

h=800
l=800

passo=50

win = turtle.Screen()

def right():
    robot.right(90)

def left():
    robot.left(90)

def forward():
    if((robot.xcor()+passo<=l/2 and robot.xcor()-passo>=-(l/2)) and (robot.ycor()+passo<=h/2 and robot.ycor()-passo>=-(h/2))):
        robot.forward(passo)
    else:
        robot.goto(0,0)
def backward():
    if((robot.xcor()+passo<=l/2 and robot.xcor()-passo>=-(l/2)) and (robot.ycor()+passo<=h/2 and robot.ycor()-passo>=-(h/2))):
        robot.backward(passo)
    else:
        robot.goto(0,0)

win.title("My game")
win.bgcolor("orange")
win.setup(l, h)

win.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)
win.onkey(forward, "Up")
win.onkey(backward, "Down")
win.onkey(right, "Right")
win.onkey(left, "Left")

win.mainloop()