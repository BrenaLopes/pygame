import pygame
import os
from config import LARGURA, ALTURA, FPS, IMAGENS_PATH
from core.tela_de_instruções import tela_instrucoes
from core.jogo import executar_jogo
def tela_inicial():
    largura_botao = 300
    altura_botao = 40
    espaco_entre_botoes = 20
    altura_base = ALTURA // 2


    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Harry Potter e as Relíquias da Morte")
    clock = pygame.time.Clock()

    fundo = pygame.image.load(os.path.join(IMAGENS_PATH, "tela_inicial.png"))
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    fonte = pygame.font.SysFont("Courier New", 28)
    input_box = pygame.Rect(860, 630, 300, 40)
    cor_input_ativa = pygame.Color("white")
    cor_input_inativa = pygame.Color("gray")
    cor_input = cor_input_inativa

    nome = ""
    ativo = False

    botao_jogar = pygame.Rect(520, 440 , largura_botao, altura_botao)
    botao_instrucoes = pygame.Rect(520, 530, largura_botao, altura_botao)
    botao_sair = pygame.Rect(LARGURA // 2 - largura_botao // 2, altura_base + 2 * (altura_botao + espaco_entre_botoes), largura_botao, altura_botao)
    
    while True:
        tela.blit(fundo, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        if botao_jogar.collidepoint(mouse_pos):
            brilho = pygame.Surface((botao_jogar.width, botao_jogar.height), pygame.SRCALPHA)
            brilho.fill((255, 255, 255, 60))  # branco translúcido
            tela.blit(brilho, botao_jogar.topleft)  # centralizado corretamente

        if botao_instrucoes.collidepoint(mouse_pos):
            brilho = pygame.Surface((botao_instrucoes.width, botao_instrucoes.height), pygame.SRCALPHA)
            brilho.fill((255, 255, 255, 60))
            tela.blit(brilho, botao_instrucoes.topleft)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(evento.pos):
                    ativo = True
                    cor_input = cor_input_ativa
                elif botao_jogar.collidepoint(evento.pos) and nome.strip():
                    return nome.strip()
                else:
                    ativo = False
                    cor_input = cor_input_inativa
        

            elif evento.type == pygame.KEYDOWN and ativo:
                if evento.key == pygame.K_RETURN and nome.strip():
                    return nome.strip()
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                else:
                    if len(nome) < 20:
                        nome += evento.unicode

        if botao_instrucoes.collidepoint(mouse_pos):
            if evento.type == pygame.MOUSEBUTTONDOWN:
                tela_instrucoes()


        pygame.draw.rect(tela, cor_input, input_box, 2)
        texto_surface = fonte.render(nome, True, cor_input_ativa)
        tela.blit(texto_surface, (input_box.x + 10, input_box.y + 5))

        pygame.display.flip()
        clock.tick(FPS)
