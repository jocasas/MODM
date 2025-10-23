import curses
from app.core.notes import list_notes, read_note, create_note
from app.cli.utils import draw_footer
from app.core.search import search_notes

def app_view(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    query = ""
    seleccion = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        # === Campo de búsqueda ===
        stdscr.addstr(1, 2, f"🔍 Buscar notas: {query}")
        stdscr.hline(2, 0, curses.ACS_HLINE, w)

        # === Resultados ===
        results = search_notes(query)
        # Posición y tamaño de la caja central
        box_top = 3
        box_left = 2
        box_height = h - 6
        box_width = w - 4

        # Dibujar borde completo
        stdscr.addch(box_top, box_left, curses.ACS_ULCORNER)
        stdscr.addch(box_top, box_left + box_width - 1, curses.ACS_URCORNER)
        stdscr.addch(box_top + box_height - 1, box_left, curses.ACS_LLCORNER)
        stdscr.addch(box_top + box_height - 1, box_left + box_width - 1, curses.ACS_LRCORNER)
        stdscr.hline(box_top, box_left + 1, curses.ACS_HLINE, box_width - 2)
        stdscr.hline(box_top + box_height - 1, box_left + 1, curses.ACS_HLINE, box_width - 2)
        stdscr.vline(box_top + 1, box_left, curses.ACS_VLINE, box_height - 2)
        stdscr.vline(box_top + 1, box_left + box_width - 1, curses.ACS_VLINE, box_height - 2)

        # Dibujar resultados dentro de la caja
        max_items = box_height - 2  # espacio disponible dentro de la caja
        for i, nota in enumerate(results[:max_items]):
            y = box_top + 1 + i
            marker = "> " if i == seleccion else "  "
            if i == seleccion:
                stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, box_left + 2, f"{marker}{nota}")
            if i == seleccion:
                stdscr.attroff(curses.color_pair(1))

        # === Footer ===
        draw_footer(stdscr, "[↑↓] Mover  [Enter] Abrir  [N] Nueva  [Esc] Salir")

        stdscr.refresh()
        key = stdscr.getch()

        # --- Entrada de texto ---
        if 32 <= key <= 126:  # caracteres visibles
            query += chr(key)
        elif key in (curses.KEY_BACKSPACE, 127,8): #BORRAR
            if query:
                 query = query[:-1]
        elif key == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif key == curses.KEY_DOWN and seleccion < len(results) - 1:
            seleccion += 1
        elif key in [10, 13] and results:
            show_note(stdscr, results[seleccion])
        elif key in [ord("n"), ord("N")]:
            new_note(stdscr)
        elif key == 27:  # ESC
            break


def show_note(stdscr, name):
    content = read_note(name)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(1, 2, f"📝 {name}", curses.A_BOLD)
    stdscr.hline(2, 0, curses.ACS_HLINE, w)
    for i, line in enumerate(content.splitlines()[: h - 4]):
        stdscr.addstr(3 + i, 2, line[: w - 4])
    draw_footer(stdscr, "[Esc] Volver")
    stdscr.refresh()
    while True:
        if stdscr.getch() == 27:
            break


def new_note(stdscr):
    stdscr.clear()
    curses.curs_set(1)
    stdscr.addstr(1, 2, "Título de la nueva nota: ")
    curses.echo()
    title = stdscr.getstr(1, 28, 50).decode("utf-8")
    curses.noecho()
    create_note(title, "")
    draw_footer(stdscr, "Nota creada. Presiona cualquier tecla para volver...")
    stdscr.refresh()
    stdscr.getch()
