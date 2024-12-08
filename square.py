class Square:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start = (start_x, start_y)
        self.end = (end_x, end_y)
        self.number = 0

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def is_empty(self):
        return self.number == 0

    def __repr__(self):
        return f"Square(start={self.start}, end={self.end}, number={self.number})"
