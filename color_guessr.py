from turtle import Turtle
import colorsys


class ColorGuessr(Turtle):
    def __init__(self):
        super().__init__()
        self.guess = "undefined"
        self.penup()
        self.hideturtle()
        self.color_r = 1
        self.color_g = 1
        self.color_b = 1
        self.goto(self.xcor(), self.ycor() - 120)

    def guess_color(self, r, g, b):
        self.color_r = r
        self.color_g = g
        self.color_b = b

        # Convert RGB to HSV
        color_hsv = colorsys.rgb_to_hsv(self.color_r, self.color_g, self.color_b)

        # Get the hue from HSV
        hue = color_hsv[0] * 360

        # Categorize the hue, label the color
        if hue < 8:
            self.guess = "red"
        elif hue < 21:
            self.guess = "red-orange"
        elif hue < 40:
            self.guess = "orange & brown"
        elif hue < 52:
            self.guess = "orange-yellow"
        elif hue < 61:
            self.guess = "yellow"
        elif hue < 81:
            self.guess = "yellow-green"
        elif hue < 139:
            self.guess = "green"
        elif hue < 169:
            self.guess = "green-cyan"
        elif hue < 200:
            self.guess = "cyan"
        elif hue < 220:
            self.guess = "cyan-blue"
        elif hue < 246:
            self.guess = "blue"
        elif hue < 276:
            self.guess = "blue-magenta"
        elif hue < 316:
            self.guess = "magenta"
        elif hue < 341:
            self.guess = "magenta-pink"
        elif hue < 351:
            self.guess = "pink"
        elif hue < 356:
            self.guess = "pink-red"
        else:
            self.guess = "red"

        self.print_guess()

    def print_guess(self):
        self.clear()
        self.color(self.color_r, self.color_g, self.color_b)
        self.write((self.guess).capitalize(), font=("Arial", 40, "bold"), align="center")
