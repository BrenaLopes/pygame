import pygame
import random
from config import LARGURA, ALTURA

class Vilao:
    def __init__(self, imagem):
        self.imagem = imagem
        self.largura = 50
        self.altura = 50
        self.x = LARGURA
        self.y = random.randint(0, ALTURA - self.altura)
        self.velocidade = 3
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def mover(self):
        self.rect.x -= self.velocidade

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.rect.x, self.rect.y))