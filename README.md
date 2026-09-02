# Barman Simulator

Protótipo de um jogo de preparo de bebidas em Pygame.

## Estrutura

- `main.py` — ponto de entrada.
- `core/` — ciclo do jogo, configurações e carregamento de assets.
- `models/` — modelos de domínio: bebida, ingrediente e copo.
- `data/` — catálogo de ingredientes e copos.
- `ui/` — componentes visuais e interação da interface.
- `images/` — recursos gráficos.

## Executar

```bash
pip install -r requirements.txt
python main.py
```

O projeto mantém a lógica de domínio independente do carregamento de imagens sempre que possível. O `AssetManager` centraliza o cache dos assets para evitar carregamentos repetidos.
