import curses

def diario(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

    opciones = ["Ver entradas", "Agregar entrada", "Eliminar entrada", "Volver al menú principal"]
    seleccion = 0

    stdscr.nodelay(True)  # Permite que se pinte la primera vez sin bloquear
    tecla = -1  # Valor inicial inválido para el loop

    while True:
        alto, ancho = stdscr.getmaxyx()

        # Crear ventana con borde centrada
        win_alto = len(opciones) + 6
        win_ancho = 50
        win_inicio_y = (alto - win_alto) // 2
        win_inicio_x = (ancho - win_ancho) // 2

        win = curses.newwin(win_alto, win_ancho, win_inicio_y, win_inicio_x)
        win.box()

        # Título
        titulo = "📔  Diario Personal"
        win.addstr(1, (win_ancho - len(titulo)) // 2, titulo, curses.A_BOLD)

        # Opciones
        for idx, opcion in enumerate(opciones):
            x = 3 + idx
            if idx == seleccion:
                win.attron(curses.color_pair(1))
                win.addstr(x, 2, f"> {opcion}")
                win.attroff(curses.color_pair(1))
            else:
                win.addstr(x, 2, f"  {opcion}")

        win.refresh()
        stdscr.refresh()

        # Captura de tecla sin bloqueo
        tecla = stdscr.getch()

        # Si no hay tecla, sigue (para que se vea desde el inicio)
        if tecla == -1:
            curses.napms(30)  # Pequeño delay para no saturar CPU
            continue

        stdscr.nodelay(False)  # Vuelve al modo normal tras el primer input

        if tecla == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif tecla == curses.KEY_DOWN and seleccion < len(opciones) - 1:
            seleccion += 1
        elif tecla in [curses.KEY_ENTER, ord('\n')]:
            opcion_elegida = opciones[seleccion]
            if opcion_elegida == "Volver al menú principal":
                break
            else:
                mostrar_subpantalla(stdscr, opcion_elegida)

def mostrar_subpantalla(stdscr, titulo):
    stdscr.clear()
    alto, ancho = stdscr.getmaxyx()

    mensaje = f"Has elegido: {titulo}"
    stdscr.addstr(alto // 2, (ancho - len(mensaje)) // 2, mensaje)
    stdscr.addstr(alto // 2 + 2, (ancho - 30) // 2, "Presiona una tecla para volver...")
    stdscr.refresh()
    stdscr.getch()
