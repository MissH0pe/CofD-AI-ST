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
        self.cat1.setFont(self.titlefont)

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

        self.cat2 = QtWidgets.QLabel(self)
        self.cat2.setText("Skills")
        self.cat2.setFont(self.titlefont)
        self.subcat1 = QtWidgets.QLabel(self)
        self.subcat1.setText("Mental")
        self.subcat1.setFont(self.subtitlefont)
        self.desc1 = QtWidgets.QLabel(self)
        self.desc1.setText("(-3 unskilled)")

        self.academics = QtWidgets.QLabel(self)
        self.academics.setText("Academics: ")
        self.boxacademics = QtWidgets.QLineEdit(self)
        self.computer = QtWidgets.QLabel(self)
        self.computer.setText("Computer: ")
        self.boxcomputer = QtWidgets.QLineEdit(self)
        self.crafts = QtWidgets.QLabel(self)
        self.crafts.setText("Crafts: ")
        self.boxcrafts = QtWidgets.QLineEdit(self)
        self.investigation = QtWidgets.QLabel(self)
        self.investigation.setText("Investigation: ")
        self.boxinvestigation = QtWidgets.QLineEdit(self)
        self.medicine = QtWidgets.QLabel(self)
        self.medicine.setText("Medicine: ")
        self.boxmedicine = QtWidgets.QLineEdit(self)
        self.occult = QtWidgets.QLabel(self)
        self.occult.setText("Occult: ")
        self.boxoccult = QtWidgets.QLineEdit(self)
        self.politics = QtWidgets.QLabel(self)
        self.politics.setText("Politics: ")
        self.boxpolitics = QtWidgets.QLineEdit(self)
        self.science = QtWidgets.QLabel(self)
        self.science.setText("Science: ")
        self.boxscience = QtWidgets.QLineEdit(self)

        self.subcat2 = QtWidgets.QLabel(self)
        self.subcat2.setText("Physical")
        self.subcat2.setFont(self.subtitlefont)
        self.desc2 = QtWidgets.QLabel(self)
        self.desc2.setText("(-1 unskilled)")

        self.athletics = QtWidgets.QLabel(self)
        self.athletics.setText("Athletics: ")
        self.boxathletics = QtWidgets.QLineEdit(self)
        self.brawl = QtWidgets.QLabel(self)
        self.brawl.setText("Brawl: ")
        self.boxbrawl = QtWidgets.QLineEdit(self)
        self.drive = QtWidgets.QLabel(self)
        self.drive.setText("Drive: ")
        self.boxdrive = QtWidgets.QLineEdit(self)
        self.firearms = QtWidgets.QLabel(self)
        self.firearms.setText("Firearms: ")
        self.boxfirearms = QtWidgets.QLineEdit(self)
        self.larceny = QtWidgets.QLabel(self)
        self.larceny.setText("Larceny: ")
        self.boxlarceny = QtWidgets.QLineEdit(self)
        self.stealth = QtWidgets.QLabel(self)
        self.stealth.setText("Stealth: ")
        self.boxstealth = QtWidgets.QLineEdit(self)
        self.survival = QtWidgets.QLabel(self)
        self.survival.setText("Survival: ")
        self.boxsurvival = QtWidgets.QLineEdit(self)
        self.weaponry = QtWidgets.QLabel(self)
        self.weaponry.setText("Weaponry: ")
        self.boxweaponry = QtWidgets.QLineEdit(self)

        self.subcat3 = QtWidgets.QLabel(self)
        self.subcat3.setText("Social")
        self.subcat3.setFont(self.subtitlefont)
        self.desc3 = QtWidgets.QLabel(self)
        self.desc3.setText("(-1 unskilled)")

        self.animalken = QtWidgets.QLabel(self)
        self.animalken.setText("Athletics: ")
        self.boxanimalken = QtWidgets.QLineEdit(self)
        self.empathy = QtWidgets.QLabel(self)
        self.empathy.setText("Brawl: ")
        self.boxempathy = QtWidgets.QLineEdit(self)
        self.expression = QtWidgets.QLabel(self)
        self.expression.setText("Drive: ")
        self.boxexpression = QtWidgets.QLineEdit(self)
        self.intimidation = QtWidgets.QLabel(self)
        self.intimidation.setText("Firearms: ")
        self.boxintimidation = QtWidgets.QLineEdit(self)
        self.persuasion = QtWidgets.QLabel(self)
        self.persuasion.setText("Larceny: ")
        self.boxpersuasion = QtWidgets.QLineEdit(self)
        self.socialize = QtWidgets.QLabel(self)
        self.socialize.setText("Stealth: ")
        self.boxsocialize = QtWidgets.QLineEdit(self)
        self.streetwise = QtWidgets.QLabel(self)
        self.streetwise.setText("Survival: ")
        self.boxstreetwise = QtWidgets.QLineEdit(self)
        self.subterfuge = QtWidgets.QLabel(self)
        self.subterfuge.setText("Weaponry: ")
        self.boxsubterfuge = QtWidgets.QLineEdit(self)

        #begin layout

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

        self.layout.addWidget(self.cat2, 8 + self.oplinecounter, 1)
        self.layout.addWidget(self.subcat1, 9 + self.oplinecounter, 1)
        self.layout.addWidget(self.desc1, 10 + self.oplinecounter, 1)

        self.layout.addWidget(self.academics, 11 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxacademics, 11 + self.oplinecounter, 1)
        self.layout.addWidget(self.computer, 12 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxcomputer, 12 + self.oplinecounter, 1)
        self.layout.addWidget(self.crafts, 13 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxcrafts, 13 + self.oplinecounter, 1)
        self.layout.addWidget(self.investigation, 14 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxinvestigation, 14 + self.oplinecounter, 1)
        self.layout.addWidget(self.medicine, 15 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxmedicine, 15 + self.oplinecounter, 1)
        self.layout.addWidget(self.occult, 16 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxoccult, 16 + self.oplinecounter, 1)
        self.layout.addWidget(self.politics, 17 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxpolitics, 17 + self.oplinecounter, 1)
        self.layout.addWidget(self.science, 18 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxscience, 18 + self.oplinecounter, 1)

        self.layout.addWidget(self.subcat2, 19 + self.oplinecounter, 1)
        self.layout.addWidget(self.desc2, 20 + self.oplinecounter, 1)

        self.layout.addWidget(self.athletics, 21 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxathletics, 21 + self.oplinecounter, 1)
        self.layout.addWidget(self.brawl, 22 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxbrawl, 22 + self.oplinecounter, 1)
        self.layout.addWidget(self.drive, 23 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxdrive, 23 + self.oplinecounter, 1)
        self.layout.addWidget(self.firearms, 24 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxfirearms, 24 + self.oplinecounter, 1)
        self.layout.addWidget(self.larceny, 25 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxlarceny, 25 + self.oplinecounter, 1)
        self.layout.addWidget(self.stealth, 26 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxstealth, 26 + self.oplinecounter, 1)
        self.layout.addWidget(self.survival, 27 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxsurvival, 27 + self.oplinecounter, 1)
        self.layout.addWidget(self.weaponry, 28 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxweaponry, 28 + self.oplinecounter, 1)

        self.layout.addWidget(self.subcat3, 29 + self.oplinecounter, 1)
        self.layout.addWidget(self.desc3, 30 + self.oplinecounter, 1)

        self.layout.addWidget(self.animalken, 31 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxanimalken, 31 + self.oplinecounter, 1)
        self.layout.addWidget(self.empathy, 32 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxempathy, 32 + self.oplinecounter, 1)
        self.layout.addWidget(self.expression, 33 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxexpression, 33 + self.oplinecounter, 1)
        self.layout.addWidget(self.intimidation, 34 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxintimidation, 34 + self.oplinecounter, 1)
        self.layout.addWidget(self.persuasion, 35 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxpersuasion, 35 + self.oplinecounter, 1)
        self.layout.addWidget(self.socialize, 36 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxsocialize, 36 + self.oplinecounter, 1)
        self.layout.addWidget(self.streetwise, 37 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxstreetwise, 37 + self.oplinecounter, 1)
        self.layout.addWidget(self.subterfuge, 38 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxsubterfuge, 38 + self.oplinecounter, 1)

        self.setLayout(self.layout)
        self.setGeometry(300, 75, 1024, 768)

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

        self.settings = QtWidgets.QPushButton('')
        self.settings.setIcon(QtGui.QIcon('gear.png'))

        self.titlefont = QtGui.QFont()
        self.titlefont.setFamily("stcaiyun")  # Set Font
        self.titlefont.setBold(True)  # Bold
        # font.setItalic(True)  # tilt
        self.titlefont.setPointSize(16)  # Set font size

        self.subtitlefont = QtGui.QFont()
        self.subtitlefont.setFamily("stcaiyun")  # Set Font
        # self.subtitlefont.setBold(True)  # Bold
        # font.setItalic(True)  # tilt
        self.subtitlefont.setPointSize(12)  # Set font size


        self.save = QtWidgets.QPushButton('Save')
        self.save.clicked.connect(self.savedef)
        self.load = QtWidgets.QPushButton('Load')
        self.load.clicked.connect(self.loaddef)

        # self.title = QtWidgets.QLabel(self)
        # self.title.setText("CofD Interactive Character Sheet")
        # self.title.setFont(self.titlefont)

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

        self.layout.addWidget(self.title, 1, 2, 1, 6)
        self.layout.addWidget(self.settings, 0, 6)

        self.makesheet()

app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(1024, 768)
widget.show()

w = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(w)
scroll = QtWidgets.QScrollArea()

scroll.setWidget(widget)
scroll.setWidgetResizable(True)
scroll.resize(16, 768)
layout.addWidget(scroll)
w.show()

sys.exit(app.exec())
