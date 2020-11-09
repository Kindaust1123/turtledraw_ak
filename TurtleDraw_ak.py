import turtle

TEXTFILENAME = input('File Name Here: ')

print("Kirby the Turtle Draw is starting...")

KirbyTheTurtle = turtle.Turtle()
KirbyTheTurtle.speed(10)
KirbyTheTurtle.penup()

drawing_area = turtle.Screen()
drawing_area.setup(width=450, height=450)

turtleDrawTextFile = open(TEXTFILENAME, 'r')
line = turtleDrawTextFile.readline()
while line:
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        KirbyTheTurtle.color(color)
        KirbyTheTurtle.goto(x,y)
        KirbyTheTurtle.pendown()

    if (len(parts) == 1):
        KirbyTheTurtle.penup()

    line = turtleDrawTextFile.readline()

KirbyTheTurtle.penup()
KirbyTheTurtle.sety(-150)
KirbyTheTurtle.setx(30)
KirbyTheTurtle.hideturtle()
KirbyTheTurtle.write("Total Distance marked = 4395.49")
input("Press the enter key to close the window: ")
turtleDrawTextFile.close()
turtle.done()

print("Kirby The Turtle Has Finished Drawing! He Hopes You Enjoyed!")