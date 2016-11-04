import pygame
import random

ANCHO=1000
ALTO=600
BLANCO=(255,255,255)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
NEGRO=(0,0,0)
segundos=0	
def crono():
        global segundos
        segundos+=1
        time.sleep(1)
        return crono
class Jugador(pygame.sprite.Sprite):
    id=0
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.puntuacion=0
  
e

    def update(self):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()

        


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

Sprite.__init__(self)
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
    jp=Jugador('salvador.png')

    pygame.mixer.music.load('grasswalk.mp3')
    puntos=0
    fuente=pygame.font.Font(None,28)
    fuente2=pygame.font.Font(None,48)
    texto=fuente.render("VIDA: "+str(jp.vida),True,NEGRO)
    #puntuacion del jjugador
    puntos=fuente.render("PUNTUACION: "+str(jp.puntuacion),True,NEGRO)
    cronometro=fuente.render("TIEMPO: "+str(segundos),True,NEGRO)

    todos=pygame.sprite.Group()
    todos.add(jp)
    jp.rect.center = pantalla.get_rect().center
    iconos=pygame.sprite.Group()

    icono=Jugador('warmachine.png')
    icono.id=1
    icono.rect.y=ALTO-85
    icono.rect.x=30
    todos.add(icono)
    iconos.add(icono)

    icono2=Jugador('Hulkbuster.png')
    icono2.id=2
    icono2.rect.y=ALTO-85
    icono2.rect.x=80
    todos.add(icono2)
    iconos.add(icono2)


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
		
                for ic in iconos:
                    if ic.rect.collidepoint(event.pos):
                        print "icono " + str(ic.id)

            if event.type == pygame.MOUSEBUTTONUP:
                icono.click = False
                jp.click = False

                icono2.click = False

        #eliminar balas fuera
        
        pantalla.blit(fondo,(0,0))
        pantalla.blit(texto,(200,30))
        pantalla.blit(puntos,(200,10))
        pantalla.blit(cronometro,(200,50))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
