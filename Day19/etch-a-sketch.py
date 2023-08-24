from turtle import Turtle, Screen


# functions
def move_forward():
    tim.forward(10)


def move_back():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


tim = Turtle()
screen = Screen()

# button commands
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_back, "s")
screen.onkeypress(turn_right, "d")
screen.onkeypress(turn_left, "a")
screen.onkey(clear, "c")

screen.listen()
screen.exitonclick()
