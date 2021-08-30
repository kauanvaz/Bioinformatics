dna = str(input('Digite a sequência de DNA: \n')).strip().upper()
tamanho = len(dna)
rna = ''

print('--'*70)
for x in range(0, tamanho):
    if(dna[x] == 'C'):
        rna += 'G'
    elif(dna[x]) == 'G':
        rna += 'C'
    elif(dna[x] == 'A'):
        rna += 'U'
    elif(dna[x] == 'T'):
        rna += 'A'

print('Fita de mRNA: ')
print(rna)        