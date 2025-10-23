import os
from app.core.notes import create_note

notas = [
    ("docker setup", "Pasos para configurar Docker en Linux."),
    ("kubernetes basics", "Conceptos básicos de Kubernetes."),
    ("devops pipeline", "Cómo se estructura un pipeline CI/CD."),
    ("rust async", "Notas sobre async/await en Rust."),
    ("obsidian shortcuts", "Lista de atajos útiles en Obsidian."),
    ("python tricks", "Tips para mejorar código Python."),
    ("git advanced", "Uso avanzado de Git: rebase, cherry-pick y reflog."),
    ("linux hardening", "Buenas prácticas para endurecer servidores Linux."),
    ("terraform intro", "Cómo desplegar infraestructuras declarativas."),
    ("ansible basics", "Playbooks, roles y handlers."),
    ("ci cd overview", "Flujo general de CI/CD en DevOps."),
    ("monitoring guide", "Notas sobre métricas y logging."),
    ("grafana dashboards", "Cómo crear dashboards personalizados."),
    ("prometheus metrics", "Configuración de Prometheus paso a paso."),
    ("cloud overview", "Comparativa rápida entre AWS, GCP y Azure."),
    ("api gateway notes", "Conceptos sobre balanceadores y gateways."),
    ("team practices", "Hábitos de trabajo eficientes en equipos DevOps."),
    ("jenkins pipelines", "Configuración de pipelines declarativos."),
    ("container security", "Buenas prácticas para imágenes Docker."),
    ("devops mindset", "Notas sobre cultura y filosofía DevOps."),
]

for title, content in notas:
    try:
        create_note(title, content)
        print(f"✅ Creada: {title}")
    except FileExistsError:
        print(f"⚠️ Ya existía: {title}")
