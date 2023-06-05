from entidade.funcionario import Funcionario
from entidade.gerente import Gerente
from entidade.filial import Filial
from entidade.cargo import Cargo
from datetime import date


class Contrato:
    def __init__(self, id: int, data_inicio: date, cargo: Cargo, empregado: Funcionario,
                 filial: Filial, empregador: Gerente):
        self.__id = id
        self.__data_inicio = data_inicio
        self.__data_final = None
        self.__cargo = cargo
        self.__empregado = empregado
        self.__filial = filial        
        self.__empregador = empregador

    @property
    def id(self):
        return self.__id

    @property
    def data_inicio(self):
        return self.__data_inicio

    @property
    def data_final(self):
        return self.__data_final

    @property
    def cargo(self):
        return self.__cargo

    @property
    def empregado(self):
        return self.__empregado

    @property
    def filial(self):
        return self.__filial

    @property
    def empregador(self):
        return self.__empregador
    
    @data_inicio.setter
    def data_inicio(self, data_inicio: date):
        self.__data_inicio = data_inicio

    @data_final.setter
    def data_final(self, data_final: date):
        self.__data_final = data_final

    @cargo.setter
    def cargo(self, cargo: Cargo):
        self.__cargo = cargo

    @empregado.setter
    def empregado(self, empregado: Funcionario):
        self.__empregado = empregado

    @filial.setter
    def filial(self, filial: Filial):
        self.__filial = filial

    @empregador.setter
    def empregador(self, empregador: Gerente):
        self.__empregador = empregador
