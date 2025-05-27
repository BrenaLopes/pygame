import pygame
import os
from config import SONS_PATH
def tocar_musica_de_fundo():
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(SONS_PATH, "Música HP fundo.mp3"))

    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

def tocar_som_tiro():
    efeito = pygame.mixer.Sound(os.path.join(SONS_PATH, "Tiro do Hp.mp3"))
    efeito.set_volume(0.2)
    efeito.play()

def tocar_som_dano():
    efeito = pygame.mixer.Sound(os.path.join(SONS_PATH, "Dano sofrido.mp3"))
    efeito.set_volume(0.3)
    efeito.play()

def tocar_som_moeda():
    efeito = pygame.mixer.Sound(os.path.join(SONS_PATH, "Pegando pomo.mp3"))
    efeito.set_volume(0.2)
    efeito.play()
