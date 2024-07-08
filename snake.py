from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            # time.sleep(0.5)
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # if self.segments[-1].heading() == RIGHT:
        #     self.add_segment((self.segments[-1].xcor()-20, self.segments[-1].ycor()))
        # elif self.segments[-1].heading() == UP:
        #     self.add_segment((self.segments[-1].xcor(), self.segments[-1].ycor()-20))
        # elif self.segments[-1].heading() == LEFT:
        #     self.add_segment((self.segments[-1].xcor() + 20, self.segments[-1].ycor()))
        # elif self.segments[-1].heading() == DOWN:
        #     self.add_segment((self.segments[-1].xcor(), self.segments[-1].ycor()+20))
        # else:
        #     pass
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # self.segments[0].left(90)
        # self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # self.segments[0].left(270)
        # self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # self.segments[0].left(180)
        # self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # self.segments[0].left(0)
        # self.move()

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
