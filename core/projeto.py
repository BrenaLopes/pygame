import pygame

class Projeto:
    def __init__(self, x, y, largura=30, altura=10, velocidade=7):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.velocidade = velocidade

    def mover(self):
        self.rect.x += self.velocidade

    def desenhar(self, tela, imagem):
        tela.blit(imagem, (self.rect.x, self.rect.y))

class TiroVilao:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10,5)
        self.vel_x = -10

    def mover(self):
        self.rect.x += self.vel_x