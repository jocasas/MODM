from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
NOTES_DIR = BASE_DIR / "data" / "notes"

# Crear la carpeta si no existe
NOTES_DIR.mkdir(parents=True, exist_ok=True)
