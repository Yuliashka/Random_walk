# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/labs/lab01/colors

from turtle import Turtle, Screen

# To import everything that is inside the turtle module we can use:
# from turtle import *

# Create Turtle class from turtle module
timmy = Turtle()
timmy.shape("turtle")
timmy.color("CornflowerBlue")

# Создаем квадрат
# for _ in range(100):
#     timmy.forward(100)
#     timmy.right(90)

# Create a broken line
# for _ in range(20):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

# Creating different geometric figures
# https://trinket.io/docs/colors
# import random
# colors = ["deep pink", "medium slate blue", "purple", "teal", "cyan", "cornflower blue", "medium orchid"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# # We loop from 3 to 10
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)

# Creating a random walk for turtle
import random
colors = ["deep pink", "medium slate blue", "purple", "teal", "cyan", "cornflower blue", "medium orchid"]
angle = [0, 90, 180, 270]

for _ in range(200):
    timmy.pensize(15)
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.right(random.choice(angle))




# Create Screen class from turtle module
screen = Screen()
screen.exitonclick()
