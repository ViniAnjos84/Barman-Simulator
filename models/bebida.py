class IngredienteBebida:
    def __init__(self, ingrediente, quantidade_ml=0):
        self.ingrediente = ingrediente
        self.quantidade_ml = quantidade_ml


class Bebida:
    def __init__(self, nome="", copo=None):
        self.nome = nome
        self.copo = copo
        self.ingredientes = []
        self.preparo = None
        self.personalizacoes = []

    @property
    def ml_atual(self):
        return sum(item.quantidade_ml for item in self.ingredientes)

    @property
    def ordem(self):
        return [item.ingrediente for item in self.ingredientes]

    @property
    def quantidades(self):
        return [item.quantidade_ml for item in self.ingredientes]

    def adicionar_ingrediente(self, ingrediente, quantidade_ml=0):
        self.ingredientes.append(IngredienteBebida(ingrediente, quantidade_ml))

    def limpar(self):
        self.ingredientes.clear()
        self.preparo = None
        self.personalizacoes.clear()
