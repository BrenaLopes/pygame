import pygame
import os
from config import LARGURA, ALTURA, FPS, IMAGENS_PATH, CINZA, PRETO

def tela_instrucoes():
    pygame.init()
    tela=pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Instruções")
    clock = pygame.time.Clock()

    fundo= pygame.image.load('assets\imagens\Tela_de_intruções.png')
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    fonte = pygame.font.SysFont("Courier New", 28)
    fonte_titulo = pygame.font.SysFont("Courier New", 36)
    fonte_botao = pygame.font.SysFont("Courier New", 24)

    botao_voltar = pygame.Rect(50, ALTURA -70, 150, 50)
    cor_botao =CINZA
    cor_texto_botao= PRETO 

    rodando = True

    while rodando:
        clock.tick(FPS)
        tela.blit(fundo, (0, 0))
      #Código gerado com auxilio de IA

        pygame.draw.rect(tela, cor_botao, botao_voltar)
        texto_botao = fonte_botao.render("Voltar", True, cor_texto_botao)
        tela.blit(texto_botao, (botao_voltar.x + 30, botao_voltar.y + 10))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.collidepoint(evento.pos):
                    return "voltar" 
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    rodando = False 

        pygame.display.flip()