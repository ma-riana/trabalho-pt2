from entidade.filial import Filial
from controladores.controlador_filial import ControladorFilial
from controladores.controlador_gerente import ControladorGerente
from controladores.controlador_contrato import ControladorContrato
from controladores.controlador_cargo import ControladorCargo
from telas.tela_sistema import TelaSistema
from exception.repeticao_exp import Repeticao
from exception.nao_existe_exp import NaoExistencia


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cargo = ControladorCargo(self)
        self.__controlador_gerente = ControladorGerente(self)
        self.__controlador_contrato = ControladorContrato(self)
        self.__lista_filiais = []

    @property
    def controlador_contrato(self):
        return self.__controlador_contrato

    @property
    def controlador_gerente(self):
        return self.__controlador_gerente

    @property
    def controlador_cargo(self):
        return self.__controlador_cargo

    def inicializa_sistema(self):
        lista_opcoes = {1: self.adicionar_filial, 2: self.excluir_filial,
                        3: self.modificar_filial, 4: self.listar,
                        0: self.sair}

        while True:
            opcao_escolhida = self.__tela_sistema.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def adicionar_filial(self):
        while True:
            dados_nova_filial = self.__tela_sistema.pega_dados_cadastro()
            # Checagem de repetição
            if self.checagem_repeticao_cep(dados_nova_filial['cep']):
                if self.checagem_repeticao_cidade(dados_nova_filial['cidade']):
                    break

        infos_gerencia = self.__controlador_gerente.add_gerente()
        nova_filial = Filial(dados_nova_filial['cep'], dados_nova_filial['cidade'], infos_gerencia['funcionario'])
        self.__lista_filiais.append(nova_filial)

        dados_contrato = {'data_inicio': infos_gerencia['data_inicio'], 'cargo': infos_gerencia['cargo'],
                          'empregado': infos_gerencia['funcionario'], 'filial': nova_filial,
                          'empregador': infos_gerencia['empregador']}
        self.__controlador_contrato.incluir_contrato(dados_contrato)

        print('Filial cadastrada com sucesso.')

    def excluir_filial(self):
        self.__tela_sistema.mostra_mensagem('\n=== EXCLUSÃO DE FILIAIS ===\nRealize a busca.')
        filial = self.busca_por_cep("Digite o CEP da filial a ser excluída: ")
        self.__lista_filiais.remove(filial)
        self.__tela_sistema.mostra_mensagem('Filial excluída com sucesso.')

    def modificar_filial(self):
        self.__tela_sistema.mostra_mensagem('\n=== Modificação filial por CEP ===')
        filial = self.busca_por_cep("Digite o CEP: ")
        ControladorFilial(self, filial).inicializa_sistema()

    def listar(self):
        if len(self.__lista_filiais) > 0:
            self.__tela_sistema.mostra_mensagem("\n=== Listagem de filiais ===\n")
            for _ in self.__lista_filiais:
                self.__tela_sistema.listagem(_.cep, _.cidade, _.gerente.nome)
        else:
            self.__tela_sistema.mostra_mensagem('Lista vazia.\n')

    # Método de checagem de repetição
    def checagem_repeticao_cep(self, cep):
        try:
            for _ in self.__lista_filiais:
                if _.cep == cep:
                    raise Repeticao('CEP', cep)
            return True
        except Repeticao:
            self.__tela_sistema.mostra_mensagem(Repeticao('CEP', cep).msg())
            return False

    def checagem_repeticao_cidade(self, cidade):
        try:
            for _ in self.__lista_filiais:
                if _.cidade == cidade:
                    raise Repeticao('Cidade', cidade)
            return True
        except Repeticao:
            self.__tela_sistema.mostra_mensagem(Repeticao('Cidade', cidade).msg())
            return False

    def busca_por_cep(self, msg):
        while True:
            cep_buscado = self.__tela_sistema.le_cep(msg)
            try:
                for _ in self.__lista_filiais:
                    if _.cep == cep_buscado:
                        return _
                raise NaoExistencia
            except NaoExistencia:
                self.__tela_sistema.mostra_mensagem('Filial não encontrada. Tente novamente.')

    def sair(self):
        exit(0)
