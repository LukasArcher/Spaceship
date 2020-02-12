from random import randint
from time import sleep
from my_pac.point import Point
from my_pac.asteroids import Asteroids
from my_pac.spaceship import Spaceship
from my_pac.map import Map
from my_pac.bonus import Bonus
from my_pac.bomb import Bomb
from my_pac.saver import Save
from my_pac.get_key import GetKey, ClearConsole


my_map = Map(size_x=20, size_y=10)
my_spaceship = Spaceship(x=20, y=5, size_y=10)
my_asteroids = Asteroids(size_x=20)
my_bonus = Bonus(size_x=20)
my_bomb = Bomb(size_x=20)
my_save = Save()
get_key = GetKey()
game_over = False
move_aster = True
dont_move_aster = False

while True:
    my_map.clear_table()
    ClearConsole()
    key = get_key()
    stop_loop = False

    if key == 27:
        break
    if key == 0:
        my_spaceship.direction.y = 0
    if key == 299:
        my_spaceship.direction.y = -1
    if key == 301:
        my_spaceship.direction.y = 1
    if key == 32:
        my_spaceship.direction.y = 0
        my_spaceship.shot()
    if key == 115:
        my_save.save(my_spaceship, my_asteroids, my_bonus, my_bomb)
    if key == 108:
        my_save.load(my_spaceship, my_asteroids, my_bonus, my_bomb)

    my_spaceship.move()
    if move_aster:
        my_asteroids.move(y=randint(1, 8))
        move_aster = False
        dont_move_aster = False

    if dont_move_aster:
        move_aster = True

    if not move_aster:
        dont_move_aster = True

    my_bonus.move(y=randint(1, 8))
    my_bomb.move(y=randint(1, 8))

    for s in range(len(my_spaceship.shot_chain)):
        for i in range(len(my_asteroids.asteroid_chain)):
            if my_spaceship.shot_chain[s].x == my_asteroids.asteroid_chain[i].x:
                if my_spaceship.shot_chain[s].y == my_asteroids.asteroid_chain[i].y:
                    del my_asteroids.asteroid_chain[i]
                    del my_spaceship.shot_chain[s]
                    my_asteroids.points += 1
                    stop_loop = True
                    break
        if stop_loop:
            break

    my_spaceship.move_shot()

    for asteroid_point in my_asteroids.asteroid_chain:
        my_map.set_value(asteroid_point.x, asteroid_point.y, asteroid_point.char)

    for spaceship_point in my_spaceship.body:
        my_map.set_value(spaceship_point.x, spaceship_point.y, spaceship_point.char)

    for shot_point in my_spaceship.shot_chain:
        my_map.set_value(shot_point.x, shot_point.y, shot_point.char)

    my_map.set_value(my_bonus.bonus.x, my_bonus.bonus.y, my_bonus.bonus.char)
    my_map.set_value(my_bomb.bomb.x, my_bomb.bomb.y, my_bomb.bomb.char)

    for s in range(len(my_spaceship.shot_chain)):
        for i in range(len(my_asteroids.asteroid_chain)):
            if my_spaceship.shot_chain[s].x == my_asteroids.asteroid_chain[i].x or my_asteroids.asteroid_chain[i].x == \
                    my_spaceship.shot_chain[s].x - 1:
                if my_spaceship.shot_chain[s].y == my_asteroids.asteroid_chain[i].y:
                    del my_asteroids.asteroid_chain[i]
                    del my_spaceship.shot_chain[s]
                    my_asteroids.points += 1
                    stop_loop = True
                    break
        if stop_loop:
            break

    for spaceship_point in my_spaceship.body:
        for asteroid_point in my_asteroids.asteroid_chain:
            if spaceship_point.x == asteroid_point.x and spaceship_point.y == asteroid_point.y:
                game_over = True

    for spaceship_point in my_spaceship.body:
        if spaceship_point.x == my_bonus.bonus.x and spaceship_point.y == my_bonus.bonus.y:
            my_bonus.bonus = Point(-1, -1, '+')
            my_bonus.check = False
            my_asteroids.time += 0.04

    for spaceship_point in my_spaceship.body:
        if spaceship_point.x == my_bomb.bomb.x and spaceship_point.y == my_bomb.bomb.y:
            my_bomb.bomb = Point(-1, -1, '+')
            my_bomb.check = False
            for i in reversed(range(len(my_asteroids.asteroid_chain))):
                my_asteroids.asteroid_chain[i].char = '*'
                my_map.set_value(my_asteroids.asteroid_chain[i].x, my_asteroids.asteroid_chain[i].y,
                                 my_asteroids.asteroid_chain[i].char)
                my_asteroids.points += 1
                del my_asteroids.asteroid_chain[i]

    my_map.print_table()
    print('Points:', my_asteroids.points)
    if game_over:
        print('GAME OVER')
        print("Press'Enter' to repeat, press 'Esc' to quit.")
        while True:
            key = get_key()
            if key == 13:
                game_over = False
                my_asteroids.points = 0
                my_asteroids.time = 0.3
                my_asteroids.remove_asteroids()
                my_spaceship.remove_shots()
                my_bonus.remove_bonus()
                my_bomb.remove_bomb()
                break
            if key == 27:
                break
    if game_over:
        break
    print(my_asteroids.time)
    sleep(my_asteroids.time)
