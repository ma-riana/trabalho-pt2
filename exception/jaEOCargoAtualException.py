class JaEOCargoAtualException(Exception):
    def __init__(self, cargo_repetido):
        super().__init__(f"Impossível realizar o registro de mudança de cargo pois o funcionário já possui o cargo de {cargo_repetido}.")