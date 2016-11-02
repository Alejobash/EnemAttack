import pygame
import random

ANCHO=1000
ALTO=600
BLANCO=(255,255,255)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
NEGRO=(0,0,0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=100

    def update(self):
        pos=pygame.mouse.get_pos()
        self.rect.x=pos[0]
        self.rect.y=pos[1]


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

class Disparo(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.vel=10
        self.dir=0

    def update(self):
        if self.dir==0:
            self.rect.x+=self.vel
        else:
            self.rect.x-=self.vel



if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.mixer.music.load('grasswalk.mp3')

    fondo=pygame.image.load('patio.png').convert()
    pygame.display.set_caption('enemyatack')

    pygame.mixer.music.load('grasswalk.mp3')


    pygame.mouse.set_visible(False)
    jp=Jugador('sprites/enem2a.png')
    todos=pygame.sprite.Group()
    todos.add(jp)

    enemigos=pygame.sprite.Group()
    for i in range(7):
        x=ANCHO
        y=random.randrange(ALTO-20)
        e=Enemigo('tree.png')
        e.rect.x=x
        e.rect.y=y
        e.vel=random.randrange(3)
        enemigos.add(e)
        todos.add(e)
        e1=Enemigo('Zombie.gif')
        e1.rect.x=x
        e1.rect.y=y
        e1.vel=random.randrange(3)
        enemigos.add(e1)
        todos.add(e1)

    balas=pygame.sprite.Group()
    ebalas=pygame.sprite.Group()

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
		
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                b=Disparo('sprites/ball.png')
                b.rect.x=jp.rect.x
                b.rect.y=jp.rect.y
                balas.add(b)
                todos.add(b)


        #eliminar balas fuera
        for b in balas:
            ls_imp=pygame.sprite.spritecollide(b,enemigos,True)
            for b_imp in ls_imp:
                balas.remove(b)
                todos.remove(b)

            if b.rect.x>ANCHO:
                balas.remove(b)
                todos.remove(b)

        for e in enemigos:
            if e.fuego==1:
                b=Disparo('sprites/bala.png')
                b.rect.x=e.rect.x
                b.rect.y=e.rect.y
                b.dir=1
                ebalas.add(b)
                todos.add(b)

            if e.rect.x<0:
                enemigos.remove(e)
                todos.remove(e)
                

        pantalla.fill(0)
        pantalla.blit(fondo,(0,0))

        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
