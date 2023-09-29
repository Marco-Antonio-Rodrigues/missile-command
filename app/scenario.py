from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
  
def scenario(width,height):      
    #Desenhando Base
    glColor((1,1,0))
    glPushMatrix()
    
    glTranslatef(0,-height+(height*0.15),0)
    glScalef(width,height*0.15,1)
    glBegin(GL_QUADS)
    glVertex3f(-1,-1,1)
    glVertex3f(1,-1,1)
    glVertex3f(1,1,1)
    glVertex3f(-1,1,1)
    glEnd()
    
    glPopMatrix()
    glFlush()
    

    