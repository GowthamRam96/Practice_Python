import turtle

skk = turtle.Turtle()
skk.goto(-700,0)
for i in range(15):
    skk.forward(100)
skk.penup()
skk.goto(-700,100)
skk.pendown()
skk.pencolor('red')
for i in range(15):
    skk.forward(100)

skk.penup()
skk.goto(-700,50)
skk.pendown()
skk.pencolor('blue')
skk.forward(-25)
for i in range(15):
    skk.pendown()
    skk.forward(75)
    skk.penup()
    skk.forward(25)



# first Car details
Car1 = turtle.Turtle()
Car1.color('red')
Car1.shape('square')
Car1.shapesize(1,2)

Car1.penup()
Car1.goto(-100 ,130)
Car1.tiltangle(90)
# Car1.pendown()

Radar1 = turtle.Turtle()
Radar1.color('black')
Radar1.shape('triangle')
Radar1.shapesize(1,3)
Radar1.penup()
Radar1.goto(-127 ,100)
Radar1.tiltangle(45)

Radar2 = turtle.Turtle()
Radar2.color('black')
Radar2.shape('triangle')
Radar2.shapesize(1,3)
Radar2.penup()
Radar2.goto(-73 ,100)
Radar2.tiltangle(135)


Car2 = turtle.Turtle()
Car2.color('blue')
Car2.shape('square')
Car2.shapesize(1,2)

Car2.penup()
Car2.goto(-500 , 25)
# Car2.pendown()
for i in range(400):
    Car2.forward(1.5)

turtle.done()

