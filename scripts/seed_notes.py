import os
from app.core.notes import create_note

notas = [
    ("docker setup", "Pasos para configurar Docker en Linux."),
    ("kubernetes basics", "Conceptos básicos de Kubernetes."),
    ("devops pipeline", "Cómo se estructura un pipeline CI/CD."),
    ("rust async", "Notas sobre async/await en Rust."),
    ("obsidian shortcuts", "Lista de atajos útiles en Obsidian."),
]

for title, content in notas:
    try:
        create_note(title, content)
        print(f"✅ Creada: {title}")
    except FileExistsError:
        print(f"⚠️ Ya existía: {title}")
