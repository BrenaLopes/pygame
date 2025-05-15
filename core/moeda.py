import pygame
import random
from config import LARGURA, ALTURA

class Moeda: 
    def __init__(self, imagem):
        self.imagem = imagem
        self.largura = 30
        self.altura = 30
        self.x = random.randint(LARGURA, LARGURA + 300)
        self.y = random.randint(50, ALTURA - 50)
        self.vel_x = random.randint(-4, -2)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
    def mover(self):
        self.rect.x += self.vel_x

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.rect.x, self.rect.y))