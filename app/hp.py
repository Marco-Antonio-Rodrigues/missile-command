import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# Dicionário que define a representação pixelizada dos dígitos
pixel_digits = {
    '0': [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
    ],
    '1': [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
    ],
    '2': [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
    ],
    '4': [
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
    ],

    '6': [
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ],

    '8': [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ],
    'H': [
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
    ],
    'P': [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 0],
        [1, 0, 0],
    ],
    ':': [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ], 

}

# Função para desenhar um números na tela
def draw_lifeboard(digitos, x, y):
    size = 0.20  #size
    glColor3f(1,1,1)
    glPointSize(30*size)
    
    for posicion,digito in enumerate('HP:'):
        for linha, pixel_linha in enumerate(pixel_digits[digito]):
            for coluna, pixel in enumerate(pixel_linha):
                if pixel == 1:
                    glBegin(GL_POINTS)
                    glVertex2f(coluna*size+x+posicion - 2.5, -linha*size+y)
                    glEnd()

    
    if(digitos >= 80):
    
        glColor3f(0,1,0)
    
    elif(digitos >=40):
        
        glColor(1,1,0)
        
    else:
        
        glColor(1,0,0)
    for posicion,digito in enumerate(str(digitos)):
        for linha, pixel_linha in enumerate(pixel_digits[digito]):
            for coluna, pixel in enumerate(pixel_linha):
                if pixel == 1:
                    glBegin(GL_POINTS)
                    glVertex2f(coluna*size+x+posicion, -linha*size+y)
                    glEnd()