import turtle as t
import colorgram
import random

t.colormode(255)
tim = t.Turtle(visible=False)


def get_colours(image_path, number_of_colours):
    rgb_colours = []
    colours = colorgram.extract(image_path, number_of_colours)

    for colour in colours:
        r = colour.rgb.r
        g = colour.rgb.g
        b = colour.rgb.b
        new_colour = (r, g, b)
        rgb_colours.append(new_colour)

    return rgb_colours


def main():

    color_list = get_colours('image.jpg', 20)

    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)

    tim.speed('fastest')
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

    screen = t.Screen()
    screen.exitonclick()


main()
