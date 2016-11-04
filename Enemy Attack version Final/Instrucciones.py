#
# autor: Alejando Bedoya - Linda Cordero
# todos los Derechos Reservados
# licencia: GPL 2


import pygame
ANCHO=1000
ALTO=600
BLANCO=(255,255,255)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
NEGRO=(0,0,0)

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    fondo=pygame.image.load('data/CJ.jpg').convert()
    pantalla.blit(fondo,(0,0))
    pygame.display.flip()

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
 

        pantalla.blit(fondo,(0,0))
        pygame.display.flip()
