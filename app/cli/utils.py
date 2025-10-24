def draw_footer(stdscr, text: str):
    """Renderiza la barra inferior con atajos."""
    # Ajuste automatico del texto para atajos comunes
    # Muestra Ctrl+N para crear nueva nota si el texto original usa [N]
    if "Nueva" in text:
        text = text.replace("[N]", "[Ctrl+N]").replace("[n]", "[Ctrl+N]")

    h, w = stdscr.getmaxyx()
    stdscr.hline(h - 2, 0, ord("-"), w)
    stdscr.addstr(h - 1, max(2, (w - len(text)) // 2), text)
