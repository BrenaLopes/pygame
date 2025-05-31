# LISTAS 

1) Usando While

def soma(lista):
    n = 0
    i = 0
    while i < len(lista):
        n += lista[i]
    return n 


2) Usando For(pelo índice)

def soma(lista):
    n = 0                  #tem que ser usado fora do loop, caso contrário será reiniciado(n=0) a cada iteração
    for i in range(len(lista)):          #for i in range(inicio, fim, passo)
        n += lista[i]
    return n 

3) Usando for (pelo termo)

def soma(lista):       
    n = 0
    for numero in lista:           #percorre direto o termo e não o índice da lista
        n += numero
    return n



if e elif ---- testa o if e só testa o elif se o if for FALSE
if e if ---- testa os dois independente se for TRUE ou FALSE


4) verificar se a lista é estritamente crescente(5.14)
    uso do NONE, atualizando o valor anteriores até que num <= anterior

5) comparar valores de uma função(ex 5.20)
    1) definir o primeiro termo termo declarando os termos i =0 antes do loop
    2) comparar normalmente dentro do while





# DICIONÁRIO 
 
1) for chave, valor in dic.items():       #lê sempre nessa ordem
        items_gaveta = len(valor["gaveta"])
        dict_final[chave] = items_gaveta
    return dict_final


2) quando não se pode chamar o dicionário direto pela chave: (ex 7.23)

    for destino, dados in pacotens.items():
        ranking, preço = dados       #!!!lista dentro de dicionário
        (...)

3) quando precisa fazer operações com valores de dicionários dentro de dicionários(ex 7.25 e 7.26)

    
    lista_compras = {}
    ingrediente = 'leite'
    qtd = 0.3

    1 iteração:

    lista_compras['leite'] = lista_compras.get('leite',0) + qtd

    #saída:  lista_compras = {'leite': 0.3}

    2 iteração: 

    qtd = 0.25
    #saída : lista_compras = {'leite': 0.55}

4) acessando dicionário dentro de dicionário com valor específico
    (ex do centro de custo, EX 7.25)

5) atribuir contagens a partir de lista
    ex: contar pontos, votos...
    dica: criar dicionário
    ver EX 5.28

6) receber nome e categoria e retornar os nomes como lista da categoria:
    ex: atletas por nacionalidade (EX 7.32 E 7.33)

    (...)

    if pais not in d_final:
        d_final[pais] = []         #!!!BIZU cria um valor numa lista vazia e só add após veirificar se aquela nacionalidade já existe
    d_final[pais].append(nome)
    
7) chave como nome com valor igual a um número onde é preciso retornar a chave com maios número(EX 7.34)7

    (...)código que calcula gasto total por bairro

    mais_custo = max(gasto_total, key = gasto_total.get())

    #max(iterável, key = função)#

# CADERNO DE ERROS 

1) retornar True ou False já na primeira iteração (ex 5.22)
2) quando se tem:
    for chave, valor in d.items()   #não precisa escrever d[valor] = ..., apenas valor  = 
3) inverter lista:

    #ERRO
    i = len(lista) - 1
    while i >= 0:
        i -= 1            #atualiza a iteração antes de add na lista
        lista_inv.append(lista[i])
    return lista_inv

    #COREEÇÃO
    i = len(lista)-1
    while i >= 0:
        lista_inv.append(list[i])        #add a lista antes de ir para o próximo termo
        i -= 1
    return lista_inv

# BIBLIOTECAS ÚTEIS

1) enumerate
    usado sempre que precisar do par índice-valor
    enumerate(iterable, start = 0)        
        - iterable = (lista, str, tupla, dicio...)
        - stard padrão = 0
    
    exemplos:

    frutas = ['maça', 'banana']

    for i, fruta in enumerate(frutas):
        print(f' {indice} fruta: {fruta}")
    

    saída: 
        1 fruta: maça
        2 fruta: banana
2) get
    Acessa o valor da chave em um dicionário sem gerar erro se essa chave não existir

    dados = {'nome': Brena, 'idade': 22}

    dados.get('nome')   #SAÍDA: Brena
    dados.get('altura')  #SAÍDA: None
    dados.get('idade')   #SAÍDA: 22

3) list
    transforma qualquer iterable em lista
    tupla = (1,2,3)
    lista = list(tupla)
    print(lista)    #SAÍDA: [1,2,3]
4) sum
    lista = [1,2,3]
    soma = sum(lista)  
    print(soma)    #saída: 6
