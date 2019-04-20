from tkinter import *
from principal import geraGrafo

def inicializa_prob_1():
    root.destroy()

    ROOT = 0

    # Fazendeiro, alface, bode, lobo:
    dicionario_heuristica = {
        'A B F L|': 22,
        'A L|B F': 18,
        'A F L|B': 17,
        'L|A B F': 14,
        'A|B F L': 12,
        'B F L|A': 10,
        'A B F|L': 8,
        'B|A F L': 5,
        'B F|A L': 4,
        '|A B F L': 0
    }

    # comecamos com id(atual) = id)pai = ROOT
    id = ROOT
    id_pai = ROOT

    estado_inicial = "A B F L|"
    estado_final = "|A B F L"

    # vetor com as restricoes do problema
    restricoes = ["A,B", "L,B"]  # Vetor de restrições

    # vetor com os pesos referentes ao transporte de cada personagem
    pesos = {'F': 1, 'A': 2, 'B': 3, 'L': 4}

    # vetor de personagens
    personagens = ['F', 'A', 'B', 'L']

    # capacidade do barco
    num_ocupantes_barco = 2

    geraGrafo(id, id_pai, estado_inicial, estado_final, restricoes, pesos, personagens, num_ocupantes_barco, dicionario_heuristica, 1)

def inicializa_prob_2():
    root.destroy()

    ROOT = 0

    # Cachorro Fazendeiro Gato Queijo Rato:
    dicionario_heuristica = {
        'C F G Q R|': 17,  # 0
        'G Q|C F R': 8,  # 1
        'C R|F G Q': 10,  # 2
        'C Q|F G R': 17,  # 3
        'F G Q|C R': 7,  # 4
        'C F G Q|R': 18,  # 5, 10
        'F G Q R|C': 12,  # 6
        'C F R|G Q': 9,  # 7
        'C F G R|Q': 19,  # 8
        'C F Q R|G': 19,  # 9, 11
        'Q|C F G R': 12,  # 12, 15, 19, 28, 30, 34
        'G|C F Q R': 10,  # 13, 16, 20, 25, 31
        '|C F G Q R': 0,  # 14, 23
        'C|F G Q R': 13,  # 17, 22, 26, 29, 32, 35
        'R|C F G Q': 13,  # 18, 21, 24, 27, 33
        'F G R|C Q': 8  # 36, 37, 38, 39, 40, 41, 42, 43....
    }

    # comecamos com id(atual) = id)pai = ROOT
    id = ROOT

    id_pai = ROOT

    estado_inicial = "C F G Q R|"
    estado_final = "|C F G Q R"

    # vetor com as restricoes do problema
    restricoes = ["C,G", "G,R", "R,Q"]  # Vetor de restrições

    # vetor com os pesos referentes ao transporte de cada personagem
    pesos = {'F': 1, 'Q': 2, 'R': 3, 'G': 4, 'C': 5}

    # vetor de personagens
    personagens = ['F', 'C', 'G', 'R', 'Q']

    # capacidade do barco
    num_ocupantes_barco = 3

    geraGrafo(id, id_pai, estado_inicial, estado_final, restricoes, pesos, personagens, num_ocupantes_barco, dicionario_heuristica, 2)


root = Tk()

canvas1 = Canvas(root, width=300, height=350, bg='gray90', relief='raised')
canvas1.pack()

label1 = Label(root, text='IA - Travessia do rio', bg='gray90')
label1.config(font=('helvetica', 14))
canvas1.create_window(150, 80, window=label1)

button1 = Button(text='Problema 1', command=inicializa_prob_1, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'), width=20)
canvas1.create_window(150, 180, window=button1)

button2 = Button(text='Problema 2', command=inicializa_prob_2, bg='coral3', fg='white',
                    font=('helvetica', 12, 'bold'), width=20)
canvas1.create_window(150, 230, window=button2)

root.mainloop()