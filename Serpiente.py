import pygame
from configuracion import *

class Serpiente:

    def __init__(self):

        self.cuerpo = [
            [100,100],
            [80,100],
            [60,100]
        ]

        self.direccion = "DERECHA"

    def mover(self):

        cabeza = self.cuerpo[0].copy()

        if self.direccion == "DERECHA":
            cabeza[0] += TAM_CELDA

        elif self.direccion == "IZQUIERDA":
            cabeza[0] -= TAM_CELDA

        elif self.direccion == "ARRIBA":
            cabeza[1] -= TAM_CELDA

        elif self.direccion == "ABAJO":
            cabeza[1] += TAM_CELDA

        self.cuerpo.insert(0,cabeza)
        self.cuerpo.pop()

    def crecer(self):

        cola = self.cuerpo[-1].copy()
        self.cuerpo.append(cola)

    def dibujar(self, pantalla):

        for bloque in self.cuerpo:

            pygame.draw.rect(
                pantalla,
                COLOR_SERPIENTE,
                (bloque[0], bloque[1], TAM_CELDA, TAM_CELDA)
            )

    def colision(self):

        cabeza = self.cuerpo[0]

        if cabeza[0] < 0 or cabeza[0] >= ANCHO:
            return True

        if cabeza[1] < 0 or cabeza[1] >= ALTO:
            return True

        if cabeza in self.cuerpo[1:]:
            return True

        return False