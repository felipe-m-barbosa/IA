from node import Node
from tree import Tree
import itertools
import networkx as nx
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from tkinter import *
from PIL import Image, ImageTk
import time

ROOT = 0
#Criando no
no = Node("L B A F|", 0)

#vetor com as restricoes do problema
restricoes = ["L,B", "B,A"] #Nao pode Lobo com Bode(L,B) e nem Bode com Alface(B,A)

#numero de ocupantes do barco
num_ocupantes_barco = 2

#O sinal de | separa as margens do rio. Entao o vetor margens contem a configuracao das margens esquerda(margens[0]) e direita(margens[1])
margens = no.getData().split('|') #Dá algo da forma [[F L B],[A]], ou seja, tem os valores das margens direita e esquerda

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

#Testa se a configuracao da margem eh valida
    #Para a margem esquerda        e     Para a margem direita
#if(testa_margem_valida(margens[0]) and testa_margem_valida(margens[1])):
    #pode ir para o no

#comecamos com id(atual) = id)pai = ROOT
id = ROOT
id_pai = ROOT

#criando objeto arvore
arvore = Tree()
#inserindo o no raiz
arvore.addNode("L B A F|", 0)

'''arvore.addNode("L A|F B", 1)
arvore.addNode("L A F|B", 2)
arvore.addNode("L|F A B", 3)
arvore.addNode("L B F|A", 4)
arvore.addNode("B|F A L", 5)
arvore.addNode("F B|A L", 6)
arvore.addNode("|F B A L", 7)'''


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


#inicializa variavel para testar se houve bifurcacao no grafo
global gemeos
gemeos = False

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
                            msg = margem_esq_resultante[0]

                            for i in range(1,len(margem_esq_resultante)):
                                msg = msg + ' ' + margem_esq_resultante[i]
                        else:
                            msg = ''

                        msg = msg + '|'
                        margem_dir_resultante = list(set(margem_dir).union(set(barco))) #a margem direita apos a chegada dos ocupantes do barco

                        if(len(margem_dir_resultante)):
                            msg = msg + margem_dir_resultante[0]

                            for i in range(1,len(margem_dir_resultante)):
                                msg = msg + ' ' + margem_dir_resultante[i]
                        else:
                            msg = msg + ''

                        if (not ja_existe(msg, id_pai)): #se o no ainda nao existe
                            id = id + 1
                            arvore.addNode(msg, id, id_pai) #cria um novo no

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
                                msg = margem_esq_resultante[0]

                                for i in range(1, len(margem_esq_resultante)):
                                    msg = msg + ' ' + margem_esq_resultante[i]
                            else:
                                msg = ''

                            msg = msg + '|'

                            if (len(margem_dir_resultante)):
                                msg = msg + margem_dir_resultante[0]

                                for i in range(1, len(margem_dir_resultante)):
                                    msg = msg + ' ' + margem_dir_resultante[i]
                            else:
                                msg = msg + ''

                            if(not ja_existe(msg, id_pai)): #se o no ainda nao existe
                                id = id + 1
                                arvore.addNode(msg, id, id_pai) #cria um novo no


    #vai para o proximo no
    id_pai = id_pai + 1


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

#Exibindo grafo

arestas = []
for node in arvore.getAllNodes():
    for child in node.getChildren():
        arestas.append((node.getData(), arvore.getNode(child).getData()))

nos = [v.getData() for v in arvore.getAllNodes()]
#labels = [i for i in range(len(arvore.getAllNodes()))]

caminho_busca_largura = arvore.buscaLargura(arvore)

g = nx.Graph()
g.add_nodes_from(nos)
g.add_edges_from(arestas)
node_colors = ['green' if n in caminho_busca_largura else 'blue' for n in g.nodes()]

green_patch = mpatches.Patch(color='green', label='Menor caminho')
blue_patch = mpatches.Patch(color='blue', label='Nos nao visitados')
plt.legend(handles=[green_patch,blue_patch])

pos = nx.spring_layout(g)
nx.draw(g, with_labels=True, pos=pos, node_size=700, node_color=node_colors)

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