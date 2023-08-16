import random
import turtle as t

opposite_ways = (2, 3, 0, 1)
possible_ways = [0, 1, 2, 3]
suitable_ways = list(possible_ways)


def next_direction():
    l_list_len = len(suitable_ways)
    l_rnd_idx = random.randint(0, l_list_len - 1)
    r_direction = suitable_ways[l_rnd_idx]
    return r_direction


def check_direction(p_screensize, p_screen_position):
    """Returns True if the direction will be within
    screen bounds, otherwise returns False"""

    l_halfscreen = p_screensize // 2
    #   if -l_halfscreen <= p_screen_position <= l_halfscreen :
    #   r_direction_ok = True
    # else:
    #   r_direction_ok = False

    r_direction_ok = -l_halfscreen <= p_screen_position <= l_halfscreen

    # return_val = False if l_abs_position >= l_halfscreen else True

    # r_direction_ok = not l_abs_position >= l_halfscreen

    return r_direction_ok


def holding():
    print(t.screensize())
    print(t.position())
    t.setpos(200, -150)
    list(t.position())
    x_max = t.screensize()[0]
    y_max = t.screensize()[1]
    print(t.xcor())
    print(t.ycor())
    print(t.position())
    if t.xcor() + 10 >= x_max:
        t.setpos(0, 150)
    if t.ycor() + 10 >= y_max:
        t.setpos(200, 150)
    tmp = check_direction(x_max, t.xcor())
    print(tmp)
    t.setpos(100, 150)
    print(t.xcor())
    print(t.ycor())
    if -x_max / 2 <= t.xcor() <= x_max / 2:
        print("x in range")


def main():
    to_angle = 0.00
    t.mode(mode='logo')
    used_ways = []
    for _ in range(1, 101):
        direction_ok = False

        while not direction_ok:
            # choose next direction
            used_ways.append(next_direction())
            to_angle = (used_ways[-1]) * 90
            # direction_ok = check_direction()
            x_max = t.screensize()[0]
            y_max = t.screensize()[1]

            l_halfscreen_x = x_max // 2
            l_halfscreen_y = y_max // 2

            x_coord = t.xcor() + 25
            y_coord = t.ycor() + 25
            x_direction_ok = -l_halfscreen_x <= x_coord <= l_halfscreen_x
            y_direction_ok = -l_halfscreen_y <= y_coord <= l_halfscreen_y

            # y_direction_ok = False
            if used_ways[-1] in (1, 3) and not x_direction_ok:
                remove_way = suitable_ways.index(used_ways[-1])
                suitable_ways.pop(remove_way)
                direction_ok = False
            elif used_ways[-1] in (0, 2) and not y_direction_ok:
                remove_way = suitable_ways.index(used_ways[-1])
                suitable_ways.pop(remove_way)
                direction_ok = False
            else:

                direction_ok = True

        t.setheading(to_angle)
        t.forward(20)
        update_suitable_ways = []
        for a in used_ways:
            update_suitable_ways.append(opposite_ways[a])

        tmp = [x for x in possible_ways if x not in update_suitable_ways]
        tmp.sort()
        suitable_ways[:] = tmp


main()

t.exitonclick()
