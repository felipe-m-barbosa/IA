# Classe para o no da Arvore.

class Node:
    # Construtor
    def __init__(self, data, id):
        self.id = id            # Identificador do no
        self.data = data        # Informacao que esta no no.
        self.children = []      # Vetor com os filhos do no.

    def id(self):
        return self.id          #Retorna o id do no

    def getData(self):          # Retorna os dados do no.
        return self.data

    def getChildren(self):      # Retorna os filhos do no.
        return self.children

    def addChild(self, data):   # Adiciona um filho ao vetor de no.
        self.children.append(data)
