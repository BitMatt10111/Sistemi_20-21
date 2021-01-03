import turtle
import random

robot = turtle.Turtle()
robot.penup()
robot.speed(1)
robot.fillcolor("green")
robot.shapesize(2)

h=600
l=600

food = turtle.Turtle()
food.penup()
food.speed(0)
food.goto(random.randint(-(l/2+10),l/2-10),random.randint(-(h/2+10),h/2-10))
food.fillcolor("red")
food.shape("circle")
food.shapesize(0.5)

win = turtle.Screen()

def right():
    if(robot.heading()!=180):
        robot.setheading(0)

def left():
    if(robot.heading()!=0):
        robot.setheading(180)

def up():
    if(robot.heading()!=270):
        robot.setheading(90)

def down():
    if(robot.heading()!=90):
        robot.setheading(270)

def move():
    if(robot.heading()==90):
        y=robot.ycor()
        robot.sety(y+20)
    if(robot.heading()==270):
        y=robot.ycor()
        robot.sety(y-20)
    if(robot.heading()==180):
        x=robot.xcor()
        robot.setx(x-20)
    if(robot.heading()==0):
        x=robot.xcor()
        robot.setx(x+20)    

win.title("My game")
win.bgcolor("orange")
win.setup(l, h)

win.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(right, "Right")
win.onkeypress(left, "Left")

while True:
    win.update()
    if(robot.xcor()>l/2-10 or robot.xcor()<-(l/2-10) or robot.ycor()>h/2-10 or robot.ycor()<-(l/2-10)):
        robot.goto(0,0)
    else:
        move()
    if(robot.distance(food)<20):
        food.goto(random.randint(-(l/2+10),l/2-10),random.randint(-(h/2+10),h/2-10))

win.mainloop()