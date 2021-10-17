from turtle import Turtle, Screen, colormode
import random

colormode(255)

pop_up_window = Screen()
# print(pop_up_window.canvwidth, pop_up_window.canvheight)

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
