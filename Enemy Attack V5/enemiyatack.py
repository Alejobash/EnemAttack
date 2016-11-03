import pygame
import random
import sys
import math
import time

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
        self.vida=10
        self.click = False

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
        self.tiempo=random.randrange(100)
        self.disparar=False

    def tiempo(self):
        self.t-=1
        if self.t==0:
            self.t=40
            self.fuego=1
        else:
            self.fuego=0

    def update(self):
        self.rect.x-=self.vel






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
    pygame.mixer.music.load("grasswalk.mp3")

    fondo=pygame.image.load('patio.png').convert()
    pygame.display.set_caption('enemyatack')
    jp=Jugador('salvador.png')

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
        y=random.randrange(ALTO-150)
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
    fin=True
    conenem=50

    while  fin:
		
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
				sys.exit(0)
            if event.type == pygame.KEYDOWN:
				if event.key== pygame.K_1:

					b=Disparo('sprites/ball.png')
					b.rect.x=jp.rect.x
					b.rect.y=jp.rect.y
					balas.add(b)
					todos.add(b)
				if event.key== pygame.K_2:
					b=Disparo('sprites/ball.png')
					b.rect.x=icono.rect.x
					b.rect.y=icono.rect.y
					balas.add(b)
					todos.add(b)
				if event.key== pygame.K_3:
					b=Disparo('sprites/ball.png')
					b.rect.x=icono2.rect.x
					b.rect.y=icono2.rect.y
					balas.add(b)
					todos.add(b)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jp.rect.collidepoint(event.pos):
                    jp.click = True
                for ic in iconos:
                    if ic.rect.collidepoint(event.pos):
                        print "icono " + str(ic.id)
                if icono.rect.collidepoint(event.pos):
                    icono.click = True
                for ic in iconos:
                    if ic.rect.collidepoint(event.pos):
                        print "icono " + str(ic.id)
                if icono2.rect.collidepoint(event.pos):
                    icono2.click = True
                for ic in iconos:
                    if ic.rect.collidepoint(event.pos):
                        print "icono " + str(ic.id)

            if event.type == pygame.MOUSEBUTTONUP:
                icono.click = False
                jp.click = False

                icono2.click = False

        #eliminar balas fuera


        for b in balas:
            ls_imp=pygame.sprite.spritecollide(b,enemigos,True)
            for b_imp in ls_imp:
                balas.remove(b)
                todos.remove(b)
                jp.puntuacion+=1
                puntos=fuente.render("PUNTUACION: "+str(jp.puntuacion),True,NEGRO)
                if jp.puntuacion==10:
						texto4=fuente2.render("GANASTE",True,NEGRO)
						pantalla.blit(texto4,(500,300))
						todos.remove(jp)
						print 'Ganaste'

						fin=False

					
            if b.rect.x>ANCHO:
                balas.remove(b)
                todos.remove(b)
                

        for e in enemigos:
            if e.fuego==1:
                b=Disparo('sprites/fire.png')
                b.rect.x=e.rect.x
                b.rect.y=e.rect.y
                b.dir=1
                ebalas.add(b)
                todos.add(b)

            if e.rect.x<0:
                enemigos.remove(e)
                todos.remove(e)
                
        if conenem==0:
            e=Enemigo('tree.png')
            e.rect.x=ANCHO
            e.rect.y=random.randrange(ALTO-150)
            e.var_x=(-1)*random.randrange(3,10)
            enemigos.add(e)
            todos.add(e)
            conenem=50
            e1=Enemigo('Zombie.gif')
            e1.rect.x=ANCHO
            e1.rect.y=random.randrange(ALTO-150)
            e1.var_x=(-1)*random.randrange(3,10)
            enemigos.add(e1)
            todos.add(e1)
        else:
            conenem-=1
            
        ls_choque=pygame.sprite.spritecollide(jp, enemigos,True)
        for elemento in ls_choque:
            print 'golpe'
            jp.vida-=1
            texto=fuente.render("VIDA: "+str(jp.vida),True,NEGRO)
            
            if jp.vida==0:
					texto3=fuente2.render("FIN DE JUEGO",True,NEGRO)
					pantalla.blit(texto3,(500,300))
					todos.remove(jp)
					fin=False
					texto=fuente.render("VIDA: 0",True,NEGRO)
			           
        ls_choque1=pygame.sprite.spritecollide(icono, enemigos,True)
        for elemento in ls_choque1:
			print 'golpe'
			

        ls_choque2=pygame.sprite.spritecollide(icono2, enemigos,True)
        for elemento in ls_choque2:
            print 'golpe'
                      
            
            
        pantalla.fill(0)
        pantalla.blit(fondo,(0,0))
        pantalla.blit(texto,(200,30))
        pantalla.blit(puntos,(200,10))
        pantalla.blit(cronometro,(200,50))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
