# pyqt6_investigation.py


import sys
from PyQt6 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()

    win.setWindowTitle("PyQt6 Application")
    win.resize(600, 400)
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":

    main()

