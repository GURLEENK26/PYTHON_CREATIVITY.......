import turtle
col=('red','green','blue','yellow')
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(30)

for i in range (100):
    t.color(col[i%4])
    t.forward(i*4)
    t.left(150)
    t.width(2)
