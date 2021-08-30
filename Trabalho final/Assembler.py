from leitorEscritor import leitorEscritor
import networkx as nx


def Assembler(k, d, seq):
    grafo = []  
    for string in seq:
        prefixo = string[0:k-1] + string[k] + string[k+1:2*k]
        suffixo = string[1:k] + string[k] + string[k+2:]
        ligacao = (prefixo, suffixo)
        #print(ligacao)
        grafo.append(ligacao)

    l = len(grafo)
    digrafo = nx.DiGraph(grafo)

    nodes = list(digrafo.nodes())
    for node in nodes:
        if digrafo.in_degree(node) < digrafo.out_degree(node):
           caminho = list(nx.dfs_edges(digrafo, node))
           break
    montado = caminho[0][0][:k-1]
    for i in range (0, len(caminho)):
        montado += caminho[i][1][k-2]
    for j in range(l-k-d, len(caminho)):
        montado += caminho[j][1][-1]
    #print(montado)

    return montado

endereco_ler = str(input('Especifique o caminho do arquivo txt: '))

lei = leitorEscritor()
k, d, kdmers = lei.ler_e_tratar2(endereco_ler)

resul = Assembler(k, d, kdmers)

endereco_salvar = str(input('Especifique o caminho para salvar o resultado: '))
lei.escrever2(endereco_salvar, resul)

# C:\Arquivo 20.TXT
# C:\Users\Reynaldo\Desktop\
