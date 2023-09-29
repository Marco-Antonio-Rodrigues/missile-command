import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from time import sleep
from random import randint


from app.explosion import Explosion, list_explosion
from app.asteroids import Asteroids, list_asteroids
from app.colision import list_colision
from app.scenario import scenario
from app.scoreboard import draw_scoreboard
#configurações iniciais
pg.init()
pg.display.set_caption('Missile Command')
pg.mouse.set_cursor(*pg.cursors.diamond)
CLOCK = pg.time.Clock()

WIDTH = 600
HEIGHT = 600
WIDTH_WORLD = 20
HEIGHT_WORLD = 20

display = (WIDTH, HEIGHT)
CANVAS = pg.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

glOrtho(-WIDTH_WORLD/2,WIDTH_WORLD/2,-HEIGHT_WORLD/2,HEIGHT_WORLD/2,-1,1)

def tela_for_mundo(x_tela, y_tela):
    x_tela_centro = x_tela - WIDTH / 2
    y_tela_centro = y_tela - HEIGHT / 2
    x_mundo = x_tela_centro * (20 / WIDTH)
    y_mundo = y_tela_centro * (20 / HEIGHT)
    return x_mundo, y_mundo

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
            print('você perdeu!')
            sleep(2)
            quit()
        