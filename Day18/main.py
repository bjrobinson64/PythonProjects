from turtle import Turtle, Screen, colormode
from random import randint


# import colorgram
#
# num_colors = 30
# color_list = []
#
# colors = colorgram.extract('image.jpg', num_colors)
#
# for x in range(num_colors):
#     color_list.append((colors[x].rgb.r, colors[x].rgb.g, colors[x].rgb.b))
#
# print(color_list)

color_list = [(25, 106, 167), (231, 155, 63), (233, 214, 89), (192, 40, 83), (221, 136, 174), (142, 103, 53),
              (109, 188, 213), (207, 169, 27), (163, 21, 65), (217, 74, 96), (21, 54, 131), (116, 192, 147),
              (8, 182, 156), (141, 209, 227), (104, 107, 196), (239, 87, 47), (12, 151, 85), (19, 165, 209),
              (231, 165, 184), (85, 41, 26), (99, 50, 36), (22, 42, 78), (27, 84, 90), (237, 210, 6), (108, 7, 46),
              (159, 211, 193)]

a = Turtle()
a.penup()
a.speed(0)
a.setposition(-600, -500)
colormode(255)

y = -500

while y < 600:
    for x in range(17):
        a.color(color_list[randint(0, len(color_list)-1)])
        a.pendown()
        a.dot(50)
        a.penup()
        a.forward(75)
    y += 75
    a.goto(-600, y)




screen = Screen()
screen.exitonclick()









