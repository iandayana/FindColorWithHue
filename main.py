from turtle import Screen
from square import Square
from color_guessr import ColorGuessr
import time


SLEEP_TIME = 1

screen = Screen()
screen.setup(600, 600)  # width = 600px, height = 600px
screen.tracer(0)        # automatic screen updates are off

# Create a square with random color
square = Square()
guess = ColorGuessr()


while True:
    time.sleep(SLEEP_TIME)
    screen.update()

    # Change square's color
    square.change_color()

    # Print the computer's guess
    guess.guess_color(square.color_r, square.color_g, square.color_b)


screen.exitonclick()


