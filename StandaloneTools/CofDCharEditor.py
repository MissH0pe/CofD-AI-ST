import sys
import json
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):

    def savedef(self):
        stats = {}
        stats[self.boxname.text()] = {'name': self.boxname.text(), 'player': self.boxplayer.text(), 'chronicle': self.boxchronicle.text(), 'concept': self.boxconcept.text(), 'intelligence': self.boxintelligence.text(), 'strength': self.boxstrength.text(), 'presence': self.boxpresence.text(), 'wits': self.boxwits.text(), 'dexterity': self.boxdexterity.text(), 'manipulation': self.boxmanipulation.text(), 'resolve': self.boxresolve.text(), 'stamina': self.boxstamina.text(), 'composure': self.boxcomposure.text()}
        if self.occultflag[0]:
            stats[self.boxname.text()]['mask'] = self.boxmask.text()
            stats[self.boxname.text()]['clan'] = self.boxclan.text()
            stats[self.boxname.text()]['dirge'] = self.boxdirge.text()
            stats[self.boxname.text()]['bloodline'] = self.boxbloodline.text()
            stats[self.boxname.text()]['covenant'] = self.boxcovenant.text(),

        with open(self.saveloc.text()+'.json', 'w') as f:
            json.dump(stats, f)

    def __init__(self):
        super(MyWidget, self).__init__()

        self.setGeometry(300, 75, 1024, 768)
        self.setWindowTitle('Chronicles of Darkness Character Editor')

        oplinecounter = 0
        self.occultflag = [True, False, False]

        self.save = QtWidgets.QPushButton('Save')
        self.save.clicked.connect(self.savedef)

        self.title = QtWidgets.QLabel(self)
        self.title.setText("CofD Interactive Character Sheet")

        self.name = QtWidgets.QLabel(self)
        self.name.setText("Name: ")
        self.boxname = QtWidgets.QLineEdit(self)
        self.player = QtWidgets.QLabel(self)
        self.player.setText("Player: ")
        self.boxplayer = QtWidgets.QLineEdit(self)
        self.chronicle = QtWidgets.QLabel(self)
        self.chronicle.setText("Chronicle: ")
        self.boxchronicle = QtWidgets.QLineEdit(self)

        self.concept = QtWidgets.QLabel(self)
        self.boxconcept = QtWidgets.QLineEdit(self)
        self.concept.setText("Concept: ")

        if self.occultflag[0]:
            self.clan = QtWidgets.QLabel(self)
            self.clan.setText("Clan: ")
            self.boxclan = QtWidgets.QLineEdit(self)
            self.bloodline = QtWidgets.QLabel(self)
            self.bloodline.setText("Bloodline: ")
            self.boxbloodline = QtWidgets.QLineEdit(self)
            self.covenant = QtWidgets.QLabel(self)
            self.covenant.setText("Covenant: ")
            self.boxcovenant = QtWidgets.QLineEdit(self)

            self.mask = QtWidgets.QLabel(self)
            self.mask.setText("Mask: ")
            self.boxmask = QtWidgets.QLineEdit(self)
            self.dirge = QtWidgets.QLabel(self)
            self.dirge.setText("Dirge: ")
            self.boxdirge = QtWidgets.QLineEdit(self)

        self.cat1 = QtWidgets.QLabel(self)
        self.cat1.setText("Attributes")

        self.intelligence = QtWidgets.QLabel(self)
        self.strength = QtWidgets.QLabel(self)
        self.presence = QtWidgets.QLabel(self)
        self.intelligence.setText("Intelligence: ")
        self.strength.setText("Strength: ")
        self.presence.setText("Presence: ")
        self.boxintelligence = QtWidgets.QLineEdit(self)
        self.boxstrength = QtWidgets.QLineEdit(self)
        self.boxpresence = QtWidgets.QLineEdit(self)
        self.wits = QtWidgets.QLabel(self)
        self.dexterity = QtWidgets.QLabel(self)
        self.manipulation = QtWidgets.QLabel(self)
        self.wits.setText("Wits: ")
        self.dexterity.setText("Dexterity: ")
        self.manipulation.setText("Manipulation: ")
        self.boxwits = QtWidgets.QLineEdit(self)
        self.boxdexterity = QtWidgets.QLineEdit(self)
        self.boxmanipulation = QtWidgets.QLineEdit(self)
        self.resolve = QtWidgets.QLabel(self)
        self.stamina = QtWidgets.QLabel(self)
        self.composure = QtWidgets.QLabel(self)
        self.resolve.setText("Resolve: ")
        self.stamina.setText("Stamina: ")
        self.composure.setText("Composure: ")
        self.boxresolve = QtWidgets.QLineEdit(self)
        self.boxstamina = QtWidgets.QLineEdit(self)
        self.boxcomposure = QtWidgets.QLineEdit(self)

        self.saveloclabel = QtWidgets.QLabel(self)
        self.saveloclabel.setText("Save Location: ")
        self.saveloc = QtWidgets.QLineEdit(self)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.save, 0, 0)
        self.layout.addWidget(self.saveloclabel, 0, 1)
        self.layout.addWidget(self.saveloc, 0, 2)

        self.layout.addWidget(self.title, 1, 3)

        self.layout.addWidget(self.name, 2, 0)
        self.layout.addWidget(self.boxname, 2, 1)
        self.layout.addWidget(self.player, 2, 2)
        self.layout.addWidget(self.boxplayer, 2, 3)
        self.layout.addWidget(self.chronicle, 2, 4)
        self.layout.addWidget(self.boxchronicle, 2, 5)

        self.layout.addWidget(self.concept, 3, 0)
        self.layout.addWidget(self.boxconcept, 3, 1)

        if self.occultflag[0]:
            oplinecounter += 1
            self.layout.addWidget(self.clan, 3 + oplinecounter, 0)
            self.layout.addWidget(self.boxclan, 3 + oplinecounter, 1)
            self.layout.addWidget(self.bloodline, 3 + oplinecounter, 2)
            self.layout.addWidget(self.boxbloodline, 3 + oplinecounter, 3)
            self.layout.addWidget(self.covenant, 3 + oplinecounter, 4)
            self.layout.addWidget(self.boxcovenant, 3 + oplinecounter, 5)

            oplinecounter += 1
            self.layout.addWidget(self.mask, 3 + oplinecounter, 0)
            self.layout.addWidget(self.boxmask, 3 + oplinecounter, 1)
            self.layout.addWidget(self.dirge, 3 + oplinecounter, 2)
            self.layout.addWidget(self.boxdirge, 3 + oplinecounter, 3)

        self.layout.addWidget(self.cat1, 4 + oplinecounter, 3)

        self.layout.addWidget(self.intelligence, 5 + oplinecounter, 0)
        self.layout.addWidget(self.boxintelligence, 5 + oplinecounter, 1)
        self.layout.addWidget(self.strength, 5 + oplinecounter, 2)
        self.layout.addWidget(self.boxstrength, 5 + oplinecounter, 3)
        self.layout.addWidget(self.presence, 5 + oplinecounter, 4)
        self.layout.addWidget(self.boxpresence, 5 + oplinecounter, 5)
        self.layout.addWidget(self.wits, 6 + oplinecounter, 0)
        self.layout.addWidget(self.boxwits, 6 + oplinecounter, 1)
        self.layout.addWidget(self.dexterity, 6 + oplinecounter, 2)
        self.layout.addWidget(self.boxdexterity, 6 + oplinecounter, 3)
        self.layout.addWidget(self.manipulation, 6 + oplinecounter, 4)
        self.layout.addWidget(self.boxmanipulation, 6 + oplinecounter, 5)
        self.layout.addWidget(self.resolve, 7 + oplinecounter, 0)
        self.layout.addWidget(self.boxresolve, 7 + oplinecounter, 1)
        self.layout.addWidget(self.stamina, 7 + oplinecounter, 2)
        self.layout.addWidget(self.boxstamina, 7 + oplinecounter, 3)
        self.layout.addWidget(self.composure, 7 + oplinecounter, 4)
        self.layout.addWidget(self.boxcomposure, 7 + oplinecounter, 5)

        self.setLayout(self.layout)

app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(1024, 768)
widget.show()

sys.exit(app.exec())
