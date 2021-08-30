geneticCode = {
'UUU':'F', 'UUF':'F', 'UUA':'L', 'UUG':'L', 
'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L', 
'UAU':'T', 'UAC':'T', 'UAA':'ST', 'UAG':'ST', 
'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W', 
'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAU':'H', 'CAC':'H', 'CAA':'G', 'CAG':'G',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGU':'S', 'AGC':'S', 'AGA':'A', 'AGG':'A',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
}

rna = str(input('Digite a sequência da fita de RNAm: ')).strip().upper().replace('.', '')
tamanho = len(rna)
comeca = 0
termina = 0

print('Sequência de aminoácidos: ', end='\n')
for x in range(0, tamanho, 3):
    codon = rna[x] + rna[x+1] + rna[x+2]
    if(geneticCode[codon] == 'M'):
        comeca = 1
        continue
    elif(geneticCode[codon] == 'ST'):
        termina = 1
    elif(comeca == 1 and termina == 1):
        break
    elif(comeca == 1 and termina == 0):
        print(geneticCode[codon], end=' ')