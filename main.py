from core.jogo import executar_jogo
from core.tela_inicial import tela_inicial 
from core.tela_de_instruções import tela_instrucoes


if __name__ == "__main__":
    nome = tela_inicial()
    executar_jogo(nome) 
