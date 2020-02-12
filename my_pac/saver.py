from my_pac.point import Point
import os


class Save:
    def save(self, spaceship, asteroid, bonus, bomb):
        content = []
        for ship_point in spaceship.body:
            content.append(str(ship_point.x) + ';' + str(ship_point.y) + '\n')

        content_2 = []
        for aster_point in asteroid.asteroid_chain:
            content_2.append(str(aster_point.x) + ';' + str(aster_point.y) + '\n')

        content_3 = [str(bonus.bonus.x) + ';' + str(bonus.bonus.y) + '\n', str(bomb.bomb.x) + ';' + str(bomb.bomb.y) +
                     '\n', str(bonus.count) + '\n', str(bonus.check) + '\n', str(bomb.count) + '\n', str(bomb.check) +
                     '\n', str(asteroid.time) + '\n', str(asteroid.points)]

        with open('save_spaceship.csv', 'w') as f:
            f.writelines(content)

        with open('save_asteroids.csv', 'w') as f:
            f.writelines(content_2)

        with open('save_rest.csv', 'w') as f:
            f.writelines(content_3)

    def load(self, spaceship, asteroid, bonus, bomb):
        if os.path.exists('save_spaceship.csv'):
            with open('save_spaceship.csv', 'r') as f:
                content = f.readlines()
                spaceship.body = []
                for i in content:
                    parameters = i.split(';')
                    spaceship.body.append(Point(int(parameters[0]), int(parameters[1]), 'X'))
                spaceship.body[1].char = 'Ʌ'

        if os.path.exists('save_asteroids.csv'):
            with open('save_asteroids.csv', 'r') as f:
                content_2 = f.readlines()
                asteroid.asteroid_chain = []
                for i in content_2:
                    parameters = i.split(';')
                    asteroid.asteroid_chain.append(Point(int(parameters[0]), int(parameters[1]), '@'))

        if os.path.exists('save_rest.csv'):
            with open('save_rest.csv', 'r') as f:
                content_3 = f.readlines()
                parameters = content_3[0].split(';')
                bonus.bonus.x = int(parameters[0])
                bonus.bonus.y = int(parameters[1])

                parameters = content_3[1].split(';')
                bomb.bomb.x = int(parameters[0])
                bomb.bomb.y = int(parameters[1])

                bonus.count = int(content_3[2])
                bonus.check = bool(content_3[3])

                bomb.count = int(content_3[4])
                bomb.check = bool(content_3[5])

                asteroid.time = float(content_3[6])
                asteroid.points = int(content_3[7])
