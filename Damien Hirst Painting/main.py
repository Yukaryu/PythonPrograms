# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst_painting.jpg', 30)
# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r, g, b)
#   rgb_colors.append(new_color)

# print(rgb_colors)


color_list = [(219, 153, 107), (133, 171, 195), (222, 72, 88),
              (215, 131, 149), (24, 119, 152), (241, 208, 98),
              (121, 177, 149), (38, 119, 84), (20, 165, 204),
              (219, 83, 76), (140, 86, 62), (131, 83, 102),
              (175, 185, 215), (21, 168, 123), (161, 209, 166),
              (174, 154, 74), (3, 96, 115), (237, 161, 174),
              (238, 166, 152), (54, 59, 93), (152, 207, 220),
              (102, 126, 174), (40, 56, 76), (34, 87, 53),
              (232, 209, 16), (74, 79, 40)]

import turtle as t
import random

t.colormode(255)
dottie = t.Turtle()

dottie.speed(0)
dottie.penup()
dottie.hideturtle()

dottie.setheading(225)
dottie.forward(320)
dottie.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots + 1):
    dot_color = random.choice(color_list)
    dottie.dot(20, dot_color)
    dottie.forward(50)
    if i % 10 == 0:
        dottie.setheading(90)
        dottie.forward(50)
        dottie.setheading(180)
        dottie.forward(500)
        dottie.setheading(0)

screen = t.Screen()
screen.exitonclick()
