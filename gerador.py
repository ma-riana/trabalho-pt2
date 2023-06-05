def gera_getter_setter(nome, tipo):

    print(f'''
    @property
    def {nome}(self):
        return self.__{nome}

    @{nome}.setter
    def {nome}(self, {nome}: {tipo}):
        if isinstance({nome}, {tipo}):
            self.__{nome} = {nome}
    ''')

def gera_selfs(nome):
    print(f"self.__{nome} = {nome}")

gera_getter_setter("funcionario", "Funcionario")
gera_getter_setter("data", "str")
