import curses
from app.cli.app_view import app_view

def main(stdscr):
    app_view(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)