import sys
import json
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):

    def savedef(self):
        stats = {'box1': self.box1.text(), 'box2': self.box2.text(), 'box3': self.box3.text(), 'box4': self.box4.text()}
        with open(self.saveloc.text()+'.json', 'w') as f:
            json.dump(stats, f)

    def __init__(self):
        super(MyWidget, self).__init__()

        self.setGeometry(300, 75, 1024, 768)
        self.setWindowTitle('Vampire the Requiem Character Editor')

        self.save = QtWidgets.QPushButton('Save')
        self.save.clicked.connect(self.savedef)

        self.box1 = QtWidgets.QLineEdit(self)
        self.box2 = QtWidgets.QLineEdit(self)
        self.box3 = QtWidgets.QLineEdit(self)
        self.box4 = QtWidgets.QLineEdit(self)
        self.saveloc = QtWidgets.QLineEdit(self)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.save, 0, 0)
        self.layout.addWidget(self.box1, 0, 1)
        self.layout.addWidget(self.saveloc, 0, 2)
        self.layout.addWidget(self.box2, 1, 0)
        self.layout.addWidget(self.box3, 1, 1)
        self.layout.addWidget(self.box4, 1, 2)

        self.setLayout(self.layout)

app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(1024, 768)
widget.show()

sys.exit(app.exec())
