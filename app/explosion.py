import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math
import random

list_explosion = []

class Explosion():
  def __init__(self, x=0, y=0,ray=1,edges=36):
    self.x = x
    self.y = y
    self.ray = ray
    self.edges = edges
    list_explosion.append(self)
    
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
    
    colors_list = [[(1,1,1),(0.5,0.5,0.5)],[(1,1,0),(0.5,0.6,0)],[(1,0,0.5),(0.5,0,0.1)]]
    number_random = random.randint(0,len(colors_list)-1)    
    
    glBegin(GL_TRIANGLE_FAN)
    glColor(colors_list[number_random][1])
    glVertex3f(pos_x,pos_y,1)
    glColor(colors_list[number_random][0])
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
    if self.ray < 2:
      self.ray+=0.004
      self.draw()
    else:
      list_explosion.remove(self)
      del self