 import pygame
from player import Player
from sprites import SpriteAnimado
from constantes_jogo import *
from fases import Fases
from ui import UI

class Game:
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.FULLSCREEN)
        pygame.display.set_caption("Meu Jogo")
        self.clock = pygame.time.Clock()

        # Criar a instância do personagem (Player)
        self.player = Player((100, 100), [pygame.sprite.Group()], "frames_player", "sprite_colisao", "frames_escada")
        
        # Outras inicializações necessárias, como fases e UI
        self.fases = Fases()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Atualiza o jogo
            self.fases.update()
            self.player.update()

            # Desenha tudo na tela
            self.janela.fill((255, 255, 255))  # Limpa a tela
            self.player.draw(self.janela)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
