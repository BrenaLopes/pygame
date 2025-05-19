import pygame
import sys

#gerado por IA

pygame.init()

# Tamanho da janela (baseado na imagem)
largura, altura = 256, 256
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tela de Instruções - Harry Potter")

# Carrega a imagem da tela de instruções
imagem_instrucao = pygame.image.load("Tela de intruções.png").convert()

# Define a área do botão "VOLTAR"
botao_voltar = pygame.Rect(84, 210, 88, 28)

# Função para mostrar a tela de instruções
def mostrar_tela_instrucoes():
    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1 and botao_voltar.collidepoint(evento.pos):
                    executando = False  # Sai da tela de instruções

        # Desenha a imagem de fundo
        tela.blit(imagem_instrucao, (0, 0))

        # Atualiza a tela
        pygame.display.flip()

# Executa a função da tela de instruções
mostrar_tela_instrucoes()
