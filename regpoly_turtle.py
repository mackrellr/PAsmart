import turtle

bif = turtle.Turtle()
sides = 0

sides = input('Enter the number of sides of the regular polygon.')

def regular_polygon(n, size):
    for i in range(n):
        bif.forward(300 / n)
        bif.left(360 / n)

regular_polygon(int(sides), 20)

turtle.done()
