import random

# Tamaño del tablero
ANCHO = 20
ALTO = 20

# Posición inicial de la serpiente
serpiente = [(10, 10)]

# Dirección inicial
direccion = "DERECHA"

# Generar comida
comida = (
    random.randint(0, ANCHO - 1),
    random.randint(0, ALTO - 1)
)

puntaje = 0


def mover_serpiente():
    global serpiente

    cabeza_x, cabeza_y = serpiente[0]

    if direccion == "ARRIBA":
        nueva_cabeza = (cabeza_x, cabeza_y - 1)

    elif direccion == "ABAJO":
        nueva_cabeza = (cabeza_x, cabeza_y + 1)

    elif direccion == "IZQUIERDA":
        nueva_cabeza = (cabeza_x - 1, cabeza_y)

    else:
        nueva_cabeza = (cabeza_x + 1, cabeza_y)

    serpiente.insert(0, nueva_cabeza)
    serpiente.pop()


def verificar_colision():

    cabeza_x, cabeza_y = serpiente[0]

    if cabeza_x < 0 or cabeza_x >= ANCHO:
        return True

    if cabeza_y < 0 or cabeza_y >= ALTO:
        return True

    if serpiente[0] in serpiente[1:]:
        return True

    return False


def verificar_comida():
    global comida
    global puntaje

    if serpiente[0] == comida:

        puntaje += 1

        cola = serpiente[-1]
        serpiente.append(cola)

        comida = (
            random.randint(0, ANCHO - 1),
            random.randint(0, ALTO - 1)
        )


print("Juego de la Serpiente")
print("Puntaje:", puntaje)

mover_serpiente()
verificar_comida()

if verificar_colision():
    print("GAME OVER")
else:
    print("Juego en ejecución")