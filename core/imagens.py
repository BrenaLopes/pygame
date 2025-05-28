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

def carregar_frames_tiro(prefixo="harry_tiro_", quantidade=3, tamanho=(80, 80)):
    caminho_pasta = os.path.join("assets", "imagens", "tiro")
    frames = []
    for i in range(1, quantidade + 1):
        nome_arquivo = f"{prefixo}{i}.png"
        caminho = os.path.join(caminho_pasta, nome_arquivo)
        imagem = pygame.image.load(caminho).convert_alpha()
        imagem = pygame.transform.scale(imagem, tamanho)
        frames.append(imagem)
    return frames


def carregar_tiro(nome_arquivo="tiro.png", tamanho=(30, 30)):
    caminho = os.path.join(IMAGENS_PATH, nome_arquivo)
    imagem = pygame.image.load(caminho).convert_alpha()
    return pygame.transform.scale(imagem, tamanho)
