from app.core.notes import list_notes

def search_notes(query: str):
    """Filtra las notas por nombre (case insensitive)."""
    all_notes = list_notes()
    if not query:
        return all_notes
    q = query.lower()
    return [n for n in all_notes if q in n.lower()]
