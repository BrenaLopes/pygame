import pygame
import random
import sys
import os

# Inicialização do Pygame
pygame.init()

# Caminho da pasta atual
base_path = os.path.dirname(os.path.abspath(__file__))
imagens_path = os.path.join(base_path, "imagens")

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bruxo Invaders - Lateral")

# Cores
branco = (255, 255, 255)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
preto = (0, 0, 0)

# Fonte para pontuação
fonte = pygame.font.SysFont("Arial", 24)
pontuacao = 0

# Vida do jogador
vida = 100
dano_tiro = 10

# Taxa de disparo dos vilões
chance_tiro_vilao = 0.01

# Carregar imagens
def carregar_imagem(nome_arquivo, tamanho=None):
    caminho = os.path.join(imagens_path, nome_arquivo)
    imagem = pygame.image.load(caminho).convert_alpha()
    if tamanho:
        imagem = pygame.transform.scale(imagem, tamanho)
    return imagem

fundo = carregar_imagem("fundo.png", (largura, altura))
bruxo_imagem = carregar_imagem("bruxo.png", (60, 60))
tiro_imagem = carregar_imagem("tiro.png", (30, 10))
vilao_imagem = carregar_imagem("vilao.png", (50, 50))

# Jogador
bruxo_largura, bruxo_altura = 60, 60
bruxo_x = 20
bruxo_y = altura // 2
bruxo_velocidade = 5

# Feitiços e tiros
feiticamentos = []
tiros_vilao = []
feitico_velocidade = 7
tiro_vilao_velocidade = 5

# Vilões
viloes = []
vilao_largura, vilao_altura = 50, 50
num_viloes = 5
vilao_velocidade = 3

def criar_vilao():
    x = largura
    y = random.randint(0, altura - vilao_altura)
    return pygame.Rect(x, y, vilao_largura, vilao_altura)

def desenhar():
    tela.blit(fundo, (0, 0))
    tela.blit(bruxo_imagem, (bruxo_x, bruxo_y))

    for feitico in feiticamentos:
        tela.blit(tiro_imagem, (feitico.x, feitico.y))

    for tiro in tiros_vilao:
        pygame.draw.rect(tela, amarelo, tiro)

    for vilao in viloes:
        tela.blit(vilao_imagem, (vilao.x, vilao.y))

    texto = fonte.render(f"Pontos: {pontuacao}", True, branco)
    tela.blit(texto, (10, 10))

    # Barra de vida
    pygame.draw.rect(tela, vermelho, (10, 40, 200, 20))
    pygame.draw.rect(tela, verde, (10, 40, 2 * vida, 20))

    pygame.display.flip()

def jogo():
    global pontuacao, bruxo_y, vida
    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    feitico = pygame.Rect(bruxo_x + bruxo_largura, bruxo_y + bruxo_altura // 2, 30, 10)
                    feiticamentos.append(feitico)

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and bruxo_y > 0:
            bruxo_y -= bruxo_velocidade
        if teclas[pygame.K_DOWN] and bruxo_y < altura - bruxo_altura:
            bruxo_y += bruxo_velocidade

        if len(viloes) < num_viloes:
            viloes.append(criar_vilao())

        for vilao in viloes[:]:
            vilao.x -= vilao_velocidade

            if random.random() < chance_tiro_vilao:
                tiro = pygame.Rect(vilao.x, vilao.y + vilao_altura // 2, 10, 5)
                tiros_vilao.append(tiro)

            for feitico in feiticamentos[:]:
                if vilao.colliderect(feitico):
                    viloes.remove(vilao)
                    feiticamentos.remove(feitico)
                    pontuacao += 10
                    break

        for feitico in feiticamentos[:]:
            feitico.x += feitico_velocidade
            if feitico.x > largura:
                feiticamentos.remove(feitico)

        for tiro in tiros_vilao[:]:
            tiro.x -= tiro_vilao_velocidade
            if tiro.colliderect(pygame.Rect(bruxo_x, bruxo_y, bruxo_largura, bruxo_altura)):
                vida -= dano_tiro
                tiros_vilao.remove(tiro)
                if vida <= 0:
                    print("Você perdeu!")
                    rodando = False
            elif tiro.x < 0:
                tiros_vilao.remove(tiro)

        desenhar()
        clock.tick(30)

jogo()
pygame.quit()
