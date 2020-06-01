# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:23:57 2020

@author: elena
"""

import pygame
from init import BLACK, WIDTH, HEIGHT, img_dir, snd_dir, WHITE, path
import random

# Classe Jogador

# Construtor da classe

# Construtor da classe (Sprite)

# Carrega a animação da carro

# Inicia o processo de animação colocando a primeira imagem na tela.

# Posicionamento

# Centraliza embaixo da tela.

# Velocidade do carrinho

# Melhora a colisão estabelecendo um raio de um circulo

# Guarda o tick da primeira imagem

# Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.

# Verifica o tick atual.

# Verifica quantos ticks se passaram desde a ultima mudança de frame.

# Se já está na hora de mudar de imagem...

# Marca o tick da nova imagem.

# Avança um quadro.

# Classe Mob que representa os carrinhos Policiais

# Construtor da classe.

# Construtor da classe (Sprite).

# Carrega a animação do MOB

# Inicia o processo de animação colocando a primeira imagem na tela.

# Detalhes sobre o posicionamento.

# Lugar inicial em x

# Lugar inicial em y

# Velocidade inicial

# Define acerca do movimento aos lados do carrinho

# Melhora a colisão estabelecendo um raio de um circulo

# Guarda o tick da primeira imagem

# Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.

# Metodo que atualiza a posição do carrinho

# Acerca do movimento para os lados

# Verifica o tick atual.

# Verifica quantos ticks se passaram desde a ultima mudança de frame.

# Se já está na hora de mudar de imagem...

# Marca o tick da nova imagem.

# Avança um quadro.

# Não deixa sair da pista

# Quando o carro passar do final da tela, volta para cima e é sorteada uma posição novamente

# Classe que representa os flocos de neve

# Construtor da classe.

# Construtor da classe pai (Sprite).

# Diminuindo o tamanho da imagem.

# Diminuindo o tamanho da imagem.

# Deixando transparente.

# Detalhes sobre o posicionamento.

# Sorteia um lugar inicial em x

# Sorteia um lugar inicial em y

# Sorteia uma velocidade inicial

# Melhora a colisão estabelecendo um raio de um circulo
 
# Atualização da posição do floco      
 
# Se o floco passar do final da tela, volta para cima

# Classe Coin que representa as moedas

# Construtor da classe.

# Construtor da classe pai (Sprite).

# Carrega a animação da coin

# Inicia o processo de animação colocando a primeira imagem na tela.

# Detalhes sobre o posicionamento.

# Sorteia um lugar inicial em x

# Sorteia um lugar inicial em y

# Sorteia uma velocidade inicial

# Melhora a colisão estabelecendo um raio de um circulo

# Guarda o tick da primeira imagem

# Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.

# Verifica o tick atual.

# Verifica quantos ticks se passaram desde a ultima mudança de frame.

# Se já está na hora de mudar de imagem...

# Marca o tick da nova imagem.

# Avança um quadro.
            
# Se a moeda passar do final da tela, volta para cima

# Classe BOX que representa as caixinhas
            
# Construtor da classe.
            
# Construtor da classe (Sprite).
    
# Carregando a imagem.

# Diminuindo o tamanho da imagem.

# Deixando transparente.

# Detalhes sobre o posicionamento.

# Sorteia um lugar inicial em x
       
# Sorteia um lugar inicial em y

# Sorteia uma velocidade inicial
        
# Melhora a colisão estabelecendo um raio de um circulo

# Metodo que atualiza a posição da caixa

# Se a caixa passar do final da tela, volta para cima

# Classe que representa a nevasca (quando se tem contato com a neve)
            
# Construtor da classe.
            
# Construtor da classe (Sprite).
            
# Diminuindo o tamanho da imagem.
            
# Diminuindo o tamanho da imagem.
            
# Deixando transparente.

# Detalhes sobre o posicionamento.
        
# Sorteia um lugar inicial em x                      

# Sorteia um lugar inicial em y

# Sorteia uma velocidade inicial  
        
# Melhora a colisão estabelecendo um raio de um circulo
        
# Classe que representa os tiros

# Construtor da classe
        
# Construtor da classe (Sprite).
        
# Carregando a imagem de fundo.
        
# Deixando transparente.
        
# Detalhes sobre o posicionamento.
        
# Coloca no lugar inicial definido em x, y do constutor

# Metodo que atualiza a posição do laser
   
# Se o tiro passar do inicio da tela, morre.
