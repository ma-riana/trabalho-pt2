from telas.abstract_tela import AbstractTela
from entidade.contrato import Contrato



class TelaContrato(AbstractTela):

    def __init__(self):
        pass

    def mostra_opcoes(self):
        print('\nTELA DE MODIFICAÇÃO: CONTRATO\n'
              + '1) Mostrar contrato\n'
              + '2) Excluir contrato (deixar funcionário inativo)\n'
              + '3) Modificar informações\n'
              + '0) Retornar\n')
        opcao = self.le_int_validos([0, 1, 2, 3], 'Escolha uma opção: ')
        return opcao

    def menu_modificacao(self):
        print("O que deseja modificar?\n"
              + "1) Data de emissão\n"
              + "1) Data de finalização\n"
              + "2) Cargo\n"
              + "3) Filial\n"
              + "0) Retornar\n")
        opcao = super().le_int_validos([1, 2, 3, 4, 0], "Escolha uma opçao: ")
        return opcao

    def listar_contrato(self, contrato: Contrato):
        print(f'''
        === CONTRATO NUM {contrato.id} ===
        Funcionario: {contrato.empregado.nome}
        CPF: {contrato.empregado.cpf}
        Empregador: {contrato.empregador.nome}
        CPF: {contrato.empregador.cpf}
        Cargo: {contrato.cargo.titulo}
        Filial: {contrato.filial.cep}
        Data de emissão: {contrato.data_inicio}
        Data de termino: {contrato.data_final}
        ''')

    def pega_data(self, msg):
        data = self.le_data(msg)
        return data

    def pega_filial(self, msg):
        filial = self.le_cep(msg)
        return filial

    def pega_cargo(self, msg):
        nome_cargo = input('msg')
        return nome_cargo
