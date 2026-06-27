import pygame
from configuracion import *

class Puntuacion:

    def __init__(self):

        self.puntos = 0

        self.fuente = pygame.font.SysFont("Arial",28)

    def aumentar(self):

        self.puntos += 1

    def dibujar(self,pantalla):

        texto = self.fuente.render(
            f"Puntaje: {self.puntos}",
            True,
            COLOR_TEXTO
        )

        pantalla.blit(texto,(10,10))