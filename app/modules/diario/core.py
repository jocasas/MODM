import curses
from app.modules.diario.file_manipulation import read_entry,list_entries,delete_entry,create_entry

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
            elif opcion_elegida == "Ver entradas":
                mostrar_lista_entradas(stdscr)
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

def mostrar_lista_entradas(stdscr):
    """Submenú para listar y leer entradas existentes."""
    entradas = list_entries()

    if not entradas:
        mostrar_mensaje(stdscr, "No hay entradas disponibles.")
        return
    
    stdscr.nodelay(True)  # Permite que se pinte la primera vez sin bloquear

    seleccion = 0
    while True:
        stdscr.clear()
        alto, ancho = stdscr.getmaxyx()

        win_alto = len(entradas) + 6
        win_ancho = 60
        win_inicio_y = (alto - win_alto) // 2
        win_inicio_x = (ancho - win_ancho) // 2

        win = curses.newwin(win_alto, win_ancho, win_inicio_y, win_inicio_x)
        win.box()
        titulo = "📖  Entradas del Diario"
        win.addstr(1, (win_ancho - len(titulo)) // 2, titulo, curses.A_BOLD)

        for idx, nombre in enumerate(entradas):
            x = 3 + idx
            if idx == seleccion:
                win.attron(curses.color_pair(1))
                win.addstr(x, 2, f"> {nombre}")
                win.attroff(curses.color_pair(1))
            else:
                win.addstr(x, 2, f"  {nombre}")

        win.addstr(win_alto - 2, 2, "ENTER para leer, ESC para volver.")
        win.refresh()

        tecla = stdscr.getch()
        
        if tecla == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif tecla == curses.KEY_DOWN and seleccion < len(entradas) - 1:
            seleccion += 1
        elif tecla in [curses.KEY_ENTER, ord('\n')]:
            mostrar_contenido_entrada(stdscr, entradas[seleccion])
        elif tecla == 27:  # ESC
            break


def mostrar_contenido_entrada(stdscr, nombre):
    """Muestra el contenido completo de una entrada."""
    try:
        contenido = read_entry(nombre)
    except FileNotFoundError:
        mostrar_mensaje(stdscr, f"La entrada '{nombre}' no existe.")
        return

    stdscr.clear()
    alto, ancho = stdscr.getmaxyx()

    win = curses.newwin(alto - 4, ancho - 4, 2, 2)
    win.box()
    win.addstr(1, 2, f"📘 {nombre}", curses.A_BOLD)

    # Mostrar contenido línea por línea
    for i, linea in enumerate(contenido.splitlines()[:alto - 6]):
        win.addstr(3 + i, 2, linea[:ancho - 6])

    win.addstr(alto - 6, 2, "Presiona cualquier tecla para volver.")
    win.refresh()
    stdscr.getch()


def mostrar_mensaje(stdscr, texto):
    """Muestra un mensaje simple centrado."""
    stdscr.clear()
    alto, ancho = stdscr.getmaxyx()
    stdscr.addstr(alto // 2, (ancho - len(texto)) // 2, texto)
    stdscr.addstr(alto // 2 + 2, (ancho - 30) // 2, "Presiona una tecla para continuar...")
    stdscr.refresh()
    stdscr.getch()