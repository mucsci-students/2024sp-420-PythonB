import sys
from src.Controllers.old_controller import run as run_cli
from src.Controllers.gui_controller import run as run_gui

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'cli':
        run_cli()
    else:
        run_gui()
