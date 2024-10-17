# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 1
# Video link: https://www.youtube.com/watch?v=uWvb3QzA48c
# Project setup

import pygame as pg
import sys
import json
from os import path
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
    
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.tilemap_data = []
        with open(path.join(game_folder, 'LevelData', 'Lvl1Tiles.txt'), 'rt') as f:
            for line in f:
                self.tilemap_data.append(line)
    
    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemy = pg.sprite.Group()
        self.target = pg.sprite.Group()
        for row, tiles in enumerate(self.tilemap_data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                    self.player = Player(self, col, row, pdir=2)
                if tile == '#':
                    Wall(self, col, row)
                if tile == 'T':
                    Target(self, col, row)
                if tile == 'L':
                    Enemy(self, col, row, playerx=-1, playery=-1, edir=1)
                if tile == 'R':
                    Enemy(self, col, row, playerx=-1, playery=-1, edir=3)
                if tile == 'U':
                    Enemy(self, col, row, playerx=-1, playery=-1, edir=2)
                if tile == 'D':
                    Enemy(self, col, row, playerx=-1, playery=-1, edir=4)
        

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)


    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()