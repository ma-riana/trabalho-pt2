from abc import ABC, abstractmethod
from datetime import date
import PySimpleGUI as sg


class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        self.__window = None

    def mostra_opcoes(self):
        pass

    def init_components(self):
        pass

    def mostra_mensagem(self, msg):
        sg.popup_ok_cancel(msg, title='Mensagem')

    def pega_input(self, msg: str, titulo):
        inp = sg.popup_get_text(msg, title=titulo)
        return inp

    def le_cpf(self, cpf):
        while True:
            try:
                cpf_int = int(cpf)
                if isinstance(cpf_int, int):
                    if len(cpf) == 11:
                        return True
                raise ValueError
            except ValueError:
                return False

    def formata_cpf(self, cpf):
        f1 = cpf[:3]
        f2 = cpf[3:6]
        f3 = cpf[6:9]
        f4 = cpf[9:]
        return f'{f1}.{f2}.{f3}-{f4}'

    def le_cep(self, cep):
        while True:
            try:
                int_cep = int(cep)
                if isinstance(int_cep, int):
                    if len(cep) == 8:
                        return True
                raise ValueError
            except ValueError:
                return False

    def formata_cep(self, cep):
        f1 = cep[:5]
        f2 = cep[5:]
        return f'{f1}-{f2}'

    def le_data(self, data):
        while True:
            try:
                data_int = float(data)
                if isinstance(data_int, float):
                    if len(data) == 8:
                        return True
                raise ValueError
            except ValueError:
                return False

    def formata_data(self, data):
        f1 = int(data[:2])
        f2 = int(data[2:4])
        f3 = int(data[4:])
        return date(f3, f2, f1)

    def le_salario(self, salario):
        try:
            salario_float = float(salario)
            if salario_float > 500:
                return True
            raise ValueError
        except ValueError:
            return False

    def listagem(self, titulo, lista_listagem):
        layout = [[sg.Text(titulo)]]
        for _ in lista_listagem:
            layout.append([sg.Text(_)])
        self.__window = sg.Window('Listagem', layout, element_justification='c')
        event = self.__window.Read()
        if event == sg.WIN_CLOSED:
            self.init_components()

