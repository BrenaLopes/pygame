import pygame
import time
import random
import os
from config import *
from core.jogador import Jogador
from core.vilao import Vilao, VilaoForte
from core.projeto import Projeto, TiroVilao
from core.imagens import carregar_personagem, carregar_tiro
from core.moeda import Moeda
from core.imagens import carregar_cenario, carregar_personagem, carregar_tiro


def desenhar_barra_vida(tela, vida):
    largura_barra = 200
    altura_barra = 20
    preenchimento = int((vida / 100) * largura_barra)
    pygame.draw.rect(tela, VERMELHO, (10, 40, largura_barra, altura_barra))
    pygame.draw.rect(tela, VERDE, (10, 40, preenchimento, altura_barra))

def executar_jogo(nome_jogador):
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Harry Potter e as Relíquias da morte")
    clock = pygame.time.Clock()

    # Cenários
    cenario_dia = carregar_cenario("cenario_dia.png")
    cenario_tarde = carregar_cenario("cenario_tarde.png")
    cenario_noite = carregar_cenario("cenario_noite.jpg")

    # Imagens
    img_bruxo = carregar_personagem("Harry_Potter.png")
    img_tiro = carregar_tiro()
    img_vilao = carregar_personagem("vilao.png", tamanho=(80, 80))
    img_moeda = carregar_personagem("moeda.png", tamanho=(40, 40))
    img_vilao_forte = carregar_personagem("vilao_forte.gif", tamanho = (100,100))


    fonte = pygame.font.SysFont("Arial", 24)
    fonte_aviso = pygame.font.SysFont("Arial", 28, bold=True)

    jogador = Jogador(img_bruxo)
    feitiços = []
    tiros_vilao = []
    viloes = []
    viloes_fortes = []
    moedas = []

    pontuacao = 0
    moedas_coletadas = 0
    moedas_para_curar = 10
    cura_a_cada = 10

    start_time = time.time()
    tempo_para_moedas = 7
    tempo_para_atirar = 20
    tempo_para_viloes_atirarem = 50
    tempo_para_viloes_fortes = tempo_para_viloes_atirarem + 20
    invulneravel_ate = start_time + 10

    transicao_duracao = 3
    rodando = True

    while rodando:
        clock.tick(FPS)
        tempo_jogo = time.time() - start_time

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                if moedas_coletadas >= 5:
                    novo_tiro = Projeto(jogador.x + jogador.largura, jogador.y + jogador.altura // 2)
                    feitiços.append(novo_tiro)

        teclas = pygame.key.get_pressed()
        jogador.mover(teclas)

        # Moedas
        if tempo_jogo >= tempo_para_moedas and random.random() < 0.02:
            moedas.append(Moeda(img_moeda))

        for moeda in moedas[:]:
            moeda.mover()
            if moeda.rect.right < 0:
                moedas.remove(moeda)
            elif jogador.rect.colliderect(moeda.rect):
                moedas.remove(moeda)
                moedas_coletadas += 1
                if moedas_coletadas >= moedas_para_curar:
                    jogador.vida = min(100, jogador.vida + 20)
                    moedas_para_curar += cura_a_cada

        # Vilões comuns
        if len(viloes) < 5:
            novo = Vilao(img_vilao)
            novo.vel_x = max(-12, -3 - pontuacao // 50)
            viloes.append(novo)

        # Vilões fortes
        if tempo_jogo >= tempo_para_viloes_fortes and len(viloes_fortes) < 2:
            viloes_fortes.append(VilaoForte(img_vilao_forte))

        # Movimentação e colisões
        for vilao in viloes + viloes_fortes:
            vilao.mover()

            if tempo_jogo >= tempo_para_viloes_atirarem and random.random() < 0.01:
                tiros_vilao.append(TiroVilao(vilao.rect.x, vilao.rect.centery))

            if vilao.rect.colliderect(jogador.rect):
                if time.time() >= invulneravel_ate:
                    jogador.vida -= 10
                if vilao in viloes:
                    viloes.remove(vilao)
                    viloes.append(Vilao(img_vilao))
                elif vilao in viloes_fortes:
                    viloes_fortes.remove(vilao)
                    viloes_fortes.append(VilaoForte(img_vilao_forte))
                if jogador.vida <= 0:
                    rodando = False

            if vilao.rect.right < 0:
                if vilao in viloes:
                    viloes.remove(vilao)
                    viloes.append(Vilao(img_vilao))
                elif vilao in viloes_fortes:
                    viloes_fortes.remove(vilao)
                    viloes_fortes.append(VilaoForte(img_vilao_forte))

            for f in feitiços[:]:
                if vilao.rect.colliderect(f.rect):
                    feitiços.remove(f)
                    vilao.vida -= 1
                    if vilao.vida <= 0:
                        if vilao in viloes:
                            viloes.remove(vilao)
                            viloes.append(Vilao(img_vilao))
                        elif vilao in viloes_fortes:
                            viloes_fortes.remove(vilao)
                            viloes_fortes.append(VilaoForte(img_vilao_forte))
                        pontuacao += 10
                    break

        # Atualiza feitiços
        for f in feitiços[:]:
            f.mover()
            if f.rect.x > LARGURA:
                feitiços.remove(f)

        # Atualiza tiros dos vilões
        for t in tiros_vilao[:]:
            t.mover()
            if t.rect.colliderect(jogador.rect):
                if time.time() >= invulneravel_ate:
                    jogador.vida -= 10
                tiros_vilao.remove(t)
                if jogador.vida <= 0:
                    rodando = False
            elif t.rect.right < 0:
                tiros_vilao.remove(t)

        # CENÁRIO com transições suaves
        if tempo_jogo < tempo_para_viloes_atirarem:
            fundo_atual = cenario_dia
            proximo_fundo = cenario_tarde
            tempo_alvo = tempo_para_viloes_atirarem
        elif tempo_jogo < tempo_para_viloes_fortes:
            fundo_atual = cenario_tarde
            proximo_fundo = cenario_noite
            tempo_alvo = tempo_para_viloes_fortes
        else:
            fundo_atual = cenario_noite
            proximo_fundo = None
            tempo_alvo = None

        if proximo_fundo:
            progresso = max(0, min(1, (tempo_jogo - (tempo_alvo - transicao_duracao)) / transicao_duracao))
            alpha = int(progresso * 255)
            tela.blit(fundo_atual, (0, 0))
            fade = proximo_fundo.copy()
            fade.set_alpha(alpha)
            tela.blit(fade, (0, 0))
        else:
            tela.blit(fundo_atual, (0, 0))

        # Desenhar elementos
        jogador.desenhar(tela)
        for v in viloes + viloes_fortes: v.desenhar(tela)
        for f in feitiços: f.desenhar(tela, img_tiro)
        for t in tiros_vilao: pygame.draw.rect(tela, AMARELO, t.rect)
        for moeda in moedas: moeda.desenhar(tela)

        desenhar_barra_vida(tela, jogador.vida)
        tela.blit(fonte.render(f"Pontos: {pontuacao}", True, BRANCO), (10, 10))

        texto_moedas = fonte.render(f'Pomos de ouro: {moedas_coletadas}', True, AMARELO)
        tela.blit(texto_moedas, (LARGURA - texto_moedas.get_width() - 10, 10))

        if moedas_coletadas < 5:
            aviso = fonte_aviso.render(f'Pegue {5 - moedas_coletadas} pomos de ouro para atirar!', True, DOURADO)
            tela.blit(aviso, ((LARGURA - aviso.get_width()) // 2, ALTURA - 40))

        
        pygame.display.flip()

    from core.ranking import salvar_pontuacao, exibir_ranking
    salvar_pontuacao(nome_jogador, pontuacao)
    pygame.quit()
    exibir_ranking()

    