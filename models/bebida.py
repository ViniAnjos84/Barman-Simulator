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

    def adicionar_ingrediente(self, ingrediente):
        """Inicia um novo ingrediente com 0 ml para ser preenchido gradualmente."""
        if self.copo is None or self.ml_atual >= self.copo.capacidade_ml:
            return False

        self.ingredientes.append(IngredienteBebida(ingrediente, 0))
        return True

    def quantidade_em_andamento(self, tempo_inicio, agora_ms, atraso_ms, velocidade):
        """Retorna a quantidade do último ingrediente considerando o tempo de preenchimento."""
        if not self.ingredientes or tempo_inicio is None:
            return 0

        tempo = agora_ms - tempo_inicio
        if tempo <= atraso_ms:
            return 0

        quantidade = (tempo - atraso_ms) * velocidade / 1000
        espaco = self.copo.capacidade_ml - self.ml_atual
        return min(max(quantidade, 0), max(espaco, 0))

    def confirmar_ingrediente(self, quantidade_ml):
        """Grava a quantidade que foi preenchida no último ingrediente."""
        if not self.ingredientes or self.copo is None:
            return False

        quantidade = max(0, quantidade_ml)
        espaco = max(0, self.copo.capacidade_ml - self.ml_atual)
        quantidade = min(quantidade, espaco)
        self.ingredientes[-1].quantidade_ml += quantidade
        return quantidade > 0

    def remover_ultimo_ingrediente(self):
        if self.ingredientes:
            self.ingredientes.pop()

    def limpar(self):
        self.ingredientes.clear()
        self.preparo = None
        self.personalizacoes.clear()
