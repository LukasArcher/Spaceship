from my_pac.point import Point
import sys


class Asteroids:
    def __init__(self, size_x):
        self.asteroid_chain = []
        self.size_x = size_x
        self.time = 0.3
        self.points = 0

    def move(self, y):
        self.asteroid_chain.append(Point(0, y, '@'))
        if self.time >= 0.02:
            self.time -= 0.003
        for i in reversed(range(len(self.asteroid_chain))):
            self.asteroid_chain[i].x += 1
            if self.asteroid_chain[i].x == self.size_x:
                del self.asteroid_chain[i]

    def remove_asteroids(self):
        self.asteroid_chain = []

print(sys.path)