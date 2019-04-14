from node import Node

ROOT = 0
class Tree:

    def __init__(self):
        self.nodes = {} #obj com os nos


    def nodes(self):
        return self.nodes


    def addNode(self, data, id, parent=None):
        node = Node(data, id)
        self.nodes[id] = node

        if(parent is not None):
            self.nodes[parent].addChild(id)


    '''def display(self, id, depth=ROOT): #por default, depth=ROOT, caso seu valor nao seja informado na chamada da funcao
        children = self.nodes[id].children
        if depth == ROOT:
            print("{0}".format(id))
        else:
            print("\t" * depth, "{0}".format(id))

        depth += 1
        for child in children:
            self.display(child, depth)  # recursive call'''


    def getNode(self, key):
        return self.nodes[key]