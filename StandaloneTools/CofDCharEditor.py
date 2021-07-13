import sys
import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):

#if importing this charater to a table i need to make sure that it's added under a in that is the name with the space

    def savedef(self):
        stats = {'name': self.boxname.text(), 'supernaturaltags': [], 'player': self.boxplayer.text(), 'chronicle': self.boxchronicle.text(), 'concept': self.boxconcept.text(), 'intelligence': self.boxintelligence.text(), 'strength': self.boxstrength.text(), 'presence': self.boxpresence.text(), 'wits': self.boxwits.text(), 'dexterity': self.boxdexterity.text(), 'manipulation': self.boxmanipulation.text(), 'resolve': self.boxresolve.text(), 'stamina': self.boxstamina.text(), 'composure': self.boxcomposure.text()}
        if self.occultflag[0]:
            stats['supernaturaltags'].append('vampire')
            stats['mask'] = self.boxmask.text()
            stats['dirge'] = self.boxdirge.text()
            stats['clan'] = self.boxclan.text()
            stats['bloodline'] = self.boxbloodline.text()
            stats['covenant'] = self.boxcovenant.text()

        with open(self.saveloc.text()+'.json', 'w') as f:
            json.dump(stats, f)

    def loaddef(self):
        if path.exists(self.loadloc.text()+'.json'):
            with open(self.loadloc.text()+'.json') as f:
                stats = json.load(f)
                self.boxname.setText(stats['name'])
                self.boxplayer.setText(stats['player'])
                self.boxchronicle.setText(stats['chronicle'])
                self.boxconcept.setText(stats['concept'])
                self.boxintelligence.setText(stats['intelligence'])
                self.boxstrength.setText(stats['strength'])
                self.boxpresence.setText(stats['presence'])
                self.boxwits.setText(stats['wits'])
                self.boxdexterity.setText(stats['dexterity'])
                self.boxmanipulation.setText(stats['manipulation'])
                self.boxresolve.setText(stats['resolve'])
                self.boxstamina.setText(stats['stamina'])
                self.boxcomposure.setText(stats['composure'])
                self.occultflag = [False, False, False]
                if stats['supernaturaltags'][0]:
                    self.boxclan.setText(stats['clan'])
                    self.boxbloodline.setText(stats['bloodline'])
                    self.boxcovenant.setText(stats['covenant'])
                    self.boxmask.setText(stats['mask'])
                    self.boxdirge.setText(stats['dirge'])
                    self.occultflag[0] = True
        else:
            stats = {}

        # stats = {}
        # stats[] = {'name': self.boxname.text(), 'player': self.boxplayer.text(), 'chronicle': self.boxchronicle.text(), 'concept': self.boxconcept.text(), 'intelligence': self.boxintelligence.text(), 'strength': self.boxstrength.text(), 'presence': self.boxpresence.text(), 'wits': self.boxwits.text(), 'dexterity': self.boxdexterity.text(), 'manipulation': self.boxmanipulation.text(), 'resolve': self.boxresolve.text(), 'stamina': self.boxstamina.text(), 'composure': self.boxcomposure.text()}
        # if self.occultflag[0]:
        #     stats[self.boxname.text()]['mask'] = self.boxmask.text()
        #     stats[self.boxname.text()]['clan'] = self.boxclan.text()
        #     stats[self.boxname.text()]['dirge'] = self.boxdirge.text()
        #     stats[self.boxname.text()]['bloodline'] = self.boxbloodline.text()
        #     stats[self.boxname.text()]['covenant'] = self.boxcovenant.text(),


    def makesheet(self):
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
        self.intelligence.setText("Intelligence: ")
        self.boxintelligence = QtWidgets.QLineEdit(self)
        self.strength = QtWidgets.QLabel(self)
        self.strength.setText("Strength: ")
        self.boxstrength = QtWidgets.QLineEdit(self)
        self.presence = QtWidgets.QLabel(self)
        self.presence.setText("Presence: ")
        self.boxpresence = QtWidgets.QLineEdit(self)
        self.wits = QtWidgets.QLabel(self)
        self.wits.setText("Wits: ")
        self.dexterity = QtWidgets.QLabel(self)
        self.boxwits = QtWidgets.QLineEdit(self)
        self.dexterity.setText("Dexterity: ")
        self.boxdexterity = QtWidgets.QLineEdit(self)
        self.manipulation = QtWidgets.QLabel(self)
        self.manipulation.setText("Manipulation: ")
        self.boxmanipulation = QtWidgets.QLineEdit(self)
        self.resolve = QtWidgets.QLabel(self)
        self.resolve.setText("Resolve: ")
        self.boxresolve = QtWidgets.QLineEdit(self)
        self.stamina = QtWidgets.QLabel(self)
        self.stamina.setText("Stamina: ")
        self.boxstamina = QtWidgets.QLineEdit(self)
        self.composure = QtWidgets.QLabel(self)
        self.composure.setText("Composure: ")
        self.boxcomposure = QtWidgets.QLineEdit(self)

        #begin layout.layout2

        self.layout.addWidget(self.name, 2, 0)
        self.layout.addWidget(self.boxname, 2, 1)
        self.layout.addWidget(self.player, 2, 2)
        self.layout.addWidget(self.boxplayer, 2, 3)
        self.layout.addWidget(self.chronicle, 2, 4)
        self.layout.addWidget(self.boxchronicle, 2, 5)

        self.layout.addWidget(self.concept, 3, 0)
        self.layout.addWidget(self.boxconcept, 3, 1)

        if self.occultflag[0]:
            self.oplinecounter += 1
            self.layout.addWidget(self.clan, 3 + self.oplinecounter, 0)
            self.layout.addWidget(self.boxclan, 3 + self.oplinecounter, 1)
            self.layout.addWidget(self.bloodline, 3 + self.oplinecounter, 2)
            self.layout.addWidget(self.boxbloodline, 3 + self.oplinecounter, 3)
            self.layout.addWidget(self.covenant, 3 + self.oplinecounter, 4)
            self.layout.addWidget(self.boxcovenant, 3 + self.oplinecounter, 5)

            self.oplinecounter += 1
            self.layout.addWidget(self.mask, 3 + self.oplinecounter, 0)
            self.layout.addWidget(self.boxmask, 3 + self.oplinecounter, 1)
            self.layout.addWidget(self.dirge, 3 + self.oplinecounter, 2)
            self.layout.addWidget(self.boxdirge, 3 + self.oplinecounter, 3)

        self.layout.addWidget(self.cat1, 4 + self.oplinecounter, 3)

        self.layout.addWidget(self.intelligence, 5 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxintelligence, 5 + self.oplinecounter, 1)
        self.layout.addWidget(self.strength, 5 + self.oplinecounter, 2)
        self.layout.addWidget(self.boxstrength, 5 + self.oplinecounter, 3)
        self.layout.addWidget(self.presence, 5 + self.oplinecounter, 4)
        self.layout.addWidget(self.boxpresence, 5 + self.oplinecounter, 5)
        self.layout.addWidget(self.wits, 6 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxwits, 6 + self.oplinecounter, 1)
        self.layout.addWidget(self.dexterity, 6 + self.oplinecounter, 2)
        self.layout.addWidget(self.boxdexterity, 6 + self.oplinecounter, 3)
        self.layout.addWidget(self.manipulation, 6 + self.oplinecounter, 4)
        self.layout.addWidget(self.boxmanipulation, 6 + self.oplinecounter, 5)
        self.layout.addWidget(self.resolve, 7 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxresolve, 7 + self.oplinecounter, 1)
        self.layout.addWidget(self.stamina, 7 + self.oplinecounter, 2)
        self.layout.addWidget(self.boxstamina, 7 + self.oplinecounter, 3)
        self.layout.addWidget(self.composure, 7 + self.oplinecounter, 4)
        self.layout.addWidget(self.boxcomposure, 7 + self.oplinecounter, 5)

        self.setLayout(self.layout)

    def __init__(self):
        super(MyWidget, self).__init__()

        self.setGeometry(300, 75, 1024, 768)
        self.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')

        self.oplinecounter = 0

        self.occultflag = [True, False, False]

        self.title = QtWidgets.QLabel()

        pixMap = QtGui.QPixmap.fromImage('CofD.png')

        self.title.setPixmap( pixMap )
        self.title.show()

        self.titlefont = QtGui.QFont()
        self.titlefont.setFamily("stcaiyun")  # Set Font
        self.titlefont.setBold(True)  # Bold
        # font.setItalic(True)  # tilt
        self.titlefont.setPointSize(32)  # Set font size


        self.save = QtWidgets.QPushButton('Save')
        self.save.clicked.connect(self.savedef)
        self.load = QtWidgets.QPushButton('Load')
        self.load.clicked.connect(self.loaddef)

        # self.title = QtWidgets.QLabel(self)
        # self.title.setText("CofD Interactive Character Sheet")
        # self.title.setFont(self.titlefont)

        # self.cat2 = QtWidgets.QLabel(self)
        # self.cat2.setText("Skills")
        # self.subcat1 = QtWidgets.QLabel(self)
        # self.subcat1.setText("Mental")
        # self.desc1 = QtWidgets.QLabel(self)
        # self.desc1.setText("(-3 unskilled)")
        #
        # self.academics = QtWidgets.QLabel(self)
        # self.academics.setText("Intelligence: ")
        # self.boxacademics = QtWidgets.QLineEdit(self)
        # self.computer = QtWidgets.QLabel(self)
        # self.computer.setText("Strength: ")
        # self.boxcomputer = QtWidgets.QLineEdit(self)
        # self.crafts = QtWidgets.QLabel(self)
        # self.crafts.setText("Presence: ")
        # self.boxcrafts = QtWidgets.QLineEdit(self)
        # self.investigation = QtWidgets.QLabel(self)
        # self.investigation.setText("Wits: ")
        # self.boxinvestigation = QtWidgets.QLineEdit(self)
        # self.medicine = QtWidgets.QLabel(self)
        # self.medicine.setText("Dexterity: ")
        # self.boxmedicine = QtWidgets.QLineEdit(self)
        # self.occult = QtWidgets.QLabel(self)
        # self.occult.setText("Manipulation: ")
        # self.boxoccult = QtWidgets.QLineEdit(self)
        # self.resolve = QtWidgets.QLabel(self)
        # self.resolve.setText("Resolve: ")
        # self.boxresolve = QtWidgets.QLineEdit(self)
        # self.stamina = QtWidgets.QLabel(self)
        # self.stamina.setText("Stamina: ")
        # self.boxstamina = QtWidgets.QLineEdit(self)
        # self.composure = QtWidgets.QLabel(self)
        # self.composure.setText("Composure: ")
        # self.boxcomposure = QtWidgets.QLineEdit(self)

        self.saveloclabel = QtWidgets.QLabel(self)
        self.saveloclabel.setText("Save Location: ")
        self.saveloc = QtWidgets.QLineEdit(self)
        self.loadloclabel = QtWidgets.QLabel(self)
        self.loadloclabel.setText("Load Location: ")
        self.loadloc = QtWidgets.QLineEdit(self)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.saveloclabel, 0, 0)
        self.layout.addWidget(self.saveloc, 0, 1)
        self.layout.addWidget(self.save, 0, 2)
        self.layout.addWidget(self.load, 0, 3)
        self.layout.addWidget(self.loadloclabel, 0, 4)
        self.layout.addWidget(self.loadloc, 0, 5)


        self.layout.addWidget(self.title, 1, 0, 1, 5)

        self.makesheet()

app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(1024, 768)
widget.show()

sys.exit(app.exec())
