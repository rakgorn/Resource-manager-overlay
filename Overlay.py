from PyQt5 import QtWidgets, QtCore
import sys
from Data import ComData  

class Overlay(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.pk = ComData()#Обьект с данными

        # Настройка прозрачного окна
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        # Надпись
        self.label = QtWidgets.QLabel(self)
        self.label.setStyleSheet("""
            color: #00FF00;  /* зеленый текст */
            font-size: 10pt;
            font-weight: standart;
            background: rgba(0,0,0,0); /* прозрачный фон */
        """)
        self.label.move(0, 0)

        self.resize(1500, 500)
        self.update_data()

    def update_data(self):
        # Обновление текста каждую 0.5 секунды(при усложнении нужно поставить меньше а то будет тормозить)
        self.label.setText(f"{self.pk.cpu()}\n{self.pk.ram()}\n{self.pk.gpu_temp()}")
        QtCore.QTimer.singleShot(500, self.update_data)
pk=ComData()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    overlay = Overlay()
    overlay.move(pk.monitor()[0]-200,0)  # позиция на экране
    overlay.show()
    sys.exit(app.exec_())