from telas.tela_cargo import TelaCargo
from entidade.cargo import Cargo
from dao.cargo_dao import CargoDAO


class ControladorCargo:

    def __init__(self, control_sistema):
        self.__cargo_dao = CargoDAO()
        self.__tela_cargo = TelaCargo()
        self.__control_sistema = control_sistema

    @property
    def cargo_dao(self):
        return self.__cargo_dao

    def incluir_cargo(self):
        dados_cargo = self.__tela_cargo.pega_dados_cargo()
        novo_cargo = Cargo(dados_cargo["id"], dados_cargo["titulo"], dados_cargo["salario"])
        self.__cargo_dao.add(novo_cargo)

    def alterar_cargo(self):
        self.listar_todos_cargos()
        id_cargo = self.__tela_cargo.le_id("cargo")
        if id_cargo == 0:
            self.__tela_cargo.mostra_mensagem("O cargo de Gerente deve permanecer com o mesmo título")
        cargo = self.pega_cargo_por_id(id_cargo)

        novos_dados_cargo = self.__tela_cargo.pega_dados_cargo(id_cargo)
        if id_cargo != 0:
            cargo.titulo = novos_dados_cargo["titulo"]
        cargo.salario = novos_dados_cargo["salario"]
        self.listar_cargo(cargo)

    def listar_cargos_comuns(self):
        if len(self.__cargo_dao.get_all()) == 1: # se tiver apenas o gerente
            print("A empresa ainda não possui cadastro de cargos de funcionários comuns no sistema.")
        else:
            for cargo in self.__cargo_dao.get_all():
                if cargo.titulo != "Gerente":
                    self.__tela_cargo.mostra_cargo({"id": cargo.id, "titulo": cargo.titulo, "salario": cargo.salario})

    def listar_todos_cargos(self):
        for cargo in self.__cargo_dao.get_all():
            self.__tela_cargo.mostra_cargo({"id": cargo.id, "titulo": cargo.titulo, "salario": cargo.salario})

    def listar_cargo(self, cargo: Cargo):
        self.__tela_cargo.mostra_cargo({"id": cargo.id, "titulo": cargo.titulo, "salario": cargo.salario})

    def excluir_cargo(self):
        cargo = self.seleciona_cargo()
        self.__cargo_dao.remove(cargo.id)
        self.listar_cargos_comuns()
        self.__tela_cargo.exclui_id(cargo.id)

    def seleciona_cargo(self):
        self.listar_cargos_comuns()
        while True:
            id = self.__tela_cargo.le_id("cargo")
            if id != 0:
                break
        return self.pega_cargo_por_id(id)

    def pega_cargo_por_id(self, id: int):
        for cargo in self.__cargo_dao.get_all():
            if cargo.id == id:
                return cargo

    def retornar(self):
        self.__control_sistema.inicializa_sistema()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cargo, 2: self.alterar_cargo, 3: self.excluir_cargo,
                        4: self.listar_todos_cargos, 5: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cargo.mostra_opcoes()]()
