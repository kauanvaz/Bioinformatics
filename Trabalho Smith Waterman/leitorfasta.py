class leitorfasta:

    def __init__(self, endereco):
        self.endereco = endereco

    def ler_e_tratar(self):
        x = open(self.endereco, 'r')
        a = x.read()
        x.close()
        b = ''

        for i in range(0, len(a)):
            if a[i] == '\n':
                a = a[i+1:]
                break
        for i in range(0, len(a)):
            if a[i] == '>':
                b = a[i+1:]
                a = a[:i]
                break
        for i in range(0, len(b)):
            if b[i] == '\n':
                b = b[i+1:]
                break
        a = a.replace('\n', '')
        b = b.replace('\n', '')
        return a, b   

    def escrever(self, path, a_, b_, score):
        score = str(score)
        arquivo = open(path, 'w')
        arquivo.write(a_ + '\n')
        arquivo.write(b_ + '\n')
        arquivo.write(score)
        arquivo.close
