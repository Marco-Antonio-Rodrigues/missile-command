import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from app.explosion import Explosion, list_explosion

#configurações iniciais
pg.init()
pg.display.set_caption('Missile Command')
pg.mouse.set_cursor(*pg.cursors.diamond)
CLOCK = pg.time.Clock()

HEIGHT = 600
WIDTH = 600
display = (WIDTH, HEIGHT)
CANVAS = pg.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

gluPerspective(45, (WIDTH/HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
glOrtho(-10,10,-10,10,-1,1)

def tela_for_mundo(x_tela, y_tela):
    x_tela_centro = x_tela - WIDTH / 2
    y_tela_centro = y_tela - HEIGHT / 2
    x_mundo = x_tela_centro * (50 / WIDTH)
    y_mundo = y_tela_centro * (50 / HEIGHT)
    return x_mundo, y_mundo

def draw(x,y):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #limpa a tela
    
    for explosion in list_explosion:
        explosion.update()
        
    pg.display.flip()#atualiza toda a tela

def main():
    global list_explosion
    x = 0
    y = 0
    while True:
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
        