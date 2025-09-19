import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from settings import Setting

class Settings(QWidget):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.setWindowTitle('Settings')
        self.setGeometry(100, 100, 380, 200)

        # элементы
        self.button = QPushButton('Enter', self)
        self.line_edit_1 = QLineEdit(self)
        self.line_label_1 = QLabel("Цвет", self)
        self.line_label_2 = QLabel("Размер шрифта", self)
        self.line_label_3 = QLabel("Цвет фона (0,0,0,0 — это прозрачный)", self)
        self.line_edit_2 = QLineEdit(self)
        self.line_edit_3 = QLineEdit(self)

        self.line_pos()
        self.setup_button()

    def line_pos(self):
        self.line_label_1.move(50, 0)
        self.line_edit_1.move(50, 20)

        self.line_label_2.move(50, 50)
        self.line_edit_2.move(50, 70)

        self.line_label_3.move(50, 100)
        self.line_edit_3.move(50, 120)

    def on_click(self):
        values = [
            self.line_edit_1.text(),
            self.line_edit_2.text(),
            self.line_edit_3.text()
        ]
        settings = Setting(self.file, values)
        settings.read_user()

    def setup_button(self):    
        self.button.clicked.connect(self.on_click)
        self.button.resize(100, 30)
        self.button.move(50, 160)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Settings("config.json")
    overlay.show()
    sys.exit(app.exec_())