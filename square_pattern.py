import turtle
sc = turtle.Screen()
sc.tracer(0)
sc.setup(width=600,height=600)

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(100)
pen.hideturtle()
pen.penup()
pen.setposition(-300,-300)
pen.pendown()

def minisquare():
    for i in range(4):
        #my screen is setted for 600 to 600
        #so that 600/5 = 120 one side length for my square
        pen.forward(120)
        pen.left(90)
    pen.forward(120)

if __name__ == "__main__":
    for i in range(6):
        pen.up()
        pen.setposition(-300, 300-120*i)
        pen.down()
        for j in range(6):
            #even numbers will be black
            if (i+j)%2 == 0:
                color = 'black'
            #odd numbers will be white
            else:
                color = 'white'

            pen.fillcolor(color)
            pen.begin_fill()
            minisquare()
            pen.end_fill()
