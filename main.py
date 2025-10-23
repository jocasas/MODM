import curses
from app.cli.menu import main_menu

def main(stdscr):
    curses.curs_set(0)
    main_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
