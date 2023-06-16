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
            [sg.Button('Adicionar uma filial', key=1, size=[30, 1])],
            [sg.Button('Excluir uma filial', key=2, size=[30, 1])],
            [sg.Button('Modificar uma filial', key=3, size=[30, 1])],
            [sg.Button('Listar filiais', key=4, size=[30, 1])],
            [sg.Button('Sair', key=0, size=[30, 1])]
        ]
        self.__window = sg.Window('Sistema de manuzeio de filiais', layout, element_justification='c')

    def pega_dados_cadastro(self):

        while True:
            layout = [
                [sg.Text('Cadastro de Filial')],
                [sg.Text('Aviso.: CEPs e Cidades repetidas não podem ser cadastrados.')],
                [sg.Text('CEP:', size=(15, 1)), sg.InputText('', key='cep')],
                [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de manuzeio de filiais', layout, element_justification='c')
            event, values = self.__window.Read()

            # Checagem cep
            resultado = self.le_cep(values['cep'])
            if resultado[1] is False:
                layout = [
                    [sg.Text('Cadastro de Filial')],
                    [sg.Text(resultado[0])],
                    [sg.Button('Confirmar')]
                ]
                self.__window = sg.Window('Sistema de manuzeio de filiais', layout, element_justification='c')
            else:
                break

        nova_filial = {"cep": resultado[0], "cidade": values['cidade']}
        return nova_filial

    def pega_cep(self):
        cep = self.le_int_positivo("Informe o CEP: ")
        return cep

    def listagem(self, cep, cidade, gerente):
        print(f"CEP: {cep}\nCidade: {cidade}\nGerente: {gerente}\n")

    def mostra_mensagem(self, msg):
        return super().mostra_mensagem(msg)
