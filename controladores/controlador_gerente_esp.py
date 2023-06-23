from telas.tela_gerente import TelaGerente


class ControladorGerenteEsp:

    def __init__(self, controlador_filial, gerente):
        self.__controlador_filial = controlador_filial
        self.__controlador_sistema = self.__controlador_filial.controlador_sistema
        self.__controlador_contrato = self.__controlador_sistema.controlador_contrato
        self.__tela_gerente = TelaGerente()
        self.__gerente = gerente

    def inicializa_sistema(self):
        lista_opcoes = {1: self.modificar_dados, 2: self.demitir,
                        3: self.listar_contratos, 4: self.acessar_contrato,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_gerente.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def modificar_dados(self):
        opcao = self.__tela_gerente.menu_modificacao()
        if opcao == 1:
            novo_nome = self.__tela_gerente.pega_input("Digite o novo nome:", 'Modificação de dados.')
            self.__gerente.nome = novo_nome
        if opcao == 2:
            novo_cpf = self.__tela_gerente.pega_cpf('Digite o novo CPF: ')
            self.__gerente.cpf = novo_cpf
        if opcao == 3:
            nova_data_nasc = self.__tela_gerente.pega_data('Digite a nova data de nascimento: ')
            self.__gerente.data_nasc = nova_data_nasc
        if opcao == 0:
            return

    def demitir(self):
        self.__tela_gerente.mostra_mensagem("Cadastre um novo gerente antes de demitir o anterior")
        self.subs_cargo()
        self.__controlador_contrato.demitir(self.__gerente)
        self.__tela_gerente.mostra_mensagem('Gerente demitido com sucesso.')

    def subs_cargo(self):
        infos_gerencia = self.__controlador_sistema.controlador_gerente.add_gerente()
        filial = self.__controlador_contrato.pega_contrato_por_cpf(self.__gerente.cpf).filial
        dados_contrato = {'data_inicio': infos_gerencia['data_inicio'], 'cargo': infos_gerencia['cargo'],
                          'empregado': infos_gerencia['funcionario'], 'filial': filial,
                          'empregador': infos_gerencia['empregador']}
        filial.gerente = infos_gerencia['funcionario']
        self.__controlador_sistema.filial_dao.update(filial)
        self.__controlador_contrato.incluir_contrato(dados_contrato)

    def listar_contratos(self):
        if len(self.__gerente.contratos) > 0:
            lista = []
            for contrato in self.__gerente.contratos:
                lista.append(self.__controlador_contrato.tela_contrato.formata_contrato(contrato))
            self.__tela_gerente.listagem(f'Listagem de contrator por {self.__gerente.nome}', lista)
        else:
            self.__tela_gerente.mostra_mensagem('Lista vazia.')

    def acessar_contrato(self):
        self.__controlador_contrato.inicializa_sistema(self, self.__gerente)

    def retornar(self):
        self.__controlador_filial.inicializa_sistema()
