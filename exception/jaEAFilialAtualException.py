class JaEAFilialAtualException(Exception):
    def __init__(self, filial_repetida):
        super().__init__(f"Impossível realizar o registro da transferência pois o funcionário já trabalha na filial {filial_repetida}.")