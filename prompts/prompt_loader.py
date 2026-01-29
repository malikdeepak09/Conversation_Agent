from pathlib import Path

BASE_PATH = Path(__file__).parent

def load_prompt(filename: str) -> str:
    return (BASE_PATH / filename).read_text().strip()
