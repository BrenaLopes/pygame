import os

# TELA
LARGURA = 1500
ALTURA = 750
FPS = 30

# CORES
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
DOURADO = (255, 215, 0)
CINZA = (80, 80, 80)
PRETO= (0,0,0)

# CAMINHOS
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMAGENS_PATH = os.path.join(BASE_PATH, "assets", "imagens")
SONS_PATH = os.path.join(BASE_PATH, "assets", "sons")
