import pygame
from config import ALTURA

class Jogador:
    def __init__(self, imagem):
        self.imagem = imagem
        self.largura = 60
        self.altura = 60
        self.x = 20
        self.y = ALTURA // 2
        self.velocidade = 7
        self.vida = 100
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def mover(self, teclas):
        if teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.y < ALTURA - self.altura:
            self.y += self.velocidade
        self.rect.y = self.y

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))