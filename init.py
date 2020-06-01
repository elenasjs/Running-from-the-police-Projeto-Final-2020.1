# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:26:58 2020

@author: Bruno
"""

from os import path

# Pastas que contem imagens e sons
img = path.join(path.dirname(__file__), 'img_dir')
som = path.join(path.dirname(__file__), 'snd_dir')


# Dimensoes da tela e FPS
WIDTH = 600 
HEIGHT = 800 
FPS = 65 

# Cores para serem usadas em textos 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
