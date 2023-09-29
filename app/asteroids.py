import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math
import random
from app.colision import Colision


list_asteroids = []


class Asteroids():
  
  
  def __init__(self):
    self.x = random.randint(-9,9)
    self.y = 10
    self.ray = 0.2 * random.randint(1,2)
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
  
  def Colide(self,x=None,y=None,ray=None):
    if x and y and ray:
      distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
      if distance < self.ray or distance < ray:
        Colision(self.x,self.y)
        list_asteroids.remove(self)#Remove asteroide atingido
        del self
        return True
    return False
  
  def update(self):
    if self.y > -6.5:
      self.y-=0.02
      self.draw()
      return False
    else:
      Colision(self.x,self.y-self.ray)
      list_asteroids.remove(self)#Remove asteroide atingido
      del self
      return True