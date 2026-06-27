import random
import pygame
from configuracion import *

class Comida:

    def __init__(self):

        self.nueva()

    def nueva(self):

        self.x = random.randrange(0,ANCHO,TAM_CELDA)
        self.y = random.randrange(0,ALTO,TAM_CELDA)

    def dibujar(self,pantalla):

        pygame.draw.rect(
            pantalla,
            COLOR_COMIDA,
            (self.x,self.y,TAM_CELDA,TAM_CELDA)
        )