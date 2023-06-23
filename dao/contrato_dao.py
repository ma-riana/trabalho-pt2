from dao.list_dao import ListDAO
from entidade.contrato import Contrato


class ContratoDAO(ListDAO):
    def __init__(self):
        super().__init__('contratos.pkl')

    def add(self, contrato: Contrato):
        if((contrato is not None) and isinstance(contrato, Contrato)):
            if len(super().cache) == 0:
                super().add(0, contrato)
            else:
                for indice in range(len(super().cache)):
                    if super().cache[indice].data_inicio < contrato.data_inicio:
                        super().add(indice, contrato)
                        return
                    super().add(len(super().cache), contrato)

    def update(self, cpf: str, contrato: Contrato):
        if((contrato is not None) and isinstance(contrato, Contrato) and isinstance(cpf, str)):
            for indice in range(len(super().cache)):
                if super().cache[indice].empregado.cpf is cpf:
                    super().update(indice, contrato)
                    return

    def get(self, key: str):
        print("chave:", key)
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)