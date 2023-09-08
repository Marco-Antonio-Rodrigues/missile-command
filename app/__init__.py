import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from app.draw import draw
pg.init()

pg.mouse.set_cursor(*pg.cursors.diamond)

INFO = pg.display.Info()

WIDTH = int(INFO.current_h * 0.8)
HEIGHT = int(INFO.current_h * 0.8)

display = (WIDTH, HEIGHT)
CANVAS = pg.display.set_mode(display, DOUBLEBUF|OPENGL)

CLOCK = pg.time.Clock()

pg.display.set_caption('Missile Command')

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glTranslatef(0.0, 0.0, -5)

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw()
        pg.display.flip()
        CLOCK.tick(60)