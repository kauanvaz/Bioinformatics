import itertools
import numpy as np

class smithwaterman:

    def __init__(self, prim_ite=0, score=-100, aux_repetir_letra=0):
        self.prim_ite = prim_ite    #Ajuda na identificação da primeira iteração do traceback
        self.score = score          #Guarda o score
        self.aux_repetir_letra = aux_repetir_letra #Auxiliar para indicar se uma letra vai ser repetida ou não

    def matrix(self, a, b, local, match_score, mismatch_score, gap_cost):
        H = np.zeros((len(a) + 1, len(b) + 1), np.int)

        if local == 0: # É global
            k=1
            aux = -2
            for i in range(0, H.shape[0]):
                for j in range(0, H.shape[1]):
                    
                    if (i==0 or j==0) and (i+j == k):
                        if k <= min(H.shape[0]-1, H.shape[1]-1):
                            H[0][k] = aux
                            H[k][0] = aux
                        else:
                            if (H.shape[0]-1) > (H.shape[1]-1):
                                H[k][0] = aux
                            else:
                                H[0][k] = aux

                        k = k + 1
                        aux = aux - 2
                
        for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):
            match = H[i - 1, j - 1] + (match_score if a[i - 1] == b[j - 1] else mismatch_score)
            delete = H[i - 1, j] + gap_cost
            insert = H[i, j - 1] + gap_cost
            if local == 0:
                H[i, j] = max(match, delete, insert) #Construção da matriz inserindo os maiores valores, considerando global
            else:
                H[i, j] = max(match, delete, insert, 0) #Construção da matriz inserindo os maiores valores, considerando local
        return H

    def traceback(self, H, b, local, sco_cad, b_='', old_i=0, old_j=0): 
        H_flip = np.flip(np.flip(H, 0), 1)
        i_, j_ = np.unravel_index(H_flip.argmax(), H_flip.shape)
        i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))  # (i, j) são os últimos índices de H.max()
        print(H)
        print('\n')
        print(H_flip)
        print(i_, j_)
        print(i, j)

        if (i_ == 0 and j_ == 0) and self.prim_ite == 0:
            sco_cad = 0
        
        if sco_cad == 0 and (i_ != 0 or j_ != 0) and self.prim_ite == 0:  # sco_cad é 1 se considerar score e 0 se considerar a cadeia
            self.score = H_flip[0,0]
            if i_ == 0 and j_ != 0:
                old_j = j + 2
            if i_ != 0 and j_ == 0:
                old_i = i+2
                print(i)
                print(old_i)
            if i_ != 0 and j_ != 0:
                i_, j_ = 0, 0
                i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))
            self.prim_ite = self.prim_ite + 1
        
        if self.prim_ite == 0: #Guarda o score
            self.score = H[i,j]
            self.prim_ite = self.prim_ite + 1

        if local == 0 and (i_ == H.shape[0]-1 and j_ == H.shape[1]-1) and H_flip[i_, j_]== 0:
            aux = H_flip
            aux[i_, j_] = -100
            i_, j_ = np.unravel_index(aux.argmax(), H_flip.shape)
            i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))
        if local == 1 and H[i, j] == 0:
            self.prim_ite = 0
            return b_, self.score

        k = j-1
        if old_j - j > 1:
            b_ = b[k+1] + b_
        if k >= 0:
            b_ = b[k] + '-' + b_ if old_i - i > 1 else b[k] + b_

        if ((i==1 and j==0) or (j==1 and i==0) or (i==1 and j==1)):
            if i == 1 and j == 0:
                b_ = '-'  + b_  
            if j>0:
                j = j-1
            self.prim_ite = 0
            return b_, self.score
        return self.traceback(H[0:i, 0:j], b, local, sco_cad, b_, i, j) 


    def smith_waterman(self, a, b, local, sco_cad, match_score, mismatch_score, gap_cost):
        a, b = a.upper(), b.upper()
        H_a = self.matrix(b, a, local, match_score, mismatch_score, gap_cost) #Matriz para fazer o traceback segundo a fita A
        H_b = self.matrix(a, b, local, match_score, mismatch_score, gap_cost) #Matriz para fazer o traceback segundo a fita 
        print(H_b)
        a_, self.score = self.traceback(H_a, a, local, sco_cad) #Retorna a fita a após o traceback
        b_, self.score = self.traceback(H_b, b, local, sco_cad) ##Retorna a fita b após o traceback
        return a_, b_, self.score