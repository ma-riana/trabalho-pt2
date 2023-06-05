from telas.abstract_tela import AbstractTela
from exception.naoExistencia import NaoExistencia


class TelaCargo(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__id_gerados = [0]

    def mostra_opcoes(self):
        print("\nTela de gerenciamento dos cargos"
              "\n1 - Adicionar cargo"
              "\n2 - Alterar cargo"
              "\n3 - Excluir cargo"
              "\n4 - Listar todos os cargos"
              "\n5 - Retornar")
        return super().le_int_validos([1, 2, 3, 4, 5], "Digite a opção do menu que deseja: ")

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