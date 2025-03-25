from turtle import *


class Boxes:

    def __init__(self):
        self.all_boxes = []

    def create_boxes(self, x, y):
        new_box = Turtle(shape="square")
        new_box.color("white")
        new_box.shapesize(stretch_wid=2, stretch_len=4)  # Adjust size if needed
        new_box.penup()
        new_box.goto(x, y)
        self.all_boxes.append(new_box)

    def get_on_line(self):
        num_columns = 8

        # Create first row (y=200)
        for i in range(num_columns):
            x_position = -355 + i * 100
            self.create_boxes(x_position, 200)

        # Create second row (y=150)
        for b in range(num_columns):
            x_position = -355 + b * 100
            self.create_boxes(x_position, 150)


