import os
from datetime import datetime

# Carpeta donde se guardan las entradas del diario
DIARIO_DIR = "app/modules/diario/diario_entries"

def ensure_dir():
    """Crea el directorio del diario si no existe."""
    os.makedirs(DIARIO_DIR, exist_ok=True)


def list_entries():
    """Devuelve una lista con los nombres de las entradas (sin extensión)."""
    ensure_dir()
    archivos = [
        f.replace(".md", "")
        for f in os.listdir(DIARIO_DIR)
        if f.endswith(".md")
    ]
    return sorted(archivos)


def create_entry(title: str, content: str):
    """
    Crea una nueva entrada del diario con el título y contenido dados.
    El archivo se guarda como Markdown (.md).
    """
    ensure_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    safe_title = title.strip().replace(" ", "_")

    path = os.path.join(DIARIO_DIR, f"{safe_title}.md")

    if os.path.exists(path):
        raise FileExistsError(f"Ya existe una entrada llamada '{title}'.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"_Creado el {timestamp}_\n\n")
        f.write(content.strip() + "\n")

    return path


def read_entry(title: str):
    """
    Devuelve el contenido de una entrada por su nombre (sin extensión).
    """
    ensure_dir()
    path = os.path.join(DIARIO_DIR, f"{title}.md")

    if not os.path.exists(path):
        raise FileNotFoundError(f"No existe la entrada '{title}'.")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def delete_entry(title: str):
    """
    Elimina una entrada del diario.
    """
    ensure_dir()
    path = os.path.join(DIARIO_DIR, f"{title}.md")

    if not os.path.exists(path):
        raise FileNotFoundError(f"No existe la entrada '{title}'.")

    os.remove(path)
    return True
