import sys
from pathlib import Path

# Додаємо src/ до імпортів
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
