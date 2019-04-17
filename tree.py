from node import Node

class Tree:

    def __init__(self):
        self.nodes = [] #vetor com os nos

    def getAllNodes(self):
        return self.nodes

    def addNode(self, data, id, peso_filho=None, parent=None):
        node = Node(data, id, parent)
        self.nodes.append(node)

        if(parent is not None):
            self.nodes[parent].addChild(id, peso_filho)

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

    def busca_A_estrela(self, arvore, vet_dist_estado_final):

        # Vetor com os processos que estao aberto no momento, este vetor ira gerar o caminho no final.
        vet_processo_aberto = [] #eh um vetor de nos

        raiz = arvore.getNode(0)
        vet_processo_aberto.append(raiz)  # Insere a raiz no vetor como primeiro no em aberto.

        # Vetor que ira conter os processos em espera, ou seja, aqueles que nao foram selecionados.
        # Este vetor ira conter os valores da funcao de avaliacao (f = g + h), no qual g eh a distancia
        # ate o no raiz e h a distancia ate o estado final, dado pelo vet_dist_estado_final.
        # As posicoes do vetor remetem ao id do no da arvore, ou seja, na posicao 1 contem o valor da
        # funcao de avaliacao do no de id = 1 da arvore.
        vet_proc_espera = [-1 for i in range(len(arvore.getAllNodes()))]

        # Vetor com as distancias para o estado inicial. Cada posicao representa o id do no da arvore,
        # e a informacao desta posicao representa a distancia ate o no raiz.
        vet_dist_estado_inicial = [0 for i in range(len(arvore.getAllNodes()))]

        # Vetor com os nos que ja foram visitados pelo algoritmo, contendo True ou False para visitado ou nao.
        # Cada posicao do vetor remete a um id da arvore
        vet_nos_visitados = [False for i in range(len(arvore.getAllNodes()))]

        while True:
            # Primeira posicao do vetor sera o no atual que esta em aberto.
            no_atual = vet_processo_aberto[0]
            # Visitei o no_atual, entao este recebe True
            vet_nos_visitados[no_atual.getId()] = True

            # Se o no_atual for o estado final, entao cheguei no final.
            if no_atual.getData().split('|')[0] == '':
                break

            # Somo as distancias (pesos) para o estado inicial
            for i in range(len(no_atual.getChildren())):
                vet_dist_estado_inicial[no_atual.getChildren()[i]] += no_atual.getPesosParaOsFilhos()[i]

            # Agora iremos procurar a menor funcao de avaliacao (g + h) entre os filhos do no.
            # Comeco selecionando o primeiro filho como ideal
            id_filho_selecionado = no_atual.getChildren()[0]
            custo_avaliacao = vet_dist_estado_inicial[id_filho_selecionado] + vet_dist_estado_final[id_filho_selecionado]

            # Se existir mais filhos, comparo para ver qual que possui a menor funcao de avaliacao.
            if len(no_atual.getChildren()) > 1:
                for child in range(len(no_atual.getChildren()) - 1):
                    id_prox_filho = no_atual.getChildren()[child + 1]
                    custo_avaliacao_prox = vet_dist_estado_inicial[id_prox_filho] + vet_dist_estado_final[id_prox_filho]
                    if custo_avaliacao_prox < custo_avaliacao:
                        #coloca o filho atual em espera
                        vet_proc_espera[id_filho_selecionado] = custo_avaliacao
                        custo_avaliacao = custo_avaliacao_prox
                        id_filho_selecionado = id_prox_filho
                    # Se nao for selecionado, o no sera colocado em espera
                    else:
                        vet_proc_espera[id_prox_filho] = custo_avaliacao_prox

            # Precisamos verificar se este eh o no com o menor custo de avaliacao, que seja maior que -1 e que nao
            # tenha sido visitado ainda
            # Pega o primeiro valor que aparecer que nao seja -1
            menor_custo = 0
            for i in range(len(vet_proc_espera)):
                if vet_proc_espera[i] is not -1:
                    menor_custo = vet_proc_espera[i]
                    break

            # Agora comparo para ver se este eh de fato o menor valor e se ele nao foi visitado ainda
            for i in range(len(arvore.getAllNodes())):
                # Se o valor que eu estou lendo eh menor e ele ainda nao foi visitado
                if (menor_custo > vet_proc_espera[i]) and (vet_nos_visitados[i] is False):
                    menor_custo = vet_proc_espera[i]
                    id_filho_selecionado = i

            # Seleciono o no do id_filho_selecionado como proximo no em aberto e insere no comeco.
            vet_processo_aberto.insert(0, arvore.getNode(id_filho_selecionado))
        # end While True

        # Agora precisamos reconstruir o caminho para retornar a main.py
        caminho = []
        # O no de posicao 0 neste ponto sera o no de estado final, entao ja colocamos ele no caminho
        caminho.append(vet_processo_aberto[0])
        no_atual = vet_processo_aberto[0]
        while True:
            # Se este no nao tem um pai, entao ele eh o no raiz
            if no_atual.getParent() is None:
                break

            # Verifico se o pai esta presente como um processo que foi aberto
            id_pai_no_atual = no_atual.getParent()
            for father in range(len(vet_processo_aberto)):
                if vet_processo_aberto[father].getId() == id_pai_no_atual:
                    no_atual = vet_processo_aberto[father]
                    caminho.insert(0, no_atual)
                    break

        return caminho



