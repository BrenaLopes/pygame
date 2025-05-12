import pygame
from constantes_jogo import *

class Sprites(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center=pos)

class SpriteAnimado(Sprites):
    def __init__(self, pos, frames, groups, vel_animacao=VEL_ANIMACAO):
        self.frames = frames
        self.frame_index = 0
        self.vel_animacao = vel_animacao
        super().__init__(pos, self.frames[self.frame_index], groups)

    def update(self):
        # Atualiza o frame da animação
        self.frame_index += 1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[self.frame_index]
