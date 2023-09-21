import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from time import sleep
from random import randint

from app.explosion import Explosion,list_explosion
from app.asteroids import Asteroids

#configurações iniciais
pg.init()
pg.display.set_caption('Missile Command')
pg.mouse.set_cursor(*pg.cursors.diamond)
CLOCK = pg.time.Clock()

HEIGHT = 600
WIDTH = 600
display = (WIDTH, HEIGHT)
CANVAS = pg.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

glOrtho(-10,10,-10,10,-1,1)

def tela_for_mundo(x_tela, y_tela):
    x_tela_centro = x_tela - WIDTH / 2
    y_tela_centro = y_tela - HEIGHT / 2
    x_mundo = x_tela_centro * (20 / WIDTH)
    y_mundo = y_tela_centro * (20 / HEIGHT)
    return x_mundo, y_mundo

def draw(x,y):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #limpa a tela
    for asteroid in Asteroids.list_asteroids:
        asteroid.update()
    for explosion in list_explosion:
        explosion.update()
        
    pg.display.flip()#atualiza toda a tela

def main():
    x = 0
    y = 0
    cond = 50 #Dificuldade, quanto mais perto do 0, mais asteroids aparecem
    
    while True:
        if len(Asteroids.list_asteroids) < 20 and randint(-cond,cond) == 0: 
            Asteroids()
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                x, y = tela_for_mundo(x,HEIGHT-y)
                Explosion(x=x,y=y)
                
        draw(x,HEIGHT-y)
        CLOCK.tick(60)
        