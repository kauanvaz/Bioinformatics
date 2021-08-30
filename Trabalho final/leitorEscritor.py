class leitorEscritor:

    def ler_e_tratar1(self, endereco):
        x = open(endereco, 'r')
        a = x.read()
        x.close()
        k = ''
        d = ''
        string = ''

        for i in range(0, len(a)):
            if a[i] == 'd':
                k = int(a[:i].replace('>k=', ''))
                d = a[i+2:]
                for j in range (0, len(d)):
                    if d[j] == '\n':
                        d = int(d[:j])
                        break
        for i in range(0, len(a)):
            if a[i] == '\n':
                string = a[i+1:].replace('\n', '')
                break

        return k, d, string  

    def escrever1(self, path, resultado, k, d):
        k = str(k)
        d = str(d)
        titulo = 'k'+k+'d'+d+'mer.txt'
        arquivo = open(path + titulo, 'w')

        arquivo.write('>k='+k+'d='+d+'\n')

        arquivo.write('[')
        tamanho = len(resultado)
        for i in range(0, tamanho):
            dado = resultado[i]
            if i != tamanho-1:
                arquivo.write(dado+', ')
            else:
                arquivo.write(dado+']')

        arquivo.close
        print('Arquivo salvo ('+titulo+')')

    def ler_e_tratar2(self, endereco):
        x = open(endereco, 'r')
        a = x.read()
        x.close()
        k = ''
        d = ''
        string = ''

        for i in range(0, len(a)):
            if a[i] == 'd':
                k = int(a[:i].replace('>k=', ''))
                d = a[i+2:]
                for j in range (0, len(d)):
                    if d[j] == '\n':
                        d = int(d[:j])
                        break
        for i in range(0, len(a)):
            if a[i] == '\n':
                string = a[i+1:]
                break

        string = string.replace('[', '')
        string = string.replace(']', '')
        string = string.replace("'", '')
        listakdmers = string.split(', ')

        return k, d, listakdmers

    def escrever2(self, path, sequencia):
        titulo = 'SequenciaRemontada.fasta'
        arquivo = open(path + titulo, 'w')

        dado = sequencia

        arquivo.write(dado)
        arquivo.close
        print('Arquivo salvo ('+titulo+')')