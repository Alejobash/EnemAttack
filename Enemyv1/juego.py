import pygame
import ConfigParser
import os


ANCHO=600
ALTO=400

class torre (pygame.sprite.Sprite):
    id=0
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.click = False

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)
        
        
def Recortar(archivo, anc, alc):
    matriz=[]
    imagen=pygame.image.load(archivo).convert_alpha()
    i_ancho, i_alto=imagen.get_size()
    print i_ancho, ' ', i_alto
    for x in range(0, i_ancho/anc):
        linea=[]
        for y in range(0,i_alto/alc):
            cuadro=(x*anc, y*alc, anc, alc)
            linea.append(imagen.subsurface(cuadro))
        matriz.append(linea)
    return matriz

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])

    interprete=ConfigParser.ConfigParser()
    interprete.read('nivel.map')

    ar_origen=interprete.get("nivel","origen")
    mapa=interprete.get("nivel","mapa").split("\n")
    al=int (interprete.get("nivel","corte_alto"))
    an=int (interprete.get("nivel","corte_ancho"))

    fondo=Recortar(ar_origen,an,al)


    vary=0
    for fila in mapa:
        varx=0        
        for col in fila:
            px=int (interprete.get(col,"x"))
            py=int (interprete.get(col,"y"))
            pantalla.blit(fondo[px][py], (varx,vary))
            varx+=an
        vary+=al
    pygame.display.flip()

 
    
    b=torre('bloque1.png')
    b.id=0
    todos=pygame.sprite.Group()
    todos.add(b)
    #b.rect.center = pantalla.get_rect().center

    iconos=pygame.sprite.Group()

    icono=torre('defenza1.png')
    icono.id=1
    icono.rect.y=ALTO-85
    icono.rect.x=30
    todos.add(icono)
    iconos.add(icono)

    icono2=torre('defenza2.png')
    icono2.id=2
    icono2.rect.y=ALTO-85
    icono2.rect.x=80
    todos.add(icono2)
    iconos.add(icono2)

    reloj = pygame.time.Clock()
    fin=False
    
    
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if icono.rect.collidepoint(event.pos):
                    icono.click = True
                for ic in iconos:
                    if ic.rect.collidepoint(event.pos):
                        print "icono " + str(ic.id)
                if icono2.rect.collidepoint(event.pos):
                    icono2.click = True
                for ic in iconos:
                    if ic.rect.collidepoint(event.pos):
                        print "icono2 " + str(ic.id)

            if event.type == pygame.MOUSEBUTTONUP:
                icono.click = False
                icono2.click = False
            elif event.type == pygame.QUIT:
                fin=True
         
                
        todos.update(pantalla)
        todos.draw(pantalla)
        
        pygame.display.update()
        reloj.tick(60)
