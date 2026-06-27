import pygame

from configuracion import *
from serpiente import Serpiente
from comida import Comida
from puntuacion import Puntuacion


class Juego:

    def __init__(self):

        pygame.init()

        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption(TITULO)

        self.reloj = pygame.time.Clock()

        self.fuente = pygame.font.SysFont("Arial", 48)

        self.reiniciar()

    def reiniciar(self):

        self.serpiente = Serpiente()
        self.comida = Comida()
        self.puntuacion = Puntuacion()

        self.game_over = False

    def procesar_eventos(self):

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:

                if not self.game_over:

                    if evento.key == pygame.K_UP and self.serpiente.direccion != "ABAJO":
                        self.serpiente.direccion = "ARRIBA"

                    elif evento.key == pygame.K_DOWN and self.serpiente.direccion != "ARRIBA":
                        self.serpiente.direccion = "ABAJO"

                    elif evento.key == pygame.K_LEFT and self.serpiente.direccion != "DERECHA":
                        self.serpiente.direccion = "IZQUIERDA"

                    elif evento.key == pygame.K_RIGHT and self.serpiente.direccion != "IZQUIERDA":
                        self.serpiente.direccion = "DERECHA"

                else:

                    if evento.key == pygame.K_r:
                        self.reiniciar()

        return True

    def actualizar(self):

        if self.game_over:
            return

        self.serpiente.mover()

        cabeza = self.serpiente.cuerpo[0]

        if cabeza[0] == self.comida.x and cabeza[1] == self.comida.y:

            self.serpiente.crecer()
            self.comida.nueva()
            self.puntuacion.aumentar()

        if self.serpiente.colision():

            self.game_over = True

    def dibujar(self):

        self.pantalla.fill(COLOR_FONDO)

        self.comida.dibujar(self.pantalla)

        self.serpiente.dibujar(self.pantalla)

        self.puntuacion.dibujar(self.pantalla)

        if self.game_over:

            texto = self.fuente.render(
                "GAME OVER",
                True,
                (255, 0, 0)
            )

            texto2 = pygame.font.SysFont(
                "Arial",
                28
            ).render(
                "Presione R para reiniciar",
                True,
                COLOR_TEXTO
            )

            self.pantalla.blit(
                texto,
                (250, 220)
            )

            self.pantalla.blit(
                texto2,
                (210, 300)
            )

        pygame.display.flip()

    def ejecutar(self):

        ejecutando = True

        while ejecutando:

            ejecutando = self.procesar_eventos()

            self.actualizar()

            self.dibujar()

            self.reloj.tick(FPS)

        pygame.quit()