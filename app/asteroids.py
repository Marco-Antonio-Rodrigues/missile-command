import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math
import random
  
list_asteroids = []


class Asteroids():
  
  
  def __init__(self):
    self.x = random.randint(-9,9)
    self.y = 10
    self.ray = 0.2 * random.randint(0,2)
    self.edges = 36
    list_asteroids.append(self)
    
  def draw(self,pos_x=None,pos_y=None,ray=None,edges = None):
    if pos_x:
      self.x = pos_x
    if pos_y:
      self.y = pos_y
    if ray:
      self.ray = ray
    if edges:
      self.edges = edges
        
    pos_x = self.x
    pos_y = self.y
        
    
    glColor((1,1,1))
    
          
    
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(pos_x,pos_y,1)
    for aresta in range(0,self.edges):
      pos_x = self.ray*math.cos(aresta*(2*math.pi/self.edges))
      pos_y = self.ray*math.sin(aresta*(2*math.pi/self.edges))
      glVertex3f(pos_x+self.x,pos_y+self.y,1)
      
    pos_x = self.ray*math.cos(0)
    pos_y = self.ray*math.sin(0)
    glVertex3f(pos_x+self.x, pos_y+self.y ,1)
    glEnd()

    glFlush() #Todas as instruções anteriores apenas indicaram o que deve ser feito. Essa Ã© a ordem pra GPU redesenhar com as informaÃ§Ãµes enviadas
    
  def update(self):
    if self.y > -5.5:
      self.y-=0.01
      self.draw()
    else:
      self.ray = 0
      list_asteroids.remove(self)
    