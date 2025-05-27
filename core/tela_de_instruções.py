import pygame
import os
from config import LARGURA, ALTURA, FPS, IMAGENS_PATH

def tela_instrucoes():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Instruções")
    clock = pygame.time.Clock()

    fundo = pygame.image.load('assets/imagens/Tela_de_intruções.png')
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    botao_voltar = pygame.Rect(598, ALTURA - 142, 300, 40)

    rodando = True

    while rodando:
        clock.tick(FPS)
        tela.blit(fundo, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        if botao_voltar.collidepoint(mouse_pos):
            brilho = pygame.Surface((botao_voltar.width, botao_voltar.height), pygame.SRCALPHA)
            brilho.fill((255, 255, 255, 60))
            tela.blit(brilho, botao_voltar.topleft)

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
