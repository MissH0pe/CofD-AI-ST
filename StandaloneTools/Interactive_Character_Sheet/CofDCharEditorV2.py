import sys
import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

# errors
# AGG1 couldn't add array to grid in a group because the grid doesn't have as many elements as needed to add in a group
# SI1 settings file corrupted

# LabeledTextBox array              label           box
# grid  array                       gridlayout      columnsint     nextopenslotint  rowcount

def makeScrollBar(layout, widget):
    scroll_area = QtWidgets.QScrollArea()
    scroll_area.setWidget(widget)
    scroll_area.setWidgetResizable(True)
    scroll_area.resize(16, 768)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
    scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    layout.setContentsMargins(0,0,0,0)
    layout.addWidget(scroll_area)
    return layout

class MyWidget(QtWidgets.QWidget):

    def pullData(self):
        data = {"name": self.name[1].text(), "player": self.player[1].text(), "chronicle": self.chronicle[1].text(), "concept": self.concept[1].text(), "age": self.age[1].text()}
        if self.settingsdict['isHuman'] == True:
            data["is human"] = True
            data = data | {"group name": self.groupname[1].text(), "virtue": self.virtue[1].text(), "vice": self.vice[1].text(), "faction": self.faction[1].text()}
        else:
            data["is human"] = False
        return data

    def quickSave(self):
        data = self.pullData()
        with open('backup.json', 'w') as f:
            json.dump(data, f)

    def save(self):
        data = self.pullData()
        if self.savepath == "":
            path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save as')
            self.savepath = path[0]
            with open(self.savepath, 'w') as f:
                json.dump(data, f)
        else:
            with open(self.savepath, 'w') as f:
                json.dump(data, f)

    def saveas(self):
        data = self.pullData()
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save as')
        self.savepath = path[0]
        with open(self.savepath, 'w') as f:
            json.dump(data, f)

    def open(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', '', 'Json Files (*.json)')
        self.savepath = path[0]
        if self.savepath != ('', 'json'):
            with open(self.savepath) as f:
                data = json.load(f)

                self.name[1].setText(data.get('name'))
                self.player[1].setText(data.get('player'))
                self.chronicle[1].setText(data.get('chronicle'))
                self.concept[1].setText(data.get('concept'))
                self.age[1].setText(data.get('age'))

                if data['is human'] == True:
                    if self.settingsdict['isHuman'] == False:
                        self.addHuman()
                    self.groupname[1].setText(data.get('group name'))
                    self.virtue[1].setText(data.get('virtue'))
                    self.vice[1].setText(data.get('vice'))
                    self.faction[1].setText(data.get('faction'))
                else:
                    if self.settingsdict['isHuman'] == True:
                        self.removeHuman()

    def deleteArray(self, array, grid):
        for k in range(len(array)):
            # print(array[k])
            grid[0].removeWidget(array[k])
            array[k].deleteLater()
            array[k] = None
        return None

    def makeBlankLabel(self):
        label = QtWidgets.QLabel(self)
        label.setText(" ")
        return label

    def makeLabel(self, text):
        label = QtWidgets.QLabel(self)
        label.setText(text)
        return label

    def MakeGrid(self, columns):
        return [QtWidgets.QGridLayout(), columns, 0, 0]

    def LabeledTextBox(self, labelName, charsheetbool = True): #pass charsheetbool = False when not using for charsheet
        label = self.makeLabel(labelName + ": ")
        box = QtWidgets.QLineEdit(self)
        if charsheetbool == True:
            box.textChanged.connect(self.quickSave)
        return [label, box]

    def LabeledCheckBox(self, labelName, checkdef):
        checkbox = QtWidgets.QCheckBox()
        checkbox.clicked.connect(checkdef)
        return [self.makeLabel(labelName + " "), checkbox]

    def areColumnsFull(self, grid):
        if grid[2] == grid[1]:
            grid[2] = 0
            grid[3] = grid[3] + 1
        return grid

    def forLoopWOColumnsCheck(self, element, grid):
        for k in range(len(element)):
            grid[0].addWidget(element[k], grid[3], grid[2])
            grid[2] = grid[2] + 1
        return grid

    def addElementtoGrid(self, element, grid):
        grid[0].addWidget(element, grid[3], grid[2])
        grid[2] = grid[2] + 1
        grid = self.areColumnsFull(grid)

    def addGridtoLayout(self, element, grid):
        grid[0].addLayout(element, grid[3], grid[2])
        grid[2] = grid[2] + 1
        grid = self.areColumnsFull(grid)

    def addArraystoGridGroup(self, element, grid):
        if len(element) <= grid[1]:
            if grid[2] < grid[1] - (len(element) - 1):
                grid = self.forLoopWOColumnsCheck(element, grid)
                grid = self.areColumnsFull(grid)
            else:
                grid[2] = 0
                grid[3] = grid[3] + 1
                grid = self.forLoopWOColumnsCheck(element, grid)
        else:
            print("error code: AGG1")

    def addArraystoGridIndividualGroups(self, element, grid):
        for k in range(len(element)):
            self.addArraystoGridGroup(element[k], grid)
            grid = self.areColumnsFull(grid)

    def addArraystoGridIndividual(self, element, grid):
        for k in range(len(element)):
            grid[0].addWidget(element[k], grid[3], grid[2])
            grid[2] = grid[2] + 1
            grid = self.areColumnsFull(grid)

    def positionElementsSettings(self):
        self.addArraystoGridIndividual([self.makeBlankLabel(), self.settingsTitle, self.makeBlankLabel()], self.settingsTitleLayout)
        self.addArraystoGridIndividualGroups([self.humanCheck], self.basicSettingsLayout)

    def addHuman(self):
        self.settingsdict['isHuman'] = True
        self.groupname = self.LabeledTextBox("Group Name")
        self.virtue = self.LabeledTextBox("Virtue")
        self.vice = self.LabeledTextBox("Vice")
        self.faction = self.LabeledTextBox("Faction")
        with open('settings.json', 'w') as f:
            json.dump(self.settingsdict, f)
        self.positionElements()

    def removeHuman(self):
        self.settingsdict['isHuman'] = False
        self.deleteArray(self.groupname, self.charDetailsGrid)
        self.deleteArray(self.virtue, self.charDetailsGrid)
        self.deleteArray(self.vice, self.charDetailsGrid)
        self.deleteArray(self.faction, self.charDetailsGrid)
        with open('settings.json', 'w') as f:
            json.dump(self.settingsdict, f)
        self.positionElements()

    def humanDef(self):
        if self.humanCheck[1].isChecked():
            self.humanCheck[1].setChecked(True)
            self.addHuman()
        else:
            self.humanCheck[1].setChecked(False)
            self.removeHuman()

    def basicSettings(self):
        self.basicSettingsLayout = self.MakeGrid(6)
        self.humanCheck = self.LabeledCheckBox("Is Human?", self.humanDef)
        if self.settingsdict['isHuman'] == True:
            self.humanCheck[1].setChecked(True)

    def settingsdef(self):
        self.settings = QtWidgets.QWidget()
        self.settings.setWindowTitle('Settings')
        self.settings.setGeometry(400, 150, 384, 512)
        self.settingsLayout = self.MakeGrid(1)
        self.settings.setLayout(self.settingsLayout[0])
        self.settings.show()
        self.settingsTitleLayout = self.MakeGrid(3)
        self.settingsTitle = self.makeLabel("Settings")
        self.settingsTitle.setFont(self.titlefont)

        self.basicSettings()

        self.addGridtoLayout(self.settingsTitleLayout[0], self.settingsLayout)
        self.addGridtoLayout(self.basicSettingsLayout[0], self.settingsLayout)

        self.positionElementsSettings()

    def positionElements(self):
        self.charDetailsGrid[2] = 0
        self.charDetailsGrid[3] = 0
        self.addArraystoGridIndividualGroups([self.name, self.player, self.chronicle, self.concept, self.age], self.charDetailsGrid)
        if self.settingsdict['isHuman'] == True:
            self.addArraystoGridIndividualGroups([self.groupname, self.virtue, self.vice, self.faction], self.charDetailsGrid)

    def makeMenu(self):
        saveAction = QtGui.QAction('&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save Character')
        saveAction.triggered.connect(self.save)

        saveAsAction = QtGui.QAction('&Save As', self)
        saveAsAction.setShortcut('Ctrl+Shift+S')
        saveAsAction.setStatusTip('Save Character As...')
        saveAsAction.triggered.connect(self.saveas)

        loadAction = QtGui.QAction('&Open', self)
        loadAction.setShortcut('Ctrl+O')
        loadAction.setStatusTip('Open Character')
        loadAction.triggered.connect(self.open)

        quitAction = QtGui.QAction('&Quit', self)
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Quit')
        quitAction.triggered.connect(QtWidgets.QApplication.instance().quit)

        settingsAction = QtGui.QAction('&Settings', self)
        settingsAction.setShortcut('Ctrl+I')
        settingsAction.setStatusTip('Settings')
        settingsAction.triggered.connect(self.settingsdef)

        QtWidgets.QStatusBar()

        self.menubar = QtWidgets.QMenuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(saveAction)
        self.fileMenu.addAction(saveAsAction)
        self.fileMenu.addAction(loadAction)
        self.fileMenu.addAction(quitAction)
        self.settingsMenu = self.menubar.addMenu('&Settings')
        self.settingsMenu.addAction(settingsAction)

    def charDetailsUniversal(self):
        self.charDetailsGrid = self.MakeGrid(6)

        self.name = self.LabeledTextBox("Name")
        self.player = self.LabeledTextBox("Player")
        self.chronicle = self.LabeledTextBox("Chronicle")
        self.concept = self.LabeledTextBox("Concept")
        self.age = self.LabeledTextBox("Age")

        if self.settingsdict['isHuman'] == True:
            self.groupname = self.LabeledTextBox("Group Name")
            self.virtue = self.LabeledTextBox("Virtue")
            self.vice = self.LabeledTextBox("Vice")
            self.faction = self.LabeledTextBox("Faction")

    def makeTitle(self):
        self.titleGrid = self.MakeGrid(3)
        self.title = QtWidgets.QLabel()
        pixMap = QtGui.QPixmap.fromImage('CofD.png')
        self.title.setPixmap( pixMap )
        self.title.show()

    def settingsInit(self):
        if path.exists('settings.json'):
            with open('settings.json') as f:
                self.settingsdict = json.load(f)
            if self.settingsdict['settingsVersion'] < 0:
                print("error code: SI1")
        else:
            self.settingsdict = {'settingsVersion': 0}
            self.settingsdict['isHuman'] = True
            with open('settings.json', 'w') as f:
                json.dump(self.settingsdict, f)

    def __init__(self):
        super(MyWidget, self).__init__()

        self.setGeometry(300, 75, 1024, 768)
        self.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')

        self.settingsInit()

        self.savepath = ""

        self.titlefont = QtGui.QFont()
        self.titlefont.setFamily("stcaiyun")  # Set Font
        self.titlefont.setBold(True)  # Bold
        self.titlefont.setPointSize(16)  # Set font size

        self.mainSheet = self.MakeGrid(1)
        self.setLayout(self.mainSheet[0])
        self.mainSheet[0].setContentsMargins(0,0,0,0)

        self.makeMenu()
        self.addElementtoGrid(self.menubar, self.mainSheet)
        self.makeTitle()
        self.addGridtoLayout(self.titleGrid[0], self.mainSheet)
        self.addArraystoGridIndividual([self.makeBlankLabel(), self.title, self.makeBlankLabel()], self.titleGrid)

        self.charDetailsUniversal()

        self.addGridtoLayout(self.charDetailsGrid[0], self.mainSheet)

        self.positionElements()

app = QtWidgets.QApplication([])
widget = MyWidget()
w = QtWidgets.QWidget()
w.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')

layout = QtWidgets.QGridLayout(w)
layout = makeScrollBar(layout, widget)

w.show()

sys.exit(app.exec())
