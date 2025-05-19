import pygame
import os
import json
from config import LARGURA, ALTURA, FPS, IMAGENS_PATH


### está parte foi gerada por IA cotendo alterações dos autores
ARQUIVO_RANKING = os.path.join("dados", "ranking.json")

def salvar_pontuacao(nome, pontos):
    if not os.path.exists("dados"):
        os.makedirs("dados")
    if os.path.exists(ARQUIVO_RANKING):
        with open(ARQUIVO_RANKING, "r") as f:
            ranking = json.load(f)
    else:
        ranking = []

    ranking.append({"nome": nome, "pontos": pontos})
    if len(ranking) > 5:
        ranking = []

    with open(ARQUIVO_RANKING, "w") as f:
        json.dump(ranking, f, indent=4)

def exibir_ranking():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Ranking")
    clock = pygame.time.Clock()

    fundo = pygame.image.load(os.path.join(IMAGENS_PATH, "tela_ranking.png"))
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    fonte = pygame.font.SysFont("Courier New", 32, bold=True)
    fonte_pequena = pygame.font.SysFont("Arial", 24)

    if os.path.exists(ARQUIVO_RANKING):
        with open(ARQUIVO_RANKING, "r") as f:
            ranking = json.load(f)
    else:
        ranking = []

    rodando = True
    while rodando:
        tela.blit(fundo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        for i, jogador in enumerate(ranking):
            texto = fonte.render(f"{i+1}. {jogador['nome']} - {jogador['pontos']} pts", True, (255, 255, 255))
            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, 150 + i*50))

        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
