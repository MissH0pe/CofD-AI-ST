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

        self.currenttilepm = QtGui.QPixmap.fromImage('resources/blank.png')

        self.gendisplaybutton = QtWidgets.QPushButton()
        self.gendisplaybutton.setText('Regenerate Display Size')
        self.gendisplaysizextext = QtWidgets.QLabel()
        self.gendisplaysizextext.setText('X Dimension: ')
        self.gendisplaysizexbox = QtWidgets.QLineEdit()
        self.gendisplaysizeytext = QtWidgets.QLabel()
        self.gendisplaysizeytext.setText('Y Dimension: ')
        self.gendisplaysizeybox = QtWidgets.QLineEdit()

        self.gendisplaybutton.clicked.connect(self.gendisplay)

        self.twallbutton = QtWidgets.QPushButton()
        self.twallbutton.setIcon(QtGui.QIcon('resources/twallw.png'))
        self.lwallbutton = QtWidgets.QPushButton()
        self.lwallbutton.setIcon(QtGui.QIcon('resources/lwallw.png'))
        self.rwallbutton = QtWidgets.QPushButton()
        self.rwallbutton.setIcon(QtGui.QIcon('resources/rwallw.png'))
        self.bwallbutton = QtWidgets.QPushButton()
        self.bwallbutton.setIcon(QtGui.QIcon('resources/bwallw.png'))

        self.tdoorbutton = QtWidgets.QPushButton()
        self.tdoorbutton.setIcon(QtGui.QIcon('resources/tdoorw.png'))
        self.ldoorbutton = QtWidgets.QPushButton()
        self.ldoorbutton.setIcon(QtGui.QIcon('resources/ldoorw.png'))
        self.rdoorbutton = QtWidgets.QPushButton()
        self.rdoorbutton.setIcon(QtGui.QIcon('resources/rdoorw.png'))
        self.bdoorbutton = QtWidgets.QPushButton()
        self.bdoorbutton.setIcon(QtGui.QIcon('resources/bdoorw.png'))

        self.twallbutton.clicked.connect(self.settile0)
        self.lwallbutton.clicked.connect(self.settile1)
        self.rwallbutton.clicked.connect(self.settile2)
        self.bwallbutton.clicked.connect(self.settile3)

        self.tdoorbutton.clicked.connect(self.settile4)
        self.ldoorbutton.clicked.connect(self.settile5)
        self.rdoorbutton.clicked.connect(self.settile6)
        self.bdoorbutton.clicked.connect(self.settile7)

        self.currenttext = QtWidgets.QLabel()
        self.currenttext.setText('Current Tile: ')
        self.currenttile = QtWidgets.QLabel()
        self.currenttile.setPixmap(self.currenttilepm)
        self.currenttilenum = 0

        self.sxptext = QtWidgets.QLabel()
        self.sxptext.setText('Starting X Position: ')
        self.sxpbox = QtWidgets.QLineEdit()
        self.syptext = QtWidgets.QLabel()
        self.syptext.setText('Starting Y Position: ')
        self.sypbox = QtWidgets.QLineEdit()

        self.exptext = QtWidgets.QLabel()
        self.exptext.setText('Ending X Position: ')
        self.expbox = QtWidgets.QLineEdit()
        self.eyptext = QtWidgets.QLabel()
        self.eyptext.setText('Ending Y Position: ')
        self.eypbox = QtWidgets.QLineEdit()

        self.addbutton = QtWidgets.QPushButton()
        self.addbutton.setText('Add Lines')

        self.undobutton = QtWidgets.QPushButton()
        self.undobutton.setText('Undo')

        self.undobutton.clicked.connect(self.undo)
        self.addbutton.clicked.connect(self.add)

        self.layout.addWidget(self.gendisplaybutton, 0, 0)
        self.layout.addWidget(self.gendisplaysizextext, 0, 1)
        self.layout.addWidget(self.gendisplaysizexbox, 0, 2)
        self.layout.addWidget(self.gendisplaysizeytext, 0, 3)
        self.layout.addWidget(self.gendisplaysizeybox, 0, 4)

        self.layout.addWidget(self.twallbutton, 1, 0)
        self.layout.addWidget(self.lwallbutton, 1, 1)
        self.layout.addWidget(self.rwallbutton, 1, 2)
        self.layout.addWidget(self.bwallbutton, 1, 3)

        self.layout.addWidget(self.tdoorbutton, 2, 0)
        self.layout.addWidget(self.ldoorbutton, 2, 1)
        self.layout.addWidget(self.rdoorbutton, 2, 2)
        self.layout.addWidget(self.bdoorbutton, 2, 3)

        self.layout.addWidget(self.currenttext, 3, 0)
        self.layout.addWidget(self.currenttile, 3, 1)

        self.layout.addWidget(self.sxptext, 4, 0)
        self.layout.addWidget(self.sxpbox, 4, 1)
        self.layout.addWidget(self.syptext, 4, 2)
        self.layout.addWidget(self.sypbox, 4, 3)

        self.layout.addWidget(self.exptext, 5, 0)
        self.layout.addWidget(self.expbox, 5, 1)
        self.layout.addWidget(self.eyptext, 5, 2)
        self.layout.addWidget(self.eypbox, 5, 3)

        self.layout.addWidget(self.addbutton, 4, 4)
        self.layout.addWidget(self.undobutton, 5, 4)

    def undo(self):
        self.display.pop()

    def add(self):
        self.display.append([])
        # self.display[len(self.display) - 1]
        for xit in range(int(float(self.expbox.text())) - int(float(self.sxpbox.text())) + 1):
            self.display[len(self.display) - 1].append([])
            for yit in range(int(float(self.eypbox.text())) - int(float(self.sypbox.text())) + 1):
                self.display[len(self.display) - 1][xit].append(QtWidgets.QLabel())
                self.display[len(self.display) - 1][xit][yit].setPixmap(self.currenttilepmt)
                self.layout.addWidget(self.display[len(self.display) - 1][xit][yit], yit + int(self.sypbox.text()) + 3, xit + int(self.sxpbox.text()) + 6)

    def settile0(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/twallw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/twallt.png')
        self.currenttile.setPixmap(self.currenttilepm)

    def settile1(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/lwallw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/lwallt.png')
        self.currenttile.setPixmap(self.currenttilepm)

    def settile2(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/rwallw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/rwallt.png')
        self.currenttile.setPixmap(self.currenttilepm)

    def settile3(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/bwallw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/bwallt.png')
        self.currenttile.setPixmap(self.currenttilepm)

    def settile4(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/tdoorw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/tdoort.png')
        self.currenttile.setPixmap(self.currenttilepm)

    def settile5(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/ldoorw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/ldoort.png')
        self.currenttile.setPixmap(self.currenttilepm)

    def settile6(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/rdoorw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/rdoort.png')
        self.currenttile.setPixmap(self.currenttilepm)

    def settile7(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/bdoorw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/bdoort.png')
        self.currenttile.setPixmap(self.currenttilepm)

    def gendisplay(self):
        # print('test')
        if self.gendisplaysizexbox.text() != '' and self.gendisplaysizeybox.text() != '':
            self.display = []
            self.numsx = []
            self.numsy = []

            for it in range(int(self.gendisplaysizexbox.text())):
                self.numsx.append(QtWidgets.QLabel())
                self.numsx[it].setText(str(it))
                self.layout.addWidget(self.numsx[it], 2, it + 6)
            for it in range(int(self.gendisplaysizeybox.text())):
                self.numsy.append(QtWidgets.QLabel())
                self.numsy[it].setText(str(it))
                self.layout.addWidget(self.numsy[it], it + 3, 5)

            self.display.append([])

            pixMap = QtGui.QPixmap.fromImage('resources/blank.png')

            for xit in range(int(float(self.gendisplaysizexbox.text()))):
                self.display[0].append([])
                for yit in range(int(float(self.gendisplaysizeybox.text()))):
                    self.display[0][xit].append(QtWidgets.QLabel())
                    self.display[0][xit][yit].setPixmap( pixMap )
                    self.layout.addWidget(self.display[0][xit][yit], yit + 3, xit + 6)

            # twallt = QtGui.QPixmap.fromImage('resources/twallt.png')
            #
            # self.display.append([])
            #
            # for it in range(xrooms):
            #     self.display[1].append(QtWidgets.QLabel())
            #     self.display[1][it].setPixmap(twallt)
            #     self.layout.addWidget(self.display[1][it], 3, it + 6)
            #
            # lwallt = QtGui.QPixmap.fromImage('resources/lwallt.png')
            #
            # self.display.append([])
            #
            # for it in range(xrooms):
            #     self.display[2].append(QtWidgets.QLabel())
            #     self.display[2][it].setPixmap(lwallt)
            #     self.layout.addWidget(self.display[2][it], it + 3, 6)

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

    gentwall(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/twallt.png')

if path.exists('resources/lwallt.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genlwall(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/lwallt.png')

if path.exists('resources/rwallt.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genrwall(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/rwallt.png')

if path.exists('resources/bwallt.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genbwall(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/bwallt.png')

if path.exists('resources/tdoort.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    gentdoor(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/tdoort.png')

if path.exists('resources/ldoort.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genldoor(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/ldoort.png')

if path.exists('resources/rdoort.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genrdoor(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/rdoort.png')

if path.exists('resources/bdoort.png') == False:
    img = Image.new('RGBA', (16, 16), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genbdoor(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/bdoort.png')



if path.exists('resources/twallw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    gentwall(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/twallw.png')

if path.exists('resources/lwallw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genlwall(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/lwallw.png')

if path.exists('resources/rwallw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genrwall(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/rwallw.png')

if path.exists('resources/bwallw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genbwall(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/bwallw.png')

if path.exists('resources/tdoorw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    gentdoor(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/tdoorw.png')

if path.exists('resources/ldoorw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genldoor(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/ldoorw.png')

if path.exists('resources/rdoorw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genrdoor(0, 0, 1, 1, 16, 16, 8)

    img.save('resources/rdoorw.png')

if path.exists('resources/bdoorw.png') == False:
    img = Image.new('RGBA', (16, 16), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genbdoor(0, 0, 1, 1, 16, 16, 8)

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
