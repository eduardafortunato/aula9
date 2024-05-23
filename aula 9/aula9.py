#Título: Um game PVP com timer.
#link do material da aula: https://bit.ly/pythontela01
#saiba mais: comentários do autor - https://vemfazermatematicaegames.blogspot.com/2020/06/pygames-construindo-um-game-pvp-com.htm

import pygame, sys
import math
import random
import time

pygame.init()

largura_janela = 2000   
altura_janela = 1000
pygame.display.set_caption('Galinhazinha')
clock = pygame.time.Clock()

fgExit = False

personagemImg = pygame.image.load('galinha.png')
personagem2Img = pygame.image.load('pintinho.png')
cenario = pygame.image.load('cenario.jpg')

DEFAULT_IMAGE_SIZE = (100, 100) #tamando do personagem
escala = (2000, 1000)
inexistir = (0, 0)
personagem2Img = pygame.transform.scale(personagem2Img, DEFAULT_IMAGE_SIZE)
personagemImg = pygame.transform.scale(personagemImg, DEFAULT_IMAGE_SIZE)

DEFAULT_IMAGE_SIZE = (2000, 1000) #tamanho do cenario
escala = (2000, 1000)
inexistir = (0, 0)
cenario = pygame.transform.scale(cenario, DEFAULT_IMAGE_SIZE)
pulo = pygame.mixer.Sound('pulo.mp3')

somdefundo = pygame.mixer.music.load('som de fundo.mp3')
pygame.mixer.music.set_volume(50)
pygame.mixer.music.play(-1)

fonte = pygame.font.SysFont("dejavusans", 30)
textoperdeu = fonte.render("Você perdeu! Reinicie o jogo!", True, (255,0,0))
textoperdeu2 = fonte.render("Tempo Total:", True, (255,0,0))
texto0 = fonte.render("Clique com o mouse para instruções.", True, (255,0,0))
texto1 = fonte.render("Olá gamer, seja bem vindo ao jogo do Mário!", True, (255,0,0))
texto2 = fonte.render("Vamos começar a jogar?", True, (255,0,0))
texto3 = fonte.render("Use as setas para se movimentar.", True, (255,0,0))
texto4 = fonte.render("Desvie do cogumelo para ficar vivo!", True, (255,0,0))
texto5 = fonte.render("Obrigado por prestigiar esse game!", True, (255,0,0))
contador = 0

tela = pygame.display.set_mode((largura_janela, altura_janela))
x = (550+largura_janela * 0.1)
y = (280+altura_janela * 0.1)
a = (largura_janela * 0.1)
b = (altura_janela * 0.1)
x1 = 0
x2 = 0
y1 = 0
y2 = 0
a1 = 0 #posição do cugumelo
a2 = 0
b1 = 0
b2 = 0
personagem_speed = 0

xmario = x+45
ymario = y+65
xcogumelo = a+128
ycogumelo = b+128
x_1 = x
y_1 = y
a_1 = a
b_1 = b
t = 0

cronometro = pygame.time.get_ticks()

def colidiu():
    distancia =  math.sqrt(math.pow(xmario-xcogumelo,2)+math.pow(ymario-ycogumelo,2))
    print (distancia)
    if distancia<128+50:
        return True
    else:
        return False
    
while not fgExit:
    segundos = (pygame.time.get_ticks()-cronometro)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            contador = contador +1
            if contador == 1:
               tela.fill((0,0,0))
               tela.blit(texto1, (0,550))
            if contador == 2:
               tela.fill((0,0,0))
               tela.blit(texto2, (0,550))
            if contador == 3:
               tela.fill((0,0,0))
               tela.blit(texto3, (0,550))
            if contador == 4:
               tela.fill((0,0,0))
               tela.blit(texto4, (0,550))
            if contador == 5:
               tela.fill((0,0,0))
               tela.blit(texto5, (0,550))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1 = 0
            if event.key == pygame.K_RIGHT:
                x2 = 0
            if event.key == pygame.K_UP:
                y1 = 0
            if event.key == pygame.K_DOWN:
                y2 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -5
            if event.key == pygame.K_RIGHT:
                x2 = 5
            if event.key == pygame.K_UP:
                y1 = -5
            if event.key == pygame.K_DOWN:
                y2 = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: #teclas do cogumelo
                a1 = 0
            if event.key == pygame.K_d:
                a2 = 0
            if event.key == pygame.K_w:
                b1 = 0
            if event.key == pygame.K_s:
                b2 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a1 = -5
            if event.key == pygame.K_d:
                a2 = 5
            if event.key == pygame.K_w:
                b1 = -5
            if event.key == pygame.K_s:
                b2 = 5

    x += x1 + x2
    y += y1 + y2
    a += a1 + a2
    b += b1 + b2
    xmario = x+45 #onde ele começa
    ymario = y+65
    xcogumelo = a+128
    ycogumelo = b+128
    if colidiu():
        pulo.play()
        tela.fill((0,0,0))
        tela.blit(textoperdeu, (150,300))
        tela.blit(textoperdeu2, (150,350))
        rsegundos = fonte.render(str(segundos), True, (255,0,0))
        tela.blit(rsegundos, (150,400))
        pygame.display.update()
        time.sleep(4)
        pygame.quit()        
        print ('bateu')
        print (segundos) 
        x = x_1
        y = y_1        
    else:
        x_1 = x
        y_1 = y        
    tela.blit(cenario,(0,0))
    tela.blit(personagemImg, (x, y))
    tela.blit(personagem2Img, (a, b))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
