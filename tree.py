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
        fila.append(arvore.getNode(0))                                  # Primeiro coloca a raiz na fila.
        while len(fila):
            noAtual = fila.pop(0)
            for i in range(0, len(noAtual.getChildren())):
                antecessor[noAtual.getChildren()[i]] = noAtual.id      # Colo o id do filho na posicao referente ao no pai.
                fila.append(arvore.getNode(noAtual.getChildren()[i]))  # Coloco o no do filho na fila.
            if noAtual.getData().split('|')[0] == '':                  # Se for um estado final, cheguei na solucao mais curta.
                id_estado_final = noAtual.id
                break
        caminho = [id_estado_final]                                     # O caminho comeca a partir do estado final
        while antecessor[id_estado_final] is not -1:                    # Enquanto o pai nao for -1
            caminho.append(antecessor[id_estado_final])                 # Insiro o pai no caminho
            id_estado_final = antecessor[id_estado_final]               # Atualizo a variavel, agora ela passa a ser o pai.
        for i in range(0, len(caminho)):                                # For para mudar os ids para os dados dentro do no.
            id_aux = caminho[i]
            caminho[i] = arvore.getNode(id_aux).getData()
        caminho.reverse()                                               # Reverse para apresentar o caminho da raiz ate o estado final.
        return caminho




