import pygame
import os
import sys
from config import LARGURA, ALTURA, FPS, IMAGENS_PATH

def tela_game_over(): 

    pygame.init()
    tela=pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Game Over")
    clock=pygame.time.Clock()

    fundo= pygame.image.load(os.path.join(IMAGENS_PATH, "Tela_você_morreu.png"))
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    fonte = pygame.font.SysFont("Courier New", 28)

    #Código gerado com auxilio de IA
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    rodando = False
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        tela.blit(fundo, (0, 0))

        texto_info = fonte.render("Game Over. You Died", True, (255, 255, 255))
        texto_rect = texto_info.get_rect(center=(LARGURA // 2, ALTURA - 50))
        tela.blit(texto_info, texto_rect)

        pygame.display.flip()
        clock.tick(60)