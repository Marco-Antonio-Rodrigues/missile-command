import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from time import sleep
from random import randint

from app.explosion import Explosion, list_explosion
from app.asteroids import Asteroids, list_asteroids
from app.colision import list_colision
from app.scoreboard import draw_scoreboard
from app.hp import draw_lifeboard
from app.contants import HEIGHT,WIDTH,HEIGHT_WORLD,WIDTH_WORLD
from app.utils import load_texture,tela_for_mundo
#configurações iniciais
pg.init()
pg.display.set_caption('Missile Command')
pg.mouse.set_cursor(*pg.cursors.diamond)
CLOCK = pg.time.Clock()
display = (WIDTH, HEIGHT)
CANVAS = pg.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

glOrtho(-WIDTH_WORLD/2,WIDTH_WORLD/2,-HEIGHT_WORLD/2,HEIGHT_WORLD/2,-1,1)

glEnable(GL_TEXTURE_2D)                             #habilitando o uso de texturas
glEnable(GL_BLEND);                                 #habilitando a funcionalidade de mistura (necessário para objetos transparentes)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)   #definindo como a mistura entre objetos transparência deve ser realizada

texture_galaxy = load_texture('galaxia.jpg')   
texture_planet = load_texture('planet.jpg')   
texture_game_over = load_texture('game_over.png') 

def scenario(width,height):  
    #Desenhando galaxy    
    glColor((0,0,0))
    glPushMatrix()
    glTranslatef(0,height,0)
    glScalef(width,height+height*0.85,1)
    glBindTexture(GL_TEXTURE_2D, texture_galaxy)    #tornando a textura 1 ativa 
    glBegin(GL_QUADS)
    
    glTexCoord2f(0,0) ,glVertex3f(-1,-1,1)
    glTexCoord2f(1,0) ,glVertex3f(1,-1,1)
    glTexCoord2f(1,1) ,glVertex3f(1,1,1)
    glTexCoord2f(0,1) ,glVertex3f(-1,1,1)
    
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)     #desativando todas as texturas
    glPopMatrix()
      
    #Desenhando Base
    glColor((1,1,0))
    glPushMatrix()
    glTranslatef(0,-height+(height*0.15),0)
    glScalef(width,height*0.15,1)
    glBindTexture(GL_TEXTURE_2D, texture_planet)    #tornando a textura 1 ativa 
    glBegin(GL_QUADS)
    
    glTexCoord2f(0,0) ,glVertex3f(-1,-1,1)
    glTexCoord2f(1,0) ,glVertex3f(1,-1,1)
    glTexCoord2f(1,1) ,glVertex3f(1,1,1)
    glTexCoord2f(0,1) ,glVertex3f(-1,1,1)
    
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)     #desativando todas as texturas
    glPopMatrix()
    glFlush()

def game_over(width,height):
    #Desenhando game over
    glColor((1,1,0))
    glPushMatrix()
    glScalef(width/4,height/4,1)
    glBindTexture(GL_TEXTURE_2D, texture_game_over)    #tornando a textura 1 ativa 
    glBegin(GL_QUADS)
    
    glTexCoord2f(0,0) ,glVertex3f(-1,-1,1)
    glTexCoord2f(1,0) ,glVertex3f(1,-1,1)
    glTexCoord2f(1,1) ,glVertex3f(1,1,1)
    glTexCoord2f(0,1) ,glVertex3f(-1,1,1)
    
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)#desativando todas as texturas
    glPopMatrix()
    glFlush()
    pg.display.flip()

asteroids_killed = 0
life = 100

def draw(x,y):
    global asteroids_killed, life
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #limpa a tela
    scenario(WIDTH_WORLD/2,HEIGHT_WORLD/2)
    for explosion in list_explosion: #Atualiza o Status das Explosoes
        explosion.update()
    
    for asteroid in list_asteroids: #Atualiza o Status dos Asteroides
        if asteroid.update():
            life -= 20
            print(life)
    draw_lifeboard(life, 7.0,9.5)
  
    for colision in list_colision: #Atualiza o Status das colisões
        colision.update()
    draw_scoreboard(asteroids_killed,-9.5,9.5)
    pg.display.flip()#atualiza toda a tela
    
    for asteroid in list_asteroids: #Checa se uma explosão atingiu um asteroide
        for explosion in list_explosion:
            if asteroid.Colide(explosion.x,explosion.y,explosion.ray):
                asteroids_killed+=1
                break

def main():
    x = 0
    y = 0
    cond = 20 #Dificuldade, quanto mais perto do 0, mais asteroids aparecem
    global list_asteroids
    global list_explosion
    while True:
        if len(list_asteroids) < 20 and randint(-cond,cond) == 0: 
            Asteroids()
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                x, y = tela_for_mundo(x,HEIGHT-y)
                if y > -HEIGHT_WORLD/4:
                    Explosion(x=x,y=y)
        
        draw(x,HEIGHT-y)
        CLOCK.tick(60)
        if life == 0:
            game_over(WIDTH_WORLD,HEIGHT_WORLD)
            print('você perdeu!')
            sleep(5)
            quit()
        