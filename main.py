from core.jogo import executar_jogo
from core.tela_inicial import tela_inicial 


if __name__ == "__main__":
    nome = tela_inicial()
    executar_jogo(nome) 


    

if __name__ == "__main__":
    nome = tela_inicial()
    print(f"[DEBUG] Nome digitado: {nome}")
    executar_jogo(nome)