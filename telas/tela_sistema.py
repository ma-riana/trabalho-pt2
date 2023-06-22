from telas.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaSistema(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_components()

    def mostra_opcoes(self):
        self.init_components()
        event, values = self.__window.Read()
        self.close()
        if event == 0 or event in (None, 'Cancelar'):
            exit(0)
        return int(event)

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        font = "Yu Gothic UI Semibold", 11
        sg.set_options(font=font)
        layout = [
            [sg.Text('Tela Principal: Controle de Filiais')],
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Adicionar uma filial', key=1, size=(30, 1))],
            [sg.Button('Excluir uma filial', key=2, size=(30, 1))],
            [sg.Button('Modificar uma filial', key=3, size=(30, 1))],
            [sg.Button('Listar filiais', key=4, size=(30, 1))],
            [sg.Button('Sair', key=0, size=(30, 1))]
        ]
        self.__window = sg.Window('Sistema de manuzeio de filiais', layout, element_justification='c')

    def pega_dados_cadastro(self):

        layout = [
            [sg.Text('Cadastro de Filial')],
            [sg.Text('Aviso.: CEPs e Cidades repetidas não podem ser cadastrados.')],
            [sg.Text(size=(15, 1), key='-OUTPUT-')],
            [sg.Text('CEP:', size=(15, 1)), sg.InputText('', key='cep')],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de manuzeio de filiais', layout, element_justification='c')

        while True:
            event, values = self.__window.read()
            if event == 'Confirmar':
                if self.le_cep(values['cep']):
                    cep = self.formata_cep(values['cep'])
                    nova_filial = {"cep": cep, "cidade": values['cidade']}
                    self.__window.close()
                    return nova_filial
                else:
                    self.__window['-OUTPUT-'].update('Digite um CEP válido.')
            if event in [sg.WIN_CLOSED, 'Cancelar']:
                self.__window.close()
                return None

    def pega_cep(self, titulo):
        while True:
            cep = self.pega_input('Digite o CEP: ', titulo)
            if cep is None:
                return cep
            else:
                if self.le_cep(cep):
                    cep = self.formata_cep(cep)
                    return cep
                else:
                    self.mostra_mensagem('Digite um CEP válido.')


    def formata_listagem(self, cep, cidade, gerente):
        return f"CEP: {cep}\nCidade: {cidade}\nGerente: {gerente}\n"
