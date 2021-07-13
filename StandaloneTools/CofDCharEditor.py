import sys
import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):

#if importing this charater to a table i need to make sure that it's added under a in that is the name with the space

    def savedef(self):
        if path.exists(self.saveloc.text()+'.json'):
            with open(self.saveloc.text()+'.json') as f:
                backup = json.load(f)
            with open(self.saveloc.text()+'backup.json', 'w') as f:
                json.dump(backup, f)

        stats = {'name': self.boxname.text(), 'supernaturaltags': [], 'player': self.boxplayer.text(), 'chronicle': self.boxchronicle.text(), 'concept': self.boxconcept.text(), 'stats': {'intelligence': self.boxintelligence.text(), 'strength': self.boxstrength.text(), 'presence': self.boxpresence.text(), 'wits': self.boxwits.text(), 'dexterity': self.boxdexterity.text(), 'manipulation': self.boxmanipulation.text(), 'resolve': self.boxresolve.text(), 'stamina': self.boxstamina.text(), 'composure': self.boxcomposure.text()}, 'skills': {'academics': self.boxacademics.text(), 'computer': self.boxcomputer.text(), 'crafts': self.boxcrafts.text(), 'investigation': self.boxinvestigation.text(), 'medicine': self.boxmedicine.text(), 'occult': self.boxoccult.text(), 'politics': self.boxpolitics.text(), 'science': self.boxscience.text(), 'athletics': self.boxathletics.text(), 'brawl': self.boxbrawl.text(), 'drive': self.boxdrive.text(), 'firearms': self.boxfirearms.text(), 'larceny': self.boxlarceny.text(), 'stealth': self.boxstealth.text(), 'survival': self.boxsurvival.text(), 'weaponry': self.boxweaponry.text(), 'animalken': self.boxanimalken.text(), 'empathy': self.boxempathy.text(), 'expression': self.boxexpression.text(), 'intimidation': self.boxintimidation.text(), 'persuasion': self.boxpersuasion.text(), 'socialize': self.boxsocialize.text(), 'streetwise': self.boxstreetwise.text(), 'subterfuge': self.boxsubterfuge.text()}}
        if self.occultflag[0]:
            stats['supernaturaltags'].append('vampire')
            stats['mask'] = self.boxmask.text()
            stats['dirge'] = self.boxdirge.text()
            stats['clan'] = self.boxclan.text()
            stats['bloodline'] = self.boxbloodline.text()
            stats['covenant'] = self.boxcovenant.text()
        self.filledmerits = 0
        stats['merits'] = []
        stats['merits'].append(['filledmerits', 0])
        if self.meritcount >= 1 and self.meritnamebox1.text() != "" and self.meritlevelbox1.text() != "":
            stats['merits'].append([self.meritnamebox1.text(), self.meritlevelbox1.text()])
            self.filledmerits +=1
        if self.meritcount >= 2 and self.meritnamebox2.text() != "" and self.meritlevelbox2.text() != "":
            stats['merits'].append([self.meritnamebox2.text(), self.meritlevelbox2.text()])
            self.filledmerits +=1
        if self.meritcount >= 3 and self.meritnamebox3.text() != "" and self.meritlevelbox3.text() != "":
            stats['merits'].append([self.meritnamebox3.text(), self.meritlevelbox3.text()])
            self.filledmerits +=1
        if self.meritcount >= 4 and self.meritnamebox4.text() != "" and self.meritlevelbox4.text() != "":
            stats['merits'].append([self.meritnamebox4.text(), self.meritlevelbox4.text()])
            self.filledmerits +=1
        if self.meritcount >= 5 and self.meritnamebox5.text() != "" and self.meritlevelbox5.text() != "":
            stats['merits'].append([self.meritnamebox5.text(), self.meritlevelbox5.text()])
            self.filledmerits +=1
        if self.meritcount >= 6 and self.meritnamebox6.text() != "" and self.meritlevelbox6.text() != "":
            stats['merits'].append([self.meritnamebox6.text(), self.meritlevelbox6.text()])
            self.filledmerits +=1
        if self.meritcount >= 7 and self.meritnamebox7.text() != "" and self.meritlevelbox7.text() != "":
            stats['merits'].append([self.meritnamebox7.text(), self.meritlevelbox7.text()])
            self.filledmerits +=1
        if self.meritcount >= 8 and self.meritnamebox8.text() != "" and self.meritlevelbox8.text() != "":
            stats['merits'].append([self.meritnamebox8.text(), self.meritlevelbox8.text()])
            self.filledmerits +=1
        if self.meritcount >= 9 and self.meritnamebox9.text() != "" and self.meritlevelbox9.text() != "":
            stats['merits'].append([self.meritnamebox9.text(), self.meritlevelbox9.text()])
            self.filledmerits +=1
        if self.meritcount >= 10 and self.meritnamebox10.text() != "" and self.meritlevelbox10.text() != "":
            stats['merits'].append([self.meritnamebox10.text(), self.meritlevelbox10.text()])
            self.filledmerits +=1
        if self.meritcount >= 11 and self.meritnamebox11.text() != "" and self.meritlevelbox11.text() != "":
            stats['merits'].append([self.meritnamebox11.text(), self.meritlevelbox11.text()])
            self.filledmerits +=1
        if self.meritcount >= 12 and self.meritnamebox12.text() != "" and self.meritlevelbox12.text() != "":
            stats['merits'].append([self.meritnamebox12.text(), self.meritlevelbox12.text()])
            self.filledmerits +=1
        if self.meritcount >= 13 and self.meritnamebox13.text() != "" and self.meritlevelbox13.text() != "":
            stats['merits'].append([self.meritnamebox13.text(), self.meritlevelbox13.text()])
            self.filledmerits +=1
        if self.meritcount >= 14 and self.meritnamebox14.text() != "" and self.meritlevelbox14.text() != "":
            stats['merits'].append([self.meritnamebox14.text(), self.meritlevelbox14.text()])
            self.filledmerits +=1
        if self.meritcount >= 15 and self.meritnamebox15.text() != "" and self.meritlevelbox15.text() != "":
            stats['merits'].append([self.meritnamebox15.text(), self.meritlevelbox15.text()])
            self.filledmerits +=1
        if self.meritcount >= 16 and self.meritnamebox16.text() != "" and self.meritlevelbox16.text() != "":
            stats['merits'].append([self.meritnamebox16.text(), self.meritlevelbox16.text()])
            self.filledmerits +=1
        if self.meritcount >= 17 and self.meritnamebox17.text() != "" and self.meritlevelbox17.text() != "":
            stats['merits'].append([self.meritnamebox17.text(), self.meritlevelbox17.text()])
            self.filledmerits +=1
        if self.meritcount >= 18 and self.meritnamebox18.text() != "" and self.meritlevelbox18.text() != "":
            stats['merits'].append([self.meritnamebox18.text(), self.meritlevelbox18.text()])
            self.filledmerits +=1
        if self.meritcount >= 19 and self.meritnamebox19.text() != "" and self.meritlevelbox19.text() != "":
            stats['merits'].append([self.meritnamebox19.text(), self.meritlevelbox19.text()])
            self.filledmerits +=1
        if self.meritcount >= 20 and self.meritnamebox20.text() != "" and self.meritlevelbox20.text() != "":
            stats['merits'].append([self.meritnamebox20.text(), self.meritlevelbox20.text()])
            self.filledmerits +=1
        stats['merits'][0] = ['filledmerits', self.filledmerits]

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
                self.occultflag = [False, False, False]
                if stats['supernaturaltags'][0]:
                    self.boxclan.setText(stats['clan'])
                    self.boxbloodline.setText(stats['bloodline'])
                    self.boxcovenant.setText(stats['covenant'])
                    self.boxmask.setText(stats['mask'])
                    self.boxdirge.setText(stats['dirge'])
                    self.occultflag[0] = True
                if stats['merits'][0][1] > self.meritcount:
                    self.meritcount = stats['merits'][0][1]

                    self.makesheet()
                if stats['merits'][0][1] >= 1:
                    self.meritnamebox1.setText(stats['merits'][1][0])
                    self.meritlevelbox1.setText(stats['merits'][1][1])
                if stats['merits'][0][1] >= 2:
                    self.meritnamebox2.setText(stats['merits'][2][0])
                    self.meritlevelbox2.setText(stats['merits'][2][1])
                if stats['merits'][0][1] >= 3:
                    self.meritnamebox3.setText(stats['merits'][3][0])
                    self.meritlevelbox3.setText(stats['merits'][3][1])
                if stats['merits'][0][1] >= 4:
                    self.meritnamebox4.setText(stats['merits'][4][0])
                    self.meritlevelbox4.setText(stats['merits'][4][1])
                if stats['merits'][0][1] >= 5:
                    self.meritnamebox5.setText(stats['merits'][5][0])
                    self.meritlevelbox5.setText(stats['merits'][5][1])
                if stats['merits'][0][1] >= 6:
                    self.meritnamebox6.setText(stats['merits'][6][0])
                    self.meritlevelbox6.setText(stats['merits'][6][1])
                if stats['merits'][0][1] >= 7:
                    self.meritnamebox7.setText(stats['merits'][7][0])
                    self.meritlevelbox7.setText(stats['merits'][7][1])
                if stats['merits'][0][1] >= 8:
                    self.meritnamebox8.setText(stats['merits'][8][0])
                    self.meritlevelbox8.setText(stats['merits'][8][1])
                if stats['merits'][0][1] >= 9:
                    self.meritnamebox9.setText(stats['merits'][9][0])
                    self.meritlevelbox9.setText(stats['merits'][9][1])
                if stats['merits'][0][1] >= 10:
                    self.meritnamebox10.setText(stats['merits'][10][0])
                    self.meritlevelbox10.setText(stats['merits'][10][1])
                if stats['merits'][0][1] >= 11:
                    self.meritnamebox11.setText(stats['merits'][11][0])
                    self.meritlevelbox11.setText(stats['merits'][11][1])
                if stats['merits'][0][1] >= 12:
                    self.meritnamebox12.setText(stats['merits'][12][0])
                    self.meritlevelbox12.setText(stats['merits'][12][1])
                if stats['merits'][0][1] >= 13:
                    self.meritnamebox13.setText(stats['merits'][13][0])
                    self.meritlevelbox13.setText(stats['merits'][13][1])
                if stats['merits'][0][1] >= 14:
                    self.meritnamebox14.setText(stats['merits'][14][0])
                    self.meritlevelbox14.setText(stats['merits'][14][1])
                if stats['merits'][0][1] >= 15:
                    self.meritnamebox15.setText(stats['merits'][15][0])
                    self.meritlevelbox15.setText(stats['merits'][15][1])
                if stats['merits'][0][1] >= 16:
                    self.meritnamebox16.setText(stats['merits'][16][0])
                    self.meritlevelbox16.setText(stats['merits'][16][1])
                if stats['merits'][0][1] >= 17:
                    self.meritnamebox17.setText(stats['merits'][17][0])
                    self.meritlevelbox17.setText(stats['merits'][17][1])
                if stats['merits'][0][1] >= 18:
                    self.meritnamebox18.setText(stats['merits'][18][0])
                    self.meritlevelbox18.setText(stats['merits'][18][1])
                if stats['merits'][0][1] >= 19:
                    self.meritnamebox19.setText(stats['merits'][19][0])
                    self.meritlevelbox19.setText(stats['merits'][19][1])
                if stats['merits'][0][1] >= 20:
                    self.meritnamebox20.setText(stats['merits'][20][0])
                    self.meritlevelbox20.setText(stats['merits'][20][1])
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
        if self.meritcount >= 1:
            self.meritnamebox1 = QtWidgets.QLineEdit(self)
            self.meritlevelbox1 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 2:
            self.meritnamebox2 = QtWidgets.QLineEdit(self)
            self.meritlevelbox2 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 3:
            self.meritnamebox3 = QtWidgets.QLineEdit(self)
            self.meritlevelbox3 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 4:
            self.meritnamebox4 = QtWidgets.QLineEdit(self)
            self.meritlevelbox4 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 5:
            self.meritnamebox5 = QtWidgets.QLineEdit(self)
            self.meritlevelbox5 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 6:
            self.meritnamebox6 = QtWidgets.QLineEdit(self)
            self.meritlevelbox6 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 7:
            self.meritnamebox7 = QtWidgets.QLineEdit(self)
            self.meritlevelbox7 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 8:
            self.meritnamebox8 = QtWidgets.QLineEdit(self)
            self.meritlevelbox8 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 9:
            self.meritnamebox9 = QtWidgets.QLineEdit(self)
            self.meritlevelbox9 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 10:
            self.meritnamebox10 = QtWidgets.QLineEdit(self)
            self.meritlevelbox10 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 11:
            self.meritnamebox11 = QtWidgets.QLineEdit(self)
            self.meritlevelbox11 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 12:
            self.meritnamebox12 = QtWidgets.QLineEdit(self)
            self.meritlevelbox12 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 13:
            self.meritnamebox13 = QtWidgets.QLineEdit(self)
            self.meritlevelbox13 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 14:
            self.meritnamebox14 = QtWidgets.QLineEdit(self)
            self.meritlevelbox14 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 15:
            self.meritnamebox15 = QtWidgets.QLineEdit(self)
            self.meritlevelbox15 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 16:
            self.meritnamebox16 = QtWidgets.QLineEdit(self)
            self.meritlevelbox16 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 17:
            self.meritnamebox17 = QtWidgets.QLineEdit(self)
            self.meritlevelbox17 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 18:
            self.meritnamebox18 = QtWidgets.QLineEdit(self)
            self.meritlevelbox18 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 19:
            self.meritnamebox19 = QtWidgets.QLineEdit(self)
            self.meritlevelbox19 = QtWidgets.QLineEdit(self)
        if self.meritcount >= 20:
            self.meritnamebox20 = QtWidgets.QLineEdit(self)
            self.meritlevelbox20 = QtWidgets.QLineEdit(self)

        #begin layout

        self.layout.addWidget(self.name, 2, 0)
        self.layout.addWidget(self.boxname, 2, 1)
        self.layout.addWidget(self.player, 2, 2)
        self.layout.addWidget(self.boxplayer, 2, 3)
        self.layout.addWidget(self.chronicle, 2, 4)
        self.layout.addWidget(self.boxchronicle, 2, 5)

        self.layout.addWidget(self.concept, 3, 0)
        self.layout.addWidget(self.boxconcept, 3, 1)

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
            self.layout.addWidget(self.mask, 3 + self.oplinecounter, 0)
            self.layout.addWidget(self.boxmask, 3 + self.oplinecounter, 1)
            self.layout.addWidget(self.dirge, 3 + self.oplinecounter, 2)
            self.layout.addWidget(self.boxdirge, 3 + self.oplinecounter, 3)
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

        #other traits
        self.cat3 = QtWidgets.QLabel(self)
        self.cat3.setText("Other Traits")
        self.cat3.setFont(self.titlefont)

        self.merits = QtWidgets.QLabel(self)
        self.merits.setText("Merits")
        self.merits.setFont(self.subtitlefont)
        self.meritslevel = QtWidgets.QLabel(self)
        self.meritslevel.setText("Level")

        self.layout.addWidget(self.cat3, 8 + self.oplinecounter, 4)
        self.layout.addWidget(self.merits, 9 + self.oplinecounter, 2)
        self.layout.addWidget(self.meritslevel, 9 + self.oplinecounter, 3)

        #merits

        self.meritcounter = 0
        if self.oldmeritcount >= 1:
            self.layout.removeWidget(self.meritnamebox1)
            self.meritnamebox1.deleteLater()
            self.meritnamebox1 = None
            self.layout.removeWidget(self.meritlevelbox1)
            self.meritlevelbox1.deleteLater()
            self.meritlevelbox1 = None
            self.meritnamebox1 = QtWidgets.QLineEdit(self)
            self.meritlevelbox1 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 2:
            self.layout.removeWidget(self.meritnamebox2)
            self.meritnamebox2.deleteLater()
            self.meritnamebox2 = None
            self.layout.removeWidget(self.meritlevelbox2)
            self.meritlevelbox2.deleteLater()
            self.meritlevelbox2 = None
            self.meritnamebox2 = QtWidgets.QLineEdit(self)
            self.meritlevelbox2 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 3:
            self.layout.removeWidget(self.meritnamebox3)
            self.meritnamebox3.deleteLater()
            self.meritnamebox3 = None
            self.layout.removeWidget(self.meritlevelbox3)
            self.meritlevelbox3.deleteLater()
            self.meritlevelbox3 = None
            self.meritnamebox3 = QtWidgets.QLineEdit(self)
            self.meritlevelbox3 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 4:
            self.layout.removeWidget(self.meritnamebox4)
            self.meritnamebox4.deleteLater()
            self.meritnamebox4 = None
            self.layout.removeWidget(self.meritlevelbox4)
            self.meritlevelbox4.deleteLater()
            self.meritlevelbox4 = None
            self.meritnamebox4 = QtWidgets.QLineEdit(self)
            self.meritlevelbox4 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 5:
            self.layout.removeWidget(self.meritnamebox5)
            self.meritnamebox5.deleteLater()
            self.meritnamebox5 = None
            self.layout.removeWidget(self.meritlevelbox5)
            self.meritlevelbox5.deleteLater()
            self.meritlevelbox5 = None
            self.meritnamebox5 = QtWidgets.QLineEdit(self)
            self.meritlevelbox5 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 6:
            self.layout.removeWidget(self.meritnamebox6)
            self.meritnamebox6.deleteLater()
            self.meritnamebox6 = None
            self.layout.removeWidget(self.meritlevelbox6)
            self.meritlevelbox6.deleteLater()
            self.meritlevelbox6 = None
            self.meritnamebox6 = QtWidgets.QLineEdit(self)
            self.meritlevelbox6 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 7:
            self.layout.removeWidget(self.meritnamebox7)
            self.meritnamebox7.deleteLater()
            self.meritnamebox7 = None
            self.layout.removeWidget(self.meritlevelbox7)
            self.meritlevelbox7.deleteLater()
            self.meritlevelbox7 = None
            self.meritnamebox7 = QtWidgets.QLineEdit(self)
            self.meritlevelbox7 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 8:
            self.layout.removeWidget(self.meritnamebox8)
            self.meritnamebox8.deleteLater()
            self.meritnamebox8 = None
            self.layout.removeWidget(self.meritlevelbox8)
            self.meritlevelbox8.deleteLater()
            self.meritlevelbox8 = None
            self.meritnamebox8 = QtWidgets.QLineEdit(self)
            self.meritlevelbox8 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 9:
            self.layout.removeWidget(self.meritnamebox9)
            self.meritnamebox9.deleteLater()
            self.meritnamebox9 = None
            self.layout.removeWidget(self.meritlevelbox9)
            self.meritlevelbox9.deleteLater()
            self.meritlevelbox9 = None
            self.meritnamebox9 = QtWidgets.QLineEdit(self)
            self.meritlevelbox9 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 10:
            self.layout.removeWidget(self.meritnamebox10)
            self.meritnamebox10.deleteLater()
            self.meritnamebox10 = None
            self.layout.removeWidget(self.meritlevelbox10)
            self.meritlevelbox10.deleteLater()
            self.meritlevelbox10 = None
            self.meritnamebox10 = QtWidgets.QLineEdit(self)
            self.meritlevelbox10 = QtWidgets.QLineEdit(self)
            self.meritcounter -= 1
        if self.oldmeritcount >= 11:
            self.layout.removeWidget(self.meritnamebox11)
            self.meritnamebox11.deleteLater()
            self.meritnamebox11 = None
            self.layout.removeWidget(self.meritlevelbox11)
            self.meritlevelbox11.deleteLater()
            self.meritlevelbox11 = None
            self.meritnamebox11 = QtWidgets.QLineEdit(self)
            self.meritlevelbox11 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 12:
            self.layout.removeWidget(self.meritnamebox12)
            self.meritnamebox12.deleteLater()
            self.meritnamebox12 = None
            self.layout.removeWidget(self.meritlevelbox12)
            self.meritlevelbox12.deleteLater()
            self.meritlevelbox12 = None
            self.meritnamebox12 = QtWidgets.QLineEdit(self)
            self.meritlevelbox12 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 13:
            self.layout.removeWidget(self.meritnamebox13)
            self.meritnamebox13.deleteLater()
            self.meritnamebox13 = None
            self.layout.removeWidget(self.meritlevelbox13)
            self.meritlevelbox13.deleteLater()
            self.meritlevelbox13 = None
            self.meritnamebox13 = QtWidgets.QLineEdit(self)
            self.meritlevelbox13 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 14:
            self.layout.removeWidget(self.meritnamebox14)
            self.meritnamebox14.deleteLater()
            self.meritnamebox14 = None
            self.layout.removeWidget(self.meritlevelbox14)
            self.meritlevelbox14.deleteLater()
            self.meritlevelbox14 = None
            self.meritnamebox14 = QtWidgets.QLineEdit(self)
            self.meritlevelbox14 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 15:
            self.layout.removeWidget(self.meritnamebox15)
            self.meritnamebox15.deleteLater()
            self.meritnamebox15 = None
            self.layout.removeWidget(self.meritlevelbox15)
            self.meritlevelbox15.deleteLater()
            self.meritlevelbox15 = None
            self.meritnamebox15 = QtWidgets.QLineEdit(self)
            self.meritlevelbox15 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 16:
            self.layout.removeWidget(self.meritnamebox16)
            self.meritnamebox16.deleteLater()
            self.meritnamebox16 = None
            self.layout.removeWidget(self.meritlevelbox16)
            self.meritlevelbox16.deleteLater()
            self.meritlevelbox16 = None
            self.meritnamebox16 = QtWidgets.QLineEdit(self)
            self.meritlevelbox16 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 17:
            self.layout.removeWidget(self.meritnamebox17)
            self.meritnamebox17.deleteLater()
            self.meritnamebox17 = None
            self.layout.removeWidget(self.meritlevelbox17)
            self.meritlevelbox17.deleteLater()
            self.meritlevelbox17 = None
            self.meritnamebox17 = QtWidgets.QLineEdit(self)
            self.meritlevelbox17 = QtWidgets.QLineEdit(self)
            self.meritcounter -= 1
        if self.oldmeritcount >= 18:
            self.layout.removeWidget(self.meritnamebox18)
            self.meritnamebox18.deleteLater()
            self.meritnamebox18 = None
            self.layout.removeWidget(self.meritlevelbox18)
            self.meritlevelbox18.deleteLater()
            self.meritlevelbox18 = None
            self.meritnamebox18 = QtWidgets.QLineEdit(self)
            self.meritlevelbox18 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 19:
            self.layout.removeWidget(self.meritnamebox19)
            self.meritnamebox19.deleteLater()
            self.meritnamebox19 = None
            self.layout.removeWidget(self.meritlevelbox19)
            self.meritlevelbox19.deleteLater()
            self.meritlevelbox19 = None
            self.meritnamebox19 = QtWidgets.QLineEdit(self)
            self.meritlevelbox19 = QtWidgets.QLineEdit(self)
        if self.oldmeritcount >= 20:
            self.layout.removeWidget(self.meritnamebox20)
            self.meritnamebox20.deleteLater()
            self.meritnamebox20 = None
            self.layout.removeWidget(self.meritlevelbox20)
            self.meritlevelbox20.deleteLater()
            self.meritlevelbox20 = None
            self.meritnamebox20 = QtWidgets.QLineEdit(self)
            self.meritlevelbox20 = QtWidgets.QLineEdit(self)
        self.meritcounter = 0
        if self.meritcount >= 1:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox1, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox1, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 2:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox2, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox2, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 3:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox3, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox3, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 4:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox4, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox4, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 5:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox5, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox5, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 6:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox6, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox6, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 7:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox7, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox7, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 8:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox8, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox8, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 9:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox9, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox9, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 10:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox10, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox10, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 11:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox11, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox11, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 12:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox12, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox12, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 13:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox13, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox13, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 14:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox14, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox14, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 15:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox15, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox15, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 16:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox16, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox16, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 17:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox17, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox17, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 18:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox18, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox18, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 19:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox19, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox19, 10 + self.oplinecounter + self.meritcounter, 3)
        if self.meritcount >= 20:
            self.meritcounter += 1
            self.layout.addWidget(self.meritnamebox20, 10 + self.oplinecounter + self.meritcounter, 2)
            self.layout.addWidget(self.meritlevelbox20, 10 + self.oplinecounter + self.meritcounter, 3)

        self.setLayout(self.layout)
        self.setGeometry(300, 75, 1024, 768)

    def vamptoggledef(self):
        if self.vamptoggle.isChecked():
            self.vamptoggle.setChecked(True)
            self.occultflag[0] = True
            self.oldmeritcount = 5

            self.layout.removeWidget(self.cat3)
            self.cat3.deleteLater()
            self.cat3 = None

            self.layout.removeWidget(self.merits)
            self.merits.deleteLater()
            self.merits = None
            self.layout.removeWidget(self.meritslevel)
            self.meritslevel.deleteLater()
            self.meritslevel = None
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
            self.oplinecounter -= 2
            self.oldmeritcount = 5
            self.runonce1 = True
        self.makesheet()

    def meritdef(self):
        self.oldmeritcount = self.meritcount
        self.meritcount = int(self.meritslotsbox.text())

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

        self.vamplabel = QtWidgets.QLabel()
        self.vamplabel.setText("Character is Vampire: ")
        self.vamptoggle = QtWidgets.QCheckBox()
        self.vamptoggle.clicked.connect(self.vamptoggledef)

        self.meritslotslabel = QtWidgets.QLabel()
        self.meritslotslabel.setText("Merit Slots Available (Max 20): ")
        self.meritslotsbox = QtWidgets.QLineEdit()
        self.meritslotsbox.setText(str(self.meritcount))
        self.meritslotsupdate = QtWidgets.QPushButton('Update Merit Slots')
        self.meritslotsupdate.clicked.connect(self.meritdef)

        self.settingslayout.addWidget(self.settingstitle, 0, 1, 0, 5)

        self.settingslayout.addWidget(self.vamplabel, 1, 0)
        self.settingslayout.addWidget(self.vamptoggle, 1, 1)

        self.settingslayout.addWidget(self.meritslotslabel, 2, 0)
        self.settingslayout.addWidget(self.meritslotsbox, 2, 1)
        self.settingslayout.addWidget(self.meritslotsupdate, 2, 2)
        self.setLayout(self.layout)

    def __init__(self):
        super(MyWidget, self).__init__()

        self.setGeometry(300, 75, 1024, 768)
        self.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')

        self.oplinecounter = 0

        self.oldmeritcount = 0
        self.meritcount = 5 #max 20

        self.runonce1 = True

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

        self.makesheet()

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
