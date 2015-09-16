#!/usr/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

TAMANHO_TELA = 640, 480


def inicio():
    global tela
    tela = pygame.display.set_mode(TAMANHO_TELA)


def desenha(pos, tamanho):
    pygame.draw.rect(tela, (255, 0, 0), (pos[0], pos[1], tamanho, tamanho))
    pygame.display.flip()


def principal():
    atraso = 30
    tamanho = 50
    x, y = 100, 100
    contador = 0
    velocidade = 10
    vx = vy = 0
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

        x = x + vx
        y = y + vy

        if x < 0 or x > TAMANHO_TELA[0] or y < 0 or y > TAMANHO_TELA[1]:
            print("Você morreu por que saiu da tela")
            break

        desenha((x, y), tamanho)
        pygame.time.delay(atraso)


def fim():
    pygame.quit()

try:
    inicio()
    principal()
finally:
    fim()
