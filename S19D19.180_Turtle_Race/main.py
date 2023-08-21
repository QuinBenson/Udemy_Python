from turtle import Turtle, Screen
import random

runner_colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
                  "wheat", "SlateGray"]


class Runner:

    def __init__(self, p_runner_number, p_runner_colour):
        self.runner_position = [0, 0]
        self.runner_movement = 10
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


def runner_move():
    finish = False
    while not finish:
        for runner in runner_list:
            runner.turtle.forward(random.randint(-5, 5) + 10)
            if runner.turtle.xcor() + 20 >= screen.window_width()/2:
                finish = True


def main():
    user_bet = screen.textinput("Bet", "what colour d'y'think?")

    runner_create()

    runner_move()

    screen.exitonclick()


main()
