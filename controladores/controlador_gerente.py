from telas.tela_gerente import TelaGerente
from entidade.gerente import Gerente
from exception.repeticao_exp import Repeticao
from datetime import date
from dao.gerente_dao import GerenteDAO


class ControladorGerente:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_cargo = self.__controlador_sistema.controlador_cargo
        self.__tela_gerente = TelaGerente()
        self.__gerente_dao = GerenteDAO()

    @property
    def gerente_dao(self):
        return self.__gerente_dao

    def add_gerente(self):
        self.__tela_gerente.mostra_mensagem("\nPor favor, realize o cadastro do gerente na janela seguinte.")
        # Realizando a checagem de repetição de CPF
        while True:
            dados_novo_gerente = self.__tela_gerente.pega_dados_cadastro()
            if self.checagem_repeticao(dados_novo_gerente['CPF']):
                break
            self.__tela_gerente.mostra_mensagem('CPF já cadastrado.')
        obj_novo_gerente = Gerente(dados_novo_gerente['nome'], dados_novo_gerente['CPF'], dados_novo_gerente['data_nasc'])
        self.__gerente_dao.add(obj_novo_gerente)

        # Infomações constantes para todos os gerentes
        cargo_gerente = self.__controlador_cargo.cargo_dao.get(0)
        infos_gerencia = {'funcionario': obj_novo_gerente, 'empregador': 'Empresa',
                          'cargo': cargo_gerente, 'data_inicio': dados_novo_gerente['data_inicio']}
        return infos_gerencia

    def checagem_repeticao(self, cpf):
        while True:
            try:
                if self.__gerente_dao.get(cpf) is not None:
                    raise Repeticao('CPF', cpf)
                return True
            except Repeticao:
                return False
