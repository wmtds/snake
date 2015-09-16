#!/usr/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

TAMANHO = 640, 480

def inicio():
    global tela
    tela = pygame.display.set_mode(TAMANHO)

def principal():
    pygame.draw.rect(tela, (255,0,0), (0,0,50, 50))
    pygame.display.flip()
    pygame.time.delay(2000)

def fim():
    pygame.quit()

try:
    inicio()
    principal()
finally:
    fim()
