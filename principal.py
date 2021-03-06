from tree import Tree
import itertools
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from gera_grafo import exibeGrafo


def geraGrafo(id, id_pai, estado_inicial, estado_final, restricoes, pesos, personagens, num_ocupantes_barco, dicionario_heuristica, problema):
    def prob_1():
        root.destroy()

        ROOT = 0

        # Fazendeiro, alface, bode, lobo:
        dicionario_heuristica = {
            'A B F L|': 22,
            'A L|B F': 18,
            'A F L|B': 17,
            'L|A B F': 14,
            'A|B F L': 12,
            'B F L|A': 10,
            'A B F|L': 8,
            'B|A F L': 5,
            'B F|A L': 4,
            '|A B F L': 0
        }

        # comecamos com id(atual) = id)pai = ROOT
        id = ROOT
        id_pai = ROOT

        estado_inicial = "A B F L|"
        estado_final = "|A B F L"

        # vetor com as restricoes do problema
        restricoes = ["A,B", "L,B"]  # Vetor de restrições

        # vetor com os pesos referentes ao transporte de cada personagem
        pesos = {'F': 1, 'A': 2, 'B': 3, 'L': 4}

        # vetor de personagens
        personagens = ['F', 'A', 'B', 'L']

        # capacidade do barco
        num_ocupantes_barco = 2

        geraGrafo(id, id_pai, estado_inicial, estado_final, restricoes, pesos, personagens, num_ocupantes_barco,
                  dicionario_heuristica, 1)

    def prob_2():
        root.destroy()

        ROOT = 0

        # Cachorro Fazendeiro Gato Queijo Rato:
        dicionario_heuristica = {
            'C F G Q R|': 17,  # 0
            'G Q|C F R': 8,  # 1
            'C R|F G Q': 10,  # 2
            'C Q|F G R': 17,  # 3
            'F G Q|C R': 7,  # 4
            'C F G Q|R': 18,  # 5, 10
            'F G Q R|C': 12,  # 6
            'C F R|G Q': 9,  # 7
            'C F G R|Q': 19,  # 8
            'C F Q R|G': 19,  # 9, 11
            'Q|C F G R': 12,  # 12, 15, 19, 28, 30, 34
            'G|C F Q R': 10,  # 13, 16, 20, 25, 31
            '|C F G Q R': 0,  # 14, 23
            'C|F G Q R': 13,  # 17, 22, 26, 29, 32, 35
            'R|C F G Q': 13,  # 18, 21, 24, 27, 33
            'F G R|C Q': 8  # 36, 37, 38, 39, 40, 41, 42, 43....
        }

        # comecamos com id(atual) = id)pai = ROOT
        id = ROOT

        id_pai = ROOT

        estado_inicial = "C F G Q R|"
        estado_final = "|C F G Q R"

        # vetor com as restricoes do problema
        restricoes = ["C,G", "G,R", "R,Q"]  # Vetor de restrições

        # vetor com os pesos referentes ao transporte de cada personagem
        pesos = {'F': 1, 'Q': 2, 'R': 3, 'G': 4, 'C': 5}

        # vetor de personagens
        personagens = ['F', 'C', 'G', 'R', 'Q']

        # capacidade do barco
        num_ocupantes_barco = 3

        geraGrafo(id, id_pai, estado_inicial, estado_final, restricoes, pesos, personagens, num_ocupantes_barco,
                  dicionario_heuristica, 2)

    # criando objeto arvore
    arvore = Tree()

    # adicionando no raiz
    arvore.addNode(estado_inicial, 0)

    # Gerando os conjuntos de restricoes
    global restr_sep
    restr_sep = [x.split(',') for x in restricoes]

    def valida_margem(margem):

        # Se o fazendeiro está na margem, nao tem problema
        if not ('F' in margem):
            combinacoes = list(itertools.combinations(margem, 2))

            for i in combinacoes:  # passando por todas as combinacoes, 2 a 2, dos elementos da margem
                for j in restr_sep:  # passando pelas restricoes
                    if (set(i) == set(
                            j)):  # comparando se as combinacoes batem com alguma das restricoes -> movimento invalido

                        return False
        return True

    # verifica se um no ja existe
    def ja_existe(msg, id_pai_atual):

        # separa a msg no |(que se refere ao rio). Assim, ficamos com os vetores referentes as margens esquerda e direita
        msg_arr = msg.split('|')
        msg_arr_esq = msg_arr[0].split()  # elementos presentes na margem esquerda
        msg_arr_dir = msg_arr[1].split()  # elementos presentes na margem direita

        # iterando sobre os nos presentes na arvore para verificar se existe um no que tenha como dado o mesmo valor presente em msg
        for i in arvore.getAllNodes():
            dado_no = i.getData().split('|')  # divide a mensagem em margem direita e esquerda por meio do sinal |
            dado_no_esq = dado_no[0].split()  # elementos referentes a margem esquerda
            dado_no_dir = dado_no[1].split()  # elementos referentes a margem esquerda
            if ((sorted(dado_no_esq) == sorted(msg_arr_esq)) or (sorted(dado_no_dir) == sorted(
                    msg_arr_dir))):  # trabalha com os elementos ordenados JA que, para o problema, A B seja igual a B A
                if (i.getId() <= ((id_pai_atual) - 1)) or (
                        i.getId() == 0):  # testa se o id do no igual é o inicial ou se esta pelo menos 1 valor atras do atual
                    return True

        return False  # o no ainda nao existe, ou sua criacao nao resulta em um loop

    def calcula_custo(estado_pai, estado_filho):
        custo = 0
        quem_viajou = []
        margens_pai = estado_pai.split('|')
        margem_dir_pai = margens_pai[0].split()
        margem_esq_pai = margens_pai[1].split()
        margens_filho = estado_filho.split('|')
        margem_dir_filho = margens_filho[0].split()
        margem_esq_filho = margens_filho[1].split()
        if ('F' in margem_dir_pai):
            quem_viajou = list(set(margem_dir_pai) - set(margem_dir_pai).intersection(set(margem_dir_filho)))
        else:
            quem_viajou = list(set(margem_esq_pai) - set(margem_esq_pai).intersection(set(margem_esq_filho)))

        for ator in personagens:
            custo = custo + (ator in quem_viajou) * pesos[ator]

        return custo

    arestas = []

    custos_arestas = dict()
    custo_transicao = 0
    # enquanto o id do no atual nao ultrapassar o numero de nos da arvore(caso em que a geracao da arvore deve encerrar, pois o ultimo no foi atingido e nao gerou nenhum filho)
    while (id_pai < len(arvore.getAllNodes())):
        num_gerados = 0  # ainda nao gerou nenhum filho

        # recupera o no atual
        no = arvore.getNode(id_pai)
        # recupera a informacao presente no nó, referente à modelagem das margens esquerda e direita
        margens = no.getData().split('|')
        margem_esq = margens[0].split()
        margem_dir = margens[1].split()

        # se o fazendeiro esta na margem esquerda, o barco saira dela
        if ('F' in margem_esq):

            for k in range(num_ocupantes_barco):
                # gera as combinacoes, 1 a 1 e 2 a 2, dos elementos da margem esquerda para que ocupem o barco, nao excedendo sua capacidade
                combinacoes = list(itertools.combinations(margem_esq, k + 1))

                for barco in combinacoes:
                    # se o fazendeiro esta no barco, a configuracao do barco eh valida, ja que soh o fazendeiro pode guia-lo
                    if ('F' in barco):
                        # a margem esquerda apos a saida dos ocupantes do barco
                        margem_esq_resultante = list(set(margem_esq) - set(barco))

                        # testa se a configuracao da margem, caso os ocupantes do barco zarpem, continua valida segundo as restricoes do problema
                        if (valida_margem(margem_esq_resultante)):

                            # constroi a mensagem referente ao estado do no, na forma: margem_esquerda|margem_direita
                            if (len(margem_esq_resultante)):
                                margem_esq_resultante = sorted(margem_esq_resultante)
                                msg = margem_esq_resultante[0]

                                for i in range(1, len(margem_esq_resultante)):
                                    msg = msg + ' ' + margem_esq_resultante[i]
                            else:
                                msg = ''

                            msg = msg + '|'
                            margem_dir_resultante = list(set(margem_dir).union(
                                set(barco)))  # a margem direita apos a chegada dos ocupantes do barco

                            if (len(margem_dir_resultante)):
                                margem_dir_resultante = sorted(margem_dir_resultante)
                                msg = msg + margem_dir_resultante[0]

                                for i in range(1, len(margem_dir_resultante)):
                                    msg = msg + ' ' + margem_dir_resultante[i]
                            else:
                                msg = msg + ''

                            if (not ja_existe(msg, id_pai)):  # se o no ainda nao existe
                                id = id + 1
                                aresta = (arvore.getNode(id_pai).getData(), msg)
                                arestas.append(aresta)

                                custo_transicao = calcula_custo(arvore.getNode(id_pai).getData(), msg)
                                custos_arestas[aresta] = custo_transicao

                                arvore.addNode(msg, id, custo_transicao, id_pai)  # cria um novo no

        else:
            # se o fazendeiro esta na margem esquerda, o barco saira dela
            if ('F' in margem_dir):

                for k in range(num_ocupantes_barco):
                    # gera as combinacoes, 1 a 1 e 2 a 2, dos elementos da margem esquerda para que ocupem o barco, nao excedendo sua capacidade
                    combinacoes = list(itertools.combinations(margem_dir, k + 1))

                    for barco in combinacoes:
                        # se o fazendeiro esta no barco, a configuracao do barco eh valida, ja que soh o fazendeiro pode guia-lo
                        if ('F' in barco):
                            # a margem direita apos a saida dos ocupantes do barco
                            margem_dir_resultante = list(set(margem_dir) - set(barco))
                            # testa se a configuracao da margem, caso os ocupantes do barco zarpem, continua valida segundo as restricoes do problema
                            if (valida_margem(margem_dir_resultante)):
                                # a margem esquerda apos a chegada dos ocupantes do barco
                                margem_esq_resultante = list(set(margem_esq).union(set(barco)))

                                # constroi a mensagem referente ao estado do no, na forma: margem_esquerda|margem_direita
                                if (len(margem_esq_resultante)):
                                    margem_esq_resultante = sorted(margem_esq_resultante)
                                    msg = margem_esq_resultante[0]

                                    for i in range(1, len(margem_esq_resultante)):
                                        msg = msg + ' ' + margem_esq_resultante[i]
                                else:
                                    msg = ''

                                msg = msg + '|'

                                if (len(margem_dir_resultante)):
                                    margem_dir_resultante = sorted(margem_dir_resultante)
                                    msg = msg + margem_dir_resultante[0]

                                    for i in range(1, len(margem_dir_resultante)):
                                        msg = msg + ' ' + margem_dir_resultante[i]
                                else:
                                    msg = msg + ''

                                if (not ja_existe(msg, id_pai)):  # se o no ainda nao existe
                                    id = id + 1

                                    aresta = (arvore.getNode(id_pai).getData(), msg)
                                    arestas.append(aresta)

                                    custo_transicao = calcula_custo(arvore.getNode(id_pai).getData(), msg)
                                    custos_arestas[aresta] = custo_transicao

                                    arvore.addNode(msg, id, custo_transicao, id_pai)  # cria um novo no

        # vai para o proximo no
        id_pai = id_pai + 1

    def converteDicToList(dicionario):
        num_nos = len(arvore.getAllNodes())
        lista = np.zeros(num_nos)
        for no in arvore.getAllNodes():
            for chave in dicionario:
                if chave == no.getData():
                    lista[no.getId()] = dicionario[chave]
                    break
        return lista

    for i in arvore.getAllNodes():
        print(i.getData())

    # exibe o grafo gerado
    '''f = open("grafo.txt","w+")
    print("\n\nPrintando grafo")
    for i in arvore.getAllNodes():
        f.write("-----\n")
        print("-----")
        f.write("[" + str(i.getId()) + "]\n")
        print("[", i.getId(),"]")
        if(not i.getParent() is None):
            f.write("Meu papai eh: " + str(i.getParent()) + "\n")
            print("Meu papai eh: " + str(i.getParent()))
        else:
            f.write("Nao tenho papai :(\n")
            print("Nao tenho papai :(")
        f.write("Minha informacao eh: " + str(i.getData()) + "\n")
        print("Minha informacao eh: ", i.getData())
        f.write("Meus filhinhos sao: " + str(i.getChildren()) + "\n")
        print("Meus filhinhos sao: ", i.getChildren())
        f.write("Os peso pra ir nos meus filhinhos são: " + str(i.getPesosParaOsFilhos()) + "\n\n")
        print("Os peso pra ir nos meus filhinhos são: ", i.getPesosParaOsFilhos())

    f.close()'''

    caminho_busca_largura = arvore.buscaLargura(arvore)

    vet_dist_estado_final = converteDicToList(dicionario_heuristica)

    caminho_busca_a_estrela = arvore.busca_A_estrela(arvore, vet_dist_estado_final)

    # Parte de exibição **********************************************

    nos = [v.getData() for v in arvore.getAllNodes()]

    exibeGrafo(nos, arestas, custos_arestas, personagens, estado_inicial, estado_final, caminho_busca_largura)

    # exibir em janela
    root = Tk()

    root.geometry("1000x620+0+0")
    if(problema == 1):
        root.title("IA - Travessia do rio: Fazendeiro, Lobo, Bode e Alface")
    else:
        if (problema == 2):
            root.title("IA - Travessia do rio: Fazendeiro, Cachorro, Gato, Rato e Queijo")

    # Frame superior ********************************
    FImgs = Frame(root, width=700, height=500, bd=1, relief=SUNKEN)
    FImgs.grid(row=0, padx=10, pady=15)

    imgEntrada = PhotoImage(file="grafo.png")
    labelImgEntrada = Label(FImgs, image=imgEntrada)
    labelImgEntrada.pack(side=LEFT, padx=15, pady=15)

    FLegenda = Frame(root, width=700, height=60, bd=1, relief=SUNKEN)
    FLegenda.grid(row=1)

    canvas = Canvas(FLegenda, width=50, height=50)
    canvas.pack(side=LEFT)

    greenCircle = canvas.create_oval(10, 10, 40, 40, fill="green")

    Label(FLegenda, text="Caminho resultante").pack(side=LEFT)

    canvas = Canvas(FLegenda, width=50, height=50)
    canvas.pack(side=LEFT, padx=10)

    purpleCircle = canvas.create_oval(10, 10, 40, 40, fill="purple")

    Label(FLegenda, text="Estado inicial").pack(side=LEFT)

    canvas = Canvas(FLegenda, width=50, height=50)
    canvas.pack(side=LEFT, padx=10)

    yellowCircle = canvas.create_oval(10, 10, 40, 40, fill="yellow")

    Label(FLegenda, text="Estado final").pack(side=LEFT)

    canvas = Canvas(FLegenda, width=50, height=50)
    canvas.pack(side=LEFT, padx=10)

    blueCircle = canvas.create_oval(10, 10, 40, 40, fill="blue")

    Label(FLegenda, text="Estado do grafo").pack(side=LEFT)

    FResultadoBuscaLargura = Frame(root, width=300, height=500, bd=1, relief=SUNKEN)
    FResultadoBuscaLargura.grid(row=0, column=1)

    Label(FResultadoBuscaLargura, text='Resultado Busca em Largura', justify=CENTER).grid(row=0, pady=10, sticky=W)

    i = 1
    for estado in caminho_busca_largura:
        Label(FResultadoBuscaLargura, text=estado, justify=CENTER).grid(row=i, pady=10)
        i += 1

    FResultadoBuscaAEstrela = Frame(root, width=300, height=500, bd=1, relief=SUNKEN)
    FResultadoBuscaAEstrela.grid(row=0, column=2, padx=15)

    Label(FResultadoBuscaAEstrela, text='Resultado Busca A*', justify=CENTER).grid(row=0, pady=10, sticky=W)

    if(problema == 1):
        botao = Button(root, text="Ir para o problema 2", command=prob_2, width=25, height=3)
        botao.grid(row=1, column=1, columnspan=2)
    else:
        if (problema == 2):
            botao = Button(root, text="Ir para o problema 1", command=prob_1, width=25, height=3)
            botao.grid(row=1, column=1, columnspan=2)

    i = 1
    for no in caminho_busca_a_estrela:
        Label(FResultadoBuscaAEstrela, text=no.getData(), justify=CENTER).grid(row=i, pady=10)
        i += 1

    root.mainloop()