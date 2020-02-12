#!/usr/bin/python
# -*- coding: UTF-8 -*-


from my_pac.point import Point


class Spaceship:
    def __init__(self, x, y, size_y):
        self.body = [Point(x - 2, y, 'X'), Point(x - 3, y, 'Ʌ'), Point(x - 2, y - 1, 'X'), Point(x - 2, y + 1, 'X')]
        self.size_y = size_y
        self.direction = Point(0, 0, '')
        self.shot_chain = []
        self.shot_direction = Point(-1, 0, '')

    def move(self):
        for i in range(len(self.body)):
            self.body[i].x += self.direction.x
            self.body[i].y += self.direction.y
        if self.body[0].y == 0:
            self.body[0].y = 1
        elif self.body[0].y == self.size_y - 1:
            self.body[0].y = self.size_y - 2

        if self.body[1].y == 0:
            self.body[1].y = 1
        elif self.body[1].y == self.size_y - 1:
            self.body[1].y = self.size_y - 2

        if self.body[2].y == -1:
            self.body[2].y = 0
        elif self.body[2].y == self.size_y - 2:
            self.body[2].y = self.size_y - 3

        if self.body[3].y == 1:
            self.body[3].y = 2
        elif self.body[3].y == self.size_y:
            self.body[3].y = self.size_y - 1

    def shot(self):
        self.shot_chain.append((Point(x=self.body[1].x, y=self.body[1].y, char='*')))

    def move_shot(self):
        if len(self.shot_chain) >= 1:
            for i in reversed(range(len(self.shot_chain))):
                self.shot_chain[i].x += self.shot_direction.x
                if self.shot_chain[i].x == -1:
                    del self.shot_chain[i]

    def remove_shots(self):
        self.shot_chain = []
