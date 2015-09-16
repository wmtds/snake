#!/usr/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

TAMANHO_TELA = 640, 480

cor_cobra = (255, 0, 0)
cor_fundo = (0, 0, 0)

def inicio():
    global tela
    tela = pygame.display.set_mode(TAMANHO_TELA)


def desenha(pos, tamanho, cor):
    pygame.draw.rect(tela, cor, (pos[0], pos[1], tamanho, tamanho))
    pygame.display.flip()


def principal():
    atraso = 30
    tamanho = 20
    x, y = 100, 100
    contador = 0
    velocidade = 20
    vx = vy = 0
    ox = oy = 0
    x1 = y1 = 0
    x2 = y2 = 0
    x3 = y3 = 0
    while True:
        contador += 1
        pygame.event.pump()
        teclas = pygame.key.get_pressed()
        if teclas[K_UP]:
            vy = -velocidade
            vx = 0
        if teclas[K_DOWN]:
            vy = velocidade
            vx = 0
        if teclas[K_LEFT]:
            vx = -velocidade
            vy = 0
        if teclas[K_RIGHT]:
            vx = velocidade
            vy = 0
        if teclas[K_ESCAPE]:
            break

        ox = x3; oy = y3
        x3 = x2; y3 = y2
        x2 = x1; y2 = y1
        x1 = x; y1 = y

        x = x + vx
        y = y + vy

        if x < 0 or x > TAMANHO_TELA[0] or y < 0 or y > TAMANHO_TELA[1]:
            print("Você morreu por que saiu da tela")
            break

        desenha((ox, oy), tamanho, cor_fundo)
        desenha((x, y), tamanho, cor_cobra)
        pygame.time.delay(atraso)


def fim():
    pygame.quit()

try:
    inicio()
    principal()
finally:
    fim()
