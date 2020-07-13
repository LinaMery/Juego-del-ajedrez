import pygame

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
FONDO = (24, 25, 30)
AZUL = (20, 80, 240)
SELECCIONA = (220, 220, 0)
DIMENCIONES = (600, 600)
LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H"]


def dibujarTablero(screen, dimension, p_inicio, tamanio_fuente, fuente, seleccion):
    color = 0
    for i in range(8):
        for j in range(8):
            x = i * dimension + p_inicio[0]
            y = j * dimension + p_inicio[1]
            if color % 2 == 0:
                pygame.draw.rect(screen, BLANCO, [x, y, dimension, dimension], 0)
            else:
                pygame.draw.rect(screen, NEGRO, [x, y, dimension, dimension], 0)
            if seleccion[0] == LETRAS[i] and j == seleccion[1] - 1:
                pygame.draw.rect(screen, SELECCIONA, [x, y, dimension, dimension], 0)
            color += 1
        color += 1
        dibujarTexto(screen, LETRAS[i], [i * dimension + p_inicio[0], p_inicio[1] - tamanio_fuente], fuente)
        dibujarTexto(screen, str(i + 1), [p_inicio[0] - tamanio_fuente, i * dimension + p_inicio[1]], fuente)


def dibujarTexto(screen, texto, posicion, fuente):
    Texto = fuente.render(texto, 1, BLANCO)
    screen.blit(Texto, posicion)


def ajustarMedidas(tamanio_fuente):
    if DIMENCIONES[1] < DIMENCIONES[0]:
        ancho = int((DIMENCIONES[1] - (tamanio_fuente * 2)) / 8)
        inicio = ((DIMENCIONES[0] - DIMENCIONES[1]) / 2) + tamanio_fuente, tamanio_fuente
    else:
        ancho = int((DIMENCIONES[0] - (tamanio_fuente * 2)) / 8)
        inicio = tamanio_fuente, ((DIMENCIONES[0] - DIMENCIONES[1]) / 2) + tamanio_fuente
    return [inicio, ancho]


def obetnerPosicion(mouse, dimension, p_inicio, actual):
    rx, ry = mouse[0], mouse[1]
    for i in range(8):
        for j in range(8):
            x = j * dimension + p_inicio[0]
            y = j * dimension + p_inicio[1]
            if (rx >= x) and (rx <= x + dimension) and (ry >= y) and (ry <= y + dimension):
                actual = [LETRAS[i], j + 1]
    return actual


def main():
    pygame.init()
    screen = pygame.display.set_mode(DIMENCIONES)
    pygame.display.set_caption("MOBIBLE CHESS")
    game_over = False
    clock = pygame.time.Clock()
    tamanio_fuente = 30
    seleccion = ["Z", -1]
    fuente = pygame.font.Font(None, tamanio_fuente)
    puntoInicio, dimension = ajustarMedidas(tamanio_fuente)
    while game_over is False:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        botones = pygame.mouse.get_pressed()
        if botones[0]:
            pos = pygame.mouse.get_pos()
            seleccion = obetnerPosicion(pos, dimension, puntoInicio, seleccion)
        screen.fill(FONDO)
        dibujarTablero(screen, dimension, puntoInicio, tamanio_fuente, fuente, seleccion)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
