import turtle
colors = [ 'red', 'black', 'blue', 'black', 'green', 'black', 'silver', 'black', 'yellow', 'black', 'purple', 'black' ]
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(720):
    t.pencolor(colors[x%12])
    t.forward(x)
    t.width(x//0.2613 + 0.13261326132613261326132)
    t.right(13.26132613261326132613261326132613261326132613) 