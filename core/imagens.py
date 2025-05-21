import pygame
import os
from config import IMAGENS_PATH, LARGURA, ALTURA

def carregar_cenario(nome_arquivo):
    caminho = os.path.join(IMAGENS_PATH, nome_arquivo)
    imagem = pygame.image.load(caminho)
    return pygame.transform.scale(imagem, (LARGURA, ALTURA))

def carregar_personagem(nome_arquivo, tamanho=(60, 60)):
    caminho = os.path.join(IMAGENS_PATH, nome_arquivo)
    imagem = pygame.image.load(caminho).convert_alpha()
    return pygame.transform.scale(imagem, tamanho)

def carregar_tiro(nome_arquivo="tiro.png", tamanho=(30, 30)):
    caminho = os.path.join(IMAGENS_PATH, nome_arquivo)
    imagem = pygame.image.load(caminho).convert_alpha()
    return pygame.transform.scale(imagem, tamanho)
