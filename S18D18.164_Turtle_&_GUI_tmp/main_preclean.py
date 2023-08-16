import random
import turtle as t

reverse_directions = (2, 3, 0, 1)
all_directions = (0, 1, 2, 3)
possibilities = list(all_directions)
# if the next direction is 0 then plus y
# if the next direction is 1 then plus x
# if the next direction is 2 then minus y
# if the next direction is 3 then minus x
direction_mods = [[0, 25], [25, 0], [0, -25], [-25, 0]]

def next_direction():
    l_list_len = len(possibilities)
    l_rnd_idx = random.randint(0, l_list_len - 1)
    r_direction = possibilities[l_rnd_idx]
    return r_direction


def check_direction(p_used_direction):
    """Returns True if the direction will be within
    screen bounds, otherwise returns False"""

    x_max = t.screensize()[0]
    y_max = t.screensize()[1]

    l_half_screen_x = x_max // 2
    l_half_screen_y = y_max // 2

    # if p_used_direction == 0:
    #     x_modval = 0
    #     y_modval = 25
    # elif p_used_direction == 1:
    #     x_modval = 25
    #     y_modval = 0
    # elif p_used_direction == 2:
    #     x_modval = 0
    #     y_modval = -25
    # else:
    #     x_modval = -25
    #     y_modval = 0

    # x_coord = t.xcor() + x_modval
    # y_coord = t.ycor() + y_modval
    x_coord = t.xcor() + direction_mods[p_used_direction][0]
    y_coord = t.ycor() + direction_mods[p_used_direction][1]

    x_direction_ok = -l_half_screen_x <= x_coord <= l_half_screen_x
    y_direction_ok = -l_half_screen_y <= y_coord <= l_half_screen_y

    if p_used_direction in (1, 3) and not x_direction_ok:
        r_direction_ok = False
    elif p_used_direction in (0, 2) and not y_direction_ok:
        r_direction_ok = False
    else:
        r_direction_ok = True
    return r_direction_ok


def main():
    t.mode(mode='logo')
    l_dir = next_direction()
    used_direction = [l_dir]
    possibilities.pop(reverse_directions[l_dir])
    to_angle = (used_direction[-1]) * 90

    for _ in range(1, 1001):
        direction_ok = False
        while not direction_ok:
            if check_direction(used_direction[-1]):
                t.setheading(to_angle)
                t.forward(20)
                possibilities[:] = list(all_directions)
                possibilities.pop(reverse_directions[used_direction[-1]])
                direction_ok = True

            else:

                possibilities.pop(possibilities.index(used_direction[-1]))
            # choose next direction
            l_dir = next_direction()
            used_direction = [l_dir]
            to_angle = (used_direction[-1]) * 90


main()
t.exitonclick()