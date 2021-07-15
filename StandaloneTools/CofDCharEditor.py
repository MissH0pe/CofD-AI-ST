import sys
import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):

#if importing this character to a table i need to make sure that it's added under a in that is the name with the space

    def savesettings(self):
        with open('settings.txt', 'w') as f:
            f.write(str(self.meritcount)+'# Merit Slots Displayed Count\n')
            f.write(str(self.aspirationcount)+'# Aspiration Slots Displayed Count\n')
            f.write(str(self.conditioncount)+'# Condition Slots Displayed Count\n')
            f.write(str(self.banecount)+'# Bane Slots Displayed Count\n')
            if self.occultflag[0]:
                f.write(str(self.disciplinecount)+'# Discipline Slots Displayed Count\n')
            # print(self.vvflag)
            if self.vvflag:
                f.write('True# Has a Vice and Virtue\n')
            else:
                f.write('False# Has a Vice and Virtue\n')

            if self.occultflag[0]:
                f.write('True# Is Vampire\n')
            else:
                f.write('False# Is Vampire\n')

    def savedef(self):
        if path.exists(self.saveloc.text()+'.json'):
            with open(self.saveloc.text()+'.json') as f:
                backup = json.load(f)
            with open(self.saveloc.text()+'backup.json', 'w') as f:
                json.dump(backup, f)

        stats = {'name': self.boxname.text(), 'supernaturaltags': [], 'player': self.boxplayer.text(), 'chronicle': self.boxchronicle.text(), 'concept': self.boxconcept.text(), 'stats': {'intelligence': self.boxintelligence.text(), 'strength': self.boxstrength.text(), 'presence': self.boxpresence.text(), 'wits': self.boxwits.text(), 'dexterity': self.boxdexterity.text(), 'manipulation': self.boxmanipulation.text(), 'resolve': self.boxresolve.text(), 'stamina': self.boxstamina.text(), 'composure': self.boxcomposure.text()}, 'skills': {'academics': self.boxacademics.text(), 'computer': self.boxcomputer.text(), 'crafts': self.boxcrafts.text(), 'investigation': self.boxinvestigation.text(), 'medicine': self.boxmedicine.text(), 'occult': self.boxoccult.text(), 'politics': self.boxpolitics.text(), 'science': self.boxscience.text(), 'athletics': self.boxathletics.text(), 'brawl': self.boxbrawl.text(), 'drive': self.boxdrive.text(), 'firearms': self.boxfirearms.text(), 'larceny': self.boxlarceny.text(), 'stealth': self.boxstealth.text(), 'survival': self.boxsurvival.text(), 'weaponry': self.boxweaponry.text(), 'animalken': self.boxanimalken.text(), 'empathy': self.boxempathy.text(), 'expression': self.boxexpression.text(), 'intimidation': self.boxintimidation.text(), 'persuasion': self.boxpersuasion.text(), 'socialize': self.boxsocialize.text(), 'streetwise': self.boxstreetwise.text(), 'subterfuge': self.boxsubterfuge.text()}}

        if self.vvflag == True:
            stats['supernaturaltags'].append('human')
            stats['vice'] = self.boxvice.text()
            stats['virtue'] = self.boxvirtue.text()

        if self.occultflag[0] == True:
            stats['supernaturaltags'].append('vampire')
            stats['mask'] = self.boxmask.text()
            stats['dirge'] = self.boxdirge.text()
            stats['clan'] = self.boxclan.text()
            stats['bloodline'] = self.boxbloodline.text()
            stats['covenant'] = self.boxcovenant.text()
        self.filledmerits = 0
        stats['merits'] = []
        stats['merits'].append(['filledmerits', 0])
        for x in range(self.meritcount):
            if self.meritcount >= x and self.meritnamebox[x].text() != "" and self.meritlevelbox[x].text() != "":
                stats['merits'].append([self.meritnamebox[x].text(), self.meritlevelbox[x].text()])
                self.filledmerits += 1
        stats['merits'][0] = ['filledmerits', self.filledmerits]

        self.filledaspirations = 0
        stats['aspirations'] = []
        stats['aspirations'].append(['filledaspirations', 0])                                      #remove the != part and condition num from 1
        self.filledconditions = 0
        stats['conditions'] = []
        stats['conditions'].append(['filledconditions', 0])
        self.filledbanes = 0
        stats['banes'] = []
        stats['banes'].append(['filledbanes', 0])
        for x in range(self.aspirationcount):
            if self.aspirationcount >= x and self.aspirationnamebox[x].text() != "":
                stats['aspirations'].append([self.aspirationnamebox[x].text()])
                self.filledaspirations += 1
        for x in range(self.conditioncount):
            if self.conditioncount >= x and self.conditionnamebox[x].text() != "":
                stats['conditions'].append([self.conditionnamebox[x].text()])
                self.filledconditions += 1
        for x in range(self.banecount):
            if self.banecount >= x and self.banenamebox[x].text() != "":
                stats['banes'].append([self.banenamebox[x].text()])
                self.filledbanes += 1
        stats['aspirations'][0] = ['filledaspirations', self.filledaspirations]
        stats['conditions'][0] = ['filledconditions', self.filledconditions]
        stats['banes'][0] = ['filledbanes', self.filledbanes]

        if self.occultflag[0]:
            self.filleddisciplines = 0
            stats['disciplines'] = []
            stats['disciplines'].append(['filleddisciplines', 0])
            for x in range(self.disciplinecount):
                if self.disciplinecount >= x and self.disciplinenamebox[x].text() != "" and self.disciplinelevelbox[x].text() != "":
                    stats['disciplines'].append([self.disciplinenamebox[x].text(), self.disciplinelevelbox[x].text()])
                    self.filleddisciplines += 1
            stats['disciplines'][0] = ['filleddisciplines', self.filleddisciplines]

        stats['size'] = 5 + self.sizebonus

        stats['speed'] = int(self.sizeval.text()) + self.strengthstat + self.dexteritystat + self.speedbonus

        if self.dexteritystat <= self.witsstat:
            stats['defense'] = self.athleticsskill + self.dexteritystat + self.defensebonus
        else:
            stats['defense'] = self.athleticsskill + self.witsstat + self.defensebonus

        stats['armor'] = self.armorbonus

        stats['initiative'] = self.composurestat + self.dexteritystat + self.initiativebonus

        with open(self.saveloc.text()+'.json', 'w') as f:
            json.dump(stats, f)

        self.savesettings()

    def loaddef(self):
        if path.exists(self.loadloc.text()+'.json'):
            with open(self.loadloc.text()+'.json') as f:
                stats = json.load(f)
                self.boxname.setText(stats['name'])
                self.boxplayer.setText(stats['player'])
                self.boxchronicle.setText(stats['chronicle'])
                self.boxconcept.setText(stats['concept'])
                self.boxintelligence.setText(stats['stats']['intelligence'])
                self.boxstrength.setText(stats['stats']['strength'])
                self.boxpresence.setText(stats['stats']['presence'])
                self.boxwits.setText(stats['stats']['wits'])
                self.boxdexterity.setText(stats['stats']['dexterity'])
                self.boxmanipulation.setText(stats['stats']['manipulation'])
                self.boxresolve.setText(stats['stats']['resolve'])
                self.boxstamina.setText(stats['stats']['stamina'])
                self.boxcomposure.setText(stats['stats']['composure'])
                self.boxacademics.setText(stats['skills']['academics'])
                self.boxcomputer.setText(stats['skills']['computer'])
                self.boxcrafts.setText(stats['skills']['crafts'])
                self.boxinvestigation.setText(stats['skills']['investigation'])
                self.boxmedicine.setText(stats['skills']['medicine'])
                self.boxoccult.setText(stats['skills']['occult'])
                self.boxpolitics.setText(stats['skills']['politics'])
                self.boxscience.setText(stats['skills']['science'])
                self.boxathletics.setText(stats['skills']['athletics'])
                self.boxbrawl.setText(stats['skills']['brawl'])
                self.boxdrive.setText(stats['skills']['drive'])
                self.boxfirearms.setText(stats['skills']['firearms'])
                self.boxlarceny.setText(stats['skills']['larceny'])
                self.boxstealth.setText(stats['skills']['stealth'])
                self.boxsurvival.setText(stats['skills']['survival'])
                self.boxweaponry.setText(stats['skills']['weaponry'])
                self.boxanimalken.setText(stats['skills']['animalken'])
                self.boxempathy.setText(stats['skills']['empathy'])
                self.boxexpression.setText(stats['skills']['expression'])
                self.boxintimidation.setText(stats['skills']['intimidation'])
                self.boxpersuasion.setText(stats['skills']['persuasion'])
                self.boxsocialize.setText(stats['skills']['socialize'])
                self.boxstreetwise.setText(stats['skills']['streetwise'])
                self.boxsubterfuge.setText(stats['skills']['subterfuge'])
                # self.occultflag = [False, False, False]

                if stats['merits'][0][1] > self.meritcount:
                    self.oldmeritcount = self.meritcount
                    self.meritcount = stats['merits'][0][1]

                    self.makesheet()
                # print(stats['merits'][0][1])
                for x in range(stats['merits'][0][1]):
                    if stats['merits'][0][1] >= x:
                        self.meritnamebox[x].setText(stats['merits'][x+1][0])
                        self.meritlevelbox[x].setText(stats['merits'][x+1][1])

                if stats['aspirations'][0][1] > self.aspirationcount:
                    self.oldaspirationcount = self.aspirationcount
                    self.aspirationcount = stats['aspirations'][0][1]

                    self.makesheet()

                if stats['conditions'][0][1] > self.conditioncount:
                    self.oldconditioncount = self.conditioncount
                    self.conditioncount = stats['conditions'][0][1]

                    self.makesheet()

                if stats['banes'][0][1] > self.banecount:
                    self.oldbanecount = self.banecount
                    self.banecount = stats['banes'][0][1]

                    self.makesheet()

                for x in range(stats['aspirations'][0][1]):
                    if stats['aspirations'][0][1] >= x:
                        self.aspirationnamebox[x].setText(stats['aspirations'][x+1][0])
                for x in range(stats['conditions'][0][1]):
                    if stats['conditions'][0][1] >= x:
                        self.conditionnamebox[x].setText(stats['conditions'][x+1][0])
                for x in range(stats['banes'][0][1]):
                    if stats['banes'][0][1] >= x:
                        self.banenamebox[x].setText(stats['banes'][x+1][0])

                self.sizeval.setText(str(stats['size']))
                self.sizebonus = stats['size'] - 5

                self.speedval.setText(str(stats['speed']))
                self.speedbonus = stats['speed'] - int(self.sizeval.text()) - self.strengthstat - self.dexteritystat

                if self.dexteritystat <= self.witsstat:
                    self.defenseval.setText(str(stats['defense']))
                    self.defensebonus = stats['defense'] - self.athleticsskill - self.dexteritystat
                else:
                    self.defenseval.setText(str(stats['defense']))
                    self.defensebonus = stats['defense'] - self.athleticsskill - self.witsstat

                self.armorval.setText(str(stats['armor']))
                self.armorbonus = stats['armor']

                self.initiativeval.setText(str(stats['initiative']))
                self.initiativebonus = stats['initiative'] - self.composurestat - self.dexteritystat

                for x in stats['supernaturaltags']:
                    if x == 'human':
                        self.boxvice.setText(stats['vice'])
                        self.boxvirtue.setText(stats['virtue'])
                    if x == 'vampire':
                        self.boxclan.setText(stats['clan'])
                        self.boxbloodline.setText(stats['bloodline'])
                        self.boxcovenant.setText(stats['covenant'])
                        self.boxmask.setText(stats['mask'])
                        self.boxdirge.setText(stats['dirge'])
                        self.occultflag[0] = True
                        if stats['disciplines'][0][1] > self.disciplinecount:
                            self.olddisciplinecount = self.disciplinecount
                            self.disciplinecount = stats['disciplines'][0][1]

                            self.makesheet()

                        for x in range(stats['disciplines'][0][1]):
                            if stats['disciplines'][0][1] >= x:
                                self.disciplinenamebox[x].setText(stats['disciplines'][x+1][0])
                                self.disciplinelevelbox[x].setText(stats['disciplines'][x+1][1])

                self.savesettings()
        else:
            stats = {}

    def updatestatsdef(self):
        self.intelligencestat = int(self.boxintelligence.text())
        self.witsstat = int(self.boxwits.text())
        self.resolvestat = int(self.boxresolve.text())
        self.strengthstat = int(self.boxstrength.text())
        self.dexteritystat = int(self.boxdexterity.text())
        self.staminastat = int(self.boxstamina.text())
        self.presencestat = int(self.boxpresence.text())
        self.manipulationstat = int(self.boxmanipulation.text())
        self.composurestat = int(self.boxcomposure.text())
        self.athleticsskill = int(self.boxathletics.text())


        self.layout.removeWidget(self.sizeval)
        self.sizeval.deleteLater()
        self.sizeval = None
        self.layout.removeWidget(self.speedval)
        self.speedval.deleteLater()
        self.speedval = None
        self.layout.removeWidget(self.defenseval)
        self.defenseval.deleteLater()
        self.defenseval = None
        self.layout.removeWidget(self.armorval)
        self.armorval.deleteLater()
        self.armorval = None
        self.layout.removeWidget(self.initiativeval)
        self.initiativeval.deleteLater()
        self.initiativeval = None


        self.sizeval = QtWidgets.QLabel(self)
        self.sizeval.setText(str(5 + self.sizebonus))
        self.speedval = QtWidgets.QLabel(self)
        self.speedval.setText(str(int(self.sizeval.text()) + self.strengthstat + self.dexteritystat + self.speedbonus))
        self.defenseval = QtWidgets.QLabel(self)
        if self.dexteritystat <= self.witsstat:
            self.defenseval.setText(str(self.athleticsskill + self.dexteritystat + self.defensebonus))
        else:
            self.defenseval.setText(str(self.athleticsskill + self.witsstat + self.defensebonus))
        self.armorval = QtWidgets.QLabel(self)
        self.armorval.setText(str(self.armorbonus))
        self.initiativeval = QtWidgets.QLabel(self)
        self.initiativeval.setText(str(self.composurestat + self.dexteritystat + self.initiativebonus))

        self.layout.addWidget(self.sizeval, 9 + self.oplinecounter, 5)
        self.layout.addWidget(self.speedval, 11 + self.oplinecounter, 5)
        self.layout.addWidget(self.defenseval, 13 + self.oplinecounter, 5)
        self.layout.addWidget(self.armorval, 15 + self.oplinecounter, 5)
        self.layout.addWidget(self.initiativeval, 17 + self.oplinecounter, 5)

    def makesheet(self):
        #make here delete all stuff in here if not in first run
        if self.makesheetflag:
            self.layout.removeWidget(self.cat3)
            self.cat3.deleteLater()
            self.cat3 = None
            self.layout.removeWidget(self.merits)
            self.merits.deleteLater()
            self.merits = None
            self.layout.removeWidget(self.meritslevel)
            self.meritslevel.deleteLater()
            self.meritslevel = None

            self.meritcounter = 0
            for x in range(self.oldmeritcount):
                if self.oldmeritcount >= x + 1:
                    self.layout.removeWidget(self.meritnamebox[x])
                    self.meritnamebox[x].deleteLater()
                    self.meritnamebox[x] = None
                    self.layout.removeWidget(self.meritlevelbox[x])
                    self.meritlevelbox[x].deleteLater()
                    self.meritlevelbox[x] = None

            self.layout.removeWidget(self.aspirations)
            self.aspirations.deleteLater()
            self.aspirations = None
            self.layout.removeWidget(self.conditions)
            self.conditions.deleteLater()
            self.conditions = None

            self.aspirationcounter = 0
            for x in range(self.oldaspirationcount):
                if self.oldaspirationcount >= x + 1:
                    self.layout.removeWidget(self.aspirationnamebox[x])
                    self.aspirationnamebox[x].deleteLater()
                    self.aspirationnamebox[x] = None
            self.conditioncounter = 0
            for x in range(self.oldconditioncount):
                if self.oldconditioncount >= x + 1:
                    self.layout.removeWidget(self.conditionnamebox[x])
                    self.conditionnamebox[x].deleteLater()
                    self.conditionnamebox[x] = None
            self.banecounter = 0
            for x in range(self.oldbanecount):
                if self.oldbanecount >= x + 1:
                    self.layout.removeWidget(self.banenamebox[x])
                    self.banenamebox[x].deleteLater()
                    self.banenamebox[x] = None

            self.layout.removeWidget(self.updatestats)
            self.updatestats.deleteLater()
            self.updatestats = None

            self.layout.removeWidget(self.size)
            self.size.deleteLater()
            self.size = None
            self.layout.removeWidget(self.sizeval)
            self.sizeval.deleteLater()
            self.sizeval = None
            self.layout.removeWidget(self.sizebonuslabel)
            self.sizebonuslabel.deleteLater()
            self.sizebonuslabel = None
            self.layout.removeWidget(self.sizebonusbox)
            self.sizebonusbox.deleteLater()
            self.sizebonusbox = None

            self.layout.removeWidget(self.speed)
            self.speed.deleteLater()
            self.speed = None
            self.layout.removeWidget(self.speedval)
            self.speedval.deleteLater()
            self.speedval = None
            self.layout.removeWidget(self.speedbonuslabel)
            self.speedbonuslabel.deleteLater()
            self.speedbonuslabel = None
            self.layout.removeWidget(self.speedbonusbox)
            self.speedbonusbox.deleteLater()
            self.speedbonusbox = None

            self.layout.removeWidget(self.defense)
            self.defense.deleteLater()
            self.defense = None
            self.layout.removeWidget(self.defenseval)
            self.defenseval.deleteLater()
            self.defenseval = None
            self.layout.removeWidget(self.defensebonuslabel)
            self.defensebonuslabel.deleteLater()
            self.defensebonuslabel = None
            self.layout.removeWidget(self.defensebonusbox)
            self.defensebonusbox.deleteLater()
            self.defensebonusbox = None

            self.layout.removeWidget(self.armor)
            self.armor.deleteLater()
            self.armor = None
            self.layout.removeWidget(self.armorval)
            self.armorval.deleteLater()
            self.armorval = None
            self.layout.removeWidget(self.armorbonuslabel)
            self.armorbonuslabel.deleteLater()
            self.armorbonuslabel = None
            self.layout.removeWidget(self.armorbonusbox)
            self.armorbonusbox.deleteLater()
            self.armorbonusbox = None

            self.layout.removeWidget(self.initiative)
            self.initiative.deleteLater()
            self.initiative = None
            self.layout.removeWidget(self.initiativeval)
            self.initiativeval.deleteLater()
            self.initiativeval = None
            self.layout.removeWidget(self.initiativebonuslabel)
            self.initiativebonuslabel.deleteLater()
            self.initiativebonuslabel = None
            self.layout.removeWidget(self.initiativebonusbox)
            self.initiativebonusbox.deleteLater()
            self.initiativebonusbox = None

            if self.occultflag[0]:
                self.layout.removeWidget(self.disciplines)
                self.disciplines.deleteLater()
                self.disciplines = None
                self.layout.removeWidget(self.disciplineslevel)
                self.disciplineslevel.deleteLater()
                self.disciplineslevel = None

                self.disciplinecounter = 0
                for x in range(self.olddisciplinecount):
                    if self.olddisciplinecount >= x + 1:
                        self.layout.removeWidget(self.disciplinenamebox[x])
                        self.disciplinenamebox[x].deleteLater()
                        self.disciplinenamebox[x] = None
                        self.layout.removeWidget(self.disciplinelevelbox[x])
                        self.disciplinelevelbox[x].deleteLater()
                        self.disciplinelevelbox[x] = None

        #other traits
        self.cat3 = QtWidgets.QLabel(self)
        self.cat3.setText("Other Traits")
        self.cat3.setFont(self.titlefont)

        self.merits = QtWidgets.QLabel(self)
        self.merits.setText("Merits")
        self.merits.setFont(self.subtitlefont)
        self.meritslevel = QtWidgets.QLabel(self)
        self.meritslevel.setText("Level")

        #initialize merits
        self.meritnamebox = []
        self.meritlevelbox = []
        for x in range(self.meritcount):
            if self.meritcount >= x:
                self.meritnamebox.append(QtWidgets.QLineEdit(self))
                self.meritlevelbox.append(QtWidgets.QLineEdit(self))

        #begin aspirations
        self.aspirations = QtWidgets.QLabel(self)
        self.aspirations.setText("Aspirations")
        self.aspirations.setFont(self.subtitlefont)

        self.conditions = QtWidgets.QLabel(self)
        self.conditions.setText("Conditions")
        self.conditions.setFont(self.subtitlefont)

        self.banes = QtWidgets.QLabel(self)
        self.banes.setText("Banes")
        self.banes.setFont(self.subtitlefont)

        self.aspirationnamebox = []
        for x in range(self.aspirationcount):
            if self.aspirationcount >= x:
                self.aspirationnamebox.append(QtWidgets.QLineEdit(self))

        self.conditionnamebox = []
        for x in range(self.conditioncount):
            if self.conditioncount >= x:
                self.conditionnamebox.append(QtWidgets.QLineEdit(self))

        self.banenamebox = []
        for x in range(self.banecount):
            if self.banecount >= x:
                self.banenamebox.append(QtWidgets.QLineEdit(self))

        #begin other traits

        self.updatestats = QtWidgets.QPushButton('Update Derived Stats')
        self.updatestats.clicked.connect(self.updatestatsdef)

        self.size = QtWidgets.QLabel(self)
        self.size.setText("Size: ")
        self.sizeval = QtWidgets.QLabel(self)
        self.sizeval.setText(str(5 + self.sizebonus))

        self.sizebonuslabel = QtWidgets.QLabel(self)
        self.sizebonuslabel.setText("Size Bonus: ")
        self.sizebonusbox = QtWidgets.QLineEdit(self)

        self.speed = QtWidgets.QLabel(self)
        self.speed.setText("Speed: ")
        self.speedval = QtWidgets.QLabel(self)
        self.speedval.setText(str(int(self.sizeval.text()) + self.strengthstat + self.dexteritystat + self.speedbonus))

        self.speedbonuslabel = QtWidgets.QLabel(self)
        self.speedbonuslabel.setText("Speed Bonus: ")
        self.speedbonusbox = QtWidgets.QLineEdit(self)

        self.defense = QtWidgets.QLabel(self)
        self.defense.setText("Defense: ")
        self.defenseval = QtWidgets.QLabel(self)
        if self.dexteritystat <= self.witsstat:
            self.defenseval.setText(str(self.athleticsskill + self.dexteritystat + self.defensebonus))
        else:
            self.defenseval.setText(str(self.athleticsskill + self.witsstat + self.defensebonus))

        self.defensebonuslabel = QtWidgets.QLabel(self)
        self.defensebonuslabel.setText("Defense Bonus: ")
        self.defensebonusbox = QtWidgets.QLineEdit(self)

        self.armor = QtWidgets.QLabel(self)
        self.armor.setText("Armor: ")
        self.armorval = QtWidgets.QLabel(self)
        self.armorval.setText(str(self.armorbonus))

        self.armorbonuslabel = QtWidgets.QLabel(self)
        self.armorbonuslabel.setText("Armor Bonus: ")
        self.armorbonusbox = QtWidgets.QLineEdit(self)

        self.initiative = QtWidgets.QLabel(self)
        self.initiative.setText("Initiative Mod: ")
        self.initiativeval = QtWidgets.QLabel(self)
        self.initiativeval.setText(str(self.composurestat + self.dexteritystat + self.initiativebonus))

        self.initiativebonuslabel = QtWidgets.QLabel(self)
        self.initiativebonuslabel.setText("Initiative Bonus: ")
        self.initiativebonusbox = QtWidgets.QLineEdit(self)

        if self.occultflag[0]:
            self.disciplines = QtWidgets.QLabel(self)
            self.disciplines.setText("Disciplines")
            self.disciplines.setFont(self.subtitlefont)
            self.disciplineslevel = QtWidgets.QLabel(self)
            self.disciplineslevel.setText("Level")

            #initialize disciplines
            self.disciplinenamebox = []
            self.disciplinelevelbox = []
            for x in range(self.disciplinecount):
                if self.disciplinecount >= x:
                    self.disciplinenamebox.append(QtWidgets.QLineEdit(self))
                    self.disciplinelevelbox.append(QtWidgets.QLineEdit(self))

        #begin layout

        self.layout.addWidget(self.name, 2, 0)
        self.layout.addWidget(self.boxname, 2, 1)
        self.layout.addWidget(self.player, 2, 2)
        self.layout.addWidget(self.boxplayer, 2, 3)
        self.layout.addWidget(self.chronicle, 2, 4)
        self.layout.addWidget(self.boxchronicle, 2, 5)

        self.layout.addWidget(self.concept, 3, 0)
        self.layout.addWidget(self.boxconcept, 3, 1)

        if self.vvflag and self.runonce1:
            self.virtue = QtWidgets.QLabel(self)
            self.virtue.setText("Virtue: ")
            self.boxvirtue = QtWidgets.QLineEdit(self)
            self.vice = QtWidgets.QLabel(self)
            self.vice.setText("Vice: ")
            self.boxvice = QtWidgets.QLineEdit(self)
            self.layout.addWidget(self.vice, 3, 2)
            self.layout.addWidget(self.boxvice, 3, 3)
            self.layout.addWidget(self.virtue, 3, 4)
            self.layout.addWidget(self.boxvirtue, 3, 5)

        if self.occultflag[0] and self.runonce1:
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

            self.oplinecounter += 1
            self.layout.addWidget(self.clan, 3 + self.oplinecounter, 0)
            self.layout.addWidget(self.boxclan, 3 + self.oplinecounter, 1)
            self.layout.addWidget(self.bloodline, 3 + self.oplinecounter, 2)
            self.layout.addWidget(self.boxbloodline, 3 + self.oplinecounter, 3)
            self.layout.addWidget(self.covenant, 3 + self.oplinecounter, 4)
            self.layout.addWidget(self.boxcovenant, 3 + self.oplinecounter, 5)

            self.oplinecounter += 1
            self.layout.addWidget(self.mask, 3 + self.oplinecounter, 1)
            self.layout.addWidget(self.boxmask, 3 + self.oplinecounter, 2)
            self.layout.addWidget(self.dirge, 3 + self.oplinecounter, 3)
            self.layout.addWidget(self.boxdirge, 3 + self.oplinecounter, 4)
            self.runonce1 = False

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

        self.layout.addWidget(self.cat3, 8 + self.oplinecounter, 4)

        self.layout.addWidget(self.merits, 9 + self.oplinecounter, 2)
        self.layout.addWidget(self.meritslevel, 9 + self.oplinecounter, 3)

        #merits
        self.meritcounter = 0
        for x in range(self.meritcount):
            if self.meritcount >= 1:
                self.meritcounter += 1
                self.layout.addWidget(self.meritnamebox[x], 9 + self.oplinecounter + self.meritcounter, 2)
                self.layout.addWidget(self.meritlevelbox[x], 9 + self.oplinecounter + self.meritcounter, 3)

        self.layout.addWidget(self.aspirations, 10 + self.oplinecounter + self.meritcounter, 2)

        self.layout.addWidget(self.conditions, 10 + self.oplinecounter + self.meritcounter, 3)

        self.mabc = 0
        self.aspirationcounter = 0
        for x in range(self.aspirationcount):
            if self.aspirationcount >= 1:
                self.aspirationcounter += 1
                self.layout.addWidget(self.aspirationnamebox[x], 10 + self.oplinecounter + self.meritcounter + self.aspirationcounter, 2)
        self.conditioncounter = 0
        for x in range(self.conditioncount):
            if self.conditioncount >= 1:
                self.conditioncounter += 1
                self.layout.addWidget(self.conditionnamebox[x], 10 + self.oplinecounter + self.meritcounter + self.conditioncounter, 3)

        if self.aspirationcounter <= self.conditioncounter:
            self.layout.addWidget(self.banes, 11 + self.oplinecounter + self.meritcounter + self.aspirationcounter, 2)
            self.mabc += self.meritcounter + self.aspirationcounter
        else:
            self.layout.addWidget(self.banes, 11 + self.oplinecounter + self.meritcounter + self.conditioncounter, 3)
            self.mabc += self.meritcounter + self.conditioncounter

        self.banecounter = 0
        for x in range(self.banecount):
            if self.banecount >= 1:
                self.banecounter += 1
                if self.aspirationcounter <= self.conditioncounter:
                    self.layout.addWidget(self.banenamebox[x], 11 + self.oplinecounter + self.meritcounter + self.aspirationcounter + self.banecounter, 2)
                else:
                    self.layout.addWidget(self.banenamebox[x], 11 + self.oplinecounter + self.meritcounter + self.conditioncounter + self.banecounter, 3)

        self.mabc += self.banecounter

        self.layout.addWidget(self.updatestats, 8 + self.oplinecounter, 5)

        self.layout.addWidget(self.size, 9 + self.oplinecounter, 4)
        self.layout.addWidget(self.sizeval, 9 + self.oplinecounter, 5)
        self.layout.addWidget(self.sizebonuslabel, 10 + self.oplinecounter, 4)
        self.layout.addWidget(self.sizebonusbox, 10 + self.oplinecounter, 5)

        self.layout.addWidget(self.speed, 11 + self.oplinecounter, 4)
        self.layout.addWidget(self.speedval, 11 + self.oplinecounter, 5)
        self.layout.addWidget(self.speedbonuslabel, 12 + self.oplinecounter, 4)
        self.layout.addWidget(self.speedbonusbox, 12 + self.oplinecounter, 5)

        self.layout.addWidget(self.defense, 13 + self.oplinecounter, 4)
        self.layout.addWidget(self.defenseval, 13 + self.oplinecounter, 5)
        self.layout.addWidget(self.defensebonuslabel, 14 + self.oplinecounter, 4)
        self.layout.addWidget(self.defensebonusbox, 14 + self.oplinecounter, 5)

        self.layout.addWidget(self.armor, 15 + self.oplinecounter, 4)
        self.layout.addWidget(self.armorval, 15 + self.oplinecounter, 5)
        self.layout.addWidget(self.armorbonuslabel, 16 + self.oplinecounter, 4)
        self.layout.addWidget(self.armorbonusbox, 16 + self.oplinecounter, 5)

        self.layout.addWidget(self.initiative, 17 + self.oplinecounter, 4)
        self.layout.addWidget(self.initiativeval, 17 + self.oplinecounter, 5)
        self.layout.addWidget(self.initiativebonuslabel, 18 + self.oplinecounter, 4)
        self.layout.addWidget(self.initiativebonusbox, 18 + self.oplinecounter, 5)

        if self.occultflag[0]:
            self.layout.addWidget(self.disciplines, 12 + self.oplinecounter + self.mabc, 2)
            self.layout.addWidget(self.disciplineslevel, 12 + self.oplinecounter + self.mabc, 3)

            #disciplines
            self.disciplinecounter = 0
            for x in range(self.disciplinecount):
                if self.disciplinecount >= 1:
                    self.disciplinecounter += 1
                    self.layout.addWidget(self.disciplinenamebox[x], 12 + self.oplinecounter + self.mabc + self.disciplinecounter, 2)
                    self.layout.addWidget(self.disciplinelevelbox[x], 12 + self.oplinecounter + self.mabc + self.disciplinecounter, 3)

        self.setLayout(self.layout)
        self.setGeometry(300, 75, 1024, 768)

        self.makesheetflag = True

    def humantoggledef(self):
        if self.humantoggle.isChecked():
            self.humantoggle.setChecked(True)
            self.vvflag = True
        else:
            self.vamptoggle.setChecked(False)
            self.vvflag = False
            self.layout.removeWidget(self.vice)
            self.vice.deleteLater()
            self.vice = None
            self.layout.removeWidget(self.boxvice)
            self.boxvice.deleteLater()
            self.boxvice = None
            self.layout.removeWidget(self.virtue)
            self.virtue.deleteLater()
            self.virtue = None
            self.layout.removeWidget(self.boxvirtue)
            self.boxvirtue.deleteLater()
            self.boxvirtue = None
            self.runonce1 = True

        self.savesettings()

        self.makesheet()

    def vamptoggledef(self):
        if self.vamptoggle.isChecked():
            self.vamptoggle.setChecked(True)
            self.occultflag[0] = True
            self.oldmeritcount = self.meritcount
            self.oldaspirationcount = self.aspirationcount
            self.oldconditioncount = self.conditioncount
            self.oldbanecount = self.banecount
        else:
            self.vamptoggle.setChecked(False)
            self.occultflag[0] = False
            self.layout.removeWidget(self.clan)
            self.clan.deleteLater()
            self.clan = None
            self.layout.removeWidget(self.boxclan)
            self.boxclan.deleteLater()
            self.boxclan = None
            self.layout.removeWidget(self.bloodline)
            self.bloodline.deleteLater()
            self.bloodline = None
            self.layout.removeWidget(self.boxbloodline)
            self.boxbloodline.deleteLater()
            self.boxbloodline = None
            self.layout.removeWidget(self.covenant)
            self.covenant.deleteLater()
            self.covenant = None
            self.layout.removeWidget(self.boxcovenant)
            self.boxcovenant.deleteLater()
            self.boxcovenant = None
            self.layout.removeWidget(self.mask)
            self.mask.deleteLater()
            self.mask = None
            self.layout.removeWidget(self.boxmask)
            self.boxmask.deleteLater()
            self.boxmask = None
            self.layout.removeWidget(self.dirge)
            self.dirge.deleteLater()
            self.dirge = None
            self.layout.removeWidget(self.boxdirge)
            self.boxdirge.deleteLater()
            self.boxdirge = None

            self.layout.removeWidget(self.disciplines)
            self.disciplines.deleteLater()
            self.disciplines = None
            self.layout.removeWidget(self.disciplineslevel)
            self.disciplineslevel.deleteLater()
            self.disciplineslevel = None

            self.disciplinecounter = 0
            for x in range(self.olddisciplinecount):
                if self.olddisciplinecount >= x + 1:
                    self.layout.removeWidget(self.disciplinenamebox[x])
                    self.disciplinenamebox[x].deleteLater()
                    self.disciplinenamebox[x] = None
                    self.layout.removeWidget(self.disciplinelevelbox[x])
                    self.disciplinelevelbox[x].deleteLater()
                    self.disciplinelevelbox[x] = None

            self.oplinecounter -= 2
            self.oldmeritcount = 5
            self.runonce1 = True

        self.savesettings()

        self.makesheet()

    def meritdef(self):
        self.oldmeritcount = self.meritcount
        self.meritcount = int(self.meritslotsbox.text())

        self.savesettings()

        self.makesheet()

    def aspirationdef(self):
        self.oldaspirationcount = self.aspirationcount
        self.aspirationcount = int(self.aspirationslotsbox.text())

        self.savesettings()

        self.makesheet()

    def conditiondef(self):
        self.oldconditioncount = self.conditioncount
        self.conditioncount = int(self.conditionslotsbox.text())

        self.savesettings()

        self.makesheet()

    def banedef(self):
        self.oldbanecount = self.banecount
        self.banecount = int(self.baneslotsbox.text())

        self.savesettings()

        self.makesheet()

    def disciplinedef(self):
        self.olddisciplinecount = self.disciplinecount
        self.disciplinecount = int(self.disciplineslotsbox.text())

        self.savesettings()

        self.makesheet()

    def settingsdef(self):
        self.settings = QtWidgets.QWidget()
        self.settings.setWindowTitle('Settings')
        self.settings.setGeometry(400, 150, 384, 512)
        self.settings.show()
        self.settingslayout = QtWidgets.QGridLayout(self.settings)

        self.settingstitle = QtWidgets.QLabel()
        self.settingstitle.setText("Settings")
        self.settingstitle.setFont(self.titlefont)

        self.humanlabel = QtWidgets.QLabel()
        self.humanlabel.setText("Character has a Vice and Virtue: ")
        self.humantoggle = QtWidgets.QCheckBox()
        self.humantoggle.clicked.connect(self.humantoggledef)

        self.vamplabel = QtWidgets.QLabel()
        self.vamplabel.setText("Character is Vampire: ")
        self.vamptoggle = QtWidgets.QCheckBox()
        self.vamptoggle.clicked.connect(self.vamptoggledef)

        self.meritslotslabel = QtWidgets.QLabel()
        self.meritslotslabel.setText("Merit Slots Available: ")
        self.meritslotsbox = QtWidgets.QLineEdit()
        self.meritslotsbox.setText(str(self.meritcount))
        self.meritslotsupdate = QtWidgets.QPushButton('Update Merit Slots')
        self.meritslotsupdate.clicked.connect(self.meritdef)

        self.aspirationslotslabel = QtWidgets.QLabel()
        self.aspirationslotslabel.setText("Aspiration Slots Available: ")
        self.aspirationslotsbox = QtWidgets.QLineEdit()
        self.aspirationslotsbox.setText(str(self.aspirationcount))
        self.aspirationslotsupdate = QtWidgets.QPushButton('Update Aspiration Slots')
        self.aspirationslotsupdate.clicked.connect(self.aspirationdef)

        self.conditionslotslabel = QtWidgets.QLabel()
        self.conditionslotslabel.setText("Condition Slots Available: ")
        self.conditionslotsbox = QtWidgets.QLineEdit()
        self.conditionslotsbox.setText(str(self.conditioncount))
        self.conditionslotsupdate = QtWidgets.QPushButton('Update Condition Slots')
        self.conditionslotsupdate.clicked.connect(self.conditiondef)

        self.baneslotslabel = QtWidgets.QLabel()
        self.baneslotslabel.setText("Bane Slots Available: ")
        self.baneslotsbox = QtWidgets.QLineEdit()
        self.baneslotsbox.setText(str(self.banecount))
        self.baneslotsupdate = QtWidgets.QPushButton('Update Bane Slots')
        self.baneslotsupdate.clicked.connect(self.banedef)

        self.disciplineslotslabel = QtWidgets.QLabel()
        self.disciplineslotslabel.setText("Discipline Slots Available: ")
        self.disciplineslotsbox = QtWidgets.QLineEdit()
        self.disciplineslotsbox.setText(str(self.disciplinecount))
        self.disciplineslotsupdate = QtWidgets.QPushButton('Update Discipline Slots')
        self.disciplineslotsupdate.clicked.connect(self.disciplinedef)

        self.settingslayout.addWidget(self.settingstitle, 0, 2, 0, 5)

        self.settingslayout.addWidget(self.meritslotslabel, 2, 0)
        self.settingslayout.addWidget(self.meritslotsbox, 2, 1)
        self.settingslayout.addWidget(self.meritslotsupdate, 2, 2)
        self.settingslayout.addWidget(self.aspirationslotslabel, 2, 3)
        self.settingslayout.addWidget(self.aspirationslotsbox, 2, 4)
        self.settingslayout.addWidget(self.aspirationslotsupdate, 2, 5)

        self.settingslayout.addWidget(self.conditionslotslabel, 3, 0)
        self.settingslayout.addWidget(self.conditionslotsbox, 3, 1)
        self.settingslayout.addWidget(self.conditionslotsupdate, 3, 2)
        self.settingslayout.addWidget(self.baneslotslabel, 3, 3)
        self.settingslayout.addWidget(self.baneslotsbox, 3, 4)
        self.settingslayout.addWidget(self.baneslotsupdate, 3, 5)

        self.settingslayout.addWidget(self.disciplineslotslabel, 4, 0)
        self.settingslayout.addWidget(self.disciplineslotsbox, 4, 1)
        self.settingslayout.addWidget(self.disciplineslotsupdate, 4, 2)

        self.settingslayout.addWidget(self.humanlabel, 6, 2)
        self.settingslayout.addWidget(self.humantoggle, 6, 3)

        self.settingslayout.addWidget(self.vamplabel, 7, 2)
        self.settingslayout.addWidget(self.vamptoggle, 7, 3)
        self.setLayout(self.layout)

    def initsettings(self):
        if path.exists('settings.txt'):
            with open('settings.txt') as f:
                nonemptylines = [line.strip("\n") for line in f if line != "\n"]
                for i, line in enumerate(nonemptylines):
                    if i == 0:
                        splitline = line.split('#')
                        self.oldmeritcount = self.meritcount
                        self.meritcount = int(splitline[0])
                    if i == 1:
                        splitline = line.split('#')
                        self.oldaspirationcount = self.aspirationcount
                        self.aspirationcount = int(splitline[0])
                    if i == 2:
                        splitline = line.split('#')
                        self.oldconditioncount = self.conditioncount
                        self.conditioncount = int(splitline[0])
                    if i == 3:
                        splitline = line.split('#')
                        self.oldbanecount = self.banecount
                        self.banecount = int(splitline[0])
                    if i == 4:
                        splitline = line.split('#')
                        self.olddisciplinecount = self.disciplinecount
                        self.disciplinecount = int(splitline[0])
                    if i == 5:
                        splitline = line.split('#')
                        if splitline[0] == 'True':
                            self.vvflag = True
                    if i == 6:
                        # print('test')
                        splitline = line.split('#')
                        if splitline[0] == 'True':
                            # print('test2')
                            self.occultflag[0] = True
                            self.oldmeritcount = self.meritcount
                            self.oldaspirationcount = self.aspirationcount
                            self.oldconditioncount = self.conditioncount
                            self.oldbanecount = self.banecount

        self.resize(1024, 768)
        self.makesheet()

    def __init__(self):
        super(MyWidget, self).__init__()

        self.setGeometry(300, 75, 1024, 768)
        self.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')

        self.oplinecounter = 0

        self.oldmeritcount = 0
        self.meritcount = 5 #no max

        self.oldaspirationcount = 0
        self.aspirationcount = 5

        self.oldconditioncount = 0
        self.conditioncount = 5

        self.oldbanecount = 0
        self.banecount = 5

        self.olddisciplinecount = 0
        self.disciplinecount = 5

        self.sizebonus = 0

        self.speedbonus = 0

        self.defensebonus = 0

        self.armorbonus = 0

        self.initiativebonus = 0

        self.intelligencestat = 1
        self.witsstat = 1
        self.resolvestat = 1
        self.strengthstat = 1
        self.dexteritystat = 1
        self.staminastat = 1
        self.presencestat = 1
        self.manipulationstat = 1
        self.composurestat = 1

        self.athleticsskill = -1

        self.runonce1 = True
        self.makesheetflag = False

        self.vvflag = False

        self.occultflag = [False, False, False]

        self.title = QtWidgets.QLabel()

        pixMap = QtGui.QPixmap.fromImage('CofD.png')

        self.title.setPixmap( pixMap )
        self.title.show()

        self.settings = QtWidgets.QPushButton('')
        self.settings.setIcon(QtGui.QIcon('gear.png'))
        self.settings.clicked.connect(self.settingsdef)

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

        self.initsettings()

app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(1024, 768)
widget.show()

w = QtWidgets.QWidget()

w.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')

layout = QtWidgets.QVBoxLayout(w)
scroll = QtWidgets.QScrollArea()

scroll.setWidget(widget)
scroll.setWidgetResizable(True)
scroll.resize(16, 768)
layout.addWidget(scroll)
w.show()

sys.exit(app.exec())
