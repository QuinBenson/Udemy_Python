from turtle import Screen, Turtle


class Segment:

    def __init__(self, p_segment_no, p_segment_position):
        self.segment_position = p_segment_position
        self.runner_movement = 20
        self.segment_turtle = Turtle(shape="square")
        self.segment_turtle.color("white")
        self.segment_turtle.goto(p_segment_position)


def main():
    segment_list = []
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snakies!')

    for i in range(0, 2):
        start_position_x = 0 - i * 20
        segment_list.append(Segment(i, [start_position_x, 0]))

    screen.exitonclick()


main()
