from tree import Tree
import itertools
import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from tkinter import *
from PIL import Image, ImageTk
import time

ROOT = 0
#comecamos com id(atual) = id)pai = ROOT
id = ROOT
id_pai = ROOT

#criando objeto arvore
arvore = Tree()

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

arvore.addNode("A B F L|", 0)

#vetor com as restricoes do problema
restricoes = ["L,B", "B,A"] #Vetor de restrições
pesos = {'F' : 1, 'A' : 2, 'B' : 3, 'L' : 4}
global personagens
personagens = ['F', 'L', 'B', 'A']
num_ocupantes_barco = 2

#inserindo o no raiz
'''arvore.addNode("F R G S L A|", 0)

#vetor com as restricoes do problema
restricoes = ["R,G", "G,S", "S,L", "L,A"] #Vetor de restrições
pesos = {'F' : 1, 'A' : 2, 'L' : 3, 'S' : 4, 'G' : 5, 'R' : 6}
global personagens
personagens = ['F', 'A', 'L', 'S', 'G', 'R']

#numero de ocupantes do barco
num_ocupantes_barco = 3'''

#Gerando os conjuntos de restricoes
global restr_sep
restr_sep = [x.split(',') for x in restricoes]

def valida_margem(margem):

    #Se o fazendeiro está na margem, nao tem problema
    if not ('F' in margem):
        combinacoes = list(itertools.combinations(margem, 2))

        for i in combinacoes:   #passando por todas as combinacoes, 2 a 2, dos elementos da margem
            for j in restr_sep: #passando pelas restricoes
                '''print(set(i) == set(j))
                print(set(i), " == ", set(j))'''

                if (set(i) == set(j)): #comparando se as combinacoes batem com alguma das restricoes -> movimento invalido

                    return False

    return True


#verifica se um no ja existe
def ja_existe(msg, id_pai_atual):

    #separa a msg no |(que se refere ao rio). Assim, ficamos com os vetores referentes as margens esquerda e direita
    msg_arr = msg.split('|')
    msg_arr_esq = msg_arr[0].split() #elementos presentes na margem esquerda
    msg_arr_dir = msg_arr[1].split() #elementos presentes na margem direita

    #iterando sobre os nos presentes na arvore para verificar se existe um no que tenha como dado o mesmo valor presente em msg
    for i in arvore.getAllNodes():
        dado_no = i.getData().split('|') #divide a mensagem em margem direita e esquerda por meio do sinal |
        dado_no_esq = dado_no[0].split() #elementos referentes a margem esquerda
        dado_no_dir = dado_no[1].split() #elementos referentes a margem esquerda
        if((sorted(dado_no_esq) == sorted(msg_arr_esq)) or (sorted(dado_no_dir) == sorted(msg_arr_dir))): #trabalha com os elementos ordenados JA que, para o problema, A B seja igual a B A
            if(i.getId() <= ((id_pai_atual)-1)) or (i.getId() == 0): #testa se o id do no igual é o inicial ou se esta pelo menos 1 valor atras do atual
                return True

    return False #o no ainda nao existe, ou sua criacao nao resulta em um loop

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

    # print('\n', quem_viajou)
    for ator in personagens:
        custo = custo + (ator in quem_viajou) * pesos[ator]

    return custo


arestas = []

custos_arestas = dict()
custo_transicao = 0
#enquanto o id do no atual nao ultrapassar o numero de nos da arvore(caso em que a geracao da arvore deve encerrar, pois o ultimo no foi atingido e nao gerou nenhum filho)
while(id_pai < len(arvore.getAllNodes())):
    num_gerados = 0 #ainda nao gerou nenhum filho

    #recupera o no atual
    no = arvore.getNode(id_pai)
    #recupera a informacao presente no nó, referente à modelagem das margens esquerda e direita
    margens = no.getData().split('|')
    margem_esq = margens[0].split()
    margem_dir = margens[1].split()

    #se o fazendeiro esta na margem esquerda, o barco saira dela
    if('F' in margem_esq):

        for k in range(num_ocupantes_barco):
            #gera as combinacoes, 1 a 1 e 2 a 2, dos elementos da margem esquerda para que ocupem o barco, nao excedendo sua capacidade
            combinacoes = list(itertools.combinations(margem_esq, k+1))

            for barco in combinacoes:
                #se o fazendeiro esta no barco, a configuracao do barco eh valida, ja que soh o fazendeiro pode guia-lo
                if ('F' in barco):
                    #a margem esquerda apos a saida dos ocupantes do barco
                    margem_esq_resultante = list(set(margem_esq)-set(barco))

                    #testa se a configuracao da margem, caso os ocupantes do barco zarpem, continua valida segundo as restricoes do problema
                    if(valida_margem(margem_esq_resultante)):

                        #constroi a mensagem referente ao estado do no, na forma: margem_esquerda|margem_direita
                        if(len(margem_esq_resultante)):
                            margem_esq_resultante = sorted(margem_esq_resultante)
                            msg = margem_esq_resultante[0]

                            for i in range(1,len(margem_esq_resultante)):
                                msg = msg + ' ' + margem_esq_resultante[i]
                        else:
                            msg = ''

                        msg = msg + '|'
                        margem_dir_resultante = list(set(margem_dir).union(set(barco))) #a margem direita apos a chegada dos ocupantes do barco

                        if(len(margem_dir_resultante)):
                            margem_dir_resultante = sorted(margem_dir_resultante)
                            msg = msg + margem_dir_resultante[0]

                            for i in range(1,len(margem_dir_resultante)):
                                msg = msg + ' ' + margem_dir_resultante[i]
                        else:
                            msg = msg + ''

                        if (not ja_existe(msg, id_pai)): #se o no ainda nao existe
                            id = id + 1
                            aresta = (arvore.getNode(id_pai).getData(), msg)
                            arestas.append(aresta)

                            custo_transicao = calcula_custo(arvore.getNode(id_pai).getData(), msg)
                            custos_arestas[aresta] = custo_transicao

                            arvore.addNode(msg, id, custo_transicao, id_pai) #cria um novo no

    else:
        # se o fazendeiro esta na margem esquerda, o barco saira dela
        if ('F' in margem_dir):

            for k in range(num_ocupantes_barco):
                # gera as combinacoes, 1 a 1 e 2 a 2, dos elementos da margem esquerda para que ocupem o barco, nao excedendo sua capacidade
                combinacoes = list(itertools.combinations(margem_dir, k+1))

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

                            if(not ja_existe(msg, id_pai)): #se o no ainda nao existe
                                id = id + 1

                                aresta = (arvore.getNode(id_pai).getData(), msg)
                                arestas.append(aresta)

                                custo_transicao = calcula_custo(arvore.getNode(id_pai).getData(), msg)
                                custos_arestas[aresta] = custo_transicao

                                arvore.addNode(msg, id, custo_transicao, id_pai) #cria um novo no

    #vai para o proximo no
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


vet_dist_estado_final = converteDicToList(dicionario_heuristica)
print("Teste de conversão: ")
print(vet_dist_estado_final)


for i in arvore.getAllNodes():
    print(i.getData())

#exibe o grafo gerado
print("\n\nPrintando grafo")
for i in arvore.getAllNodes():
    print("-----")
    print("[", i.getId(),"]")
    if(not i.getParent() is None):
        print("Meu papai eh: ", i.getParent())
    else:
        print("Nao tenho papai :(")
    print("Minha informacao eh: ", i.getData())
    print("Meus filhinhos sao: ", i.getChildren())
    print("Os peso pra ir nos meus filhinhos são: ", i.getPesosParaOsFilhos())


'''print('Custos : ', custos)
custos_arestas = {x:y for x in arestas for y in custos}
'''
#print(custos_arestas)

caminho_busca_largura = arvore.buscaLargura(arvore)
print("\n\nResultado da busca em largura: ", caminho_busca_largura)

caminho_busca_a_estrela = arvore.busca_A_estrela(arvore, vet_dist_estado_final)
print("\n\nResultado da busca A*: ")
for aux in caminho_busca_a_estrela:
    print("-> ", aux.getData())

#Parte de exibição **********************************************

nos = [v.getData() for v in arvore.getAllNodes()]
#labels = [i for i in range(len(arvore.getAllNodes()))]

g = nx.Graph()
g.add_nodes_from(nos)
g.add_edges_from(arestas)

permutacoes_personagens = list(itertools.permutations(personagens, len(personagens)))
nos_finais = []
prim = True
for i in permutacoes_personagens:
    msg = '|'
    for aux in i:
        if(prim):
            msg = msg + aux
            prim = False
        else:
            msg = msg + ' ' + aux
    prim = True
    nos_finais.append(msg)
'''string_finais = ['|'.join(nos_finais)]
print(string_finais)'''

#print('Nós finais: ', nos_finais)
#print('Caminho: ', caminho_busca_largura)
caminho_sem_no_final_e_sem_no_inicial = list(set(caminho_busca_largura)-set(caminho_busca_largura).intersection(set(nos_finais))-set('A B F L|')) #caminho sem o no final
#print('Caminho sem no final: ', caminho_sem_no_final)

#pinta de verde o caminho encontrado pela busca em largura, de vermelho o no final e de azul os demais nos
node_colors = ['purple' if n == 'A B F L|' else 'yellow' if n in nos_finais else 'green' if n in caminho_sem_no_final_e_sem_no_inicial else 'blue' for n in g.nodes()]

#legenda
'''green_patch = mpatches.Patch(color='green', label='Menor caminho')
blue_patch = mpatches.Patch(color='blue', label='Nos nao visitados')
plt.legend(handles=[green_patch,blue_patch])'''

#pos = nx.kamada_kawai_layout(g)
pos = nx.spring_layout(g)
nx.draw(g, pos=pos, with_labels=True, node_size=700, node_color=node_colors)
nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=custos_arestas)

plt.savefig('grafo1.png')
plt.show()


#exibir em janela - ta dando pau por enquanto
'''root = Tk()

root.geometry("1350x620+0+0")

root.title("IA - Travessia do rio")

#Frame superior ********************************
FImgs = Frame(root, width=900, height=500, bd=1, relief=SUNKEN)
FImgs.grid(row=0, padx=10, pady=20)


imgEntrada = PhotoImage(file="grafo1.png")
labelImgEntrada = Label(FImgs, image=imgEntrada)
labelImgEntrada.pack(side=LEFT, padx=15, pady=15)

root.mainloop()'''

# Teste para printar o menor caminho utilizando busca em largura.
'''caminho = arvore.buscaLargura(arvore)
print("\nCaminho mais curto: ")
print(' -> '.join(caminho))'''