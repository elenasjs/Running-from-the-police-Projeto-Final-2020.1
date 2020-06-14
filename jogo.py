# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:23:33 2020
@author: elena
"""


import pygame
import time
from os import path
import os

# Deixa a tela centralizada quando rodar
os.environ['SDL_VIDEO_CENTERED'] = '1'
# Importando as informações iniciais
from init import img, som, BLACK, WHITE, WIDTH, HEIGHT, FPS
# Importando todas as classes
from Classes import Jogador, Policia, Estrela, Mais
# Definindo o tamanho da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
    assets['som_carro']= pygame.mixer.Sound(path.join(som,'carro.wav'))
    assets['som_batida']= pygame.mixer.Sound(path.join(som, 'batida.wav'))
    assets['som_estrela']= pygame.mixer.Sound(path.join(som, 'estrela.wav'))
    return assets

# Função que vê qual foi o high score no outro arquivo
def maior_pontuacao(pont, nomecolocado):
    RECORDE = get_high_score()
    if pont > RECORDE:
        save_high_score(pont)
        save_nome(nomecolocado) 
# Função que lê o high score no outro arquivo
def get_high_score():
    high_score_file = open("ponto_high_score.txt", "r")
    high_score = int(high_score_file.read())
    high_score_file.close()
    return high_score
 
# Função para salvar o novo high score, caso seja maior
def save_high_score(new_high_score):
    high_score_file = open("ponto_high_score.txt", "w")
    high_score_file.write(str(new_high_score))
    high_score_file.close()

# Função para salvar o nome da pessoa do novo high score
def save_nome(nomecolocado):
    nome = open("nome_high_score.txt", "w")
    nome.write(nomecolocado)
    nome.close()
# Função para ler o nome da pessoa do high score
def get_name():
    nome = open("nome_high_score.txt", "r")
    nomee = nome.read()
    nome.close()
    return nomee

# Função para os "botões" no final do jogo
def botao(comando, x, y, w, h, inactive, active):

    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, active, (x, y, w, h))
          
    else:
        pygame.draw.rect(screen, inactive, (x, y, w, h))    

    fonte = pygame.font.Font(pygame.font.get_default_font(), 15)
    texto, pos_texto = fonte.render('{}'.format(comando), True, BLACK)
    pos_texto.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(texto, pos_texto)
    
# Função tela inicial do jogo
def tela_inicial(screen):

    # Definindo fonte com o tamanho almejado e tudo o que será usado abaixo com a caixinha
    fonte= pygame.font.Font(pygame.font.get_default_font(), 27)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(200, 250, 150, 40)
    active = False
    texto = ''

# Imagem de fundo
    background = pygame.image.load(path.join(img, 'pista.jpeg')).convert()


    done = False
    while not done:
        # Vendo o que o usuário fez
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se ele clicar na caixinha
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        nomecolocado = texto
                        texto = ''
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                    else:
                        texto += event.unicode
# Definindo botão "start"
    
        
        # Muda imagem para botar o nome 
        texto_ = fonte.render(texto, True, BLACK)
        width = max(200, texto_.get_width()+10)
        input_box.w = width
        screen.blit(texto_, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, WHITE, input_box, 2)    
       
        # Coloca o "INSIRA SEU NOME" junto
        pedenome, pos_texto = fonte.render('INSIRA SEU NOME', True, BLACK)
        pos_texto.center = ((WIDTH/2),(HEIGHT/2 - 170))
        screen.blit(pedenome, pos_texto)
        
        # Coloca o "APERTE ENTER" abaixo
        enter, pos_texto = fonte.render('APERTE ENTER', True, BLACK)
        pos_texto.center = ((WIDTH/2),(HEIGHT/2 - 80))
        screen.blit(enter, pos_texto)
        
        # Coloca a maior pontuação e o nome do recordista
        pontos = get_high_score()
        nomes = get_name()
        poemaior, poe = fonte.render('RECORDISTA', True, BLACK)
        poe.center = ((WIDTH/2),(HEIGHT/2 - 360))
        screen.blit(poemaior, poe)
        pedenome, pos_texto = fonte.render('{}:{}'.format(nomes, pontos), True, BLACK)
        pos_texto.center = ((WIDTH/2),(HEIGHT/2 - 330))
        screen.blit(pedenome, pos_texto)

        pygame.display.flip()
        clock.tick(30)
        
    # Retorna o nome para utilizar no High Score, caso necessário
    return nomecolocado

# Função da tela final do jogo (Perder o jogo)
def tela_final(screen, nomecolocado, pontuacao):
    
    # Definindo as fontes com os tamanhos desejados
    fonte = pygame.font.Font(pygame.font.get_default_font(), 30)
    Fonte = pygame.font.Font(pygame.font.get_default_font(), 40)
    clock = pygame.time.Clock()
    
    # Printando todas as informações na tela, junto com a imagem de fundo (tela inicial, nome, pontuação)
    
    
    #PRECISAMOS DE TELA INICIAL
    
    
    
    poetexto, pos_texto = Fonte.render('{}'.format(nomecolocado), True, BLACK)
    pos_texto.center = ((WIDTH/2),(HEIGHT/2-360))
    screen.blit(poetexto, pos_texto)

    poetexto_, pos_texto = fonte.render('SUA PONTUAÇÃO:', True, BLACK)
    pos_texto.center = ((WIDTH/2),(HEIGHT/2 - 300))
    screen.blit(poetexto_, pos_texto)

    poenome, pos_texto = Fonte.render('{}'.format(pontuacao), True, BLACK)
    pos_texto.center = ((WIDTH/2),(HEIGHT/2 - 250))
    screen.blit(poenome, pos_texto)
    
    # Colocando os botões 
    botao("RESTART (R)", 180, 540, 75, 50, WHITE, WHITE)
    botao("QUIT (Q )", 345, 540, 75, 50, WHITE, WHITE)

    # Vendo se a pessoa foi recordista ou não
    maior_pontuacao = get_high_score()
    if pontuacao >= maior_pontuacao:
        poenome, pos_texto = fonte.render('O MAIS NOVO', True, BLACK)
        pos_texto.center = ((WIDTH/2),(HEIGHT/2 - 100))
        screen.blit(poenome, pos_texto)
        poenome, pos_texto = fonte.render('RECORDISTA!', True, BLACK)
        pos_texto.center = ((WIDTH/2),(HEIGHT/2 - 40))
        screen.blit(poenome, pos_texto)
    
    pygame.display.flip()
    clock.tick(30)
    
    # Ações dos botoes do final do jogo
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    principal("")
                    done = True
                if event.key == pygame.K_r:
                    principal(nomecolocado) 
                    done = True
    
# Função principal do jogo, onde todas as ações estão
def principal(nomecolocado):
    
    jogo_roda= True
    while jogo_roda:
        
        # Toca música para o jogo
        #PRECISA DE MUSICA PARA O JOGO
        carrega_assets(img, som)['som_carro'].play()
        pygame.mixer.music.set_volume(0.5)
        
        #Fonte para o score
        fonte_score= pygame.font.Font(pygame.font.get_default_font(), 25)
        
    
        # Cria um carrinho
        carro=[]
        jogador =Jogador(carrega_assets(img, som)['img_jogador'])
        jogador = pygame.transform.scale(jogador, (58, 75))
        jogador.set_colorkey(WHITE)
        carro.append(jogador)
    
        # Cria todos os sprites e adiciona o player em tal
        all_sprites = pygame.sprite.Group()
        all_sprites.add(jogador)
        
        # Cria um grupo só dos carrinhos policiais
        inimigos= pygame.sprite.Group()
        policial=[]
        policia= Policia(carrega_assets(img, som)['img_policial'])
        policia= pygame.transform.scale(policia, (58, 75))
        policia.set_colorkey(WHITE)
        policial.append(policia)
        
# Cria grupo para as estrelas
    
# Cria um grupo para os 'Mais' (+)
    
# Cria um grupo para os tiros
    
        # Cria carrinhos e adiciona no grupo policiais
        for i in range(4):
            p = Policia(policia)
            all_sprites.add(p)
            inimigos.add(p)
    
# Cria os "Mais"(+)
    
# Adiciona as Estrelinhas
    

        speedx = 0
        time_= 0
        clock.tick(FPS)
        velocidade=0
        aceleracao=0.5
        background_y_cima = -HEIGHT
        background_y = 0
        # Define com quantos pontos o jogador comeca
        score=0

        # Caso a pessoa aperte RESTART não precise colocar o nome novamente
        if nomecolocado == "":
            # Pegar o nome colocado pela pessoa chamando a função da tela inicial
            nomecolocado = tela_inicial(screen)

        # Loop principal
        rodando = True
        while rodando:
        
            # Ajusta a velocidade do jogo
            clock.tick(FPS)
            
        
# Propabilidade de aparecer Estrelinha
        
# Probabilidade de aparecer "Mais"(+)
        
        
            # Processa os eventos (Mouse, teclado, botao, etc)
            for event in pygame.event.get():
                
                # Verifica se foi fechado
                if event.type == pygame.QUIT:
                    rodando = False
            
                # Verifica se apertou alguma tecla
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_LEFT:
                        speedx = -5 
                    if event.key == pygame.K_RIGHT:
                        speedx = 5 
                        
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT:
                        speedx = 0
                    if event.key  == pygame.K_RIGHT:
                        speedx = 0
                        
            # Indica a velocidade do jogador
            jogador.speedx= speedx
            
                 
# Se for a tecla espaco, atira! (caso tenha tiro)
        
            # Verifica se encostou na parede, se encostou, morreu
            if jogador.rect.right > 519:
                carrega_assets(img, som)['som_batida'].play()
                rodando = False
            if jogador.rect.left < 89:
                carrega_assets(img, som)['som_batida'].play()
                rodando = False    
        
            # Atualiza a ação de cada sprite
            all_sprites.update()
            
# Verifica se houve colisao entre tiro e carrinho
        
            # Verifica se houve colisao entre os carrinhos
            batida = pygame.sprite.spritecollide(jogador, policial, False, pygame.sprite.collide_circle)
            if batida:
                carrega_assets(img, som)['som_batida'].play()
                # Se teve, tem que dar um delay pro jogador ver que bateu
                time.sleep(0.5)
                rodando = False