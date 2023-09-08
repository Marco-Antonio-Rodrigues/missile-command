import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    glBegin(GL_QUADS)
    glVertex3f(0,0,1)
    glVertex3f(1,0,1)
    glVertex3f(1,1,1)
    glVertex3f(0,1,1)
    glEnd()
    
        