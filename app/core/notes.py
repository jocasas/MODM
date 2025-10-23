from datetime import datetime
from pathlib import Path
from app.core.config import NOTES_DIR

def list_notes():
    """Lista todas las notas Markdown."""
    return sorted([f.stem for f in NOTES_DIR.glob("*.md")])

def create_note(title: str, content: str):
    """Crea una nueva nota con fecha."""
    safe_title = title.strip().replace(" ", "_")
    path = NOTES_DIR / f"{safe_title}.md"

    if path.exists():
        raise FileExistsError(f"Ya existe una nota llamada '{title}'.")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n_Creado el {timestamp}_\n\n{content}\n")

def read_note(title: str):
    """Lee una nota Markdown."""
    path = NOTES_DIR / f"{title}.md"
    if not path.exists():
        raise FileNotFoundError(f"No existe la nota '{title}'.")
    return path.read_text(encoding="utf-8")

def delete_note(title: str):
    """Elimina una nota."""
    path = NOTES_DIR / f"{title}.md"
    if not path.exists():
        raise FileNotFoundError(f"No existe la nota '{title}'.")
    path.unlink()
