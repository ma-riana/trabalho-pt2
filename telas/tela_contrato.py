from telas.abstract_tela import AbstractTela
from entidade.contrato import Contrato
import PySimpleGUI as sg
from datetime import date


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
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('TELA DE MODIFICAÇÃO: CONTRATO')],
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Mostrar contrato', key=1, size=[30, 1])],
            [sg.Button('Excluir contrato (desativar funcionário)', key=2, size=[30, 1])],
            [sg.Button('Modificar informações', key=3, size=[30, 1])],
            [sg.Button('Retornar', key=0, size=[30, 1])]
        ]
        self.__window = sg.Window('Controle do Contrato', layout, element_justification='c')

    def menu_modificacao(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('TELA DE MODIFICAÇÃO: CONTRATO')],
            [sg.Text('O que deseja modificar?')],
            [sg.Button('Data de emissão', key=1, size=[30, 1])],
            [sg.Button('Data de finalização', key=2, size=[30, 1])],
            [sg.Button('Filial', key=3, size=[30, 1])],
            [sg.Button('Cargo', key=3, size=[30, 1])],
            [sg.Button('Retornar', key=0, size=[30, 1])]
        ]
        self.__window = sg.Window('Controle do Contrato', layout, element_justification='c')

        event, values = self.__window.Read()
        self.__window.Close()
        return int(event)

    def listar_contrato(self, contratos):
        # antes gerava excecao ao tentar pegar o atributo nome da string empresa 
        string = None
        for contrato in contratos:
            if contrato.empregador == "Empresa":
                empregador = "Empresa"
            else:
                empregador = contrato.empregador.nome 
            string += f'''
            === CONTRATO NUM {contrato.id} ===
            Funcionario: {contrato.empregado.nome}
            CPF: {contrato.empregado.cpf}
            Empregador: {empregador}
            Cargo: {contrato.cargo.titulo}
            Filial: {contrato.filial.cep}
            Data de emissão: {contrato.data_inicio}
            Data de termino: {contrato.data_final}
            '''
        sg.Popup("Listagem de Contratos", string)

    def pega_filial(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('Modificação de Contrato')],
            [sg.Text('Digite no campo abaixo o CEP da filial')],
            [sg.Text('CEP:', size=(15, 1)), sg.InputText('', key='CEP')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controle do Contrato', layout, element_justification='c')
        event, values = self.__window.Read()
        self.__window.Close()
        cep = f"{values['cep'][:5]}-{values['cep'][5:]}"
        return cep
    
    def pega_data(self, msg):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('Modificação de Contrato')],
            [sg.Text('Digite no campo abaixo a nova data do contrato')],
            [sg.Text('Data:', size=(15, 1)), sg.InputText('', key='data')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controle do Contrato', layout, element_justification='c')
        event, values = self.__window.Read()
        self.__window.Close()
        data = date(int(values['data'][4:]), int(values['data'][2:4]), int(values['data'][:2]))
        return data

    def pega_cargo(self, msg):
        nome_cargo = input('msg')
        return nome_cargo
    
    def mostra_mensagem(self, msg):
        sg.popup("", msg)
