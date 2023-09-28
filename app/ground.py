import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


class Ground():
  
  def __init__(self):      
    
    #Desenhando Base
    glColor((1,1,0))
    
    glPushMatrix()
    glScalef(2,1,0)
    glTranslatef(0,-6,0)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex3f(-5,0,1)
    glVertex3f(5,0,1)
    glVertex3f(-5,-5,1)
    glVertex3f(5,-5,1)
    
    glEnd()
    glPopMatrix()
    glFlush() #Todas as instruções anteriores apenas indicaram o que deve ser feito. Essa Ã© a ordem pra GPU redesenhar com as informaÃ§Ãµes enviadas
    

    