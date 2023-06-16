from abc import ABC, abstractmethod
from datetime import date
from exception.opcao_invalida_exp import OpcaoInvalida
import PySimpleGUI as sg


class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def mostra_opcoes(self):
        pass

    def mostra_mensagem(self, msg: str):
        print(msg)

    def pega_input(self, msg: str):
        inp = input(msg)
        return inp

    def le_cpf(self, msg):
        while True:
            print('Formatação CPF válido: 13255870950 (11 ints)')
            cpf = input(msg)
            try:
                if len(cpf) == 11:
                    f1 = cpf[:3]
                    f2 = cpf[3:6]
                    f3 = cpf[6:9]
                    f4 = cpf[9:]
                    return f'{f1}.{f2}.{f3}-{f4}'
                else:
                    raise ValueError
            except ValueError:
                print('CPF inválido')

    def le_cep(self, cep):
        while True:
            try:
                if len(cep) == 8:
                    f1 = cep[:5]
                    f2 = cep[5:]
                    return f'{f1}-{f2}', True
                else:
                    raise ValueError
            except ValueError:
                return 'Digite um valor válido para o CEP.', False

    def le_data(self, msg):
        while True:
            print('Formatação data válido: 11012000 (8 ints)')
            data = input(msg)
            data_int = float(data)
            try:
                if len(data) == 8:
                    f1 = int(data[:2])
                    f2 = int(data[2:4])
                    f3 = int(data[4:])
                    return date(f3, f2, f1)
                else:
                    raise ValueError
            except ValueError:
                print('Digite uma data válida.')

    def le_int_validos(self, int_validos: list, msg):
        while True:
            variavel = input(msg)
            try:
                opcao = int(variavel)
                if opcao not in int_validos:
                    raise OpcaoInvalida
                return opcao
            except ValueError:
                print('Esse valor deve ser um inteiro.')
            except OpcaoInvalida:
                print('Digite uma opção disponível.')

    def le_intervalo(self, menor_valor, maior_valor, msg):
        while True:
            variavel = input(msg)
            try:
                opcao = int(variavel)
                if menor_valor <= opcao <= maior_valor:
                    return opcao
                else:
                    raise OpcaoInvalida
            except ValueError:
                print('Esse valor deve ser um inteiro.')
            except OpcaoInvalida:
                print('Digite uma opção disponível.')

    def le_int_positivo(self, msg):
        while True:
            variavel = input(msg)
            try:
                variavel_int = int(variavel)
                if variavel_int < 0:
                    raise ValueError
                return variavel_int
            except ValueError:
                print('Esse valor deve ser um inteiro positivo.')
