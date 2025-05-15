import pygame

class Projeto:
    def __init__(self, x, y, largura=30, altura=10, velocidade=7):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.velocidade = velocidade

    def mover(self):
        self.rect.x += self.velocidade

    def desenhar(self, tela, imagem):
        tela.blit(imagem, (self.rect.x, self.rect.y))

class TiroVilao(Projeto):
    def __init__(self, x, y):
        super().__init__(x, y, largura=10, altura=5, velocidade=5)
        self.velocidade *= -1