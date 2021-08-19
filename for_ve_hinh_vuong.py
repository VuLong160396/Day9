import turtle
t = turtle.Turtle()
w = turtle.Screen()
w.bgcolor('black')
w.title('square')
t.speed(1)
t.color('red')

for i in range(4):
    t.forward(100)
    t.left(90)
turtle.done()