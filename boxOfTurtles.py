import turtle

#make a empty box for turtles
boxOfTurtles = {}

#make 72 turtles
#and put them in a box
for i in range(72):
    boxOfTurtles[i] = turtle.Turtle()

#for every turtle in "the box"
#go forward 100, next turtle turn 5 degrees
#go forward 100 ...
angle = 0
for aTurtle in boxOfTurtles:
    angle = angle + 5
    boxOfTurtles[aTurtle].speed(0)
    boxOfTurtles[aTurtle].left(angle)
    boxOfTurtles[aTurtle].forward(100)

#can you see the relationship between
#72 turtles and a 5 degree turn?


# function: small turn
# for every turtle in the box
# move 2 and turn one degree
def doASmallTurn():
    global aTurtle
    for aTurtle in boxOfTurtles:
        boxOfTurtles[aTurtle].speed(0)
        boxOfTurtles[aTurtle].left(1)
    for aTurtle in boxOfTurtles:
        boxOfTurtles[aTurtle].forward(2)

for i in range(300):
 doASmallTurn()

for aTurtle in boxOfTurtles:
        boxOfTurtles[aTurtle].hideturtle()

turtle.mainloop()
