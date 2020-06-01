# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:23:33 2020

@author: elena
"""

import pygame
import sys
import time
from os import path
import os
import random

# Deixa a tela centralizada quando rodar

# Importando as informações iniciais

# Importando todas as classes
from classes import Player, Policia, Estrela, Mais, Oleo, Tiro
# Definindo o tamanho da tela

# Carrega todos os assets de uma vez só
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

# Função que vê qual foi o high score no outro arquivo

# Função que lê o high score no outro arquivo

# Função para salvar o novo high score, caso seja maior

# Função para salvar o nome da pessoa do novo high score

# Função para ler o nome da pessoa do high score

# Função tela inicial do jogo
    
# Definindo botão "start"
    
# Imagem de fundo
    
# Muda imagem para botar o nome 
    
# Coloca o "INSIRA SEU NOME" junto
    
# Coloca o "E APERTE ENTER" abaixo
    
# Coloca a maior pontuação e o nome do recordista
    
# Retorna o nome para utilizar no High Score, caso necessário

# Função da tela final do jogo (Perder o jogo)
    
# Printando todas as informações na tela, junto com a imagem de fundo (tela inicial, nome, pontuação)
    
# Colocando os botões 
    
# Vendo se a pessoa foi recordista ou não
    
# Ações "botões" do final do jogo
    
# Função principal do jogo, onde todas as ações estão
    
# Toca música para o jogo
    
# Cria um carrinho
    
# Cria todos os sprites e adiciona o player em tal
    
# Cria um grupo só dos carrinhos policiais
        
# Cria grupo para as estrelas
    
# Cria um grupo para os 'Mais' (+)
    
# Cria grupo para os Oleos
    
# Cria um grupo para os tiros
    
# Cria carrinhos e adiciona no grupo policiais
    
# Cria os "Mais"(+)
    
# Adiciona as Estrelinhas
    
# Adiciona poças de oleo
    
# Define quantos tiros a pessoa começa e quantos pontos
    
# Um if para caso a pessoa aperte RESTART não precise colocar o nome novamente
        
# Pegar o nome colocado pela pessoa chamando a função da tela inicial

# Loop principal
        
# Ajusta a velocidade do jogo
        
# Propabilidade de aparecer Estrelinha
        
# Probabilidade de aparecer "Mais"(+)
        
# Probabilidade de aparecer Oleo
        
# Processa os eventos (Mouse, teclado, botao, etc)
        
# Verifica se foi fechado
            
# Verifica se apertou alguma tecla
                 
# Se for a tecla espaco, atira! (caso tenha tiro)
        
# Verifica se encostou na parede, se encosotu, morreu
        
# Atualiza a ação de cada sprite
        
# Verifica se houve colisao entre tiro e carrinho
        
# Verifica se houve colisao entre os carrinhos
             
# Se teve, tem que dar um delay pro jogador ver que bateu
        
# Verifica se houve colisao com 'Mais'(+)
        
# Verifica se houve colisao com Estrelinha
        
# Verifica se houve colisao com Oleo
             
# Velocidade do player, aumenta e estabiliza
        
# A cada loop, redesenha o fundo e os sprites
        
# Desenha o score, por tempo
        
# Depois de desenhar tudo, inverte o display
        
# Verifica se fez a maior pontuacao com a funcao
        
# se for a maior pontuacao, mostra na tela
        
# Tela final que mostra a pontuacao do player
        
# Mata os policiais e o player pra recomecar no novo loop
        
# Inicializacao do pygame
        
# Nome do jogo
        
# Icone do jogo

# Carrega todos os assets uma vez só e guarda em um dicionário

# Ajustar velocidde 

# Carrega o fundo do jogo

# Carrega os sons do jogo

# Comando para evitar travamentos.
        