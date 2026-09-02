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

    def adicionar_ingrediente(self, ingrediente, quantidade_ml):
        if quantidade_ml <= 0 or self.copo is None:
            return False

        espaco_disponivel = self.copo.capacidade_ml - self.ml_atual
        quantidade_adicionada = min(quantidade_ml, espaco_disponivel)

        if quantidade_adicionada <= 0:
            return False

        self.ingredientes.append(
            IngredienteBebida(ingrediente, quantidade_adicionada)
        )
        return True

    def limpar(self):
        self.ingredientes.clear()
        self.preparo = None
        self.personalizacoes.clear()
