from my_pac.point import Point


class Bonus:
    def __init__(self, size_x):
        self.bonus = Point(-1, -1, '+')
        self.size_x = size_x
        self.count = 0
        self.check = False

    def move(self, y):
        if self.count < 40:
            self.count += 1
        else:
            self.bonus = Point(0, y, '+')
            self.count = 0
            self.check = True
        if self.check:
            self.bonus.x += 1
        if self.bonus.x == self.size_x:
            self.bonus = Point(-1, -1, '+')
            self.check = False

    def remove_bonus(self):
        self.bonus = Point(-1, -1, '+')
        self.check = False
