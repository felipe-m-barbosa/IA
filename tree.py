from node import Node

class Tree:

    def __init__(self):
        self.nodes = [] #vetor com os nos

    def getAllNodes(self):
        return self.nodes

    def addNode(self, data, id, parent=None):
        node = Node(data, id, parent)
        self.nodes.append(node)

        if(parent is not None):
            self.nodes[parent].addChild(id)

    def getNode(self, id):
        return self.nodes[id]

    def buscaLargura(self, arvore):
        fila = []
        antecessor = []
        id_estado_final = -1
        for i in range(len(arvore.getAllNodes())):
            antecessor.append(-1)
        fila.append(arvore.getNode(0))  # Primeiro coloca a raiz na fila.
        while len(fila):
            noAtual = fila.pop(0)
            for i in range(0, len(noAtual.getChildren())):
                antecessor[noAtual.getChildren()[i]] = noAtual.id  # Colo o id do filho na posicao referente ao no pai.
                fila.append(arvore.getNode(noAtual.getChildren()[i]))  # Coloco o no do filho na fila.
            if noAtual.getData().split('|')[0] == '':  # Se for um estado final, cheguei na solucao mais curta.
                id_estado_final = noAtual.id
                break
        caminho = [id_estado_final]  # O caminho comeca a partir do estado final
        while antecessor[id_estado_final] is not -1:  # Enquanto o pai nao for -1
            caminho.append(antecessor[id_estado_final])  # Insiro o pai no caminho
            id_estado_final = antecessor[id_estado_final]  # Atualizo a variavel, agora ela passa a ser o pai.
        for i in range(0, len(caminho)):  # For para mudar os ids para os dados dentro do no.
            id_aux = caminho[i]
            caminho[i] = arvore.getNode(id_aux).getData()
        caminho.reverse()  # Reverse para apresentar o caminho da raiz ate o estado final.
        return caminho

    '''def busca_A_estrela(self, arvore):

        raiz = arvore.getNode(0)  # Nó de início

        explorados = []  # Vetor com os nós já explorados
        em_aberto = []  # Vetor de processo em aberto
        caminho = []  # Vetor de caminho
        percorrido = []  # Vetor com a distância já percorrida

        for i in range(len(arvore.getAllNodes())):  # Inicializa as dists percorridas
            percorrido.append(-1)

        em_aberto.append(raiz)  # Põe a raiz como processo aberto
        percorrido[raiz.id] = 0  # Dist percorrida da raiz

        # Deepende da definição da heurística!!!
        # estimado = valor da heuristica de cada nó
        # for i in range(len(arvore.getAllNodes())):
        #    estimado.append(-1)
        # estimado[raiz.id] = valor heurística para a raiz

        while (len(em_aberto)):  # Enquanto houver processo em aberto
            atual = em_aberto[0]

            for i in range(len(em_aberto)):  # Pega o processo em aberto de menor valor
                if percorrido[em_aberto[i]] < estimado[atual.id]:
                    atual = em_aberto[i]

            if atual.getData().split('|')[0] == '':  # Se for um estado final, cheguei na solucao mais curta.
                return caminho

            em_aberto.pop()  # remove o no da lista de aberto
            explorados.append(atual)  # coloca como já explorado

            for i in range(0, len(atual.getChildren())):  # para todos os vizinhos do nó atual
                vizinho = atual.getChildren()[i]
                if (vizinho in explorados)  # se estiver no explorados, ignora
                    continue
                # custo = percorrido[atual.id] + valor heurística #calcula o custo atual

                if (vizinho not in em_aberto):  # se o vizinho não for processo aberto, coloca como aberto
                    em_aberto.append(vizinho)
                else if (custo >= percorrido[vizinho.id]):  # se o custo for maior que o valor percorrido do vizinho, ignora
                    continue

                caminho[vizinho.id] = atual  # coloca o nó atual no caminho do vizinho
                percorrido[vizinho.id] = custo  # distancia para chegar no vizinho é o custo calculado
                # estimado[vizinho.id] = percorrido[vizinho.id] + valor_heuristica #valor total estimado para chegar no vizinho'''

