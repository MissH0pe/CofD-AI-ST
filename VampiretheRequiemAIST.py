from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import sys

class PyQtLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):

        Button1 = QPushButton('Up')
        Button2 = QPushButton('Left')
        Button3 = QPushButton('Right')
        Button4 = QPushButton('Down')

        grid = QGridLayout()
        grid.addWidget(Button1, 0, 1)
        grid.addWidget(Button2, 1, 0)
        grid.addWidget(Button3, 1, 2)
        grid.addWidget(Button4, 1, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('PyQt5 Layout')
        self.show()

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Vampire the Requiem AI Storyteller'
        self.left = 10
        self.top = 10
        self.width = 768
        self.height = 512
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('layout.png')
        label.setPixmap(pixmap)
        pixmap = pixmap.scaledToWidth(768)
        # self.resize(pixmap.width(),pixmap.height())

        showscreenkeys = True
        if showscreenkeys:
            userinterface = PyQtLayout()

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

# class Window():
#
#     def __init__(self):
#         super().__init__()
#         self.window()
#
#     def window(self):
#         app = QApplication(sys.argv)
#         win = QMainWindow()
#         win.setGeometry(400,400,500,300)
#         win.setWindowTitle("VampiretheRequiemAI")
#
#         showscreenkeys = False
#         if showscreenkeys:
#             userinterface = PyQtLayout()
#
#         win.show()
#         sys.exit(app.exec_())
