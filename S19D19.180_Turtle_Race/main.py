from turtle import Turtle, Screen
from random import randint
from operator import attrgetter

runner_colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
                  "wheat", "SlateGray"]


class Runner:

    def __init__(self, p_runner_number, p_runner_colour):
        self.runner_position = [0, 0]
        self.runner_movement = randint(9, 11)
        self.winner = False
        self.finish_position = 0
        self.runner_number = p_runner_number
        self.turtle = Turtle(shape="turtle")
        self.turtle.color(p_runner_colour)


screen = Screen()
screen.setup(width=600, height=400)
runner_list = []


def runner_create():
    for i, col in enumerate(runner_colours):
        runner_list.append(Runner(i, col))
        runner_to_start(runner_list[-1], i)


def runner_to_start(p_runner, p_runner_number):
    p_runner.turtle.up()
    x_width = screen.window_width()
    y_height = screen.window_height()
    x_pos = -x_width / 2 + 10
    y_pos = (y_height - 40) / 2 - p_runner_number * (y_height / len(runner_colours))
    p_runner.turtle.goto(x_pos, y_pos)
    p_runner.runner_position = [x_pos, y_pos]


def runner_move():
    finish = False
    l_finish_position = 0
    while not finish:

        for runner in runner_list:
            runner.turtle.forward(
                randint(int(-runner.runner_movement // 2), int(runner.runner_movement // 2)) + runner.runner_movement)

            runner.runner_position = runner.turtle.position()

            if runner.turtle.xcor() + 20 >= screen.window_width() / 2 and runner.finish_position == 0:
                if l_finish_position == 0:
                    runner.winner = True

                l_finish_position += 1
                runner.finish_position = l_finish_position

            if l_finish_position == len(runner_list):
                finish = True


def main():
    user_bet = screen.textinput("Bet", "what colour d'y'think?")

    runner_create()

    runner_move()

    # yes, I could have simply passed the winner back from the runner_move() function,
    # but this way I learned something new.
    min_thing = min(runner_list, key=attrgetter("finish_position"))
    min_thing.turtle.setheading(min_thing.turtle.towards(0, 0))
    min_thing.turtle.goto(0,0)
    min_thing.turtle.setheading(min_thing.turtle.towards(0, 1))

    min_thing.turtle.shapesize(10, 10, 1)

    screen.exitonclick()


main()
