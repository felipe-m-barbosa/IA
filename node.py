# Classe para o no da Arvore.

class Node:
    # Construtor
    def __init__(self, data, id, parent=None):
        self.id = id            # Identificador do no
        self.data = data        # Informacao que esta no no.
        self.children = []      # Vetor com os filhos do no.
        self.parent = parent
        self.pesos_para_filhos = []  # Vetor com os pesos para os filhos i.

    def getId(self):
        return self.id          # Retorna o id do no

    def getData(self):          # Retorna os dados do no.
        return self.data

    def getParent(self):
        return self.parent      # Retorna o pai

    def getChildren(self):      # Retorna os filhos do no.
        return self.children

    def addChild(self, data, peso_filho=None):   # Adiciona um filho ao vetor de no.
        self.children.append(data)
        self.pesos_para_filhos.append(peso_filho)
        return

    def getPesosParaOsFilhos(self):
        return self.pesos_para_filhos