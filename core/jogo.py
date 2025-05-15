import pygame
import time
from config import *
from core.jogador import Jogador
from core.vilao import Vilao
from core.projeto import Projeto, TiroVilao
from core.imagens import carregar_fundo, carregar_personagem, carregar_tiro

def desenhar_barra_vida(tela, vida):
    largura_barra = 200
    altura_barra = 20
    preenchimento = int((vida / 100) * largura_barra)
    pygame.draw.rect(tela, VERMELHO, (10, 40, largura_barra, altura_barra))
    pygame.draw.rect(tela, VERDE, (10, 40, preenchimento, altura_barra))

def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Bruxo Invaders")
    clock = pygame.time.Clock()

    fundo = carregar_fundo()
    img_bruxo = carregar_personagem("Harry Potter.gif")
    img_tiro = carregar_tiro()
    img_vilao = carregar_personagem("vilao.png.jpg", tamanho=(50, 50))

    fonte = pygame.font.SysFont("Arial", 24)
    jogador = Jogador(img_bruxo)
    feitiços = []
    tiros_vilao = []
    viloes = []
    pontuacao = 0
    cadencia_tiro = 2
    ultimo_tiro = time.time()

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                novo_tiro = Projeto(jogador.x + jogador.largura, jogador.y + jogador.altura // 2)
                feitiços.append(novo_tiro)

        teclas = pygame.key.get_pressed()
        jogador.mover(teclas)

        if len(viloes) < 5:
            viloes.append(Vilao(img_vilao))

        for vilao in viloes[:]:
            vilao.mover()
            if time.time() - ultimo_tiro > cadencia_tiro:
                tiros_vilao.append(TiroVilao(vilao.rect.x, vilao.rect.y + 20))
            for feitiço in feitiços[:]:
                if vilao.rect.colliderect(feitiço.rect):
                    viloes.remove(vilao)
                    feitiços.remove(feitiço)
                    pontuacao += 10
                    break
        ultimo_tiro = time.time()

        for f in feitiços[:]:
            f.mover()
            if f.rect.x > LARGURA:
                feitiços.remove(f)

        for t in tiros_vilao[:]:
            t.mover()
            if t.rect.colliderect(jogador.rect):
                jogador.vida -= 10
                tiros_vilao.remove(t)
                if jogador.vida <= 0:
                    print("Game Over!")
                    rodando = False
            elif t.rect.x < 0:
                tiros_vilao.remove(t)

        tela.blit(fundo, (0, 0))
        jogador.desenhar(tela)
        for v in viloes: v.desenhar(tela)
        for f in feitiços: f.desenhar(tela, img_tiro)
        for t in tiros_vilao: pygame.draw.rect(tela, AMARELO, t.rect)

        desenhar_barra_vida(tela, jogador.vida)
        texto = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()