import turtle as t
import random

tim = t.Turtle()


def get_quadrant(previous_choice,pt_direction_choices):
    dynamic_list = list(pt_direction_choices)
    dynamic_list.pop(previous_choice)
    choice = dynamic_list[random.randint(0, len(dynamic_list)-1)]

    return choice

def get_redirect_quadrant(previous_choice,pt_direction_choices):
    dynamic_list = list(pt_direction_choices)
    choice = dynamic_list[random.randint(0, len(dynamic_list)-1)]

    return choice

def pos_in_range (p_screensize, p_screen_position):

    summation = abs(p_screen_position) + pen_size + pen_step
    if summation >= int(p_screensize // 2):
        return_val = False
    else:
        return_val = True

    return return_val


# tuple of choices, just for the fun of tuples
t_opposite_list = (2, 3, 0, 1)
t_redirect_x = (0, 2)
t_redirect_y = (1, 3)

# ########## Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]

screensize_tuple = t.screensize()

pen_size = 12
pen_step = 30
tim.pensize(pen_size)

previous = random.randint(0, 3)
x_latch=False
for _ in range(1, 1001):
    tim.color(random.choice(colours))
    current = get_quadrant(previous,t_opposite_list)
    # current = random.randint(0, 3)


    # check x coord is not outside limits
    t_position=tim.pos()

    pir = pos_in_range(t.window_width(),tim.xcor())
    if not pir:
        current = get_redirect_quadrant(previous,t_redirect_x)




    # check y coord is not outside limits
    pir=pos_in_range(t.window_height(), tim.ycor())
    if not pir:
        current = get_redirect_quadrant(previous, t_redirect_y)

    to_angle = (current + 1) * 90
    tim.setheading(to_angle)
    tim.pendown()
    tim.forward(pen_step)
    tim.penup()
    tim.forward(int(pen_size // 2))

    previous = current

t.exitonclick()
