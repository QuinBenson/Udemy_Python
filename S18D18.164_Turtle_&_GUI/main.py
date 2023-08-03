import turtle as t
import random

tim = t.Turtle()


def get_quadrant(previous_choice):
    dynamic_list = list(tuple_opposite_list)
    dynamic_list.pop(previous_choice)
    choice = dynamic_list[random.randint(0, 2)]

    return choice


# tuple of choices, just for the fun of tuples
tuple_opposite_list = (2, 3, 0, 1)

# ########## Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]
pensize = 20
tim.pensize(pensize)
previous = random.randint(0, 3)
for _ in range(1, 101):
    tim.color(random.choice(colours))
    # current = get_quadrant(previous)
    current = random.randint(0, 3)
    to_angle = (current + 1) * 90
    tim.setheading(to_angle)
    tim.pendown()
    tim.forward(20)
    tim.penup()
    tim.forward(int(pensize // 2))

    previous = current

t.exitonclick()
