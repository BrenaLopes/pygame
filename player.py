import pygame
from sprites import SpriteAnimado

class Player(SpriteAnimado):
    def __init__(self, pos, groups, frames, sprites_colisao, frames_escada):
        # Inicializa a classe pai (SpriteAnimado)
        super().__init__(pos, frames, groups)

        self.sprites_colisao = sprites_colisao
        self.frames_escada = frames_escada
        self.estado = 'parado'

    def update(self):
        # Lógica de movimento do personagem
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Atualiza a animação com base no estado
        if self.estado == 'andando':
            self.image = self.frames['andar'][0]  # Exemplo de animação
        else:
            self.image = self.frames['parado'][0]

