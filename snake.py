#!/usr/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

TAMANHO_TELA = 640, 480

def inicio():
    global tela
    tela = pygame.display.set_mode(TAMANHO_TELA)


def desenha(pos, tamanho):
    pygame.draw.rect(tela, (255,0,0), (pos[0], pos[1],tamanho, tamanho))
    pygame.display.flip()

def principal():
    atraso = 30
    tamanho = 50
    x, y = 100, 100
    contador = 0
    while True:
        desenha((x,y), tamanho)
        pygame.time.delay(30)
        if contador >= 100:
            break
        contador += 1

def fim():
    pygame.quit()

try:
    inicio()
    principal()
finally:
    fim()
