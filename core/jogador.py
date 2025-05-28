import pygame
import time
import math
from config import ALTURA
from random import *
from core.imagens import carregar_frames_tiro
import os

caminho_animacao = os.path.join("assets", "imagens", "tiro")

class Jogador:
    def __init__(self, imagem):
        self.imagem = imagem
        self.largura = 60
        self.altura = 60
        self.velocidade = 7
        self.vida = 100

        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.midleft = (20, ALTURA // 2)

        self.tiros_restantes = 8
        self.cooldown_ativo_ate = 0
        self.tempo_proximo_tiro = 0
        self.frames_tiro = carregar_frames_tiro()

        self.animando_tiro = False
        self.indice_frame_tiro = 0
        self.tempo_ultimo_frame = 0
        self.intervalo_frame = 100  # milissegundos entre frames
        self.posicao_tiro = None  # Armazena posição fixa durante animação

    def mover(self, teclas):
        if not self.animando_tiro:  # Só move se não estiver animando o tiro
            if teclas[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.velocidade
            if teclas[pygame.K_DOWN] and self.rect.bottom < ALTURA:
                self.rect.y += self.velocidade

    def pode_atirar(self):
        agora = time.time()
        return (
            self.tiros_restantes > 0 and
            agora >= self.tempo_proximo_tiro and
            agora >= self.cooldown_ativo_ate
        )

    def atirar(self):
        agora = time.time()
        print(self.rect.center)
        self.tiros_restantes -= 1
        self.tempo_proximo_tiro = agora + 0.2
        if self.tiros_restantes == 0:
            self.cooldown_ativo_ate = agora + 2

        # Iniciar animação
        self.animando_tiro = True
        self.indice_frame_tiro = 0
        self.tempo_ultimo_frame = pygame.time.get_ticks()
        self.posicao_tiro = self.rect.center  # Armazena a posição do tiro

    def atualizar_animacao(self):
        if not self.animando_tiro:
            return

        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_frame > self.intervalo_frame:
            self.tempo_ultimo_frame = agora
            self.indice_frame_tiro += 1

            if self.indice_frame_tiro >= len(self.frames_tiro):
                self.animando_tiro = False
                self.indice_frame_tiro = 0
                self.posicao_tiro = None  # Libera a posição fixa

    def ganhar_bala(self):
        if self.tiros_restantes < 8 and time.time() >= self.cooldown_ativo_ate:
            self.tiros_restantes += 1

    def recarregar_se_preciso(self):
        agora = time.time()
        if self.tiros_restantes == 0 and agora >= self.cooldown_ativo_ate:
            self.tiros_restantes = 8

    def desenhar(self, tela):
        if self.animando_tiro:
            centro_x, centro_y = self.posicao_tiro
            centro_x -= 60
            offset_y = 0  # sem flutuação durante animação de tiro
        else:
            centro_x, centro_y = self.rect.center
            tempo_atual = pygame.time.get_ticks() / 1000
            offset_y = math.sin(tempo_atual * 5) * 14  # flutuação em Y apenas se não estiver atirando

        pos_x = centro_x - self.imagem.get_width() // 2
        pos_y = centro_y - self.imagem.get_height() // 2 + offset_y

        if self.animando_tiro:
            frame = self.frames_tiro[self.indice_frame_tiro]
            frame_x = centro_x + self.largura // 2
            frame_y = centro_y - frame.get_height() // 2
            tela.blit(frame, (frame_x, frame_y))
        else:
            tela.blit(self.imagem, (pos_x, pos_y))
