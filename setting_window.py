import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLineEdit,QLabel
from settings import Setting

#обработка нажатия
def on_click():
    list=[line_edit_1.text(),line_edit_2.text(),line_edit_3.text()]
    print(list)
    set=Setting("config.json",list)
    set.read_user()
def on_write(text):
    print(text)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Settings')
window.setGeometry(100, 100, 380, 200)
#Строки
line_edit_1 = QLineEdit(window)
line_label_1=QLabel("Цвет",window)
line_label_2=QLabel("Размер шрифта",window)
line_label_3=QLabel("Цвет фона(0,0,0,0-это прозрачный)",window)
line_edit_2 = QLineEdit(window)
line_edit_3 = QLineEdit(window)
#Положение строк
line_label_1.move(50,0)
line_edit_1.move(50, 20)
line_label_2.move(50,50)
line_edit_2.move(50, 67)
line_label_3.move(50,97)
line_edit_3.move(50, 117)
#КНопка
button = QPushButton('Enter', window)
button.clicked.connect(on_click)
button.resize(100, 30)
button.move(50, 150)

window.show()
sys.exit(app.exec_())