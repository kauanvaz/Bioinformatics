import PySimpleGUI as sg
from leitorfasta import leitorfasta 
from smithwaterman import smithwaterman

class principal:

    def __init__(self):    
        sg.change_look_and_feel('DarkBlue')
        #Layout
        layout = [
            [sg.FileBrowse(button_text ='Arquivo', file_types=(("ALL Files", "*.*"),), key='-arquivo-')],
            [sg.Text('Digite os valores de match, mismatch e gap, respectivamente:')],
            [sg.Input(default_text='1', size=(16, 16), key='-match-'), sg.Input(default_text='-1', size=(16, 16), 
            key='-mismatch-'), sg.Input(default_text='-2', size=(16, 16), key='-gap-')],
            [sg.Text('Escolha o tipo do alinhamento:')], 
            [sg.Radio('Local','tipo', default = False, key='-tipoLocal-'), sg.Radio('Global','tipo', default = False, 
            key='-tipoGlobal-')],
            [sg.Text('Escolha o que considerar no traceback:')],
            [sg.Radio('Maior score','trace', default = False, key='-traceSco-'), sg.Radio('Cadeia maior','trace', 
            default = False, key='-traceMai-')],
            [sg.SaveAs(button_text='Salvar', file_types=(("Text File", "*.txt"),), key='-salvar-')],
            [sg.OK(key="-ok-")]
        ]
        #Janela
        self.window = sg.Window('Alinhamento').layout(layout)
        

    def Iniciar(self):     
        while True:
            #Extrair dados da tela
            self.event, self.values = self.window.read()
            if self.event == sg.WINDOW_CLOSED or self.event == 'Quit':
                break   

            passos = 0

            endereco = self.values['-arquivo-']
            if endereco == '':
                sg.popup('Erro','Nenhum arquivo selecionado.')
                continue
            else:
                leitor = leitorfasta(endereco)
                a, b = leitor.ler_e_tratar()
                passos = passos + 1     
            '''
            if len(b) > len(a):
                aux = a
                a = b
                b = aux
                '''

            tipo_local, tipo_global = self.values['-tipoLocal-'], self.values['-tipoGlobal-']   
            if tipo_local and not tipo_global:
                local = 1
                passos = passos + 1
            elif not tipo_local and tipo_global:
                local = 0
                passos = passos + 1
            else:
                sg.popup('Erro','Escolha um tipo de alinhamento.')
                continue
                
            trace_score, trace_cadeia = self.values['-traceSco-'], self.values['-traceMai-']
            if trace_score and not trace_cadeia:
                sco_cad = 1
                passos = passos + 1
            elif not trace_score and trace_cadeia:
                sco_cad = 0
                passos = passos + 1
            else:
                sg.popup('Erro','Escolha o que considerar.')
                continue
           

            match, mismatch, gap = int(self.values['-match-']), int(self.values['-mismatch-']), int(self.values['-gap-'])

            algor = smithwaterman()    
            a_, b_, score = algor.smith_waterman(a, b, local, sco_cad, match, mismatch, gap) 

            salvar = self.values['-salvar-']
            if salvar != '':
                leitor.escrever(salvar, a_, b_, score)
                passos = passos + 1
            else:
                sg.popup('Erro','Defina onde salvar.')
                continue

            if passos == 4:
                sg.popup('Sucesso','Arquivo salvo.')           

        self.window.close()

tela = principal()
tela.Iniciar()