import turtle
t = turtle.Turtle()
w = turtle.Screen()
w.title('Star')
w.bgcolor('black')
t.color('red')
t.speed(10)
for i in range (80):
    for i in range (1,6):
        t.left(144)
        t.forward(50)
    t.left(5)
turtle.done()