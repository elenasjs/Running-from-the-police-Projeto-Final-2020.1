# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:12:01 2020

@author: Bruno
"""

import pygame
from init import WIDTH, HEIGHT
import random

# Classe Jogador
class Jogador(pygame.sprite.Sprite):
    # Construtor da classe
    def __init__(self, carro):
        
        # Construtor da classe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        # Carrega a animação da carro
        self.carro= carro
        # Inicia o processo de animação colocando a primeira imagem na tela
        self.frame= 0
        self.image= self.carro[self.frame]
        
        # Posicionamento
        self.rect= self.image.get_rect()
        
        # Centraliza embaixo da tela
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = HEIGHT- 200
        
        # Velocidade do carrinho
        self.velocidadex = 0
        
        # Melhora a colisão
        self.radius = 10
        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        
        # Controle de ticks de animação
        self.frame_ticks= 12
        
    # Atualiza a posição do carrinho
    def update(self):
        self.rect.x += self.velocidadex

        # Mantém dentro da tela
        if self.rect.right > 520:
            self.rect.right = 520
        if self.rect.left < 83:
            self.rect.left = 83
            
        # Verifica o tick atual
        tick_atual= pygame.time.get_ticks()
        
        # Verifica quantos ticks se passaram desde a ultima mudança de frame
        ticks_passados= tick_atual- self.last_update
        
        # Se já está na hora de mudar de imagem...
        if ticks_passados > self.frame_ticks:
            
            # Marca o tick da nova imagem
            self.last_update= tick_atual
            
            # Avança um quadro
            self.frame +=1
            if self.frame == len(self.carro):
                self.frame= 0
            centro= self.rect.center
            self.image= self.carro[self.frame]
            self.rect= self.image.get_rect()
            self.rect.center = centro
            
# Classe Policial que representa os carrinhos Policiais
class Policia(pygame.sprite.Sprite):
    
    # Construtor da classe
    def __init__(self, policial):
        
        # Construtor da classe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        # Carrega a animação dos policiais
        self.policial= policial
        
        # Inicia o processo de animação colocando a primeira imagem na tela
        self.frame = 0
        self.image = self.policial[self.frame]
        
        # Detalhes sobre o posicionamento
        self.rect= self.image.get_rect()
        
        # Lugar inicial em x
        i= random.randrange(0,5)
        if i ==0:
            self.rect.x = 105
        elif i == 1:
            self.rect.x = 195
        elif i == 2:
            self.rect.x = 275
        elif i == 3:
            self.rect.x = 365
        elif i == 4:
            self.rect.x = 455
            
        # Lugar inicial em y
        self.rect.y= random.randrange(-150, -100)
        
        # Velocidade inicial
        self.velocidadex= 0
        self.velocidadey= 8
        
        # Define acerca do movimento aos lados do carrinho
        self.direcao= 0
        self.direcao_timer= 0
        self.referencia = 0
        
        # Melhora a colisão 
        self.radius= int(self.rect.width * 40)
        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        
        # Controle de ticks de animação
        self.frame_ticks= 80
        
    # Metodo que atualiza a posição do carrinho
    def update(self):
        
        # Acerca do movimento para os lados
        if self.direcao_timer == 0:
            self.direcao= random.randrange(3)-1
            self.direcao_timer = 100
        self.direcao_timer -=1
        if self.rect.x <=100 and self.direcao<0:
            self.direcao=0
        if self.rect.x >=455 and self.direcao>0:
            self.direcao=0
            
        if abs(self.referencia) >= 85:
            self.direcao=0
        
        self.rect.x += self.direcao * 2
        self.referencia += self.direcao * 2
        
        self.rect.y += self.velocidadey
                    
        # Verifica o tick atual
        tick_atual = pygame.time.get_ticks()
        

        # Verifica quantos ticks se passaram desde a ultima mudança de frame
        ticks_passados= tick_atual- self.last_update
        

        # Se já está na hora de mudar de imagem...
        if ticks_passados> self.frame_ticks:
            # Marca o tick da nova imagem
            self.last_update= tick_atual
            # Avança um quadro
            self.frame +=1
            if self.frame == len(self.policial):
                self.frame = 0
            centro= self.rect.centro
            self.image= self.policial[self.frame]
            self.rect= self.image.get_rect()
            self.rect.centro = centro
            
        # Não deixa sair da pista
        if self.rect.right > 520:
            self.rect.right = 520
        if self.rect.left < 90:
            self.rect.left = 90

        # Quando o palicial passar do final da tela, volta para cima e é sorteada uma posição novamente
        if self.rect.top > HEIGHT +10 or self.rect.left< -25 or self.rect.right> WIDTH +20:
            i= random.randrange(0,5)
            if i ==0:
                self.rect.x = 105
            elif i == 1:
                self.rect.x = 195
            elif i == 2:
                self.rect.x = 275
            elif i == 3:
                self.rect.x = 365
            elif i == 4:
                self.rect.x = 455
                
            self.rect.y= random.randrange(-150, -100)
            if i % 2 == 0:
                self.velocidadex = 50
            else: 
                self.velocidadex= random.randrange(-3, 3)
            self.velocidadey = random.randrange(10, 15)
            self.referencia=0          

# Classe Estrela 
class Estrela(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, estrela):
        # Construtor da classe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        # Carrega a animação da estrela
        self.estrela = estrela        
        
        # Inicia o processo de animação colocando a primeira imagem na tela
        self.frame = 0
        self.image = self.estrela[self.frame]
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        posicao_inicial=[100,195,280,365,455]
        i=random.randrange(0,5)
        self.rect.x = posicao_inicial[i]
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        self.velocidadex = 0
        self.velocidadey = 3
        
        # Melhora a colisão
        self.radius = int(self.rect.width * 40)
        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação
        self.frame_ticks = 120

    def update(self):
        # Verifica o tick atual.
        tick_atual = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        ticks_passados = tick_atual - self.last_update

        # Se já está na hora de mudar de imagem...
        if ticks_passados > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = tick_atual
            
            # Avança um quadro.
            self.frame += 1
            if self.frame == len(self.estrela):
                self.frame = 0
            
            centro = self.rect.center
            self.image = self.estrela[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centro = centro
              
        self.rect.x += 0
        self.rect.y += self.velocidadey
        
        # Se a estrela passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            posicao_inicial=[100,195,280,365,455]
            i=random.randrange(0,5)
            self.rect.x = posicao_inicial[i]
            self.rect.y = random.randrange(-100, -40)
            self.velocidadex = random.randrange(-3, 3)
            self.velocidadey = 3

# Classe + que representa os +
class Mais(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, mais):
        # Construtor da classe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        # Carrega a animação da estrela
        self.mais = mais        
        
        # Inicia o processo de animação colocando a primeira imagem na tela
        self.frame = 0
        self.image = self.mais[self.frame]
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        posicao_inicial=[100,195,280,365,455]
        i=random.randrange(0,5)
        self.rect.x = posicao_inicial[i]
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        self.velocidadex = 0
        self.velocidadey = 3
        
        # Melhora a colisão
        self.radius = int(self.rect.width * 40)
        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação
        self.frame_ticks = 120

    def update(self):
        # Verifica o tick atual.
        tick_atual = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        ticks_passados = tick_atual - self.last_update

        # Se já está na hora de mudar de imagem...
        if ticks_passados > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = tick_atual
            
            # Avança um quadro.
            self.frame += 1
            if self.frame == len(self.imagem_coin):
                self.frame = 0
            
            centro = self.rect.center
            self.image = self.imagem_coin[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centro = centro
              
        self.rect.x += 0
        self.rect.y += self.velocidadey
        
        # Se a estrela passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            posicao_inicial=[100,195,280,365,455]
            i=random.randrange(0,5)
            self.rect.x = posicao_inicial[i]
            self.rect.y = random.randrange(-100, -40)
            self.velocidadex = random.randrange(-3, 3)
            self.velocidadey = 3

# Classe que representa os tiros
class Tiro(pygame.sprite.Sprite):
    
    # Construtor da classe
    def __init__(self, tiro, x, y):
        
        # Construtor da classe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a animacao do tiro.
        self.image = tiro
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y
        self.rect.centrox = x
        self.speedy = -10

    # Metodo que atualiza a posição do tiro
    def update(self):
        self.rect.y += self.speedy
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()