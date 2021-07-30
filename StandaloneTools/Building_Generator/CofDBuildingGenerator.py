from PIL import Image, ImageDraw, ImageFont
import sys
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

def genlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, linewidthf):
    draw.line((x * imgsizex / xroomsf, y * imgsizey / yroomsf, x * imgsizex / xroomsf, (y + 1) * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def genrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, linewidthf):
    draw.line(((x+1) * imgsizex / xroomsf, y * imgsizey / yroomsf, (x+1) * imgsizex / xroomsf, (y + 1) * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def gentwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, linewidthf):
    draw.line((x * imgsizex / xroomsf, y * imgsizey / yroomsf, (x+1) * imgsizex / xroomsf, y * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def genbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, linewidthf):
    draw.line((x * imgsizex / xroomsf, (y+1) * imgsizey / yroomsf, (x+1) * imgsizex / xroomsf, (y + 1) * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def genldoor(x, y, xroomsf, yroomsf, imgsizex, imgsizey, linewidthf):
    draw.line((x * imgsizex / xroomsf, y * imgsizey / yroomsf, x * imgsizex / xroomsf, (y + 0.3333) * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)
    draw.line((x * imgsizex / xroomsf, (y + 0.6667) * imgsizey / yroomsf, x * imgsizex / xroomsf, (y + 1) * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def genrdoor(x, y, xroomsf, yroomsf, imgsizex, imgsizey, linewidthf):
    draw.line(((x+1) * imgsizex / xroomsf, y * imgsizey / yroomsf, (x+1) * imgsizex / xroomsf, (y + 0.3333) * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)
    draw.line(((x+1) * imgsizex / xroomsf, (y + 0.6667) * imgsizey / yroomsf, (x+1) * imgsizex / xroomsf, (y + 1) * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def gentdoor(x, y, xroomsf, yroomsf, imgsizex, imgsizey, linewidthf):
    draw.line((x * imgsizex / xroomsf, y * imgsizey / yroomsf, (x + 0.3333) * imgsizex / xroomsf, y * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)
    draw.line(((x + 0.6667) * imgsizex / xroomsf, y * imgsizey / yroomsf, (x+1) * imgsizex / xroomsf, y * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def genbdoor(x, y, xroomsf, yroomsf, imgsizex, imgsizey, linewidthf):
    draw.line((x * imgsizex / xroomsf, (y+1) * imgsizey / yroomsf, (x + 0.3333) * imgsizex / xroomsf, (y+1) * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)
    draw.line(((x + 0.6667) * imgsizex / xroomsf, (y+1) * imgsizey / yroomsf, (x+1) * imgsizex / xroomsf, (y+1) * imgsizey / yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()

        self.setGeometry(300, 75, 1024, 768)
        self.setWindowTitle('Chronicles of Darkness Building Generator')
        self.layout = QtWidgets.QGridLayout(self)

        # newAction = QtGui.QAction('&New', self)
        # # newAction.setShortcut('Ctrl+N')
        # newAction.setStatusTip('New Building')
        # newAction.triggered.connect(self.new)
        #
        # QtWidgets.QStatusBar()
        #
        # self.menubar = QtWidgets.QMenuBar()
        # self.fileMenu = self.menubar.addMenu('&File')
        # self.fileMenu.addAction(newAction)
        # self.layout.addWidget(self.menubar, 0, 0, 0, 20)

        self.gendisplaybutton = QtWidgets.QPushButton()
        self.gendisplaybutton.setText('Regenerate Display Size')
        self.gendisplaysizextext = QtWidgets.QLabel()
        self.gendisplaysizextext.setText('X Dimension: ')
        self.gendisplaysizexbox = QtWidgets.QLineEdit()
        self.gendisplaysizeytext = QtWidgets.QLabel()
        self.gendisplaysizeytext.setText('Y Dimension: ')
        self.gendisplaysizeybox = QtWidgets.QLineEdit()

        self.gendisplaybutton.clicked.connect(self.gendisplay)

        self.layout.addWidget(self.gendisplaybutton, 0, 0)
        self.layout.addWidget(self.gendisplaysizextext, 0, 1)
        self.layout.addWidget(self.gendisplaysizexbox, 0, 2)
        self.layout.addWidget(self.gendisplaysizeytext, 0, 3)
        self.layout.addWidget(self.gendisplaysizeybox, 0, 4)

    def gendisplay(self):
        # print('test')
        if self.gendisplaysizexbox.text() != '' and self.gendisplaysizeybox.text() != '':
            self.display = []

            self.display.append([])

            pixMap = QtGui.QPixmap.fromImage('resources/blank.png')

            for xit in range(int(float(self.gendisplaysizexbox.text()))):
                self.display[0].append([])
                for yit in range(int(float(self.gendisplaysizeybox.text()))):
                    self.display[0][xit].append(QtWidgets.QLabel())
                    self.display[0][xit][yit].setPixmap( pixMap )
                    self.layout.addWidget(self.display[0][xit][yit], yit + 2, xit + 5)

            twallt = QtGui.QPixmap.fromImage('resources/twallt.png')

            self.display.append([])

            for it in range(xrooms):
                self.display[1].append(QtWidgets.QLabel())
                self.display[1][it].setPixmap(twallt)
                self.layout.addWidget(self.display[1][it], 2, it + 5)

            lwallt = QtGui.QPixmap.fromImage('resources/lwallt.png')

            self.display.append([])

            for it in range(xrooms):
                self.display[2].append(QtWidgets.QLabel())
                self.display[2][it].setPixmap(lwallt)
                self.layout.addWidget(self.display[2][it], it + 2, 5)

    # def new(self):
    #     w = QtWidgets.QWidget()
    #
    #     w.setWindowTitle('Chronicles of Darkness Building Generator')
    #
    #     layout = QtWidgets.QGridLayout(w)

xdim = int(sys.argv[1])
ydim = int(sys.argv[2])

xrooms = int(sys.argv[3])
yrooms = int(sys.argv[4])

filename = sys.argv[5]
extension = sys.argv[6]

linewidthmod = int(sys.argv[7])

outerlinewidth = int((((xdim + ydim) / 2) / 50) * linewidthmod)
innerlinewidth = int(outerlinewidth / 2)

if path.exists('resources/blank.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))

    img.save('resources/blank.png')

if path.exists('resources/twallt.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    gentwall(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/twallt.png')

if path.exists('resources/lwallt.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genlwall(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/lwallt.png')

if path.exists('resources/rwallt.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genrwall(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/rwallt.png')

if path.exists('resources/bwallt.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genbwall(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/bwallt.png')

if path.exists('resources/tdoort.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    gentdoor(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/tdoort.png')

if path.exists('resources/ldoort.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genldoor(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/ldoort.png')

if path.exists('resources/rdoort.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genrdoor(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/rdoort.png')

if path.exists('resources/bdoort.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genbdoor(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/bdoort.png')



if path.exists('resources/twallw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    gentwall(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/twallw.png')

if path.exists('resources/lwallw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genlwall(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/lwallw.png')

if path.exists('resources/rwallw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genrwall(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/rwallw.png')

if path.exists('resources/bwallw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genbwall(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/bwallw.png')

if path.exists('resources/tdoorw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    gentdoor(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/tdoorw.png')

if path.exists('resources/ldoorw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genldoor(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/ldoorw.png')

if path.exists('resources/rdoorw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genrdoor(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/rdoorw.png')

if path.exists('resources/bdoorw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genbdoor(0, 0, 1, 1, 16, 16, 2)

    img.save('resources/bdoorw.png')

# img = Image.new('RGBA', (xdim, ydim), color = (255, 255, 255, 255))
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("arial.ttf", 50)
#
# gentwall(0, 0, xrooms, yrooms, img.size[0], img.size[1], innerlinewidth)
#
# img.save(filename+'.'+extension)

app = QtWidgets.QApplication([])

widget = MyWidget()
# widget.resize(1024, 768)
# widget.show()

w = QtWidgets.QWidget()

w.setWindowTitle('Chronicles of Darkness Building Generator')

layout = QtWidgets.QGridLayout(w)
scroll = QtWidgets.QScrollArea()

scroll.setWidget(widget)
scroll.setWidgetResizable(True)
scroll.resize(16, 768)
layout.addWidget(scroll)
w.show()


sys.exit(app.exec())
