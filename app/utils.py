import curses


"""Main Menu Script"""

def Menu():
    menu_options = ["Alimentacion Logs","Diario","Salir"]

    def draw_menu(stdscr):
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
        current_row = 0

        while True:
            stdscr.clear()
            h, w = stdscr.getmaxyx()

            # Dibujar opciones
            for idx, row in enumerate(menu_options):
                x = w//2 - len(row)//2
                y = h//2 - len(menu_options)//2 + idx
                if idx == current_row:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, row)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.addstr(y, x, row)

            stdscr.refresh()

            key = stdscr.getch()
            
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu_options) - 1:
                current_row += 1
            elif key in [10, 13]:  # Enter
                selected = menu_options[current_row]
                if selected == "Salir":
                    break
                stdscr.clear()
                stdscr.addstr(0, 0, f"Seleccionaste: {selected}")
                stdscr.addstr(1, 0, "Presiona una tecla para volver al menú...")
                stdscr.refresh()
                stdscr.getch()

    curses.wrapper(draw_menu)