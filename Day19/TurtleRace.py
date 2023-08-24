from turtle import Turtle, Screen
from random import randint


# turtles
def create_turtles():
    y = -120
    for x in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(x)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y)
        y += 50
        turtles.append(new_turtle)


# variables and lists
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# screen setup
screen = Screen()
screen.setup(width=500, height=400)

while True:
    user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet not in colors:
        print("not a valid color")
    else:
        break

# turtle setup
create_turtles()

# race
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! {winning_color} was the winner!")
            else:
                print(f"You Lost! {winning_color} was the winner!")

        distance = randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
