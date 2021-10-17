from turtle import Turtle, Screen, colormode
import random

colormode(255)

pop_up_window = Screen()
# print(pop_up_window.canvwidth, pop_up_window.canvheight)

# import colorgram
#
# # # Extract 6 colors from an image.
# # colors = colorgram.extract('sweet_pic.jpg', 6)
# #
# # # colorgram.extract returns Color objects, which let you access
# # # RGB, HSL, and what proportion of the image was that color.
# # first_color = colors[0]
# # rgb = first_color.rgb # e.g. (255, 151, 210)
# # hsl = first_color.hsl # e.g. (230, 255, 203)
# # proportion  = first_color.proportion # e.g. 0.34
# #
# # # RGB and HSL are named tuples, so values can be accessed as properties.
# # # These all work just as well:
# # red = rgb[0]
# # red = rgb.r
# # saturation = hsl[1]
# # saturation = hsl.s
#
# # colors = colorgram.extract('hirst_spot_painting.jpg', 10)
# colors = colorgram.extract('hirst_spot_painting.jpg', 30)
# # print(colors)
# rgb_colors = [tuple(colors[color_index].rgb) for color_index in range(len(colors))]
# # rgb_colors = [(colors[color_index].rgb) for color_index in range(len(colors))]
# print(rgb_colors)
# full_list_of_colors = [
#     (235, 234, 231), (236, 229, 233), (231, 239, 234), (225, 233, 238), (236, 34, 110), (149, 25, 65),
#     (239, 72, 33), (8, 147, 92), (225, 168, 42), (180, 159, 44), (26, 125, 192), (43, 191, 232),
#     (82, 24, 84), (253, 224, 0), (125, 192, 78), (246, 220, 41), (190, 35, 104), (58, 175, 101),
#     (214, 58, 24), (159, 27, 24), (209, 131, 166), (27, 184, 217), (6, 113, 49), (242, 160, 194),
#     (243, 167, 154), (163, 213, 180), (136, 214, 232), (110, 7, 7), (245, 12, 24), (85, 132, 174)
# ]
list_of_colors = [
    (236, 34, 110), (149, 25, 65), (239, 72, 33), (8, 147, 92), (225, 168, 42), (180, 159, 44), (26, 125, 192),
    (43, 191, 232), (82, 24, 84), (253, 224, 0), (125, 192, 78), (246, 220, 41), (190, 35, 104), (58, 175, 101),
    (214, 58, 24), (159, 27, 24), (209, 131, 166), (27, 184, 217), (6, 113, 49), (242, 160, 194), (243, 167, 154),
    (163, 213, 180), (136, 214, 232), (110, 7, 7), (245, 12, 24), (85, 132, 174)
]

turtle = Turtle()
# turtle.pensize(20)
turtle.pensize(10)
# turtle.speed('fast')
x_coordinate, y_coordinate = -225, -200

# for _ in range(10, 100, 10):
#     turtle.penup()
#     turtle.goto((x_coordinate, y_coordinate))
#     turtle.pendown()
#     for _ in range(10):
#         # turtle.color(list_of_colors[random.randint(0, len(list_of_colors) - 1)])
#         # turtle.circle(5)
#         # turtle.dot(20, list_of_colors[random.randint(0, len(list_of_colors) - 1)])
#         turtle.dot(20, random.choice(list_of_colors))
#         turtle.penup()
#         turtle.forward(50)
#         turtle.pendown()
#     y_coordinate += 50

turtle.hideturtle()
turtle.speed('fastest')

for dot_count in range(0, 100):
    if dot_count % 10 == 0:
        turtle.penup()
        turtle.goto((x_coordinate, y_coordinate))
        # turtle.pendown()
        y_coordinate += 50
    turtle.dot(20, random.choice(list_of_colors))
    # turtle.color(list_of_colors[random.randint(0, len(list_of_colors) - 1)])
    # turtle.circle(5)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()

pop_up_window.exitonclick()
