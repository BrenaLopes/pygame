import pygame
import time
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

        self.tiros_restantes = 8
        self.cooldown_ativo_ate = 0
        self.tempo_proximo_tiro = 0

    def mover(self, teclas):
        if teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.y < ALTURA - self.altura:
            self.y += self.velocidade
        self.rect.y = self.y

    def pode_atirar(self):
        agora = time.time()
        return (
            self.tiros_restantes > 0 and
            agora >= self.tempo_proximo_tiro and
            agora >= self.cooldown_ativo_ate
        )

    def atirar(self):
        agora = time.time()
        self.tiros_restantes -= 1
        self.tempo_proximo_tiro = agora + 0.2
        if self.tiros_restantes == 0:
            self.cooldown_ativo_ate = agora + 2

    def ganhar_bala(self):
        if self.tiros_restantes < 8 and time.time() >= self.cooldown_ativo_ate:
            self.tiros_restantes += 1

    def recarregar_se_preciso(self):
        agora = time.time()
        if self.tiros_restantes == 0 and agora >= self.cooldown_ativo_ate:
            self.tiros_restantes = 8

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))
