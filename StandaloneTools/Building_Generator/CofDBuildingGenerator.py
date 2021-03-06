from PIL import Image, ImageDraw, ImageFont
import sys
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

def genlwall(x, y, xroomsf, yroomsf, linewidthf, drawf):
    drawf.line((x, y, x, yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def genrwall(x, y, xroomsf, yroomsf, linewidthf, drawf):
    drawf.line((xroomsf - 2, y, xroomsf - 2, yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def gentwall(x, y, xroomsf, yroomsf, linewidthf, drawf):
    drawf.line((x, y, xroomsf, y), fill=(0, 0, 0, 255), width=linewidthf)

def genbwall(x, y, xroomsf, yroomsf, linewidthf, drawf):
    drawf.line((x, yroomsf - 2, xroomsf, yroomsf - 2), fill=(0, 0, 0, 255), width=linewidthf)

def genldoor(x, y, xroomsf, yroomsf, linewidthf, drawf):
    drawf.line((x, y, x, (0.3333 * yroomsf)), fill=(0, 0, 0, 255), width=linewidthf)
    drawf.line((x, (yroomsf * 0.6667), x, yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def genrdoor(x, y, xroomsf, yroomsf, linewidthf, drawf):
    drawf.line((xroomsf - 2, y, xroomsf - 2, (0.3333 * yroomsf)), fill=(0, 0, 0, 255), width=linewidthf)
    drawf.line((xroomsf - 2, (yroomsf * 0.6667), xroomsf - 2, yroomsf), fill=(0, 0, 0, 255), width=linewidthf)

def gentdoor(x, y, xroomsf, yroomsf, linewidthf, drawf):
    drawf.line((x, y, (0.3333 * xroomsf), y), fill=(0, 0, 0, 255), width=linewidthf)
    drawf.line(((0.6667 * xroomsf), y, xroomsf, y), fill=(0, 0, 0, 255), width=linewidthf)

def genbdoor(x, y, xroomsf, yroomsf, linewidthf, drawf):
    drawf.line((x, yroomsf - 2, (0.3333 * xroomsf), yroomsf - 2,), fill=(0, 0, 0, 255), width=linewidthf)
    drawf.line(((0.6667 * xroomsf), yroomsf - 2, xroomsf, yroomsf - 2,), fill=(0, 0, 0, 255), width=linewidthf)

class QLabel_alterada(QtWidgets.QLabel):
    clicked=QtCore.Signal()

    def mousePressEvent(self, ev):
        self.clicked.emit()
        self.display.append([])
        self.display[len(self.display) - 1].append([])
        self.display[len(self.display) - 1][0].append(QtWidgets.QLabel())
        self.display[len(self.display) - 1][0][0].setPixmap(self.currenttile)
        self.layout.addWidget(self.display[len(self.display) - 1][0][0], self.y + 3, self.x + 1)
        self.displaydata.append([])
        self.displaydata[len(self.displaydata) - 1].append([])
        self.displaydata[len(self.displaydata) - 1][0].append([self.tileid, self.x, self.y])

        # self.displayclicks[self.x][self.y] = QLabel_alterada(self.display[len(self.display) - 1][self.x][self.y])
        # self.displayclicks[self.x][self.y].mousePressEvent
        # self.displayclicks[self.x][self.y].mouseCoord(self.x, self.y)
        # self.displayclicks[self.x][self.y].updateDisplay(self.display, self.layout, self.displaydata)

    def mouseCoord(self, x, y):
        self.x = x
        self.y = y

    def updateTile(self, tile, tileid):
        self.currenttile = tile
        self.tileid = tileid

    def updateDisplay(self, display, layout, displaydata):
        self.display = display
        self.layout = layout
        self.displaydata = displaydata

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()

        self.setGeometry(300, 75, 1024, 768)
        self.setWindowTitle('Chronicles of Darkness Building Generator')
        self.layout = QtWidgets.QGridLayout(self)

        saveAction = QtGui.QAction('&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save Building')
        saveAction.triggered.connect(self.save)
        #
        # QtWidgets.QStatusBar()
        #
        self.menubar = QtWidgets.QMenuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(saveAction)
        self.layout.addWidget(self.menubar, 0, 0, 0, 20)

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

        self.xdimtext = QtWidgets.QLabel()
        self.xdimtext.setText('Final Image Pixel Width: ')
        self.xdimbox = QtWidgets.QLineEdit()
        self.xdimbox.setText('2048')
        self.ydimtext = QtWidgets.QLabel()
        self.ydimtext.setText('Final Image Pixel Height: ')
        self.ydimbox = QtWidgets.QLineEdit()
        self.ydimbox.setText('2048')

        self.extension = 'png'

        self.linewidthtext = QtWidgets.QLabel()
        self.linewidthtext.setText('Line Width Modifier: ')
        self.linewidthbox = QtWidgets.QLineEdit()
        self.linewidthbox.setText('1')

        self.undobutton.clicked.connect(self.undo)
        self.addbutton.clicked.connect(self.add)

        self.layout.addWidget(self.gendisplaybutton, 1, 5)
        self.layout.addWidget(self.gendisplaysizextext, 1, 6)
        self.layout.addWidget(self.gendisplaysizexbox, 1, 7)
        self.layout.addWidget(self.gendisplaysizeytext, 1, 8)
        self.layout.addWidget(self.gendisplaysizeybox, 1, 9)

        self.layout.addWidget(self.twallbutton, 2, 5)
        self.layout.addWidget(self.lwallbutton, 2, 6)
        self.layout.addWidget(self.rwallbutton, 2, 7)
        self.layout.addWidget(self.bwallbutton, 2, 8)

        self.layout.addWidget(self.tdoorbutton, 3, 5)
        self.layout.addWidget(self.ldoorbutton, 3, 6)
        self.layout.addWidget(self.rdoorbutton, 3, 7)
        self.layout.addWidget(self.bdoorbutton, 3, 8)

        self.layout.addWidget(self.currenttext, 4, 5)
        self.layout.addWidget(self.currenttile, 4, 6)

        self.layout.addWidget(self.sxptext, 5, 5)
        self.layout.addWidget(self.sxpbox, 5, 6)
        self.layout.addWidget(self.syptext, 5, 7)
        self.layout.addWidget(self.sypbox, 5, 8)

        self.layout.addWidget(self.exptext, 6, 5)
        self.layout.addWidget(self.expbox, 6, 6)
        self.layout.addWidget(self.eyptext, 6, 7)
        self.layout.addWidget(self.eypbox, 6, 8)

        self.layout.addWidget(self.addbutton, 5, 9)
        self.layout.addWidget(self.undobutton, 6, 9)

        self.layout.addWidget(self.xdimtext, 7, 5)
        self.layout.addWidget(self.xdimbox, 7, 6)
        self.layout.addWidget(self.ydimtext, 7, 7)
        self.layout.addWidget(self.ydimbox, 7, 8)

        self.layout.addWidget(self.linewidthtext, 8, 5)
        self.layout.addWidget(self.linewidthbox, 8, 6)

    def undo(self):
        self.display.pop()

    def add(self):
        self.display.append([])
        self.displaydata.append([])
        # self.display[len(self.display) - 1]
        for xit in range(int(float(self.expbox.text())) - int(float(self.sxpbox.text())) + 1):
            self.display[len(self.display) - 1].append([])
            self.displaydata[len(self.displaydata) - 1].append([])
            for yit in range(int(float(self.eypbox.text())) - int(float(self.sypbox.text())) + 1):
                self.display[len(self.display) - 1][xit].append(QtWidgets.QLabel())
                self.display[len(self.display) - 1][xit][yit].setPixmap(self.currenttilepmt)
                self.layout.addWidget(self.display[len(self.display) - 1][xit][yit], yit + int(self.sypbox.text()) + 3, xit + int(self.sxpbox.text()) + 1)
                self.displaydata[len(self.displaydata) - 1][xit].append([self.currenttileid, xit, yit])

        for x in range(len(self.displayclicks)):
            for y in range(len(self.displayclicks[x])):
                self.displayclicks[x][y].updateDisplay(self.display, self.layout, self.displaydata)

    def settile0(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/twallw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/twallt.png')
        self.currenttileid = 0
        self.currenttile.setPixmap(self.currenttilepm)
        for x in range(len(self.displayclicks)):
            for y in range(len(self.displayclicks[x])):
                self.displayclicks[x][y].updateTile(self.currenttilepmt, 0)

    def settile1(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/lwallw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/lwallt.png')
        self.currenttileid = 1
        self.currenttile.setPixmap(self.currenttilepm)
        for x in range(len(self.displayclicks)):
            for y in range(len(self.displayclicks[x])):
                self.displayclicks[x][y].updateTile(self.currenttilepmt, 1)

    def settile2(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/rwallw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/rwallt.png')
        self.currenttileid = 2
        self.currenttile.setPixmap(self.currenttilepm)
        for x in range(len(self.displayclicks)):
            for y in range(len(self.displayclicks[x])):
                self.displayclicks[x][y].updateTile(self.currenttilepmt, 2)

    def settile3(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/bwallw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/bwallt.png')
        self.currenttileid = 3
        self.currenttile.setPixmap(self.currenttilepm)
        for x in range(len(self.displayclicks)):
            for y in range(len(self.displayclicks[x])):
                self.displayclicks[x][y].updateTile(self.currenttilepmt, 3)

    def settile4(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/tdoorw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/tdoort.png')
        self.currenttileid = 4
        self.currenttile.setPixmap(self.currenttilepm)
        for x in range(len(self.displayclicks)):
            for y in range(len(self.displayclicks[x])):
                self.displayclicks[x][y].updateTile(self.currenttilepmt, 4)

    def settile5(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/ldoorw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/ldoort.png')
        self.currenttileid = 5
        self.currenttile.setPixmap(self.currenttilepm)
        for x in range(len(self.displayclicks)):
            for y in range(len(self.displayclicks[x])):
                self.displayclicks[x][y].updateTile(self.currenttilepmt, 5)

    def settile6(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/rdoorw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/rdoort.png')
        self.currenttileid = 6
        self.currenttile.setPixmap(self.currenttilepm)
        for x in range(len(self.displayclicks)):
            for y in range(len(self.displayclicks[x])):
                self.displayclicks[x][y].updateTile(self.currenttilepmt, 6)

    def settile7(self):
        self.currenttilepm = QtGui.QPixmap.fromImage('resources/bdoorw.png')
        self.currenttilepmt = QtGui.QPixmap.fromImage('resources/bdoort.png')
        self.currenttileid = 7
        self.currenttile.setPixmap(self.currenttilepm)
        for x in range(len(self.displayclicks)):
            for y in range(len(self.displayclicks[x])):
                self.displayclicks[x][y].updateTile(self.currenttilepmt, 7)

    def gendisplay(self):
        # print('test')
        if self.gendisplaysizexbox.text() != '' and self.gendisplaysizeybox.text() != '':
            self.display = []
            self.displayclicks = []
            self.displaydata = []
            self.numsx = []
            self.numsy = []

            for it in range(int(self.gendisplaysizexbox.text())):
                self.numsx.append(QtWidgets.QLabel())
                self.numsx[it].setText(str(it))
                self.layout.addWidget(self.numsx[it], 2, it + 1)
            for it in range(int(self.gendisplaysizeybox.text())):
                self.numsy.append(QtWidgets.QLabel())
                self.numsy[it].setText(str(it))
                self.layout.addWidget(self.numsy[it], it + 3, 0)

            self.display.append([])
            self.displayclicks.append([])

            pixMap = QtGui.QPixmap.fromImage('resources/blank.png')

            for xit in range(int(float(self.gendisplaysizexbox.text()))):
                self.display[0].append([])
                self.displayclicks.append([])
                for yit in range(int(float(self.gendisplaysizeybox.text()))):
                    self.display[0][xit].append(QtWidgets.QLabel())
                    self.display[0][xit][yit].mousePressEvent
                    self.displayclicks[xit].append(QLabel_alterada(self.display[0][xit][yit]))
                    self.displayclicks[xit][yit].mousePressEvent
                    self.displayclicks[xit][yit].mouseCoord(xit, yit)
                    self.displayclicks[xit][yit].updateDisplay(self.display, self.layout, self.displaydata)
                    self.display[0][xit][yit].setPixmap( pixMap )
                    self.layout.addWidget(self.display[0][xit][yit], yit + 3, xit + 1)

            self.xoff = int(float(self.gendisplaysizexbox.text()))

            self.layout.addWidget(self.gendisplaybutton, 1, 5 + self.xoff)
            self.layout.addWidget(self.gendisplaysizextext, 1, 6 + self.xoff)
            self.layout.addWidget(self.gendisplaysizexbox, 1, 7 + self.xoff)
            self.layout.addWidget(self.gendisplaysizeytext, 1, 8 + self.xoff)
            self.layout.addWidget(self.gendisplaysizeybox, 1, 9 + self.xoff)

            self.layout.addWidget(self.twallbutton, 2, 5 + self.xoff)
            self.layout.addWidget(self.lwallbutton, 2, 6 + self.xoff)
            self.layout.addWidget(self.rwallbutton, 2, 7 + self.xoff)
            self.layout.addWidget(self.bwallbutton, 2, 8 + self.xoff)

            self.layout.addWidget(self.tdoorbutton, 3, 5 + self.xoff)
            self.layout.addWidget(self.ldoorbutton, 3, 6 + self.xoff)
            self.layout.addWidget(self.rdoorbutton, 3, 7 + self.xoff)
            self.layout.addWidget(self.bdoorbutton, 3, 8 + self.xoff)

            self.layout.addWidget(self.currenttext, 4, 5 + self.xoff)
            self.layout.addWidget(self.currenttile, 4, 6 + self.xoff)

            self.layout.addWidget(self.sxptext, 5, 5 + self.xoff)
            self.layout.addWidget(self.sxpbox, 5, 6 + self.xoff)
            self.layout.addWidget(self.syptext, 5, 7 + self.xoff)
            self.layout.addWidget(self.sypbox, 5, 8 + self.xoff)

            self.layout.addWidget(self.exptext, 6, 5 + self.xoff)
            self.layout.addWidget(self.expbox, 6, 6 + self.xoff)
            self.layout.addWidget(self.eyptext, 6, 7 + self.xoff)
            self.layout.addWidget(self.eypbox, 6, 8 + self.xoff)

            self.layout.addWidget(self.addbutton, 5, 9 + self.xoff)
            self.layout.addWidget(self.undobutton, 6, 9 + self.xoff)

            self.layout.addWidget(self.xdimtext, 7, 5 + self.xoff)
            self.layout.addWidget(self.xdimbox, 7, 6 + self.xoff)
            self.layout.addWidget(self.ydimtext, 7, 7 + self.xoff)
            self.layout.addWidget(self.ydimbox, 7, 8 + self.xoff)

            self.layout.addWidget(self.linewidthtext, 8, 5 + self.xoff)
            self.layout.addWidget(self.linewidthbox, 8, 6 + self.xoff)

    def saveimage(self, filename):
        img = Image.new('RGBA', (int(self.xdimbox.text()), int(self.ydimbox.text())), color = (255, 255, 255, 255))
        draw = ImageDraw.Draw(img)

        self.outerlinewidth = int((((int(self.xdimbox.text()) + int(self.ydimbox.text()))) / 100) * int(self.linewidthbox.text()))
        self.innerlinewidth = int(self.outerlinewidth / 2)

        for it in range(len(self.displaydata)):
            for xit in range(len(self.displaydata[it])):
                for yit in range(len(self.displaydata[it][xit])):
                    # print('test')
                    if self.displaydata[it][xit][yit][0] == 0:
                        # print('test2')
                        gentwall(img.size[0]*(self.displaydata[it][xit][yit][1]/len(self.display[0])), img.size[1]*(self.displaydata[it][xit][yit][2]/len(self.display[0][0])), img.size[0]*((self.displaydata[it][xit][yit][1] + 1)/len(self.display[0])), img.size[1]*((self.displaydata[it][xit][yit][2] + 1)/len(self.display[0][0])), self.innerlinewidth, draw)
                    elif self.displaydata[it][xit][yit][0] == 1:
                        genlwall(img.size[0]*(self.displaydata[it][xit][yit][1]/len(self.display[0])), img.size[1]*(self.displaydata[it][xit][yit][2]/len(self.display[0][0])), img.size[0]*((self.displaydata[it][xit][yit][1] + 1)/len(self.display[0])), img.size[1]*((self.displaydata[it][xit][yit][2] + 1)/len(self.display[0][0])), self.innerlinewidth, draw)
                    elif self.displaydata[it][xit][yit][0] == 2:
                        genrwall(img.size[0]*(self.displaydata[it][xit][yit][1]/len(self.display[0])), img.size[1]*(self.displaydata[it][xit][yit][2]/len(self.display[0][0])), img.size[0]*((self.displaydata[it][xit][yit][1] + 1)/len(self.display[0])), img.size[1]*((self.displaydata[it][xit][yit][2] + 1)/len(self.display[0][0])), self.innerlinewidth, draw)
                    elif self.displaydata[it][xit][yit][0] == 3:
                        genbwall(img.size[0]*(self.displaydata[it][xit][yit][1]/len(self.display[0])), img.size[1]*(self.displaydata[it][xit][yit][2]/len(self.display[0][0])), img.size[0]*((self.displaydata[it][xit][yit][1] + 1)/len(self.display[0])), img.size[1]*((self.displaydata[it][xit][yit][2] + 1)/len(self.display[0][0])), self.innerlinewidth, draw)
                    elif self.displaydata[it][xit][yit][0] == 4:
                        gentdoor(img.size[0]*(self.displaydata[it][xit][yit][1]/len(self.display[0])), img.size[1]*(self.displaydata[it][xit][yit][2]/len(self.display[0][0])), img.size[0]*((self.displaydata[it][xit][yit][1] + 1)/len(self.display[0])), img.size[1]*((self.displaydata[it][xit][yit][2] + 1)/len(self.display[0][0])), self.innerlinewidth, draw)
                    elif self.displaydata[it][xit][yit][0] == 5:
                        genldoor(img.size[0]*(self.displaydata[it][xit][yit][1]/len(self.display[0])), img.size[1]*(self.displaydata[it][xit][yit][2]/len(self.display[0][0])), img.size[0]*((self.displaydata[it][xit][yit][1] + 1)/len(self.display[0])), img.size[1]*((self.displaydata[it][xit][yit][2] + 1)/len(self.display[0][0])), self.innerlinewidth, draw)
                    elif self.displaydata[it][xit][yit][0] == 6:
                        genrdoor(img.size[0]*(self.displaydata[it][xit][yit][1]/len(self.display[0])), img.size[1]*(self.displaydata[it][xit][yit][2]/len(self.display[0][0])), img.size[0]*((self.displaydata[it][xit][yit][1] + 1)/len(self.display[0])), img.size[1]*((self.displaydata[it][xit][yit][2] + 1)/len(self.display[0][0])), self.innerlinewidth, draw)
                    elif self.displaydata[it][xit][yit][0] == 7:
                        genbdoor(img.size[0]*(self.displaydata[it][xit][yit][1]/len(self.display[0])), img.size[1]*(self.displaydata[it][xit][yit][2]/len(self.display[0][0])), img.size[0]*((self.displaydata[it][xit][yit][1] + 1)/len(self.display[0])), img.size[1]*((self.displaydata[it][xit][yit][2] + 1)/len(self.display[0][0])), self.innerlinewidth, draw)

        img.save(filename)

    def save(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save as')
        self.saveimage(path[0])
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

if path.exists('resources/blank.png') == False:
    img = Image.new('RGBA', (64, 64), color = (255, 255, 255, 255))

    img.save('resources/blank.png')

if path.exists('resources/twallt.png') == False:
    img = Image.new('RGBA', (64, 64), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    gentwall(0, 0, 64, 64, 32, draw)

    img.save('resources/twallt.png')

if path.exists('resources/lwallt.png') == False:
    img = Image.new('RGBA', (64, 64), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genlwall(0, 0, 64, 64, 32, draw)

    img.save('resources/lwallt.png')

if path.exists('resources/rwallt.png') == False:
    img = Image.new('RGBA', (64, 64), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genrwall(0, 0, 64, 64, 32, draw)

    img.save('resources/rwallt.png')

if path.exists('resources/bwallt.png') == False:
    img = Image.new('RGBA', (64, 64), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genbwall(0, 0, 64, 64, 32, draw)

    img.save('resources/bwallt.png')

if path.exists('resources/tdoort.png') == False:
    img = Image.new('RGBA', (64, 64), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    gentdoor(0, 0, 64, 64, 32, draw)

    img.save('resources/tdoort.png')

if path.exists('resources/ldoort.png') == False:
    img = Image.new('RGBA', (64, 64), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genldoor(0, 0, 64, 64, 32, draw)

    img.save('resources/ldoort.png')

if path.exists('resources/rdoort.png') == False:
    img = Image.new('RGBA', (64, 64), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genrdoor(0, 0, 64, 64, 32, draw)

    img.save('resources/rdoort.png')

if path.exists('resources/bdoort.png') == False:
    img = Image.new('RGBA', (64, 64), color = (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    genbdoor(0, 0, 64, 64, 32, draw)

    img.save('resources/bdoort.png')



if path.exists('resources/twallw.png') == False:
    img = Image.new('RGBA', (64, 64), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    gentwall(0, 0, 64, 64, 32, draw)

    img.save('resources/twallw.png')

if path.exists('resources/lwallw.png') == False:
    img = Image.new('RGBA', (64, 64), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genlwall(0, 0, 64, 64, 32, draw)

    img.save('resources/lwallw.png')

if path.exists('resources/rwallw.png') == False:
    img = Image.new('RGBA', (64, 64), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genrwall(0, 0, 64, 64, 32, draw)

    img.save('resources/rwallw.png')

if path.exists('resources/bwallw.png') == False:
    img = Image.new('RGBA', (64, 64), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genbwall(0, 0, 64, 64, 32, draw)

    img.save('resources/bwallw.png')

if path.exists('resources/tdoorw.png') == False:
    img = Image.new('RGBA', (64, 64), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    gentdoor(0, 0, 64, 64, 32, draw)

    img.save('resources/tdoorw.png')

if path.exists('resources/ldoorw.png') == False:
    img = Image.new('RGBA', (64, 64), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genldoor(0, 0, 64, 64, 32, draw)

    img.save('resources/ldoorw.png')

if path.exists('resources/rdoorw.png') == False:
    img = Image.new('RGBA', (64, 64), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genrdoor(0, 0, 64, 64, 32, draw)

    img.save('resources/rdoorw.png')

if path.exists('resources/bdoorw.png') == False:
    img = Image.new('RGBA', (64, 64), color = (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    genbdoor(0, 0, 64, 64, 32, draw)

    img.save('resources/bdoorw.png')

# img = Image.new('RGBA', (xdim, ydim), color = (255, 255, 255, 255))
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("arial.ttf", 50)
#
# gentwall(0, 0, xrooms, yrooms, img.size[0], img.size[1], innerlinewidth, draw)
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
