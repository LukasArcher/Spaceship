from my_pac.point import Point


class Bomb:
    def __init__(self, size_x):
        self.bomb = Point(-1, -1, 'Ó')
        self.size_x = size_x
        self.count = 0
        self.check = False

    def move(self, y):
        if self.count < 100:
            self.count += 1
        else:
            self.bomb = Point(0, y, 'Ó')
            self.count = 0
            self.check = True
        if self.check:
            self.bomb.x += 1
        if self.bomb.x == self.size_x:
            self.bomb = Point(-1, -1, 'Ó')
            self.check = False

    def remove_bomb(self):
        self.bomb = Point(-1, -1, 'Ó')
        self.check = False
