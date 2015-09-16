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


def verifica_se_bateu(pos, tamanho, cor_fundo):
    x = pos[0] + tamanho / 2
    y = pos[1] + tamanho / 2
    cor_alvo = tela.get_at((x, y))
    if cor_alvo[0:3] != cor_fundo:
        return True
    return False


def principal():
    atraso = 30
    tamanho = 20
    x, y = 100, 100
    contador = 0
    velocidade = 12
    vx = velocidade
    vy = 0
    fator_de_tamanho = tamanho / velocidade
    comprimento = 8 * fator_de_tamanho
    posicoes = [(0, 0)]
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
        if teclas[K_SPACE] or contador % 50 == 0:
            comprimento += 1
        if teclas[K_ESCAPE]:
            break

        while len(posicoes) >= comprimento:
            desenha(posicoes.pop(0), tamanho, cor_fundo)

        x = x + vx
        y = y + vy
        posicoes.append((x, y))

        if x < 0 or x > TAMANHO_TELA[0] or y < 0 or y > TAMANHO_TELA[1]:
            print("Você morreu por que saiu da tela")
            break

        if verifica_se_bateu(posicoes[-1], tamanho, cor_fundo):
            print("Você bateu em alguma coisa")
            break

        desenha(posicoes[-1], tamanho, cor_cobra)
        pygame.time.delay(atraso)
    print ("\nVocê sobreviveu por {} ciclos! Parabéns!".format(contador))


def fim():
    pygame.quit()

try:
    inicio()
    principal()
finally:
    fim()
