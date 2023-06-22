from telas.abstract_tela import AbstractTela
from exception.nao_existe_exp import NaoExistencia
import PySimpleGUI as sg


class TelaCargo(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__id_gerados = [0, 1, 2]
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
            [sg.Text('TELA DE MODIFICAÇÃO: CARGOS')],
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Adicionar cargo', key=1, size=(30, 1))],
            [sg.Button('Alterar cargo', key=2, size=(30, 1))],
            [sg.Button('Excluir cargo', key=3, size=(30, 1))],
            [sg.Button('Listar todos os cargos', key=4, size=(30, 1))],
            [sg.Button('Retornar', key=0, size=(30, 1))]
        ]
        self.__window = sg.Window('Controle dos Cargos', layout, element_justification='c')

    def pega_dados_cargo(self, id=None):




        print("\n~~~~~~~~ Inserindo os dados do cargo ~~~~~~~~")
        if (id == None):
            id = self.gera_id()
        titulo = input("Digite o nome da função: ")
        salario = super().le_int_positivo("Digite o salário desse cargo em números: ")

        return {"id": id, "titulo": titulo, "salario": salario}

    def mostra_cargo(self, dados_cargo):
        print(f"\nIdentificação: {dados_cargo['id']}"
              f"\nTítulo: {dados_cargo['titulo']}"
              f"\nSalário: {dados_cargo['salario']}")

    def pega_cargo(self, lista_cargos):
        print('\n=== Cargos disponíveis ===')
        index = 1
        for cargo in lista_cargos:
            if cargo.titulo != 'Gerente':
                print(f'{index}. {cargo.titulo}')
                index += 1
        print('\n')
        opcao = self.le_intervalo(1, index, "Escolha uma opção: ")
        return opcao

    def mostra_mensagem(self, msg: str):
        super().mostra_mensagem(msg)

    def gera_id(self):
        novo_id = (self.__id_gerados[-1] + 1)
        self.__id_gerados.append(novo_id)
        return novo_id

    def exclui_id(self, id: int):
        self.__id_gerados.remove(id)

    def le_id(self, tipo: str):
        while True:
            try:
                id = int(input(f"\nEscolha qual {tipo} digitando seu identificador: "))
                if id not in self.__id_gerados:
                    raise NaoExistencia()
                return id
            except NaoExistencia:
                print(f"Não foi encontrado(a) nenhum(a) {tipo} com essa identificação.")