import turtle

# Set the size of the screen and the immediacy of the plot
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.tracer(0)

# Name the turtle
plotter = turtle.Turtle()

# Draw x- and y-axis
plotter.pensize(3)

# Draw x-axis
plotter.pu()
plotter.goto(-300, 0)
plotter.pd()
plotter.goto(300, 0)

# Draw y-axis
plotter.pu()
plotter.goto(0, 300)
plotter.pd()
plotter.goto(0, -300)
plotter.pu()

# Draw grid (horizontal lines)
hz = -300
plotter.pensize(0.5)
while hz < 300:
    plotter.pu()
    plotter.setpos(hz, 300)
    plotter.pd()
    plotter.setpos(hz, -300)
    hz += 30
plotter.pu()
plotter.setpos(270, -30)
plotter.write('x', font=("Arial", 14, "italic"))

# Draw grid (vertical lines)
vert = -300
plotter.pensize(0.5)
while vert < 300:
    plotter.pu()
    plotter.setpos(-300, vert)
    plotter.pd()
    plotter.setpos(300, vert)
    vert += 30
plotter.pu()
plotter.setpos(8, 270)
plotter.write('y', font=("Arial", 14, "italic"))

# Plot a parabola
x = 0
y = 0
plotter.shape('circle')
plotter.shapesize(.1, .1)
plotter.pensize(3)
for x in range (-150, 150):
    y = ((x/30)**2)*30
    plotter.setpos(x, y)
    plotter.pd()
    plotter.color('red')
    #plotter.stamp()

turtle.done()
