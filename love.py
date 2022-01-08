import turtle

turtle.bgcolor("black")
turtle.pensize(3)

a = turtle.Turtle()
a.penup()
a.goto(-200, 60)
a.pendown()
a.color("yellow")
style = ('arial', 50, 'italic')
a.write('I', font=style, align='left')
a.hideturtle()

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("red", "pink")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.0)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
a = turtle.Turtle()

a.penup()
a.goto(180, 60)
a.pendown()
a.color("red")
style = ('arial', 50, 'italic')
a.write('You', font=style, align='left')
a.hideturtle()

turtle.done()