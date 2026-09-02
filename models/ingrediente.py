class Ingrediente:
    def __init__(self, nome, icone, cor):
        self.nome = nome
        self.icone = icone
        self.cor = cor

    def __repr__(self):
        return f"Ingrediente(nome={self.nome!r})"
