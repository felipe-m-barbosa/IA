from node import Node

ROOT = 0
class Tree:

    def __init__(self):
        self.nodes = [] #obj com os nos

    def nodes(self):
        return self.nodes

    def addNode(self, data, id, parent=None):
        node = Node(data, id)
        self.nodes.append(node)

        if(parent is not None):
            self.nodes[parent].addChild(id)

    def getNode(self, id):
        return self.nodes[id]

    def buscaLargura(self, raiz):
        fila = []
        antecessor = []
        id_estado_final = -1
        for i in range(len(self.nodes)):
            antecessor[i] = -1
        fila.append(raiz)
        while len(fila):
            noAtual = fila.pop(0)
            for i in noAtual.getChildren:
                antecessor[noAtual.getChildren[i]] = noAtual.id
                fila.append(noAtual.getChildren[i])
            if noAtual.getData.split('|')[0]:       # Se for um estado final, cheguei na solucao mais curta.
                id_estado = noAtual.id
                break
        caminho = []
        contador = 0
        while antecessor[id_estado] is not -1:
            caminho[contador] = antecessor[id_estado]
            id_estado = antecessor[id_estado]
            contador += 1
        return caminho





