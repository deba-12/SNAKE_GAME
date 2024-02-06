from turtle import Turtle, Screen

steps = 20
screen = Screen()
starting_position = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.x_coordinate = self.head.xcor()
        self.y_coordinate = self.head.ycor()

    def create_snake(self):
        for position in starting_position:
            self.add_seg(position)

    def add_seg(self,position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_seg(self.segment[-1].position())

    def move(self):

        for seg in range(len(self.segment) - 1, 0, -1):
            self.segment[seg].goto(self.segment[seg - 1].xcor(), self.segment[seg - 1].ycor())
        self.segment[0].forward(steps)

    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(90)

        # self.move()

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(270)

        # self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(0)

        # self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(180)

        # self.move()
