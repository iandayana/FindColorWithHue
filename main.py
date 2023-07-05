"""
The program generates a square with white color in a window. After a while, the square's color will change to a
random color by changing the color's red, green, and blue values (from the RGB spectrum).

A label beneath the square will display the color name based on the current color's hue value (from the HSV spectrum).

The color will continue to change to a different random color until the window is closed.
"""
__author__ = "Ilma Andayana"
__email__ = "halo@ilmaandayana.com"


# Import libraries
from turtle import Screen   # graphics windows to draw turtles (https://docs.python.org/3/library/turtle.html)
from square import Square   # class to create a square and change its color (square.py)
from color_guessr import ColorGuessr  # class to label random color based in hue (color_guessr.py)
import time  # for time access (https://docs.python.org/3/library/time.html)


# Global variable(s)
SLEEP_TIME = 0.75


# Create a window
screen = Screen()
screen.setup(600, 600)  # width = 600px, height = 600px
screen.tracer(0)        # automatic screen updates are off


# Create a square with random color
square = Square()
guess = ColorGuessr()


while True:
    # IF global variable SLEEP_TIME not available, create it
    try:
        SLEEP_TIME
    except NameError:
        SLEEP_TIME = 0.5

    # Change the color, pause before each color changing
    time.sleep(SLEEP_TIME)  # add delay in the execution
    screen.update()

    # Change square's color
    square.change_color()

    # Print the computer's guess
    guess.guess_color(square.color_r, square.color_g, square.color_b)
