import pygame
import random
from config import LARGURA, ALTURA

class Vilao:
    def __init__(self, imagem, vida =1):
        self.imagem = imagem
        self.largura = 50
        self.altura = 50
        self.x = random.randint(LARGURA, LARGURA  + 300)
        self.y = random.randint(0, ALTURA - self.altura)
        self.vel_x = random.randint(-8,-5) #vilão vem da direita para esquerda 
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.vida = vida

    def mover(self):
        self.rect.x += self.vel_x

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.rect.x, self.rect.y))
        

class VilaoForte(Vilao):
    def __init__(self, imagem):
        super().__init__(imagem, vida = 5)
        self.vel_x = -4 


