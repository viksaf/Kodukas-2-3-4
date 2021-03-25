import turtle


aken = turtle.Screen()
aken.setup(300,300) # x, y
aken.bgcolor("white")
aken.title("Kodune töö - Viktorija")

x = 50

for i in range(4):
    turtle.forward(x)
    turtle.rt(90)
    turtle.forward(x)
    turtle.lt(90)
    turtle.forward(x)
    turtle.lt(90)
  