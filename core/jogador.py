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

        # Controle de tiros
        self.tiros_restantes = 8
        self.cooldown_ativo_ate = 0       # após 8 tiros
        self.tempo_proximo_tiro = 0       # tempo mínimo entre dois tiros

    def mover(self, teclas):
        if teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.y < ALTURA - self.altura:
            self.y += self.velocidade
        self.rect.y = self.y

    def pode_atirar(self):
        agora = time.time()

        # Em cooldown final
        if agora < self.cooldown_ativo_ate:
            return False

        # Entre tiros (0.3 segundos)
        if agora < self.tempo_proximo_tiro:
            return False

        # Se os 8 tiros acabaram e cooldown passou, recarrega
        if self.tiros_restantes == 0:
            self.tiros_restantes = 8

        return True

    def atirar(self):
        agora = time.time()
        if self.tiros_restantes > 0:
            self.tiros_restantes -= 1
            self.tempo_proximo_tiro = agora + 0.3  # intervalo entre tiros
            if self.tiros_restantes == 0:
                self.cooldown_ativo_ate = agora + 2  # cooldown final de 2s

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))
