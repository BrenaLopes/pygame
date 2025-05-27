import pygame
from pathlib import Path
def tocar_musica_de_fundo():
    pygame.mixer.init()
    pygame.mixer.music.load("sons\Música HP fundo.mp3")
    sound_path = Path("sons") / "Música HP fundo.mp3"

    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

def tocar_som_tiro():
    efeito = pygame.mixer.Sound("pygame\sons\Tiro do Hp.mp3")
    efeito.set_volume(0.2)
    efeito.play()

def tocar_som_dano():
    efeito = pygame.mixer.Sound("pygame\sons\Dano sofrido.mp3")
    efeito.set_volume(0.3)
    efeito.play()

def tocar_som_moeda():
    efeito = pygame.mixer.Sound("pygame\sons\Pegando pomo.mp3")
    efeito.set_volume(0.2)
    efeito.play()
