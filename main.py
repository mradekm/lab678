import sys
import converter
from PyQt5.QtWidgets import QApplication
from ui import MainWindow

def main():
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        converter.convert(input_file, output_file)
    else:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()
