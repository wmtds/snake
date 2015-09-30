import pygame
from pygame.locals import *

TAMANHO_TELA = 640, 480
TAMANHO = 64
COR_NAVE = (0, 128, 255)

def init():
    global TELA
    TELA = pygame.display.set_mode(TAMANHO_TELA)

class Nave(object):
    def __init__(self, x, y, cor, tx=TAMANHO, ty=TAMANHO):
        self.x = x
        self.y = y
        self.ox = x
        self.oy = y
        self.cor = cor
        self.tx = tx; self.ty = ty
    def apaga(self):
        pygame.draw.rect(TELA, (0,0,0), (self.ox, self.oy, self.tx, self.ty) )
    def desenha(self):
        self.rect = pygame.Rect ( (self.x, self.y, self.tx, self.ty) )
        self.apaga()
        pygame.draw.rect(TELA, self.cor, self.rect)
        self.ox = self.x
        self.oy = self.y

MAX_TIROS = 10
MAX_INIMIGOS = 10
def principal():
    inimigo = Nave(0, 0, (255,0,0))
    x = TAMANHO_TELA[0] // 2
    y = TAMANHO_TELA[1] - TAMANHO
    nave = Nave(x, y, COR_NAVE)
    velocidade = 10
    tiros = []
    velocidade_inimigo = 5
    inimigos = [inimigo]
    contador = 0 
    while True:
        if contador > 30 and len(inimigos) < MAX_INIMIGOS:
            inimigos.append(Nave(0, 0 , (255, 0, 0)))
            contador = 0
        contador += 1
        pygame.event.pump()
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            nave.x -= velocidade
        elif teclas[K_RIGHT]:
            nave.x += velocidade
        if teclas[K_ESCAPE]:
            break
        if teclas[K_SPACE] and len(tiros) <= MAX_TIROS:
            tiro = Nave(nave.x + TAMANHO//2, TAMANHO_TELA[1] - TAMANHO,
                        (255, 255,255), 12, 23)
            tiros.append(tiro)

        for inimigo in inimigos:
            inimigo.x += velocidade_inimigo
            if inimigo.x > TAMANHO_TELA[0]:
                inimigo.x = 0
                inimigo.y += TAMANHO
                if inimigo.y >= TAMANHO_TELA[1]:
                    print("Voce morreu")
                    break
            inimigo.desenha()
            
        nave.desenha()
        novos_tiros = []
        for tiro in tiros:
            tiro.y -= velocidade
            tiro.desenha()
            if tiro.y > 0:
                novos_tiros.append(tiro)
            else: tiro.apaga()
            novos_inimigos = []
            for inimigo in inimigos:
                if not tiro.rect.colliderect(inimigo.rect):
                    novos_inimigos.append(inimigo)
                else:
                    inimigo.apaga()
            inimigos = novos_inimigos
        tiros = novos_tiros
        pygame.display.flip()
    
        pygame.time.delay(30)


try:
    init()
    principal()
finally:
    pygame.quit()
    
