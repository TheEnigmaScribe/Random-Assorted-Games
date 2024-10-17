import pygame as pg
from settings import *
from os import path

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, pdir):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pdir = pdir
        xval = str(x)
        yval = str(y)
        print(xval +", " + yval)

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy) and not self.collide_with_enemy(dx, dy):
            self.x += dx
            self.y += dy
            playerx = x
            playery = y
            if dx or dy != 0:
                xval = str(self.x)
                yval = str(self.y)
                print(xval + ", " + yval)
            if dx < 0:
                dirstr = "LEFT"
            if dx > 0:
                dirstr = "RIGHT"
            if dy < 0:
                dirstr = "UP"
            if dy > 0:
                dirstr = "DOWN"
            if dirstr == "LEFT" or "RIGHT" or "UP" or "DOWN":
                pass
            

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if (wall.x == self.x + dx) and (wall.y == self.y + dy):
                return True
        return False
   
    def collide_with_enemy(self, dx=0, dy=0):
        for enemy in self.game.enemy:
            if (self.x + dx == enemy.x) and (self.y + dy == enemy.y):
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y, playerx, playery, edir):
        self.groups = game.all_sprites, game.enemy
        pg.sprite.Sprite.__init__(self, self.groups)
        img_dir = path.join(path.dirname(__file__), 'Sprites')
        self.game = game
        if edir == 1:
            eleft = pg.image.load(path.join(img_dir, "EnemyLeft.png")).convert()
            self.eleft = eleft
            self.image = pg.transform.scale(eleft, (TILESIZE, TILESIZE))
        if edir == 2:
            eup = pg.image.load(path.join(img_dir, "EnemyUp.png")).convert()
            self.eup = eup
            self.image = pg.transform.scale(eup, (TILESIZE, TILESIZE))
        if edir == 3:
            eright = pg.image.load(path.join(img_dir, "EnemyRight.png")).convert()
            self.eright = eright
            self.image = pg.transform.scale(eright, (TILESIZE, TILESIZE))
        if edir == 4:
            edown = pg.image.load(path.join(img_dir, "EnemyDown.png")).convert()
            self.edown = edown
            self.image = pg.transform.scale(edown, (TILESIZE, TILESIZE))
        print(str(edir))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.edir = edir
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def update(self, playerx, playery):
        if (playerx <= self.x) and (playery == self.y) and edir == 1:
            self.image.fill(WHITE)
        if (playerx >= self.x) and (playery == self.y) and edir == 3:
            self.image.fill(WHITE)
        if (playery <= self.y) and (playerx == self.x) and edir == 2:
            self.image.fill(WHITE)
        if (playery >= self.y) and (playerx == self.x) and edir == 4:
            self.image.fill(WHITE)
        # add shooting functionality later

    def shoot(self):
        bullet = Bullet(x, y, edir)

    def death(self):
        if (game.player.x + dx == self.x) and (game.player.y + dy == self.y):
            self.kill()
            
class Bullet(pg.sprite.Sprite):
    def __init__(self, game, x, y, edir):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self.self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.dir = edir
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def update(self):
        if dir == 1:
            x -= 1
        if dir == 2:
            y -= 1
        if dir == 3:
            x += 1
        if dir == 4:
            y += 1

class Target(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.target
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE