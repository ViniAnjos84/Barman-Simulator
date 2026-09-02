from core.config import GLASSES_DIR
from models.copo import Copo


COPO_BAIXO = Copo(
    "Copo Baixo",
    300,
    f"{GLASSES_DIR}/copo_baixo.png",
    f"{GLASSES_DIR}/copo_baixo_mask.png",
)

COPOS = [COPO_BAIXO]
