# pyqt6_application.py
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem

from UserDAO import UserDAO

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.user_dao = UserDAO("./users.db")
        self.users = self.user_dao.get_all_users()
        print (self.users)

        # create a table for the users
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Email", "Active"])
        self.table.resize(500, 350)
        self.table.move(0, 50)
        self.table.setRowCount(len(self.users))

        # populate the table
        for row, user in enumerate(self.users):
            self.table.setItem(row, 0, QTableWidgetItem(str(user.id)))
            self.table.setItem(row, 1, QTableWidgetItem(user.name))
            self.table.setItem(row, 2, QTableWidgetItem(user.email))
            self.table.setItem(row, 3, QTableWidgetItem("Yes" if user.active else "No"))
        
        self.setWindowTitle("PyQt6 Application")
        self.resize(600, 400)

        self.button = QPushButton("Press Me", self)
        #self.button.move(50, 100)
        self.button.clicked.connect(self.on_click)        

    def on_click(self):
        QMessageBox.information(self, "Clicked", "You clicked the button")

    def closeEvent(self, event):
        # database is closed with the application
        self.user_dao.close()
        # QMessageBox.information(self, "Closing", "Window is closing")

def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":

    main()
