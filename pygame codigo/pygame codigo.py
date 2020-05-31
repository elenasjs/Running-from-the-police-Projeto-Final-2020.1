# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:44:49 2020

@author: Bruno
"""

import pygame
import sys
import time
from os import path
import os
import random

# Importando as classes
from classes import Player, Policia, Estrela, Mais, Oleo, Tiro

# Carrega os assets
def carrega_assets(img, som):
    assets = {}
    assets['img_tiro']= pygame.image.load(path.join(img, 'tiro.png')).convert()
    assets['img_pista']= pygame.image.load(path.join(img, 'pista.jpeg')).convert()
    assets['img_policial']= pygame.image.load(path.join(img, 'Policiais.png')).convert()
    assets['img_mais']= pygame.image.load(path.join(img, 'Mais.png')).convert()
    assets['img_jogador']= pygame.image.load(path.join(img, 'Jogador.png')).convert()
    assets['img_gameover']= pygame.image.load(path.join(img, 'Game_Over.jpeg')).convert()
    assets['som_tiro']= pygame.mixer.Sound(path.join(som, 'tiro.wav'))
    assets['som_mais']= pygame.mixer.Sound(path.join(som, 'mais.wav'))
    assets['som_inicio']= pygame.mixer.Sound(path.join(som, 'inicio.wav'))
    assets['som_estrela']= pygame.mixer.Sound(path.join(som,'estrela.wav'))
    assets['som_carro']= pygame.mixer.Sound(path.join(som,'carro.wav'))
    assets['som_batida']= pygame.mixer.Sound(path.join(som, 'batida.wav'))
    return assets
    
    