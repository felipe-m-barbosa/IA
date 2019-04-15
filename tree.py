from node import Node

class Tree:

    def __init__(self):
        self.nodes = [] #vetor com os nos

    def nodes(self):
        return self.nodes

    def addNode(self, data, id, parent=None):
        node = Node(data, id, parent)
        self.nodes.append(node)

        if(parent is not None):
            self.nodes[parent].addChild(id)

    def getNode(self, id):
        return self.nodes[id]

    def buscaLargura(self, raiz):
        fila = []
        antecessor = []
        id_estado = -1
        for i in range(len(self.nodes)):
            antecessor.append(-1)
        #print("Vetor de antecessor: ", antecessor)
        fila.append(raiz)
        #print("Vetor fila: ", fila)
        while len(fila):
            noAtual = fila.pop(0)
            for i in range(0, len(noAtual.getChildren())):
                antecessor[noAtual.getChildren()[i]] = noAtual.id
                fila.append(noAtual.getChildren()[i])
            if noAtual.getData().split('|')[0]:      # Se for um estado final, cheguei na solucao mais curta.
                id_estado = noAtual.id
                break
        #print("Teste antecessor: ", antecessor)
        caminho = []
        contador = 0
        while antecessor[id_estado] is not -1:
            caminho[contador] = antecessor[id_estado]
            id_estado = antecessor[id_estado]
            contador += 1
        for data in range(0, len(caminho)):
            id_aux = caminho[data]
            caminho[data] = self.nodes[id_aux]
        #print("Teste caminho: ", caminho)
        return caminho.reverse()




