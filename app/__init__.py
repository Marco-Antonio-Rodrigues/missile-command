import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



def main():
    pg.init()
    display = (1680, 1050)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pg.display.flip()
        pg.time.wait(10)