import sys
from pathlib import Path

# Adiciona o diretório raiz ao caminho Python
sys.path.append(str(Path(__file__).parent.parent))

from flows.hello import hello_world

if __name__ == "__main__":
    hello_world.serve(
        name="hello-every-30min",
        cron="*/30 * * * *",
        tags=["demo"]
    )