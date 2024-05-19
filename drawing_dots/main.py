# import colorgram
#
# colors = colorgram.extract('dots.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()

color_list = [(249, 248, 248), (233, 241, 239), (227, 233, 239), (2, 9, 30), (243, 236, 241), (122, 95, 41),
              (72, 32, 22), (237, 212, 72), (220, 81, 59), (225, 117, 100), (93, 1, 21), (178, 140, 170),
              (150, 92, 115), (34, 90, 26), (7, 154, 73), (205, 63, 91), (168, 129, 77), (1, 64, 147), (4, 221, 218),
              (3, 78, 28), (220, 178, 218), (79, 135, 179), (124, 154, 178), (80, 110, 138), (121, 185, 164),
              (10, 214, 221), (121, 13, 33), (243, 204, 7), (133, 222, 208), (229, 174, 165)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_cnt in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_cnt % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
