def draw_footer(stdscr, text: str):
    """Renderiza la barra inferior con atajos."""
    h, w = stdscr.getmaxyx()
    stdscr.hline(h - 2, 0, ord("-"), w)
    stdscr.addstr(h - 1, max(2, (w - len(text)) // 2), text)
