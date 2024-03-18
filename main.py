import sys
from src.Controllers.controller import UML_Controller

def main():
    controller = UML_Controller(str(sys.argv[0:1]))
    controller.run()


if __name__ == '__main__':
    main()