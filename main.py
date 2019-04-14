from node import Node
from tree import Tree
import itertools

#Criando no
no = Node("L B A F|", 1)

#vetor com as restricoes do problema
restricoes = ["L,B", "B,A"] #Nao pode Lobo com Bode(L,B) e nem Bode com Alface(B,A)

#numero de ocupantes do barco
num_ocupantes_barco = 2

#O sinal de | separa as margens do rio. Entao o vetor margens contem a configuracao das margens esquerda(margens[0]) e direita(margens[1])
margens = no.getData().split('|') #Dá algo da forma [[F L B],[A]], ou seja, tem os valores das margens direita e esquerda

print("Restricoes")
#Gerando os conjuntos de restricoes
global restr_sep
restr_sep = [x.split(',') for x in restricoes]
print(restr_sep)
print("\n\n")

def testa_margem_valida(margem):
    #Se o fazendeiro está na margem, nao tem problema
    if not ('F' in margem.split()):
        combinacoes = itertools.combinations(margem.split(), 2)
        for i in combinacoes:   #passando por todas as combinacoes, 2 a 2, dos elementos da margem
            for j in restr_sep: #passando pelas restricoes
                print(set(i) == set(j))
                print(set(i), " == ", set(j))

                if (set(i) == set(j)): #comparando se as combinacoes batem com alguma das restricoes -> movimento invalido
                    return False

#Testa se a configuracao da margem eh valida
    #Para a margem esquerda        e     Para a margem direita
#if(testa_margem_valida(margens[0]) and testa_margem_valida(margens[1])):
    #pode ir para o no

arvore = Tree()
arvore.addNode("L B A F|", 0)
arvore.addNode("L A|F B", 1)

raiz = arvore.nodes

print(raiz)

print(arvore.getNode(0).getData())

arvore.display(0)