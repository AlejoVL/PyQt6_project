from PyQt6.QtWidgets import QApplication
from gui_interface import MainWindows

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindows()
    main_window.show()
    app.exec()