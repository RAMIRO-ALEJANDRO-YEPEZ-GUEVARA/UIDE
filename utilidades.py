import pygame

def mostrar_mensaje(
    pantalla,
    texto,
    fuente,
    color,
    x,
    y
):

    imagen = fuente.render(
        texto,
        True,
        color
    )

    pantalla.blit(imagen,(x,y))