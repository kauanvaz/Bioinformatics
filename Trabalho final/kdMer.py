from leitorEscritor import leitorEscritor

def kdmer(k, d, string):
    lista = []
    tamanho = len(string)
    prim_ped = '' #Primeira parte do kdmer
    seg_ped = '' #Segunda parte do kdmer
    i=0

    while (i+k+d)+k != tamanho+1:
        prim_ped = string[i:i+k]
        seg_ped = string[i+k+d:(i+k+d)+k]
        lista.append(prim_ped + '|' + seg_ped)
        i += 1
    #print(lista)
    lista.sort()
    return lista

endereco_ler = str(input('Especifique o caminho do arquivo fasta: '))

lei = leitorEscritor()
k, d, string = lei.ler_e_tratar1(endereco_ler)

resul = kdmer(k, d, string)
endereco_salvar = str(input('Especifique o caminho para salvar o resultado: '))
lei.escrever1(endereco_salvar, resul, k, d)
#print(resul)

# C:\A.txt
# C:\Users\Reynaldo\Desktop\