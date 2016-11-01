import pygame
import random

ANCHO=500
ALTO=400
BLANCO=(255,255,255)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
NEGRO=(0,0,0)



class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.vel=5
        self.fuego=0
        self.t=30

    def tiempo(self):
        self.t-=1
        if self.t==0:
            self.t=40
            self.fuego=1
        else:
            self.fuego=0

    def update(self):
        self.rect.x-=self.vel
        self.tiempo()
if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.mouse.set_visible(False)
    todos=pygame.sprite.Group()

    enemigos=pygame.sprite.Group()
    for i in range(6):
        x=ANCHO
        y=random.randrange(ALTO-20)
        e=Enemigo('sprites/enem1a.png')
        e.rect.x=x
        e.rect.y=y
        e.vel=random.randrange(10)
        enemigos.add(e)
        todos.add(e)


    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

