from telas.abstract_tela import AbstractTela
from entidade.contrato import Contrato
import PySimpleGUI as sg


class TelaContrato(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_components()

    def mostra_opcoes(self):
        self.init_components()
        event, values = self.__window.Read()
        self.__window.Close()
        if event in (None, 'Cancelar'):
            exit(0)
        return int(event)
    
    def init_components(self):
        layout = [
            [sg.Text('TELA DE MODIFICAÇÃO: CONTRATO')],
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Mostrar contrato', key=1, size=(30, 1))],
            [sg.Button('Excluir contrato (desativar funcionário)', key=2, size=(30, 1))],
            [sg.Button('Modificar informações', key=3, size=(30, 1))],
            [sg.Button('Retornar', key=0, size=(30, 1))]
        ]
        self.__window = sg.Window('Controle do Contrato', layout, element_justification='c')

    def menu_modificacao(self):
        layout = [
            [sg.Text('TELA DE MODIFICAÇÃO: CONTRATO')],
            [sg.Text('O que deseja modificar?')],
            [sg.Button('Data de emissão', key=1, size=(30, 1))],
            [sg.Button('Data de finalização', key=2, size=(30, 1))],
            [sg.Button('Filial', key=3, size=(30, 1))],
            [sg.Button('Cargo', key=3, size=(30, 1))],
            [sg.Button('Retornar', key=0, size=(30, 1))]
        ]
        self.__window = sg.Window('Controle do Contrato', layout, element_justification='c')

        event, values = self.__window.Read()
        self.__window.Close()
        return int(event)

    def formata_contrato(self, contrato):
        # Mantive a procura pelo empregador empresa, mas mudei a forma de listagem para generalizar
        if contrato.empregador == "Empresa":
            empregador = "Empresa"
        else:
            empregador = contrato.empregador.nome
        return f'''
        === CONTRATO NUM {contrato.id} ===
            Funcionario: {contrato.empregado.nome}
            CPF: {contrato.empregado.cpf}
            Empregador: {empregador}
            Cargo: {contrato.cargo.titulo}
            Filial: {contrato.filial.cep}
            Data de emissão: {contrato.data_inicio}
            Data de termino: {contrato.data_final}
        '''

    def pega_filial(self):
        layout = [
            [sg.Text('Modificação de Contrato')],
            [sg.Text('Digite no campo abaixo o CEP da filial')],
            [sg.Text(size=(15, 1), key='-OUTPUT-')],
            [sg.Text('CEP:', size=(15, 1)), sg.InputText('', key='cep')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controle do Contrato', layout, element_justification='c')

        while True:
            event, values = self.__window.Read()
            if event == 'Confimar':
                if self.le_cep(values['cep']):
                    cep = self.formata_cep(values['cep'])
                    return cep
                else:
                    self.__window['-OUTPUT-'].update('Digite um CEP válido.')
            if event in [sg.WIN_CLOSED, 'Cancelar']:
                self.__window.close()
                return None
    
    def pega_data(self, msg):
        data = self.pega_input(msg, 'Controle do Contrato')
        if data is None:
            return
        else:
            while True:
                if self.le_data(data):
                    data = self.formata_data(data)
                    return data
                else:
                    self.mostra_mensagem('Digite uma data válida.')

    def pega_cargo(self, msg):
        nome_cargo = input(msg)
        return nome_cargo
    
    def mostra_mensagem(self, msg):
        sg.popup("", msg)
