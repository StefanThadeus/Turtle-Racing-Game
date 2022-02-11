from turtle import Turtle, Screen
import random

screen = Screen()
width, height = 500, 400
screen.setup(width=width, height=height)
screen.title("Turtle Race!")

is_race_on = False

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_list = []

padding = height // len(colors)
y_start = (height / 2) - (padding * len(colors)) + 30

for index, color in enumerate(colors, start=0):
    turtles_list.append(Turtle(shape="turtle"))
    turtles_list[index].color(color)
    turtles_list[index].penup()
    turtles_list[index].goto(x=-230, y=y_start)
    y_start += padding

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            break

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
