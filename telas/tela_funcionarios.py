from telas.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaFuncionario(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__window = None 

    def mostra_opcoes(self):
        pass

    def menu_modificacao(self):
        layout = [
            [sg.Text('O que deseja modificar?')],
            [sg.Button('Nome', key=1, size=(30, 1))],
            [sg.Button('CPF', key=2, size=(30, 1))],
            [sg.Button('Data de nascimento', key=3, size=(30, 1))],
            [sg.Button('Retornar', key=0, size=(30, 1))]
        ]
        self.__window = sg.Window('Controle de Funcionário', layout, element_justification='c')
        event, values = self.__window.Read()
        self.__window.Close()
        return int(event)
    
    def pega_dados_cadastro(self):
        layout = [
            [sg.Text('Cadastro de Funcionário')],
            [sg.Text(size=(15, 1), key='-OUTPUT-')],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText('', key='data_nasc')],
            [sg.Text('Data de contratação:', size=(15, 1)), sg.InputText('', key='data_inicio')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Controle de Funcionário', layout, element_justification='c')

        while True:
            event, values = self.__window.read()
            if event == 'Confirmar':
                if self.le_cpf(values['cpf']) is False:
                    self.__window['-OUTPUT-'].update('Digite um CPF válido.')
                elif self.le_data(values['data_nasc']) is False or self.le_data(values['data_inicio']) is False:
                    self.__window['-OUTPUT-'].update('Digite datas válidas.')
                else:
                    nome = values['nome']
                    cpf = self.formata_cpf(values['cpf'])
                    data_nasc = self.formata_data(values['data_nasc'])
                    data_inicio = self.formata_data(values['data_inicio'])
                    novo_func = {'nome': nome, 'CPF': cpf, 'data_nasc': data_nasc, 'data_inicio': data_inicio}
                    self.__window.close()
                    return novo_func
            if event == sg.WIN_CLOSED:
                break
        self.__window.close()

    def formata_listagem(self, nome, cpf, data_nasc, status):
        return f'Nome: {nome}\nCPF: {cpf}\nData nascimento: {data_nasc}\nStatus: {status}\n'

    def pega_cpf(self, msg):
        while True:
            cpf_buscado = self.pega_input(msg, 'Controle de funcionários')
            if cpf_buscado is None:
                return cpf_buscado
            try:
                if self.le_cpf(cpf_buscado):
                    cpf_buscado = self.formata_cpf(cpf_buscado)
                    return cpf_buscado
                raise ValueError
            except ValueError:
                self.mostra_mensagem('Digite um valor válido de CPF.')

    def pega_data(self, msg):
        while True:
            nova_data = self.pega_input(msg, 'Controle de funcionários')
            if nova_data is None:
                return nova_data
            try:
                if self.le_data(nova_data):
                    nova_data = self.formata_data(nova_data)
                    return nova_data
            except ValueError:
                self.mostra_mensagem('Digite uma data válida.')

