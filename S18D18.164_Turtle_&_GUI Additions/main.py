import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]


class Tettle:
    def __init__(self):

        #     self.internal_name = p_internal_name
        self.tim = t.Turtle()

        self.opposite_ways = (2, 3, 0, 1)
        self.possible_ways = [0, 1, 2, 3]
        self.suitable_ways = list(self.possible_ways)
        self.going_to = -1
        self.coming_from = -1
        self.pen_size = 12
        self.pen_step = 30

    def check_direction(self, p_screensize, p_screen_position):
        """Returns True if the direction will be within
        screen bounds, otherwise returns False"""
        summation = abs(p_screen_position) + self.pen_size + self.pen_step
        if summation >= int(p_screensize // 2):
            return_val = False
        else:
            return_val = True

        return return_val

    def next_direction(self):
        r_direction = self.suitable_ways[random.randint(0, len(self.suitable_ways) - 1)]
        return r_direction

    def the_turtle_moves(self):
        used_directions = []
        # some kind of loop
        for _ in range(1, 1001):
            direction_ok = False
            # some kind of loop
            while not direction_ok:
                # choose next direction

                used_directions.append(self.next_direction())
                #  check if direction is safe
                if used_directions[-1] in (1, 3):
                    direction_ok = self.check_direction(t.window_width(), self.tim.xcor())
                else:
                    direction_ok = self.check_direction(t.window_height(), self.tim.ycor())

               # direction_ok = False
                # todo adjust possible directions
                if not direction_ok:
                    mm = self.suitable_ways.index(used_directions[-1])
                    self.suitable_ways.pop(mm)

            # move in direction selected
            to_angle = (used_directions[-1]) * 90
            self.tim.setheading(to_angle)
            self.tim.pendown()
            self.tim.forward(self.pen_step)
            self.tim.penup()
            self.tim.forward(int(self.pen_size // 2))
            # todo set possible directions & update coming from/going to
            self.suitable_ways = list(self.possible_ways)

            marker.undo()  # erase previous position

            marker.write(self.tim.pos(), align='center', font=FONT)

            ses = []
            for a in used_directions:
                 ses.append(self.opposite_ways[a])
            res = [x for x in self.suitable_ways if x not in ses]

            self.suitable_ways[:] = res

            used_directions = []
            # todo check if the alternative directions are all suitable. eg previous = 1, next = 2;
            # todo at bottom edge, 2 is bad, alternates are only 0 and 3. 1 does not get a look in.
            # todo MAYBE keep a list of unsuitable ways in the main loop and then remove them at the
            # todo end of the iteration?

FONT = ('Arial', 24, 'normal')
marker = t.Turtle(visible=False)  # our virtual magic marker
def main():

    y = Tettle()


    marker.penup()
    marker.color("darkgreen")
    marker.setposition(200, 200)
    marker.write((0,0), align='center', font=FONT)  # so we can undo it
    y.the_turtle_moves()
    y.tim.forward(50)
    t.exitonclick()


main()
