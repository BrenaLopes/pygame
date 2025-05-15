import pygame
import time
import random
from config import *
from core.jogador import Jogador
from core.vilao import Vilao, VilaoForte
from core.projeto import Projeto, TiroVilao
from core.imagens import carregar_fundo, carregar_personagem, carregar_tiro
from core.moeda import Moeda




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
    img_moeda = carregar_personagem("moeda.png", tamanho=(30, 30))
    img_vilao_forte = carregar_personagem("vilao_forte.gif", tamanho = (70,70))


    fonte = pygame.font.SysFont("Arial", 24)
    jogador = Jogador(img_bruxo)
    feitiços = []
    tiros_vilao = []
    viloes = []
    pontuacao = 0
    cadencia_tiro = 2
    ultimo_tiro = time.time()
    start_time = time.time()
    tempo_para_viloes_atirarem = 50 
    tempo_para_viloes_fortes = tempo_para_viloes_atirarem + 40  #segundos
    invulneravel_ate = start_time + 10
    tempo_para_moedas = 10 #as moedas aparecem depois de n segundos
    moedas = []
    moedas_criadas = False
    moedas_coletadas = 0
    tempo_para_atirar = 20 #segundos de espera antes de liberar os tiros
    viloes_fortes = []

    rodando = True
    while rodando:
        if time.time() - start_time >= tempo_para_moedas:
            if random.random() < 0.02:
                moedas.append(Moeda(img_moeda))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                if moedas_coletadas >= 5:
                    novo_tiro = Projeto(jogador.x + jogador.largura, jogador.y + jogador.altura // 2)
                    feitiços.append(novo_tiro)

        teclas = pygame.key.get_pressed()
        jogador.mover(teclas)

        if len(viloes) < 5:
            novo_vilao = Vilao(img_vilao)
            novo_vilao.vel_x = max(-12, -3 - pontuacao // 50)
            viloes.append(novo_vilao)

        # Fora do if acima:
        if time.time() - start_time >= tempo_para_viloes_fortes:
            if len(viloes_fortes) < 2:
                viloes_fortes.append(VilaoForte(img_vilao_forte))  # usa img_vilao_forte correto aqui


        for vilao in viloes + viloes_fortes:
            for moeda in moedas[:]:
                moeda.mover()
                if moeda.rect.right < 0:
                    moedas.remove(moeda)
                elif jogador.rect.colliderect(moeda.rect):
                    moedas.remove(moeda)
                    moedas_coletadas += 1
            vilao.mover()
            if time.time() - start_time >= tempo_para_viloes_atirarem:
                if random.random() < 0.01:
                    tiro = TiroVilao(vilao.rect.x, vilao.rect.y + vilao.rect.height //2)
                    tiros_vilao.append(tiro)

            if vilao.rect.colliderect(jogador.rect):
                if time.time() >= invulneravel_ate:
                    jogador.vida -= 10
                
                viloes.remove(vilao)
                viloes.append(Vilao(img_vilao))
                

                if jogador.vida <= 0:
                    rodando = False

            if vilao.rect.right < 0:
                viloes.remove(vilao)
                viloes.append(Vilao(img_vilao))    #cria um novo vilao

            for feitiço in feitiços[:]:
                if vilao.rect.colliderect(feitiço.rect):
                    feitiços.remove(feitiço)
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

        ultimo_tiro = time.time()



        for f in feitiços[:]:
            f.mover()
            if f.rect.x > LARGURA:
                feitiços.remove(f)

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

        tela.blit(fundo, (0, 0))
        jogador.desenhar(tela)
        for v in viloes: v.desenhar(tela)
        for f in feitiços: f.desenhar(tela, img_tiro)
        for t in tiros_vilao: pygame.draw.rect(tela, AMARELO, t.rect)

        desenhar_barra_vida(tela, jogador.vida)
        texto = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto, (10, 10))
        texto_moedas = fonte.render(f'Pomos de ouro:  {moedas_coletadas}', True, AMARELO)
        largura_texto = texto_moedas.get_width()
        tela.blit(texto_moedas, (LARGURA - largura_texto -10,10))
        fonte_aviso = pygame.font.SysFont("Arial", 28, bold=True)

        for moeda in moedas:
            moeda.desenhar(tela)

        if moedas_coletadas< 5:
            texto = f' Pegue {5 - moedas_coletadas} pomos de ouro para atirar!'
            aviso = fonte_aviso.render(texto, True, DOURADO)
            tela.blit(aviso, ((LARGURA- aviso.get_width())//2, ALTURA - 40))

        pygame.display.flip()
        clock.tick(FPS)
    print(f"[DEBUG] Tempo decorrido: {int(time.time() - start_time)}s | Vida: {jogador.vida} | Moedas coletadas: {moedas_coletadas}")
    pygame.quit()