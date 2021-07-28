import sys
import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):

#if importing this character to a table i need to make sure that it's added under a in that is the name with the space

    def savesettings(self):
        settingsdict = {}
        settingsdict['meritslots'] = self.meritcount
        settingsdict['aspirationslots'] = self.aspirationcount
        settingsdict['conditionslots'] = self.conditioncount
        settingsdict['baneslots'] = self.banecount
        if self.vvflag:
            settingsdict['hasvicevirtueslots'] = True
        else:
            settingsdict['hasvicevirtueslots'] = False
        if self.occultflag[0]:
            settingsdict['hasvampireslots'] = True
        else:
            settingsdict['hasvampireslots'] = False
        if self.occultflag[0]:
            settingsdict['disciplineslots'] = self.disciplinecount
        else:
            settingsdict['disciplineslots'] = -1
        if self.occultflag[1]:
            settingsdict['haswerewolfslots'] = True
        else:
            settingsdict['haswerewolfslots'] = False
        if self.occultflag[2]:
            settingsdict['hasmageslots'] = True
        else:
            settingsdict['hasmageslots'] = False
        settingsdict['othertraitslots'] = self.othertraitcount
        settingsdict['attackslots'] = self.attackcount
        settingsdict['emalliesslots'] = self.emalliescount
        settingsdict['emmentorslots'] = self.emmentorcount
        settingsdict['emcontactsslots'] = self.emcontactscount
        settingsdict['emresourcesslots'] = self.emresourcescount
        settingsdict['emfameslots'] = self.emfamecount
        settingsdict['emretainerslots'] = self.emretainercount
        with open('settings.json', 'w') as f:
            json.dump(settingsdict, f)

    def savedef(self, saveloc):
        # if path.exists(saveloc.text()+'.json'):
        #     with open(saveloc.text()+'.json') as f:
        #         backup = json.load(f)
        #     with open(saveloc.text()+'backup.json', 'w') as f:
        #         json.dump(backup, f)

        stats = {'name': self.boxname.text(), 'supernaturaltags': [], 'player': self.boxplayer.text(), 'chronicle': self.boxchronicle.text(), 'concept': self.boxconcept.text(), 'stats': {'intelligence': self.boxintelligence.text(), 'strength': self.boxstrength.text(), 'presence': self.boxpresence.text(), 'wits': self.boxwits.text(), 'dexterity': self.boxdexterity.text(), 'manipulation': self.boxmanipulation.text(), 'resolve': self.boxresolve.text(), 'stamina': self.boxstamina.text(), 'composure': self.boxcomposure.text()}, 'skills': {'academics': self.boxacademics.text(), 'academicsspec': self.boxspecacademics.text(), 'computer': self.boxcomputer.text(), 'computerspec': self.boxspeccomputer.text(), 'crafts': self.boxcrafts.text(), 'craftsspec': self.boxspeccrafts.text(), 'investigation': self.boxinvestigation.text(), 'investigationspec': self.boxspecinvestigation.text(), 'medicine': self.boxmedicine.text(), 'medicinespec': self.boxspecmedicine.text(), 'occult': self.boxoccult.text(), 'occultspec': self.boxspecoccult.text(), 'politics': self.boxpolitics.text(), 'politicsspec': self.boxspecpolitics.text(), 'science': self.boxscience.text(), 'sciencespec': self.boxspecscience.text(), 'athletics': self.boxathletics.text(), 'athleticsspec': self.boxspecathletics.text(), 'brawl': self.boxbrawl.text(), 'brawlspec': self.boxspecbrawl.text(), 'drive': self.boxdrive.text(), 'drivespec': self.boxspecdrive.text(), 'firearms': self.boxfirearms.text(), 'firearmsspec': self.boxspecfirearms.text(), 'larceny': self.boxlarceny.text(), 'larcenyspec': self.boxspeclarceny.text(), 'stealth': self.boxstealth.text(), 'stealthspec': self.boxspecstealth.text(), 'survival': self.boxsurvival.text(), 'survivalspec': self.boxspecsurvival.text(), 'weaponry': self.boxweaponry.text(), 'weaponryspec': self.boxspecweaponry.text(), 'animalken': self.boxanimalken.text(), 'animalkenspec': self.boxspecanimalken.text(), 'empathy': self.boxempathy.text(), 'empathyspec': self.boxspecempathy.text(), 'expression': self.boxexpression.text(), 'expressionspec': self.boxspecexpression.text(), 'intimidation': self.boxintimidation.text(), 'intimidationspec': self.boxspecintimidation.text(), 'persuasion': self.boxpersuasion.text(), 'persuasionspec': self.boxspecpersuasion.text(), 'socialize': self.boxsocialize.text(), 'socializespec': self.boxspecsocialize.text(), 'streetwise': self.boxstreetwise.text(), 'streetwisespec': self.boxspecstreetwise.text(), 'subterfuge': self.boxsubterfuge.text(), 'subterfugespec': self.boxspecsubterfuge.text()}}
        if self.othertraitsflag == 0:
            if self.maxhealthmodbox.text() != "":
                stats['health'] = {'maxhealth': int(self.maxhealthmodbox.text()) + int(self.sizeval.text()) + self.staminastat}
            else:
                stats['health'] = {'maxhealth': ''}
        elif self.othertraitsflag == 1:
            if self.maxhealthbox.text() != "":
                stats['health'] = {'maxhealth': int(self.maxhealthbox.text())}
            else:
                stats['health'] = {'maxhealth': ''}
        if self.bashingdamagebox.text() != "":
            stats['health']['bashingdamage'] = int(self.bashingdamagebox.text())
        else:
            stats['health']['bashingdamage'] = 0
        if self.lethaldamagebox.text() != "":
            stats['health']['lethaldamage'] = int(self.lethaldamagebox.text())
        else:
            stats['health']['lethaldamage'] = 0
        if self.aggravateddamagebox.text() != "":
            stats['health']['aggravateddamage'] = int(self.aggravateddamagebox.text())
        else:
            stats['health']['aggravateddamage'] = 0

        stats['willpower'] = {}
        if self.willpowerdotbox.text() != "":
            stats['willpower']['willpowerdot'] = int(self.willpowerdotbox.text())
        else:
            stats['willpower']['willpowerdot'] = 2
        if self.willpowerpointbox.text() != "":
            stats['willpower']['willpowerpoint'] = int(self.willpowerpointbox.text())
        else:
            stats['willpower']['willpowerpoint'] = 2

        if self.othertraitsflag == 0:
            self.maxhealthmodlabel = QtWidgets.QLabel(self)
            self.maxhealthmodlabel.setText("Max Health Mod: ")
            self.maxhealthmodbox = QtWidgets.QLineEdit(self)

        self.maxhealthlabel = QtWidgets.QLabel(self)
        self.maxhealthlabel.setText("Max Health: ")
        self.maxhealthbox = QtWidgets.QLabel(self)
        if self.othertraitsflag == 0:
            if self.maxhealthmodbox.text() != "":
                self.maxhealthbox.setText(str(int(self.maxhealthmodbox.text()) + int(self.sizeval.text()) + self.staminastat))
            else:
                self.maxhealthbox.setText(str(6))
        elif self.othertraitsflag == 1:
            if self.maxhealthbox.text() != "":
                self.maxhealthbox.setText(str(int(self.maxhealthbox.text())))
            else:
                self.maxhealthbox.setText(str(6))

        self.bashingdamagelabel = QtWidgets.QLabel(self)
        self.bashingdamagelabel.setText("Bashing Damage: ")
        self.bashingdamagebox = QtWidgets.QLineEdit(self)

        self.lethaldamagelabel = QtWidgets.QLabel(self)
        self.lethaldamagelabel.setText("Lethal Damage: ")
        self.lethaldamagebox = QtWidgets.QLineEdit(self)

        self.aggravateddamagelabel = QtWidgets.QLabel(self)
        self.aggravateddamagelabel.setText("Aggravated Damage: ")
        self.aggravateddamagebox = QtWidgets.QLineEdit(self)

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
            if self.bloodpotencybox.text() != "":
                stats['bloodpotency'] = int(self.bloodpotencybox.text())
            else:
                stats['bloodpotency'] = 1

            stats['vitae'] = {}
            if self.maxvitaebox.text() != "":
                stats['vitae']['maxvitae'] = int(self.maxvitaebox.text())
            else:
                stats['vitae']['maxvitae'] = 10
            if self.currentvitaebox.text() != "":
                stats['vitae']['currentvitae'] = int(self.currentvitaebox.text())
            else:
                stats['vitae']['currentvitae'] = 0

            stats['humanity'] = {}
            stats['humanity']['humanityarray'] = []
            if self.humanitybox1.text() != "":
                stats['humanity']['touchstone1'] = self.humanitybox1.text()
            else:
                stats['humanity']['touchstone1'] = ""
            if self.humanitycheck1.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)
            if self.humanitybox2.text() != "":
                stats['humanity']['touchstone2'] = self.humanitybox2.text()
            else:
                stats['humanity']['touchstone2'] = ""
            if self.humanitycheck2.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)
            if self.humanitybox3.text() != "":
                stats['humanity']['touchstone3'] = self.humanitybox3.text()
            else:
                stats['humanity']['touchstone3'] = ""
            if self.humanitycheck3.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)
            if self.humanitybox4.text() != "":
                stats['humanity']['touchstone4'] = self.humanitybox4.text()
            else:
                stats['humanity']['touchstone4'] = ""
            if self.humanitycheck4.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)
            if self.humanitybox5.text() != "":
                stats['humanity']['touchstone5'] = self.humanitybox5.text()
            else:
                stats['humanity']['touchstone5'] = ""
            if self.humanitycheck5.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)
            if self.humanitybox6.text() != "":
                stats['humanity']['touchstone6'] = self.humanitybox6.text()
            else:
                stats['humanity']['touchstone6'] = ""
            if self.humanitycheck6.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)
            if self.humanitybox7.text() != "":
                stats['humanity']['touchstone7'] = self.humanitybox7.text()
            else:
                stats['humanity']['touchstone7'] = ""
            if self.humanitycheck7.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)
            if self.humanitybox8.text() != "":
                stats['humanity']['touchstone8'] = self.humanitybox8.text()
            else:
                stats['humanity']['touchstone8'] = ""
            if self.humanitycheck8.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)
            if self.humanitybox9.text() != "":
                stats['humanity']['touchstone9'] = self.humanitybox9.text()
            else:
                stats['humanity']['touchstone9'] = ""
            if self.humanitycheck9.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)
            if self.humanitybox10.text() != "":
                stats['humanity']['touchstone10'] = self.humanitybox10.text()
            else:
                stats['humanity']['touchstone10'] = ""
            if self.humanitycheck10.isChecked():
                stats['humanity']['humanityarray'].append(True)
            else:
                stats['humanity']['humanityarray'].append(False)

        if self.occultflag[1] == True:
            stats['supernaturaltags'].append('werewolf')
            stats['blood'] = self.boxblood.text()
            stats['bone'] = self.boxbone.text()
            stats['auspice'] = self.boxauspice.text()
            stats['tribe'] = self.boxtribe.text()
            stats['lodge'] = self.boxlodge.text()

            stats['renown'] = {}
            stats['renown']['purity'] = self.puritybox.text()
            stats['renown']['glory'] = self.glorybox.text()
            stats['renown']['honor'] = self.honorbox.text()
            stats['renown']['wisdom'] = self.wisdombox.text()
            stats['renown']['cunning'] = self.cunningbox.text()

            stats['primalurge'] = self.primalurgebox.text()
            stats['essence'] = {}
            stats['essence']['maxessence'] = self.maxessencebox.text()
            stats['essence']['currentessence'] = self.currentessencebox.text()
            stats['harmony'] = self.harmonybox.text()
            stats['fleshtouchstone'] = self.fleshtouchstonebox.text()
            stats['spirittouchstone'] = self.spirittouchstonebox.text()

            stats['kuruth'] = {}
            stats['kuruth']['passive'] = self.passivekuruthbox.toPlainText()
            stats['kuruth']['common'] = self.commonkuruthbox.toPlainText()
            stats['kuruth']['specific'] = self.specifickuruthbox.toPlainText()

        if self.occultflag[2] == True:
            stats['supernaturaltags'].append('mage')
            stats['shadowname'] = self.shadownamebox.text()

            stats['path'] = self.pathbox.text()
            stats['order'] = self.orderbox.text()
            stats['legacy'] = self.legacybox.text()

            stats['arcana'] = {}
            stats['arcana']['death'] = self.deathbox.text()
            stats['arcana']['fate'] = self.fatebox.text()
            stats['arcana']['forces'] = self.forcesbox.text()
            stats['arcana']['life'] = self.lifebox.text()
            stats['arcana']['matter'] = self.matterbox.text()
            stats['arcana']['mind'] = self.mindbox.text()
            stats['arcana']['prime'] = self.primebox.text()
            stats['arcana']['spirit'] = self.spiritbox.text()
            stats['arcana']['space'] = self.spacebox.text()
            stats['arcana']['time'] = self.timebox.text()

            stats['obsessions'] = []
            stats['obsessions'].append(self.obsession1box.text())
            stats['obsessions'].append(self.obsession2box.text())
            stats['obsessions'].append(self.obsession3box.text())
            stats['obsessions'].append(self.obsession4box.text())

            stats['gnosis'] = self.gnosisbox.text()
            stats['mana'] = {}
            stats['mana']['maxmana'] = self.maxmanabox.text()
            stats['mana']['currentmana'] = self.currentmanabox.text()
            stats['wisdom'] = self.mwisdombox.text()

            stats['arcaneexperience'] = {}
            stats['arcaneexperience']['arcaneexperiences'] = self.arcaneexperiencesbox.text()
            stats['arcaneexperience']['arcanebeats'] = [self.arcanebeat1.isChecked(), self.arcanebeat2.isChecked(), self.arcanebeat3.isChecked(), self.arcanebeat4.isChecked(), self.arcanebeat5.isChecked()]

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

        if self.othertraitsflag == 0:
            stats['size'] = 5 + self.sizebonus
        elif self.othertraitsflag == 1:
            stats['size'] = self.sizeval.text()

        if self.othertraitsflag == 0:
            stats['speed'] = int(self.sizeval.text()) + self.strengthstat + self.dexteritystat + self.speedbonus
        elif self.othertraitsflag == 1:
            stats['speed'] = self.speedval.text()

        if self.othertraitsflag == 0:
            if self.dexteritystat <= self.witsstat:
                stats['defense'] = self.athleticsskill + self.dexteritystat + self.defensebonus
            else:
                stats['defense'] = self.athleticsskill + self.witsstat + self.defensebonus
        elif self.othertraitsflag == 1:
            stats['defense'] = self.defenseval.text()

        if self.othertraitsflag == 0:
            stats['armor'] = self.armorbonus
        elif self.othertraitsflag == 1:
            stats['armor'] = self.armorval.text()

        if self.othertraitsflag == 0:
            stats['initiative'] = self.composurestat + self.dexteritystat + self.initiativebonus
        elif self.othertraitsflag == 1:
            stats['initiative'] = self.initiativeval.text()

        stats['experience'] = {}
        stats['experience']['experiences'] = self.experiencesbox.text()
        stats['experience']['beats'] = [self.beat1.isChecked(), self.beat2.isChecked(), self.beat3.isChecked(), self.beat4.isChecked(), self.beat5.isChecked()]

        self.filledothertraits = 0
        stats['othertraits'] = []
        stats['othertraits'].append(['filledothertraits', 0])
        for x in range(self.othertraitcount):
            if self.othertraitcount >= x and self.othertraitnamebox[x].text() != "" and self.othertraitlevelbox[x].text() != "":
                stats['othertraits'].append([self.othertraitnamebox[x].text(), self.othertraitlevelbox[x].text()])
                self.filledothertraits += 1
        stats['othertraits'][0] = ['filledothertraits', self.filledothertraits]

        self.filledattacks = 0
        stats['attacks'] = []
        stats['attacks'].append(['filledattacks', 0])
        for x in range(self.attackcount):
            if self.attackcount >= x and self.attacknamebox[x].text() != "":
                stats['attacks'].append([self.attacknamebox[x].text(), self.attackdamagebox[x].text(), self.attackrangebox[x].text(), self.attackclipbox[x].text(), self.attackinitiativebox[x].text(), self.attackstrengthbox[x].text(), self.attacksizebox[x].text()])
                self.filledattacks += 1
        stats['attacks'][0] = ['filledattacks', self.filledattacks]

        stats['armorp2'] = {}
        stats['armorp2']['rating'] = self.armorratingbox.text()
        stats['armorp2']['strength'] = self.armorstrengthbox.text()
        stats['armorp2']['defense'] = self.armordefensebox.text()
        stats['armorp2']['speed'] = self.armorspeedbox.text()
        stats['armorp2']['description'] = self.armordescriptionbox.toPlainText()

        stats['expandedmerits'] = {}

        self.filledemallies = 0
        stats['expandedmerits']['emallies'] = []
        stats['expandedmerits']['emallies'].append(['filledemallies', 0])
        for x in range(self.emalliescount):
            if self.emalliescount >= x and self.emalliesbox[x].toPlainText() != "":
                stats['expandedmerits']['emallies'].append(self.emalliesbox[x].toPlainText())
                self.filledemallies += 1
        stats['expandedmerits']['emallies'][0] = ['filledemallies', self.filledemallies]

        self.filledemmentor = 0
        stats['expandedmerits']['emmentor'] = []
        stats['expandedmerits']['emmentor'].append(['filledemmentor', 0])
        for x in range(self.emmentorcount):
            if self.emmentorcount >= x and self.emmentorbox[x].toPlainText() != "":
                stats['expandedmerits']['emmentor'].append(self.emmentorbox[x].toPlainText())
                self.filledemmentor += 1
        stats['expandedmerits']['emmentor'][0] = ['filledemmentor', self.filledemmentor]

        self.filledemcontacts = 0
        stats['expandedmerits']['emcontacts'] = []
        stats['expandedmerits']['emcontacts'].append(['filledemcontacts', 0])
        for x in range(self.emcontactscount):
            if self.emcontactscount >= x and self.emcontactsbox[x].toPlainText() != "":
                stats['expandedmerits']['emcontacts'].append(self.emcontactsbox[x].toPlainText())
                self.filledemcontacts += 1
        stats['expandedmerits']['emcontacts'][0] = ['filledemcontacts', self.filledemcontacts]

        self.filledemresources = 0
        stats['expandedmerits']['emresources'] = []
        stats['expandedmerits']['emresources'].append(['filledemresources', 0])
        for x in range(self.emresourcescount):
            if self.emresourcescount >= x and self.emresourcesbox[x].toPlainText() != "":
                stats['expandedmerits']['emresources'].append(self.emresourcesbox[x].toPlainText())
                self.filledemresources += 1
        stats['expandedmerits']['emresources'][0] = ['filledemresources', self.filledemresources]

        self.filledemfame = 0
        stats['expandedmerits']['emfame'] = []
        stats['expandedmerits']['emfame'].append(['filledemfame', 0])
        for x in range(self.emfamecount):
            if self.emfamecount >= x and self.emfamebox[x].toPlainText() != "":
                stats['expandedmerits']['emfame'].append(self.emfamebox[x].toPlainText())
                self.filledemfame += 1
        stats['expandedmerits']['emfame'][0] = ['filledemfame', self.filledemfame]

        self.filledemretainer = 0
        stats['expandedmerits']['emretainer'] = []
        stats['expandedmerits']['emretainer'].append(['filledemretainer', 0])
        for x in range(self.emretainercount):
            if self.emretainercount >= x and self.emretainerbox[x].toPlainText() != "":
                stats['expandedmerits']['emretainer'].append(self.emretainerbox[x].toPlainText())
                self.filledemretainer += 1
        stats['expandedmerits']['emretainer'][0] = ['filledemretainer', self.filledemretainer]

        with open(saveloc, 'w') as f:
            json.dump(stats, f)

        self.savesettings()

    def humanitycheckdef(self, num):
        if num == 1:
            # print('test')
            if self.humanitycheck1.isChecked():
                self.humanitycheck1.setChecked(True)
            else:
                self.humanitycheck1.setChecked(False)
        elif num == 2:
            if self.humanitycheck2.isChecked():
                self.humanitycheck2.setChecked(True)
            else:
                self.humanitycheck2.setChecked(False)
        elif num == 3:
            if self.humanitycheck3.isChecked():
                self.humanitycheck3.setChecked(True)
            else:
                self.humanitycheck3.setChecked(False)
        elif num == 4:
            if self.humanitycheck4.isChecked():
                self.humanitycheck4.setChecked(True)
            else:
                self.humanitycheck4.setChecked(False)
        elif num == 5:
            if self.humanitycheck5.isChecked():
                self.humanitycheck5.setChecked(True)
            else:
                self.humanitycheck5.setChecked(False)
        elif num == 6:
            if self.humanitycheck6.isChecked():
                self.humanitycheck6.setChecked(True)
            else:
                self.humanitycheck6.setChecked(False)
        elif num == 7:
            if self.humanitycheck7.isChecked():
                self.humanitycheck7.setChecked(True)
            else:
                self.humanitycheck7.setChecked(False)
        elif num == 8:
            if self.humanitycheck8.isChecked():
                self.humanitycheck8.setChecked(True)
            else:
                self.humanitycheck8.setChecked(False)
        elif num == 9:
            if self.humanitycheck9.isChecked():
                self.humanitycheck9.setChecked(True)
            else:
                self.humanitycheck9.setChecked(False)
        elif num == 10:
            if self.humanitycheck10.isChecked():
                self.humanitycheck10.setChecked(True)
            else:
                self.humanitycheck10.setChecked(False)

    def beatscheckdef(self, num):
        if num == 1:
            # print('test')
            if self.beat1.isChecked():
                self.beat1.setChecked(True)
            else:
                self.beat1.setChecked(False)
        elif num == 2:
            if self.beat2.isChecked():
                self.beat2.setChecked(True)
            else:
                self.beat2.setChecked(False)
        elif num == 3:
            if self.beat3.isChecked():
                self.beat3.setChecked(True)
            else:
                self.beat3.setChecked(False)
        elif num == 4:
            if self.beat4.isChecked():
                self.beat4.setChecked(True)
            else:
                self.beat4.setChecked(False)
        elif num == 5:
            if self.beat5.isChecked():
                self.beat5.setChecked(True)
            else:
                self.beat5.setChecked(False)

    def arcanebeatscheckdef(self, num):
        if num == 1:
            # print('test')
            if self.arcanebeat1.isChecked():
                self.arcanebeat1.setChecked(True)
            else:
                self.arcanebeat1.setChecked(False)
        elif num == 2:
            if self.arcanebeat2.isChecked():
                self.arcanebeat2.setChecked(True)
            else:
                self.arcanebeat2.setChecked(False)
        elif num == 3:
            if self.arcanebeat3.isChecked():
                self.arcanebeat3.setChecked(True)
            else:
                self.arcanebeat3.setChecked(False)
        elif num == 4:
            if self.arcanebeat4.isChecked():
                self.arcanebeat4.setChecked(True)
            else:
                self.arcanebeat4.setChecked(False)
        elif num == 5:
            if self.arcanebeat5.isChecked():
                self.arcanebeat5.setChecked(True)
            else:
                self.arcanebeat5.setChecked(False)

    def addvvdef(self):
        if self.vvflag == False:
            self.virtue = QtWidgets.QLabel(self)
            self.virtue.setText("Virtue: ")
            self.boxvirtue = QtWidgets.QLineEdit(self)
            self.vice = QtWidgets.QLabel(self)
            self.vice.setText("Vice: ")
            self.boxvice = QtWidgets.QLineEdit(self)

            self.layout.addWidget(self.concept, 4, 1)
            self.layout.addWidget(self.boxconcept, 4, 2)
            self.layout.addWidget(self.vice, 4, 3)
            self.layout.addWidget(self.boxvice, 4, 4)
            self.layout.addWidget(self.virtue, 4, 5)
            self.layout.addWidget(self.boxvirtue, 4, 6)

    def addvampdef(self):
        if self.occultflag[0] == False:
            self.occultflag[0] = True
            self.oldmeritcount = self.meritcount
            self.oldaspirationcount = self.aspirationcount
            self.oldconditioncount = self.conditioncount
            self.oldbanecount = self.banecount

            self.disciplines = QtWidgets.QLabel(self)
            self.disciplines.setText("Disciplines")
            self.disciplines.setFont(self.subtitlefont)
            self.disciplineslevel = QtWidgets.QLabel(self)
            self.disciplineslevel.setText("Level")

            self.bloodpotencytitle = QtWidgets.QLabel(self)
            self.bloodpotencytitle.setText("Blood Potency")
            self.bloodpotencytitle.setFont(self.subtitlefont)

            self.bloodpotencylabel = QtWidgets.QLabel(self)
            self.bloodpotencylabel.setText("Blood Potency: ")
            self.bloodpotencybox = QtWidgets.QLineEdit(self)

            self.vitaetitle = QtWidgets.QLabel(self)
            self.vitaetitle.setText("Vitae")
            self.vitaetitle.setFont(self.subtitlefont)

            self.maxvitaelabel = QtWidgets.QLabel(self)
            self.maxvitaelabel.setText("Max Vitae: ")
            self.maxvitaebox = QtWidgets.QLineEdit(self)

            self.currentvitaelabel = QtWidgets.QLabel(self)
            self.currentvitaelabel.setText("Current Vitae: ")
            self.currentvitaebox = QtWidgets.QLineEdit(self)


            self.humanitytitle = QtWidgets.QLabel(self)
            self.humanitytitle.setText("Humanity")
            self.humanitytitle.setFont(self.subtitlefont)

            self.num1 = QtWidgets.QLabel(self)
            self.num1.setText("1")
            self.num2 = QtWidgets.QLabel(self)
            self.num2.setText("2")
            self.num3 = QtWidgets.QLabel(self)
            self.num3.setText("3")
            self.num4 = QtWidgets.QLabel(self)
            self.num4.setText("4")
            self.num5 = QtWidgets.QLabel(self)
            self.num5.setText("5")
            self.num6 = QtWidgets.QLabel(self)
            self.num6.setText("6")
            self.num7 = QtWidgets.QLabel(self)
            self.num7.setText("7")
            self.num8 = QtWidgets.QLabel(self)
            self.num8.setText("8")
            self.num9 = QtWidgets.QLabel(self)
            self.num9.setText("9")
            self.num10 = QtWidgets.QLabel(self)
            self.num10.setText("10")

            self.humanitybox1 = QtWidgets.QLineEdit(self)
            self.humanitybox2 = QtWidgets.QLineEdit(self)
            self.humanitybox3 = QtWidgets.QLineEdit(self)
            self.humanitybox4 = QtWidgets.QLineEdit(self)
            self.humanitybox5 = QtWidgets.QLineEdit(self)
            self.humanitybox6 = QtWidgets.QLineEdit(self)
            self.humanitybox7 = QtWidgets.QLineEdit(self)
            self.humanitybox8 = QtWidgets.QLineEdit(self)
            self.humanitybox9 = QtWidgets.QLineEdit(self)
            self.humanitybox10 = QtWidgets.QLineEdit(self)

            self.humanitycheck1 = QtWidgets.QCheckBox()
            self.humanitycheck1.clicked.connect(self.humanitycheckdef(1))
            self.humanitycheck2 = QtWidgets.QCheckBox()
            self.humanitycheck2.clicked.connect(self.humanitycheckdef(2))
            self.humanitycheck3 = QtWidgets.QCheckBox()
            self.humanitycheck3.clicked.connect(self.humanitycheckdef(3))
            self.humanitycheck4 = QtWidgets.QCheckBox()
            self.humanitycheck4.clicked.connect(self.humanitycheckdef(4))
            self.humanitycheck5 = QtWidgets.QCheckBox()
            self.humanitycheck5.clicked.connect(self.humanitycheckdef(5))
            self.humanitycheck6 = QtWidgets.QCheckBox()
            self.humanitycheck6.clicked.connect(self.humanitycheckdef(6))
            self.humanitycheck7 = QtWidgets.QCheckBox()
            self.humanitycheck7.clicked.connect(self.humanitycheckdef(7))
            self.humanitycheck8 = QtWidgets.QCheckBox()
            self.humanitycheck8.clicked.connect(self.humanitycheckdef(8))
            self.humanitycheck9 = QtWidgets.QCheckBox()
            self.humanitycheck9.clicked.connect(self.humanitycheckdef(9))
            self.humanitycheck10 = QtWidgets.QCheckBox()
            self.humanitycheck10.clicked.connect(self.humanitycheckdef(10))

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
            self.layout.addWidget(self.clan, 4 + self.oplinecounter, 1)
            self.layout.addWidget(self.boxclan, 4 + self.oplinecounter, 2)
            self.layout.addWidget(self.bloodline, 4 + self.oplinecounter, 3)
            self.layout.addWidget(self.boxbloodline, 4 + self.oplinecounter, 4)
            self.layout.addWidget(self.covenant, 4 + self.oplinecounter, 5)
            self.layout.addWidget(self.boxcovenant, 4 + self.oplinecounter, 6)

            self.oplinecounter += 1
            self.layout.addWidget(self.mask, 4 + self.oplinecounter, 2)
            self.layout.addWidget(self.boxmask, 4 + self.oplinecounter, 3)
            self.layout.addWidget(self.dirge, 4 + self.oplinecounter, 4)
            self.layout.addWidget(self.boxdirge, 4 + self.oplinecounter, 5)

            self.layout.addWidget(self.disciplines, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.disciplineslevel, 15 + self.oplinecounter + self.p1c2counter, 4)

            #disciplines
            for x in range(self.disciplinecount):
                if self.disciplinecount >= 1:
                    self.p1c2counter += 1
                    self.layout.addWidget(self.disciplinenamebox[x], 15 + self.oplinecounter + self.p1c2counter, 3)
                    self.layout.addWidget(self.disciplinelevelbox[x], 15 + self.oplinecounter + self.p1c2counter, 4)
                    if x < len(self.saveddisciplinenames):
                        self.disciplinenamebox[x].setText(self.saveddisciplinenames[x].text())
                        self.disciplinelevelbox[x].setText(self.saveddisciplinelevels[x].text())

            self.saveddisciplinenames = []
            self.saveddisciplinelevels = []

            self.p1c3counter += 1
            self.layout.addWidget(self.bloodpotencytitle, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.bloodpotencylabel, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.bloodpotencybox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.vitaetitle, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.maxvitaelabel, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.maxvitaebox, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.currentvitaelabel, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.currentvitaebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.humanitytitle, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.num1, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox1, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck1, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num2, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox2, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck2, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num3, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox3, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck3, 24 + self.oplinecounter  + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num4, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox4, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck4, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num5, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox5, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck5, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num6, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox6, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck6, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num7, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox7, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck7, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num8, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox8, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck8, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num9, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox9, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck9, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num10, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox10, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck10, 24 + self.oplinecounter + self.p1c3counter, 7)

    def addwolfdef(self):
        if self.occultflag[1] == False:
            self.whealth = True

            self.whealthcounter = 0

            self.whealthtext1 = QtWidgets.QLabel(self)
            self.whealthtext1.setText("(+2 Dalu Form, +4 Gauru")
            self.whealthtext2 = QtWidgets.QLabel(self)
            self.whealthtext2.setText("Form, +3 Urshul Form)")

            # if self.runonce3:
            self.auspice = QtWidgets.QLabel(self)
            self.auspice.setText("Auspice: ")
            self.boxauspice = QtWidgets.QLineEdit(self)
            self.tribe = QtWidgets.QLabel(self)
            self.tribe.setText("Tribe: ")
            self.boxtribe = QtWidgets.QLineEdit(self)
            self.lodge = QtWidgets.QLabel(self)
            self.lodge.setText("Lodge: ")
            self.boxlodge = QtWidgets.QLineEdit(self)

            self.blood = QtWidgets.QLabel(self)
            self.blood.setText("Blood: ")
            self.boxblood = QtWidgets.QLineEdit(self)
            self.bone = QtWidgets.QLabel(self)
            self.bone.setText("Bone: ")
            self.boxbone = QtWidgets.QLineEdit(self)

            self.renown = QtWidgets.QLabel(self)
            self.renown.setText("Renown")
            self.renown.setFont(self.subtitlefont)

            self.purity = QtWidgets.QLabel(self)
            self.purity.setText("Purity: ")
            self.puritybox = QtWidgets.QLineEdit(self)

            self.glory = QtWidgets.QLabel(self)
            self.glory.setText("Glory: ")
            self.glorybox = QtWidgets.QLineEdit(self)

            self.honor = QtWidgets.QLabel(self)
            self.honor.setText("Honor: ")
            self.honorbox = QtWidgets.QLineEdit(self)

            self.wisdom = QtWidgets.QLabel(self)
            self.wisdom.setText("Wisdom: ")
            self.wisdombox = QtWidgets.QLineEdit(self)

            self.cunning = QtWidgets.QLabel(self)
            self.cunning.setText("Cunning: ")
            self.cunningbox = QtWidgets.QLineEdit(self)

            self.primalurgetitle = QtWidgets.QLabel(self)
            self.primalurgetitle.setText("Primal Urge")
            self.primalurgetitle.setFont(self.subtitlefont)

            self.primalurge = QtWidgets.QLabel(self)
            self.primalurge.setText("Primal Urge: ")
            self.primalurgebox = QtWidgets.QLineEdit(self)

            self.essencetitle = QtWidgets.QLabel(self)
            self.essencetitle.setText("Essence")
            self.essencetitle.setFont(self.subtitlefont)

            self.maxessence = QtWidgets.QLabel(self)
            self.maxessence.setText("Max Essence: ")
            self.maxessencebox = QtWidgets.QLineEdit(self)

            self.currentessence = QtWidgets.QLabel(self)
            self.currentessence.setText("Current Essence: ")
            self.currentessencebox = QtWidgets.QLineEdit(self)

            self.harmonytitle = QtWidgets.QLabel(self)
            self.harmonytitle.setText("Harmony")
            self.harmonytitle.setFont(self.subtitlefont)

            self.harmony = QtWidgets.QLabel(self)
            self.harmony.setText("Harmony: ")
            self.harmonybox = QtWidgets.QLineEdit(self)

            self.fleshtouchstonetitle = QtWidgets.QLabel(self)
            self.fleshtouchstonetitle.setText("Flesh Touchstone")
            self.fleshtouchstonetitle.setFont(self.subtitlefont)

            self.fleshtouchstone = QtWidgets.QLabel(self)
            self.fleshtouchstone.setText("Flesh Touchstone: ")
            self.fleshtouchstonebox = QtWidgets.QLineEdit(self)

            self.spirittouchstonetitle = QtWidgets.QLabel(self)
            self.spirittouchstonetitle.setText("Spirit Touchstone")
            self.spirittouchstonetitle.setFont(self.subtitlefont)

            self.spirittouchstone = QtWidgets.QLabel(self)
            self.spirittouchstone.setText("Spirit Touchstone: ")
            self.spirittouchstonebox = QtWidgets.QLineEdit(self)

            self.passivekuruth = QtWidgets.QLabel(self)
            self.passivekuruth.setText("Passive Kuruth Trigger: ")
            self.passivekuruthbox = QtWidgets.QTextEdit(self)

            self.commonkuruth = QtWidgets.QLabel(self)
            self.commonkuruth.setText("Common Kuruth Trigger: ")
            self.commonkuruthbox = QtWidgets.QTextEdit(self)

            self.specifickuruth = QtWidgets.QLabel(self)
            self.specifickuruth.setText("Specific Kuruth Trigger: ")
            self.specifickuruthbox = QtWidgets.QTextEdit(self)

            self.p1c2counter += 1
            self.layout.addWidget(self.renown, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.purity, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.puritybox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.glory, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.glorybox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.honor, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.honorbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.wisdom, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.wisdombox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.cunning, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.cunningbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c3counter += 1
            self.layout.addWidget(self.primalurgetitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.primalurge, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.primalurgebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.essencetitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.maxessence, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.maxessencebox, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.currentessence, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.currentessencebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.fleshtouchstonetitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.fleshtouchstone, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.fleshtouchstonebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.harmonytitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.harmony, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.harmonybox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.spirittouchstonetitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.spirittouchstone, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.spirittouchstonebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.passivekuruth, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.passivekuruthbox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.commonkuruth, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.commonkuruthbox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.specifickuruth, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.specifickuruthbox, 24 + self.oplinecounter + self.p1c3counter, 6)

    def addmagedef(self):
        if self.occultflag[2] == False:
            self.shadowname = QtWidgets.QLabel(self)
            self.shadowname.setText("Shadow Name: ")
            self.shadownamebox = QtWidgets.QLineEdit(self)

            self.path = QtWidgets.QLabel(self)
            self.path.setText("Path: ")
            self.pathbox = QtWidgets.QLineEdit(self)
            self.order = QtWidgets.QLabel(self)
            self.order.setText("Order: ")
            self.orderbox = QtWidgets.QLineEdit(self)
            self.legacy = QtWidgets.QLabel(self)
            self.legacy.setText("Legacy: ")
            self.legacybox = QtWidgets.QLineEdit(self)

            self.arcana = QtWidgets.QLabel(self)
            self.arcana.setText("Arcana")
            self.arcana.setFont(self.subtitlefont)

            self.death = QtWidgets.QLabel(self)
            self.death.setText("Death: ")
            self.deathbox = QtWidgets.QLineEdit(self)

            self.fate = QtWidgets.QLabel(self)
            self.fate.setText("Fate: ")
            self.fatebox = QtWidgets.QLineEdit(self)

            self.forces = QtWidgets.QLabel(self)
            self.forces.setText("Forces: ")
            self.forcesbox = QtWidgets.QLineEdit(self)

            self.life = QtWidgets.QLabel(self)
            self.life.setText("Life: ")
            self.lifebox = QtWidgets.QLineEdit(self)

            self.matter = QtWidgets.QLabel(self)
            self.matter.setText("Matter: ")
            self.matterbox = QtWidgets.QLineEdit(self)

            self.mind = QtWidgets.QLabel(self)
            self.mind.setText("Mind: ")
            self.mindbox = QtWidgets.QLineEdit(self)

            self.prime = QtWidgets.QLabel(self)
            self.prime.setText("Prime: ")
            self.primebox = QtWidgets.QLineEdit(self)

            self.spirit = QtWidgets.QLabel(self)
            self.spirit.setText("Spirit: ")
            self.spiritbox = QtWidgets.QLineEdit(self)

            self.space = QtWidgets.QLabel(self)
            self.space.setText("Space: ")
            self.spacebox = QtWidgets.QLineEdit(self)

            self.time = QtWidgets.QLabel(self)
            self.time.setText("Time: ")
            self.timebox = QtWidgets.QLineEdit(self)

            self.gnosistitle = QtWidgets.QLabel(self)
            self.gnosistitle.setText("Gnosis")
            self.gnosistitle.setFont(self.subtitlefont)

            self.gnosis = QtWidgets.QLabel(self)
            self.gnosis.setText("Gnosis: ")
            self.gnosisbox = QtWidgets.QLineEdit(self)

            self.manatitle = QtWidgets.QLabel(self)
            self.manatitle.setText("Mana")
            self.manatitle.setFont(self.subtitlefont)

            self.maxmana = QtWidgets.QLabel(self)
            self.maxmana.setText("Max Mana: ")
            self.maxmanabox = QtWidgets.QLineEdit(self)

            self.currentmana = QtWidgets.QLabel(self)
            self.currentmana.setText("Current Mana: ")
            self.currentmanabox = QtWidgets.QLineEdit(self)

            self.mwisdomtitle = QtWidgets.QLabel(self)
            self.mwisdomtitle.setText("Wisdom")
            self.mwisdomtitle.setFont(self.subtitlefont)

            self.mwisdom = QtWidgets.QLabel(self)
            self.mwisdom.setText("Wisdom: ")
            self.mwisdombox = QtWidgets.QLineEdit(self)

            self.obsessiontitle = QtWidgets.QLabel(self)
            self.obsessiontitle.setText("Obsessions")
            self.obsessiontitle.setFont(self.subtitlefont)

            self.obsession1 = QtWidgets.QLabel(self)
            self.obsession1.setText("Obsession 1: ")
            self.obsession1box = QtWidgets.QLineEdit(self)

            self.obsession2 = QtWidgets.QLabel(self)
            self.obsession2.setText("Obsession 2: ")
            self.obsession2box = QtWidgets.QLineEdit(self)

            self.obsession3 = QtWidgets.QLabel(self)
            self.obsession3.setText("Obsession 3: ")
            self.obsession3box = QtWidgets.QLineEdit(self)

            self.obsession4 = QtWidgets.QLabel(self)
            self.obsession4.setText("Obsession 4: ")
            self.obsession4box = QtWidgets.QLineEdit(self)

            self.arcaneexperiences = QtWidgets.QLabel(self)
            self.arcaneexperiences.setText("Arcane Experiences:")
            self.arcaneexperiencesbox = QtWidgets.QLineEdit(self)

            self.arcanebeats = QtWidgets.QLabel(self)
            self.arcanebeats.setText("Arcane Beats:")
            self.arcanebeat1 = QtWidgets.QCheckBox()
            self.arcanebeat1.clicked.connect(self.arcanebeatscheckdef(1))
            self.arcanebeat2 = QtWidgets.QCheckBox()
            self.arcanebeat2.clicked.connect(self.arcanebeatscheckdef(2))
            self.arcanebeat3 = QtWidgets.QCheckBox()
            self.arcanebeat3.clicked.connect(self.arcanebeatscheckdef(3))
            self.arcanebeat4 = QtWidgets.QCheckBox()
            self.arcanebeat4.clicked.connect(self.arcanebeatscheckdef(4))
            self.arcanebeat5 = QtWidgets.QCheckBox()
            self.arcanebeat5.clicked.connect(self.arcanebeatscheckdef(5))

            self.p1c2counter += 1
            self.layout.addWidget(self.arcana, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.death, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.deathbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.fate, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.fatebox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.forces, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.forcesbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.life, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.lifebox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.matter, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.matterbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.mind, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.mindbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.prime, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.primebox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.spirit, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.spiritbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.space, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.spacebox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.time, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.timebox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c3counter += 1
            self.layout.addWidget(self.gnosistitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.gnosis, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.gnosisbox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.manatitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.maxmana, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.maxmanabox, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.currentmana, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.currentmanabox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.mwisdomtitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.mwisdom, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.mwisdombox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.obsessiontitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.obsession1, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.obsession1box, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.obsession2, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.obsession2box, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.obsession3, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.obsession3box, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.obsession4, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.obsession4box, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.arcaneexperiences, 29 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.arcaneexperiencesbox, 29 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.arcanebeats, 29 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.arcanebeat1, 29 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.arcanebeat2, 29 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.arcanebeat3, 29 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.arcanebeat4, 29 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.arcanebeat5, 29 + self.oplinecounter + self.p1c3counter, 6)

    def loaddef(self, loadloc):
        if path.exists(loadloc):
            with open(loadloc) as f:
                stats = json.load(f)

                for x in stats.get('supernaturaltags'):
                    if x == 'human':
                        self.addvvdef()
                    if x == 'vampire':
                        self.addvampdef()
                    if x == 'werewolf':
                        self.addwolfdef()
                    if x == 'mage':
                        self.addmagedef()

                self.boxname.setText(stats.get('name'))
                self.boxplayer.setText(stats.get('player'))
                self.boxchronicle.setText(stats.get('chronicle'))
                self.boxconcept.setText(stats.get('concept'))

                self.boxintelligence.setText(stats.get('stats').get('intelligence'))
                self.boxstrength.setText(stats.get('stats').get('strength'))
                self.boxpresence.setText(stats.get('stats').get('presence'))
                self.boxwits.setText(stats.get('stats').get('wits'))
                self.boxdexterity.setText(stats.get('stats').get('dexterity'))
                self.boxmanipulation.setText(stats.get('stats').get('manipulation'))
                self.boxresolve.setText(stats.get('stats').get('resolve'))
                self.boxstamina.setText(stats.get('stats').get('stamina'))
                self.boxcomposure.setText(stats.get('stats').get('composure'))

                self.boxacademics.setText(stats.get('skills').get('academics'))
                self.boxcomputer.setText(stats.get('skills').get('computer'))
                self.boxcrafts.setText(stats.get('skills').get('crafts'))
                self.boxinvestigation.setText(stats.get('skills').get('investigation'))
                self.boxmedicine.setText(stats.get('skills').get('medicine'))
                self.boxoccult.setText(stats.get('skills').get('occult'))
                self.boxpolitics.setText(stats.get('skills').get('politics'))
                self.boxscience.setText(stats.get('skills').get('science'))
                self.boxathletics.setText(stats.get('skills').get('athletics'))
                self.boxbrawl.setText(stats.get('skills').get('brawl'))
                self.boxdrive.setText(stats.get('skills').get('drive'))
                self.boxfirearms.setText(stats.get('skills').get('firearms'))
                self.boxlarceny.setText(stats.get('skills').get('larceny'))
                self.boxstealth.setText(stats.get('skills').get('stealth'))
                self.boxsurvival.setText(stats.get('skills').get('survival'))
                self.boxweaponry.setText(stats.get('skills').get('weaponry'))
                self.boxanimalken.setText(stats.get('skills').get('animalken'))
                self.boxempathy.setText(stats.get('skills').get('empathy'))
                self.boxexpression.setText(stats.get('skills').get('expression'))
                self.boxintimidation.setText(stats.get('skills').get('intimidation'))
                self.boxpersuasion.setText(stats.get('skills').get('persuasion'))
                self.boxsocialize.setText(stats.get('skills').get('socialize'))
                self.boxstreetwise.setText(stats.get('skills').get('streetwise'))
                self.boxsubterfuge.setText(stats.get('skills').get('subterfuge'))

                self.boxspecacademics.setText(stats.get('skills').get('academicsspec'))
                self.boxspeccomputer.setText(stats.get('skills').get('computerspec'))
                self.boxspeccrafts.setText(stats.get('skills').get('craftsspec'))
                self.boxspecinvestigation.setText(stats.get('skills').get('investigationspec'))
                self.boxspecmedicine.setText(stats.get('skills').get('medicinespec'))
                self.boxspecoccult.setText(stats.get('skills').get('occultspec'))
                self.boxspecpolitics.setText(stats.get('skills').get('politicsspec'))
                self.boxspecscience.setText(stats.get('skills').get('sciencespec'))
                self.boxspecathletics.setText(stats.get('skills').get('athleticsspec'))
                self.boxspecbrawl.setText(stats.get('skills').get('brawlspec'))
                self.boxspecdrive.setText(stats.get('skills').get('drivespec'))
                self.boxspecfirearms.setText(stats.get('skills').get('firearmsspec'))
                self.boxspeclarceny.setText(stats.get('skills').get('larcenyspec'))
                self.boxspecstealth.setText(stats.get('skills').get('stealthspec'))
                self.boxspecsurvival.setText(stats.get('skills').get('survivalspec'))
                self.boxspecweaponry.setText(stats.get('skills').get('weaponryspec'))
                self.boxspecanimalken.setText(stats.get('skills').get('animalkenspec'))
                self.boxspecempathy.setText(stats.get('skills').get('empathyspec'))
                self.boxspecexpression.setText(stats.get('skills').get('expressionspec'))
                self.boxspecintimidation.setText(stats.get('skills').get('intimidationspec'))
                self.boxspecpersuasion.setText(stats.get('skills').get('persuasionspec'))
                self.boxspecsocialize.setText(stats.get('skills').get('socializespec'))
                self.boxspecstreetwise.setText(stats.get('skills').get('streetwisespec'))
                self.boxspecsubterfuge.setText(stats.get('skills').get('subterfugespec'))

                # self.occultflag = [False, False, False]

                if stats.get('merits')[0][1] > self.meritcount:
                    self.oldmeritcount = self.meritcount
                    self.meritcount = stats.get('merits')[0][1]

                    self.makesheet()
                # print(stats['merits'][0][1])
                for x in range(stats.get('merits')[0][1]):
                    if stats.get('merits')[0][1] >= x:
                        self.meritnamebox[x].setText(stats.get('merits')[x+1][0])
                        self.meritlevelbox[x].setText(stats.get('merits')[x+1][1])

                if stats.get('aspirations')[0][1] > self.aspirationcount:
                    self.oldaspirationcount = self.aspirationcount
                    self.aspirationcount = stats.get('aspirations')[0][1]

                    self.makesheet()

                if stats.get('conditions')[0][1] > self.conditioncount:
                    self.oldconditioncount = self.conditioncount
                    self.conditioncount = stats.get('conditions')[0][1]

                    self.makesheet()

                if stats.get('banes')[0][1] > self.banecount:
                    self.oldbanecount = self.banecount
                    self.banecount = stats.get('banes')[0][1]

                    self.makesheet()

                for x in range(stats.get('aspirations')[0][1]):
                    if stats.get('aspirations')[0][1] >= x:
                        self.aspirationnamebox[x].setText(stats.get('aspirations')[x+1][0])
                for x in range(stats.get('conditions')[0][1]):
                    if stats.get('conditions')[0][1] >= x:
                        self.conditionnamebox[x].setText(stats.get('conditions')[x+1][0])
                for x in range(stats.get('banes')[0][1]):
                    if stats.get('banes')[0][1] >= x:
                        self.banenamebox[x].setText(stats.get('banes')[x+1][0])

                if self.othertraitsflag == 0:
                    self.sizeval.setText(str(stats.get('size')))
                    self.sizebonus = stats.get('size') - 5
                    self.sizebonusbox.setText(str(stats.get('size') - 5))

                    self.speedval.setText(str(stats.get('speed')))
                    self.speedbonus = stats.get('speed') - int(self.sizeval.text()) - self.strengthstat - self.dexteritystat
                    self.speedbonusbox.setText(str(stats.get('speed') - int(self.sizeval.text()) - self.strengthstat - self.dexteritystat))

                    if self.dexteritystat <= self.witsstat:
                        self.defenseval.setText(str(stats.get('defense')))
                        self.defensebonus = stats.get('defense') - self.athleticsskill - self.dexteritystat
                        self.defensebonusbox.setText(str(stats.get('defense') - self.athleticsskill - self.dexteritystat))
                    else:
                        self.defenseval.setText(str(stats.get('defense')))
                        self.defensebonus = stats.get('defense') - self.athleticsskill - self.witsstat
                        self.defensebonusbox.setText(str(stats.get('defense') - self.athleticsskill - self.witsstat))

                    self.armorval.setText(str(stats.get('armor')))
                    self.armorbonus = stats.get('armor')
                    self.armorbonusbox.setText(str(stats.get('armor')))

                    self.initiativeval.setText(str(stats.get('initiative')))
                    self.initiativebonus = stats.get('initiative') - self.composurestat - self.dexteritystat
                    self.initiativebonusbox.setText(str(stats.get('initiative') - self.composurestat - self.dexteritystat))

                    self.maxhealthbox.setText(str(stats.get('health').get('maxhealth')))
                    self.maxhealthmodbox.setText(str(stats.get('health').get('maxhealth') - self.staminastat - int(self.sizeval.text())))
                elif self.othertraitsflag == 1:
                    self.sizeval.setText(str(stats.get('size')))

                    self.speedval.setText(str(stats.get('speed')))

                    if self.dexteritystat <= self.witsstat:
                        self.defenseval.setText(str(stats.get('defense')))
                    else:
                        self.defenseval.setText(str(stats.get('defense')))

                    self.armorval.setText(str(stats.get('armor')))

                    self.initiativeval.setText(str(stats.get('initiative')))

                    self.maxhealthbox.setText(str(stats.get('health').get('maxhealth')))

                self.bashingdamagebox.setText(str(stats.get('health').get('bashingdamage')))
                self.lethaldamagebox.setText(str(stats.get('health').get('lethaldamage')))
                self.aggravateddamagebox.setText(str(stats.get('health').get('aggravateddamage')))

                self.willpowerdotbox.setText(str(stats.get('willpower').get('willpowerdot')))
                self.willpowerpointbox.setText(str(stats.get('willpower').get('willpowerpoint')))

                self.experiencesbox.setText(str(stats.get('experience').get('experiences')))

                if stats.get('experience').get('beats')[0]:
                    self.beat1.setChecked(True)
                if stats.get('experience').get('beats')[1]:
                    self.beat2.setChecked(True)
                if stats.get('experience').get('beats')[2]:
                    self.beat3.setChecked(True)
                if stats.get('experience').get('beats')[3]:
                    self.beat4.setChecked(True)
                if stats.get('experience').get('beats')[4]:
                    self.beat5.setChecked(True)

                for x in stats.get('supernaturaltags'):
                    if x == 'human':
                        self.boxvice.setText(stats.get('vice'))
                        self.boxvirtue.setText(stats.get('virtue'))
                    if x == 'vampire':
                        self.boxclan.setText(stats.get('clan'))
                        self.boxbloodline.setText(stats.get('bloodline'))
                        self.boxcovenant.setText(stats.get('covenant'))
                        self.boxmask.setText(stats.get('mask'))
                        self.boxdirge.setText(stats.get('dirge'))
                        self.occultflag[0] = True
                        if stats.get('disciplines')[0][1] > self.disciplinecount:
                            self.olddisciplinecount = self.disciplinecount
                            self.disciplinecount = stats.get('disciplines')[0][1]

                            self.makesheet()

                        for x in range(stats.get('disciplines')[0][1]):
                            if stats.get('disciplines')[0][1] >= x:
                                self.disciplinenamebox[x].setText(stats.get('disciplines')[x+1][0])
                                self.disciplinelevelbox[x].setText(stats.get('disciplines')[x+1][1])

                        self.bloodpotencybox.setText(str(stats.get('bloodpotency')))

                        self.maxvitaebox.setText(str(stats.get('vitae').get('maxvitae')))
                        self.currentvitaebox.setText(str(stats.get('vitae').get('currentvitae')))

                        self.humanitybox1.setText(str(stats.get('humanity').get('touchstone1')))
                        # print(stats.get('humanity').get('humanityarray')[0] == True)
                        if stats.get('humanity').get('humanityarray')[0]:
                            self.humanitycheck1.setChecked(True)
                        self.humanitybox2.setText(str(stats.get('humanity').get('touchstone2')))
                        if stats.get('humanity').get('humanityarray')[1]:
                            self.humanitycheck2.setChecked(True)
                        self.humanitybox3.setText(str(stats.get('humanity').get('touchstone3')))
                        if stats.get('humanity').get('humanityarray')[2]:
                            self.humanitycheck3.setChecked(True)
                        self.humanitybox4.setText(str(stats.get('humanity').get('touchstone4')))
                        if stats.get('humanity').get('humanityarray')[3]:
                            self.humanitycheck4.setChecked(True)
                        self.humanitybox5.setText(str(stats.get('humanity').get('touchstone5')))
                        if stats.get('humanity').get('humanityarray')[4]:
                            self.humanitycheck5.setChecked(True)
                        self.humanitybox6.setText(str(stats.get('humanity').get('touchstone6')))
                        if stats.get('humanity').get('humanityarray')[5]:
                            self.humanitycheck6.setChecked(True)
                        self.humanitybox7.setText(str(stats.get('humanity').get('touchstone7')))
                        if stats.get('humanity').get('humanityarray')[6]:
                            self.humanitycheck7.setChecked(True)
                        self.humanitybox8.setText(str(stats.get('humanity').get('touchstone8')))
                        if stats.get('humanity').get('humanityarray')[7]:
                            self.humanitycheck8.setChecked(True)
                        self.humanitybox9.setText(str(stats.get('humanity').get('touchstone9')))
                        if stats.get('humanity').get('humanityarray')[8]:
                            self.humanitycheck9.setChecked(True)
                        self.humanitybox10.setText(str(stats.get('humanity').get('touchstone10')))
                        if stats.get('humanity').get('humanityarray')[9]:
                            self.humanitycheck10.setChecked(True)
                    if x == 'werewolf':
                        self.boxauspice.setText(stats.get('auspice'))
                        self.boxtribe.setText(stats.get('tribe'))
                        self.boxlodge.setText(stats.get('lodge'))
                        self.boxblood.setText(stats.get('blood'))
                        self.boxbone.setText(stats.get('bone'))

                        self.puritybox.setText(stats.get('renown').get('purity'))
                        self.glorybox.setText(stats.get('renown').get('glory'))
                        self.honorbox.setText(stats.get('renown').get('honor'))
                        self.wisdombox.setText(stats.get('renown').get('wisdom'))
                        self.cunningbox.setText(stats.get('renown').get('cunning'))

                        self.primalurgebox.setText(stats.get('primalurge'))
                        self.maxessencebox.setText(stats.get('essence').get('maxessence'))
                        self.currentessencebox.setText(stats.get('essence').get('currentessence'))
                        self.harmonybox.setText(stats.get('harmony'))
                        self.fleshtouchstonebox.setText(stats.get('fleshtouchstone'))
                        self.spirittouchstonebox.setText(stats.get('spirittouchstone'))

                        self.passivekuruthbox.setText(stats.get('kuruth').get('passive'))
                        self.commonkuruthbox.setText(stats.get('kuruth').get('common'))
                        self.specifickuruthbox.setText(stats.get('kuruth').get('specific'))

                        self.occultflag[1] = True
                    if x == 'mage':
                        self.shadownamebox.setText(stats.get('shadowname'))

                        self.pathbox.setText(stats.get('path'))
                        self.orderbox.setText(stats.get('order'))
                        self.legacybox.setText(stats.get('legacy'))

                        self.deathbox.setText(stats.get('arcana').get('death'))
                        self.fatebox.setText(stats.get('arcana').get('fate'))
                        self.forcesbox.setText(stats.get('arcana').get('forces'))
                        self.lifebox.setText(stats.get('arcana').get('life'))
                        self.matterbox.setText(stats.get('arcana').get('matter'))
                        self.mindbox.setText(stats.get('arcana').get('mind'))
                        self.primebox.setText(stats.get('arcana').get('prime'))
                        self.spiritbox.setText(stats.get('arcana').get('spirit'))
                        self.spacebox.setText(stats.get('arcana').get('space'))
                        self.timebox.setText(stats.get('arcana').get('time'))

                        self.gnosisbox.setText(stats.get('gnosis'))
                        self.maxmanabox.setText(stats.get('mana').get('maxmana'))
                        self.currentmanabox.setText(stats.get('mana').get('currentmana'))
                        self.mwisdombox.setText(stats.get('wisdom'))

                        if len(stats.get('obsessions')) >= 1:
                            self.obsession1box.setText(stats.get('obsessions')[0])
                        if len(stats.get('obsessions')) >= 2:
                            self.obsession2box.setText(stats.get('obsessions')[1])
                        if len(stats.get('obsessions')) >= 3:
                            self.obsession3box.setText(stats.get('obsessions')[2])
                        if len(stats.get('obsessions')) >= 4:
                            self.obsession4box.setText(stats.get('obsessions')[3])

                        self.arcaneexperiencesbox.setText(str(stats.get('arcaneexperience').get('arcaneexperiences')))

                        if stats.get('arcaneexperience').get('arcanebeats')[0]:
                            self.arcanebeat1.setChecked(True)
                        if stats.get('arcaneexperience').get('arcanebeats')[1]:
                            self.arcanebeat2.setChecked(True)
                        if stats.get('arcaneexperience').get('arcanebeats')[2]:
                            self.arcanebeat3.setChecked(True)
                        if stats.get('arcaneexperience').get('arcanebeats')[3]:
                            self.arcanebeat4.setChecked(True)
                        if stats.get('arcaneexperience').get('arcanebeats')[4]:
                            self.arcanebeat5.setChecked(True)

                        self.occultflag[2] = True
                if stats.get('othertraits')[0][1] > self.othertraitcount:
                    self.oldothertraitcount = self.othertraitcount
                    self.othertraitcount = stats.get('othertraits')[0][1]

                    self.makesheet()

                for x in range(stats.get('othertraits')[0][1]):
                    if stats.get('othertraits')[0][1] >= x:
                        self.othertraitnamebox[x].setText(stats.get('othertraits')[x+1][0])
                        self.othertraitlevelbox[x].setText(stats.get('othertraits')[x+1][1])

                if stats.get('attacks')[0][1] > self.attackcount:
                    self.oldattackcount = self.attackcount
                    self.attackcount = stats.get('attacks')[0][1]

                    self.makesheet()

                for x in range(stats.get('attacks')[0][1]):
                    if stats.get('attacks')[0][1] >= x:
                        self.attacknamebox[x].setText(stats.get('attacks')[x+1][0])
                        self.attackdamagebox[x].setText(stats.get('attacks')[x+1][1])
                        self.attackrangebox[x].setText(stats.get('attacks')[x+1][2])
                        self.attackclipbox[x].setText(stats.get('attacks')[x+1][3])
                        self.attackinitiativebox[x].setText(stats.get('attacks')[x+1][4])
                        self.attackstrengthbox[x].setText(stats.get('attacks')[x+1][5])
                        self.attacksizebox[x].setText(stats.get('attacks')[x+1][6])

                self.armorratingbox.setText(stats.get('armorp2').get('rating'))
                self.armorstrengthbox.setText(stats.get('armorp2').get('strength'))
                self.armordefensebox.setText(stats.get('armorp2').get('defense'))
                self.armorspeedbox.setText(stats.get('armorp2').get('speed'))
                self.armordescriptionbox.setText(stats.get('armorp2').get('description'))

                for x in range(stats.get('expandedmerits').get('emallies')[0][1]):
                    if stats.get('expandedmerits').get('emallies')[0][1] >= x:
                        self.emalliesbox[x].setText(stats.get('expandedmerits').get('emallies')[x+1])
                for x in range(stats.get('expandedmerits').get('emmentor')[0][1]):
                    if stats.get('expandedmerits').get('emmentor')[0][1] >= x:
                        self.emmentorbox[x].setText(stats.get('expandedmerits').get('emmentor')[x+1])
                for x in range(stats.get('expandedmerits').get('emcontacts')[0][1]):
                    if stats.get('expandedmerits').get('emcontacts')[0][1] >= x:
                        self.emcontactsbox[x].setText(stats.get('expandedmerits').get('emcontacts')[x+1])
                for x in range(stats.get('expandedmerits').get('emresources')[0][1]):
                    if stats.get('expandedmerits').get('emresources')[0][1] >= x:
                        self.emresourcesbox[x].setText(stats.get('expandedmerits').get('emresources')[x+1])
                for x in range(stats.get('expandedmerits').get('emfame')[0][1]):
                    if stats.get('expandedmerits').get('emfame')[0][1] >= x:
                        self.emfamebox[x].setText(stats.get('expandedmerits').get('emfame')[x+1])
                for x in range(stats.get('expandedmerits').get('emretainer')[0][1]):
                    if stats.get('expandedmerits').get('emretainer')[0][1] >= x:
                        self.emretainerbox[x].setText(stats.get('expandedmerits').get('emretainer')[x+1])

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

        # self.sizeval = QtWidgets.QLabel(self)
        self.sizeval.setText(str(5 + self.sizebonus))
        # self.speedval = QtWidgets.QLabel(self)
        self.speedval.setText(str(int(self.sizeval.text()) + self.strengthstat + self.dexteritystat + self.speedbonus))
        # self.defenseval = QtWidgets.QLabel(self)
        if self.dexteritystat <= self.witsstat:
            self.defenseval.setText(str(self.athleticsskill + self.dexteritystat + self.defensebonus))
        else:
            self.defenseval.setText(str(self.athleticsskill + self.witsstat + self.defensebonus))
        # self.armorval = QtWidgets.QLabel(self)
        self.armorval.setText(str(self.armorbonus))
        # self.initiativeval = QtWidgets.QLabel(self)
        self.initiativeval.setText(str(self.composurestat + self.dexteritystat + self.initiativebonus))

        self.layout.addWidget(self.sizeval, 9 + self.oplinecounter, 5)
        self.layout.addWidget(self.speedval, 11 + self.oplinecounter, 5)
        self.layout.addWidget(self.defenseval, 13 + self.oplinecounter, 5)
        self.layout.addWidget(self.armorval, 15 + self.oplinecounter, 5)
        self.layout.addWidget(self.initiativeval, 17 + self.oplinecounter, 5)

    def makesheet(self):
        #make here delete all stuff in here if not in first run
        if self.makesheetflag:
            self.p1c2counter = 0
            for x in range(self.oldmeritcount):
                if self.oldmeritcount >= x + 1:
                    self.savedmeritnames.append(self.meritnamebox[x])
                    self.layout.removeWidget(self.meritnamebox[x])
                    self.meritnamebox[x].deleteLater()
                    self.meritnamebox[x] = None

                    self.savedmeritlevels.append(self.meritlevelbox[x])
                    self.layout.removeWidget(self.meritlevelbox[x])
                    self.meritlevelbox[x].deleteLater()
                    self.meritlevelbox[x] = None

            self.aspirationcounter = 0
            for x in range(self.oldaspirationcount):
                if self.oldaspirationcount >= x + 1:
                    self.savedaspirationnames.append(self.aspirationnamebox[x])
                    self.layout.removeWidget(self.aspirationnamebox[x])
                    self.aspirationnamebox[x].deleteLater()
                    self.aspirationnamebox[x] = None

            self.conditioncounter = 0
            for x in range(self.oldconditioncount):
                if self.oldconditioncount >= x + 1:
                    self.savedconditionnames.append(self.conditionnamebox[x])
                    self.layout.removeWidget(self.conditionnamebox[x])
                    self.conditionnamebox[x].deleteLater()
                    self.conditionnamebox[x] = None

            self.banecounter = 0
            for x in range(self.oldbanecount):
                if self.oldbanecount >= x + 1:
                    self.savedbanenames.append(self.banenamebox[x])
                    self.layout.removeWidget(self.banenamebox[x])
                    self.banenamebox[x].deleteLater()
                    self.banenamebox[x] = None

            self.othertraitcounter = 0
            for x in range(self.oldothertraitcount):
                if self.oldothertraitcount >= x + 1:
                    self.savedothertraitnames.append(self.othertraitnamebox[x])
                    self.layout.removeWidget(self.othertraitnamebox[x])
                    self.othertraitnamebox[x].deleteLater()
                    self.othertraitnamebox[x] = None

                    self.savedothertraitlevels.append(self.othertraitlevelbox[x])
                    self.layout.removeWidget(self.othertraitlevelbox[x])
                    self.othertraitlevelbox[x].deleteLater()
                    self.othertraitlevelbox[x] = None

            self.attackcounter = 0
            for x in range(self.oldattackcount):
                if self.oldattackcount >= x + 1:
                    self.savedattacknames.append(self.attacknamebox[x])
                    self.layout.removeWidget(self.attacknamebox[x])
                    self.attacknamebox[x].deleteLater()
                    self.attacknamebox[x] = None

                    self.savedattackdamages.append(self.attackdamagebox[x])
                    self.layout.removeWidget(self.attackdamagebox[x])
                    self.attackdamagebox[x].deleteLater()
                    self.attackdamagebox[x] = None

                    self.savedattackranges.append(self.attackrangebox[x])
                    self.layout.removeWidget(self.attackrangebox[x])
                    self.attackrangebox[x].deleteLater()
                    self.attackrangebox[x] = None

                    self.savedattackclips.append(self.attackclipbox[x])
                    self.layout.removeWidget(self.attackclipbox[x])
                    self.attackclipbox[x].deleteLater()
                    self.attackclipbox[x] = None

                    self.savedattackinitiatives.append(self.attackinitiativebox[x])
                    self.layout.removeWidget(self.attackinitiativebox[x])
                    self.attackinitiativebox[x].deleteLater()
                    self.attackinitiativebox[x] = None

                    self.savedattackstrengths.append(self.attackstrengthbox[x])
                    self.layout.removeWidget(self.attackstrengthbox[x])
                    self.attackstrengthbox[x].deleteLater()
                    self.attackstrengthbox[x] = None

                    self.savedattacksizes.append(self.attacksizebox[x])
                    self.layout.removeWidget(self.attacksizebox[x])
                    self.attacksizebox[x].deleteLater()
                    self.attacksizebox[x] = None

            self.emalliescounter = 0
            for x in range(self.oldemalliescount):
                if self.oldemalliescount >= x + 1:
                    self.savedemallies.append(self.emalliesbox[x])
                    self.layout.removeWidget(self.emalliesbox[x])
                    self.emalliesbox[x].deleteLater()
                    self.emalliesbox[x] = None

            self.emmentorcounter = 0
            for x in range(self.oldemmentorcount):
                if self.oldemmentorcount >= x + 1:
                    self.savedemmentor.append(self.emmentorbox[x])
                    self.layout.removeWidget(self.emmentorbox[x])
                    self.emmentorbox[x].deleteLater()
                    self.emmentorbox[x] = None

            self.emcontactscounter = 0
            for x in range(self.oldemcontactscount):
                if self.oldemcontactscount >= x + 1:
                    self.savedemcontacts.append(self.emcontactsbox[x])
                    self.layout.removeWidget(self.emcontactsbox[x])
                    self.emcontactsbox[x].deleteLater()
                    self.emcontactsbox[x] = None

            self.emresourcescounter = 0
            for x in range(self.oldemresourcescount):
                if self.oldemresourcescount >= x + 1:
                    self.savedemresources.append(self.emresourcesbox[x])
                    self.layout.removeWidget(self.emresourcesbox[x])
                    self.emresourcesbox[x].deleteLater()
                    self.emresourcesbox[x] = None

            self.emfamecounter = 0
            for x in range(self.oldemfamecount):
                if self.oldemfamecount >= x + 1:
                    self.savedemfame.append(self.emfamebox[x])
                    self.layout.removeWidget(self.emfamebox[x])
                    self.emfamebox[x].deleteLater()
                    self.emfamebox[x] = None

            self.emretainercounter = 0
            for x in range(self.oldemretainercount):
                if self.oldemretainercount >= x + 1:
                    self.savedemretainer.append(self.emretainerbox[x])
                    self.layout.removeWidget(self.emretainerbox[x])
                    self.emretainerbox[x].deleteLater()
                    self.emretainerbox[x] = None

        #other traits

        #initialize merits
        self.meritnamebox = []
        self.meritlevelbox = []
        for x in range(self.meritcount):
            if self.meritcount >= x:
                self.meritnamebox.append(QtWidgets.QLineEdit(self))
                self.meritlevelbox.append(QtWidgets.QLineEdit(self))

        #begin aspirations
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

        self.disciplinenamebox = []
        self.disciplinelevelbox = []
        if self.occultflag[0]:
            #initialize disciplines
            for x in range(self.disciplinecount):
                if self.disciplinecount >= x:
                    self.disciplinenamebox.append(QtWidgets.QLineEdit(self))
                    self.disciplinelevelbox.append(QtWidgets.QLineEdit(self))

        self.othertraitnamebox = []
        self.othertraitlevelbox = []
        #initialize othertraits
        for x in range(self.othertraitcount):
            if self.othertraitcount >= x:
                self.othertraitnamebox.append(QtWidgets.QLineEdit(self))
                self.othertraitlevelbox.append(QtWidgets.QLineEdit(self))

        #initialize weapons / attacks
        self.attacknamebox = []
        self.attackdamagebox = []
        self.attackrangebox = []
        self.attackclipbox = []
        self.attackinitiativebox = []
        self.attackstrengthbox = []
        self.attacksizebox = []
        for x in range(self.attackcount):
            if self.attackcount >= x:
                self.attacknamebox.append(QtWidgets.QLineEdit(self))
                self.attackdamagebox.append(QtWidgets.QLineEdit(self))
                self.attackrangebox.append(QtWidgets.QLineEdit(self))
                self.attackclipbox.append(QtWidgets.QLineEdit(self))
                self.attackinitiativebox.append(QtWidgets.QLineEdit(self))
                self.attackstrengthbox.append(QtWidgets.QLineEdit(self))
                self.attacksizebox.append(QtWidgets.QLineEdit(self))

        #expanded merits

        self.emalliesbox = []
        self.emmentorbox = []
        self.emcontactsbox = []
        self.emresourcesbox = []
        self.emfamebox = []
        self.emretainerbox = []

        for x in range(self.emalliescount):
            if self.emalliescount >= x:
                self.emalliesbox.append(QtWidgets.QTextEdit(self))

        for x in range(self.emmentorcount):
            if self.emmentorcount >= x:
                self.emmentorbox.append(QtWidgets.QTextEdit(self))

        for x in range(self.emcontactscount):
            if self.emcontactscount >= x:
                self.emcontactsbox.append(QtWidgets.QTextEdit(self))

        for x in range(self.emresourcescount):
            if self.emresourcescount >= x:
                self.emresourcesbox.append(QtWidgets.QTextEdit(self))

        for x in range(self.emfamecount):
            if self.emfamecount >= x:
                self.emfamebox.append(QtWidgets.QTextEdit(self))

        for x in range(self.emretainercount):
            if self.emretainercount >= x:
                self.emretainerbox.append(QtWidgets.QTextEdit(self))

        #begin layout

        self.layout.addWidget(self.name, 3, 1)
        self.layout.addWidget(self.boxname, 3, 2)
        self.layout.addWidget(self.player, 3, 3)
        self.layout.addWidget(self.boxplayer, 3, 4)
        self.layout.addWidget(self.chronicle, 3, 5)
        self.layout.addWidget(self.boxchronicle, 3, 6)



        if self.vvflag:
            self.layout.addWidget(self.concept, 4, 1)
            self.layout.addWidget(self.boxconcept, 4, 2)
            self.layout.addWidget(self.vice, 4, 3)
            self.layout.addWidget(self.boxvice, 4, 4)
            self.layout.addWidget(self.virtue, 4, 5)
            self.layout.addWidget(self.boxvirtue, 4, 6)
            self.runonce1 = False
        else:
            self.layout.addWidget(self.concept, 4, 3)
            self.layout.addWidget(self.boxconcept, 4, 4)

        self.oplinecounter = 0

        if self.occultflag[0]:
            self.oplinecounter += 1
            self.layout.addWidget(self.clan, 4 + self.oplinecounter, 1)
            self.layout.addWidget(self.boxclan, 4 + self.oplinecounter, 2)
            self.layout.addWidget(self.bloodline, 4 + self.oplinecounter, 3)
            self.layout.addWidget(self.boxbloodline, 4 + self.oplinecounter, 4)
            self.layout.addWidget(self.covenant, 4 + self.oplinecounter, 5)
            self.layout.addWidget(self.boxcovenant, 4 + self.oplinecounter, 6)

            self.oplinecounter += 1
            self.layout.addWidget(self.mask, 4 + self.oplinecounter, 2)
            self.layout.addWidget(self.boxmask, 4 + self.oplinecounter, 3)
            self.layout.addWidget(self.dirge, 4 + self.oplinecounter, 4)
            self.layout.addWidget(self.boxdirge, 4 + self.oplinecounter, 5)
            self.runonce2 = False

        if self.occultflag[1]:
            self.oplinecounter += 1
            self.layout.addWidget(self.auspice, 4 + self.oplinecounter, 1)
            self.layout.addWidget(self.boxauspice, 4 + self.oplinecounter, 2)
            self.layout.addWidget(self.tribe, 4 + self.oplinecounter, 3)
            self.layout.addWidget(self.boxtribe, 4 + self.oplinecounter, 4)
            self.layout.addWidget(self.lodge, 4 + self.oplinecounter, 5)
            self.layout.addWidget(self.boxlodge, 4 + self.oplinecounter, 6)

            self.oplinecounter += 1
            self.layout.addWidget(self.blood, 4 + self.oplinecounter, 2)
            self.layout.addWidget(self.boxblood, 4 + self.oplinecounter, 3)
            self.layout.addWidget(self.bone, 4 + self.oplinecounter, 4)
            self.layout.addWidget(self.boxbone, 4 + self.oplinecounter, 5)
            self.runonce3 = False

        if self.occultflag[2]:
            self.oplinecounter += 1
            self.layout.addWidget(self.shadowname, 4 + self.oplinecounter, 3)
            self.layout.addWidget(self.shadownamebox, 4 + self.oplinecounter, 4)

            self.oplinecounter += 1
            self.layout.addWidget(self.path, 4 + self.oplinecounter, 1)
            self.layout.addWidget(self.pathbox, 4 + self.oplinecounter, 2)
            self.layout.addWidget(self.order, 4 + self.oplinecounter, 3)
            self.layout.addWidget(self.orderbox, 4 + self.oplinecounter, 4)
            self.layout.addWidget(self.legacy, 4 + self.oplinecounter, 5)
            self.layout.addWidget(self.legacybox, 4 + self.oplinecounter, 6)

        self.layout.addWidget(self.blanks[0], 5 + self.oplinecounter, 3)

        self.layout.addWidget(self.cat1, 6 + self.oplinecounter, 3)

        self.layout.addWidget(self.statsubcat1, 7 + self.oplinecounter, 0)
        self.layout.addWidget(self.statsubcat2, 8 + self.oplinecounter, 0)
        self.layout.addWidget(self.statsubcat3, 9 + self.oplinecounter, 0)

        self.layout.addWidget(self.intelligence, 7 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxintelligence, 7 + self.oplinecounter, 2)
        self.layout.addWidget(self.strength, 7 + self.oplinecounter, 3)
        self.layout.addWidget(self.boxstrength, 7 + self.oplinecounter, 4)
        self.layout.addWidget(self.presence, 7 + self.oplinecounter, 5)
        self.layout.addWidget(self.boxpresence, 7 + self.oplinecounter, 6)
        self.layout.addWidget(self.wits, 8 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxwits, 8 + self.oplinecounter, 2)
        self.layout.addWidget(self.dexterity, 8 + self.oplinecounter, 3)
        self.layout.addWidget(self.boxdexterity, 8 + self.oplinecounter, 4)
        self.layout.addWidget(self.manipulation, 8 + self.oplinecounter, 5)
        self.layout.addWidget(self.boxmanipulation, 8 + self.oplinecounter, 6)
        self.layout.addWidget(self.resolve, 9 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxresolve, 9 + self.oplinecounter, 2)
        self.layout.addWidget(self.stamina, 9 + self.oplinecounter, 3)
        self.layout.addWidget(self.boxstamina, 9 + self.oplinecounter, 4)
        self.layout.addWidget(self.composure, 9 + self.oplinecounter, 5)
        self.layout.addWidget(self.boxcomposure, 9 + self.oplinecounter, 6)

        self.layout.addWidget(self.blanks[1], 10 + self.oplinecounter, 3)

        self.layout.addWidget(self.cat2, 11 + self.oplinecounter, 1)
        self.layout.addWidget(self.subcat1, 12 + self.oplinecounter, 1)
        self.layout.addWidget(self.desc1, 13 + self.oplinecounter, 1)

        self.layout.addWidget(self.academics, 14 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecacademics, 14 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxacademics, 14 + self.oplinecounter, 2)
        self.layout.addWidget(self.computer, 15 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspeccomputer, 15 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxcomputer, 15 + self.oplinecounter, 2)
        self.layout.addWidget(self.crafts, 16 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspeccrafts, 16 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxcrafts, 16 + self.oplinecounter, 2)
        self.layout.addWidget(self.investigation, 17 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecinvestigation, 17 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxinvestigation, 17 + self.oplinecounter, 2)
        self.layout.addWidget(self.medicine, 18 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecmedicine, 18 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxmedicine, 18 + self.oplinecounter, 2)
        self.layout.addWidget(self.occult, 19 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecoccult, 19 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxoccult, 19 + self.oplinecounter, 2)
        self.layout.addWidget(self.politics, 20 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecpolitics, 20 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxpolitics, 20 + self.oplinecounter, 2)
        self.layout.addWidget(self.science, 21 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecscience, 21 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxscience, 21 + self.oplinecounter, 2)

        self.layout.addWidget(self.subcat2, 22 + self.oplinecounter, 1)
        self.layout.addWidget(self.desc2, 23 + self.oplinecounter, 1)

        self.layout.addWidget(self.athletics, 24 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecathletics, 24 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxathletics, 24 + self.oplinecounter, 2)
        self.layout.addWidget(self.brawl, 25 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecbrawl, 25 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxbrawl, 25 + self.oplinecounter, 2)
        self.layout.addWidget(self.drive, 26 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecdrive, 26 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxdrive, 26 + self.oplinecounter, 2)
        self.layout.addWidget(self.firearms, 27 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecfirearms, 27 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxfirearms, 27 + self.oplinecounter, 2)
        self.layout.addWidget(self.larceny, 28 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspeclarceny, 28 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxlarceny, 28 + self.oplinecounter, 2)
        self.layout.addWidget(self.stealth, 29 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecstealth, 29 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxstealth, 29 + self.oplinecounter, 2)
        self.layout.addWidget(self.survival, 30 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecsurvival, 30 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxsurvival, 30 + self.oplinecounter, 2)
        self.layout.addWidget(self.weaponry, 31 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecweaponry, 31 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxweaponry, 31 + self.oplinecounter, 2)

        self.layout.addWidget(self.subcat3, 32 + self.oplinecounter, 1)
        self.layout.addWidget(self.desc3, 33 + self.oplinecounter, 1)

        self.layout.addWidget(self.animalken, 34 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecanimalken, 34 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxanimalken, 34 + self.oplinecounter, 2)
        self.layout.addWidget(self.empathy, 35 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecempathy, 35 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxempathy, 35 + self.oplinecounter, 2)
        self.layout.addWidget(self.expression, 36 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecexpression, 36 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxexpression, 36 + self.oplinecounter, 2)
        self.layout.addWidget(self.intimidation, 37 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecintimidation, 37 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxintimidation, 37 + self.oplinecounter, 2)
        self.layout.addWidget(self.persuasion, 38 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecpersuasion, 38 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxpersuasion, 38 + self.oplinecounter, 2)
        self.layout.addWidget(self.socialize, 39 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxsocialize, 39 + self.oplinecounter, 2)
        self.layout.addWidget(self.boxspecsocialize, 39 + self.oplinecounter, 1)
        self.layout.addWidget(self.streetwise, 40 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecstreetwise, 40 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxstreetwise, 40 + self.oplinecounter, 2)
        self.layout.addWidget(self.subterfuge, 41 + self.oplinecounter, 0)
        self.layout.addWidget(self.boxspecsubterfuge, 41 + self.oplinecounter, 1)
        self.layout.addWidget(self.boxsubterfuge, 41 + self.oplinecounter, 2)

        self.layout.addWidget(self.cat3, 11 + self.oplinecounter, 5)

        self.layout.addWidget(self.merits, 12 + self.oplinecounter, 3)
        self.layout.addWidget(self.meritslevel, 12 + self.oplinecounter, 4)

        #merits
        self.p1c2counter = 0
        for x in range(self.meritcount):
            if self.meritcount >= 1:
                self.p1c2counter += 1
                self.layout.addWidget(self.meritnamebox[x], 12 + self.oplinecounter + self.p1c2counter, 3)
                self.layout.addWidget(self.meritlevelbox[x], 12 + self.oplinecounter + self.p1c2counter, 4)
                if x < len(self.savedmeritnames):
                    self.meritnamebox[x].setText(self.savedmeritnames[x].text())
                    self.meritlevelbox[x].setText(self.savedmeritlevels[x].text())

        self.savedmeritnames = []
        self.savedmeritlevels = []

        self.layout.addWidget(self.aspirations, 13 + self.oplinecounter + self.p1c2counter, 3)

        self.layout.addWidget(self.conditions, 13 + self.oplinecounter + self.p1c2counter, 4)

        self.mabc = 0
        self.aspirationcounter = 0
        for x in range(self.aspirationcount):
            if self.aspirationcount >= 1:
                self.aspirationcounter += 1
                self.layout.addWidget(self.aspirationnamebox[x], 13 + self.oplinecounter + self.p1c2counter + self.aspirationcounter, 3)
                if x < len(self.savedaspirationnames):
                    self.aspirationnamebox[x].setText(self.savedaspirationnames[x].text())

        self.savedaspirationnames = []

        self.conditioncounter = 0
        for x in range(self.conditioncount):
            if self.conditioncount >= 1:
                self.conditioncounter += 1
                self.layout.addWidget(self.conditionnamebox[x], 13 + self.oplinecounter + self.p1c2counter + self.conditioncounter, 4)
                if x < len(self.savedconditionnames):
                    self.conditionnamebox[x].setText(self.savedconditionnames[x].text())

        if self.aspirationcounter >= self.conditioncounter:
            self.p1c2counter += self.aspirationcounter
            self.layout.addWidget(self.banes, 14 + self.oplinecounter + self.p1c2counter, 4)
            self.banecounter = 0
            for x in range(self.banecount):
                if self.banecount >= 1:
                    self.p1c2counter += 1
                    self.layout.addWidget(self.banenamebox[x], 14 + self.oplinecounter + self.p1c2counter, 4)
                    if x < len(self.savedbanenames):
                        self.banenamebox[x].setText(self.savedbanenames[x].text())
        else:
            self.p1c2counter += self.conditioncounter
            self.layout.addWidget(self.banes, 14 + self.oplinecounter + self.p1c2counter, 3)
            self.banecounter = 0
            for x in range(self.banecount):
                if self.banecount >= 1:
                    self.p1c2counter += 1
                    self.layout.addWidget(self.banenamebox[x], 14 + self.oplinecounter + self.p1c2counter, 3)
                    if x < len(self.savedbanenames):
                        self.banenamebox[x].setText(self.savedbanenames[x].text())

        self.savedconditionnames = []

        self.savedbanenames = []

        self.p1c3counter = 0

        if self.othertraitsflag == 0:
            self.layout.addWidget(self.updatestats, 11 + self.oplinecounter, 6)

        self.layout.addWidget(self.size, 12 + self.oplinecounter, 5)
        self.layout.addWidget(self.sizeval, 12 + self.oplinecounter, 6)

        if self.othertraitsflag == 0:
            self.p1c3counter += 1
            self.layout.addWidget(self.sizebonuslabel, 12 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.sizebonusbox, 12 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.speed, 13 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.speedval, 13 + self.oplinecounter + self.p1c3counter, 6)

        if self.othertraitsflag == 0:
            self.p1c3counter += 1
            self.layout.addWidget(self.speedbonuslabel, 13 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.speedbonusbox, 13 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.defense, 14 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.defenseval, 14 + self.oplinecounter + self.p1c3counter, 6)

        if self.othertraitsflag == 0:
            self.p1c3counter += 1
            self.layout.addWidget(self.defensebonuslabel, 14 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.defensebonusbox, 14 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.armor, 15 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.armorval, 15 + self.oplinecounter + self.p1c3counter, 6)

        if self.othertraitsflag == 0:
            self.p1c3counter += 1
            self.layout.addWidget(self.armorbonuslabel, 15 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.armorbonusbox, 15 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.initiative, 16 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.initiativeval, 16 + self.oplinecounter + self.p1c3counter, 6)

        if self.othertraitsflag == 0:
            self.p1c3counter += 1
            self.layout.addWidget(self.initiativebonuslabel, 16 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.initiativebonusbox, 16 + self.oplinecounter, 6)

        self.layout.addWidget(self.healthlabel, 17 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.maxhealthlabel, 18 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.maxhealthbox, 18 + self.oplinecounter + self.p1c3counter, 6)

        if self.whealth:
            self.p1c3counter += 1
            self.layout.addWidget(self.whealthtext1, 18 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.whealthtext2, 18 + self.oplinecounter + self.p1c3counter, 6)

        if self.othertraitsflag == 0:
            self.p1c3counter += 1
            self.layout.addWidget(self.maxhealthmodlabel, 18 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.maxhealthmodbox, 18 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.bashingdamagelabel, 19 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.bashingdamagebox, 19 + self.oplinecounter + self.p1c3counter, 6)
        self.layout.addWidget(self.lethaldamagelabel, 20 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.lethaldamagebox, 20 + self.oplinecounter + self.p1c3counter, 6)
        self.layout.addWidget(self.aggravateddamagelabel, 21 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.aggravateddamagebox, 21 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.willpowerlabel, 22 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.willpowerdotlabel, 23 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.willpowerdotbox, 23 + self.oplinecounter + self.p1c3counter, 6)
        self.layout.addWidget(self.willpowerpointlabel, 24 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.willpowerpointbox, 24 + self.oplinecounter + self.p1c3counter, 6)

        self.disciplinecounter = 0

        if self.occultflag[0]:
            self.layout.addWidget(self.disciplines, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.disciplineslevel, 15 + self.oplinecounter + self.p1c2counter, 4)

            #disciplines
            for x in range(self.disciplinecount):
                if self.disciplinecount >= 1:
                    self.p1c2counter += 1
                    self.layout.addWidget(self.disciplinenamebox[x], 15 + self.oplinecounter + self.p1c2counter, 3)
                    self.layout.addWidget(self.disciplinelevelbox[x], 15 + self.oplinecounter + self.p1c2counter, 4)
                    if x < len(self.saveddisciplinenames):
                        self.disciplinenamebox[x].setText(self.saveddisciplinenames[x].text())
                        self.disciplinelevelbox[x].setText(self.saveddisciplinelevels[x].text())

            self.saveddisciplinenames = []
            self.saveddisciplinelevels = []

        if self.occultflag[1]:
            self.p1c2counter += 1
            self.layout.addWidget(self.renown, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.purity, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.puritybox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.glory, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.glorybox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.honor, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.honorbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.wisdom, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.wisdombox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.cunning, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.cunningbox, 15 + self.oplinecounter + self.p1c2counter, 4)

        if self.occultflag[2]:
            self.p1c2counter += 1
            self.layout.addWidget(self.arcana, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.death, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.deathbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.fate, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.fatebox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.forces, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.forcesbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.life, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.lifebox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.matter, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.matterbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.mind, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.mindbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.prime, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.primebox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.spirit, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.spiritbox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.space, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.spacebox, 15 + self.oplinecounter + self.p1c2counter, 4)

            self.p1c2counter += 1
            self.layout.addWidget(self.time, 15 + self.oplinecounter + self.p1c2counter, 3)
            self.layout.addWidget(self.timebox, 15 + self.oplinecounter + self.p1c2counter, 4)

        if self.occultflag[0]:
            self.p1c3counter += 1
            self.layout.addWidget(self.bloodpotencytitle, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.bloodpotencylabel, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.bloodpotencybox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.vitaetitle, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.maxvitaelabel, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.maxvitaebox, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.currentvitaelabel, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.currentvitaebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.humanitytitle, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.num1, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox1, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck1, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num2, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox2, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck2, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num3, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox3, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck3, 24 + self.oplinecounter  + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num4, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox4, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck4, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num5, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox5, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck5, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num6, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox6, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck6, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num7, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox7, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck7, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num8, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox8, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck8, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num9, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox9, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck9, 24 + self.oplinecounter + self.p1c3counter, 7)

            self.p1c3counter += 1
            self.layout.addWidget(self.num10, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.humanitybox10, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.layout.addWidget(self.humanitycheck10, 24 + self.oplinecounter + self.p1c3counter, 7)

        if self.occultflag[1]:
            self.p1c3counter += 1
            self.layout.addWidget(self.primalurgetitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.primalurge, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.primalurgebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.essencetitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.maxessence, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.maxessencebox, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.currentessence, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.currentessencebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.fleshtouchstonetitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.fleshtouchstone, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.fleshtouchstonebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.harmonytitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.harmony, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.harmonybox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.spirittouchstonetitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.spirittouchstone, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.spirittouchstonebox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.passivekuruth, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.passivekuruthbox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.commonkuruth, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.commonkuruthbox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.specifickuruth, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.specifickuruthbox, 24 + self.oplinecounter + self.p1c3counter, 6)

        if self.occultflag[2]:
            self.p1c3counter += 1
            self.layout.addWidget(self.gnosistitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.gnosis, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.gnosisbox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.manatitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.maxmana, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.maxmanabox, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.currentmana, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.currentmanabox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.mwisdomtitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.mwisdom, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.mwisdombox, 24 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.obsessiontitle, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.obsession1, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.obsession1box, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.obsession2, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.obsession2box, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.obsession3, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.obsession3box, 24 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.obsession4, 24 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.obsession4box, 24 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.experiencestitle, 25 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.experiences, 26 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.experiencesbox, 26 + self.oplinecounter + self.p1c3counter, 6)

        self.layout.addWidget(self.beats, 27 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.beat1, 27 + self.oplinecounter + self.p1c3counter, 6)
        self.layout.addWidget(self.beat2, 28 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.beat3, 28 + self.oplinecounter + self.p1c3counter, 6)
        self.layout.addWidget(self.beat4, 29 + self.oplinecounter + self.p1c3counter, 5)
        self.layout.addWidget(self.beat5, 29 + self.oplinecounter + self.p1c3counter, 6)

        if self.occultflag[2]:
            self.p1c3counter += 1
            self.layout.addWidget(self.arcaneexperiences, 29 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.arcaneexperiencesbox, 29 + self.oplinecounter + self.p1c3counter, 6)

            self.p1c3counter += 1
            self.layout.addWidget(self.arcanebeats, 29 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.arcanebeat1, 29 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.arcanebeat2, 29 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.arcanebeat3, 29 + self.oplinecounter + self.p1c3counter, 6)
            self.p1c3counter += 1
            self.layout.addWidget(self.arcanebeat4, 29 + self.oplinecounter + self.p1c3counter, 5)
            self.layout.addWidget(self.arcanebeat5, 29 + self.oplinecounter + self.p1c3counter, 6)

        self.p2counter = 0
        if 41 >= self.p1c2counter:
            if 41 >= self.p1c3counter:
                self.p2counter = 41 + self.oplinecounter
            else:
                self.p2counter = 29 + self.oplinecounter + self.p1c3counter
        else:
            if self.p1c2counter >= self.p1c3counter:
                self.p2counter = 15 + self.oplinecounter + self.p1c2counter
            else:
                self.p2counter = 29 + self.oplinecounter + self.p1c3counter

        #begin page 2

        self.layout.addWidget(self.blanks[2], self.p2counter + 1, 4)
        self.layout.addWidget(self.blanks[3], self.p2counter + 2, 4)
        self.layout.addWidget(self.blanks[4], self.p2counter + 3, 4)
        self.layout.addWidget(self.blanks[5], self.p2counter + 4, 4)
        self.layout.addWidget(self.blanks[6], self.p2counter + 5, 4)

        self.p2counter += 5

        # self.layout.addWidget(self.titlep2, self.p2counter, 3, self.p2counter, 6)

        self.p2counter += 1
        self.layout.addWidget(self.othertraits, self.p2counter, 3)

        self.othertraitcounter = self.othertraitcount

        #othertraits
        while self.othertraitcounter > 0:
            # print(self.p2counter)
            if self.othertraitcounter >= 3:
                self.p2counter += 1
                self.layout.addWidget(self.othertraitnamebox[self.othertraitcounter - 1], self.p2counter, 1)
                self.layout.addWidget(self.othertraitlevelbox[self.othertraitcounter - 1], self.p2counter, 2)
                self.layout.addWidget(self.othertraitnamebox[self.othertraitcounter - 2], self.p2counter, 3)
                self.layout.addWidget(self.othertraitlevelbox[self.othertraitcounter - 2], self.p2counter, 4)
                self.layout.addWidget(self.othertraitnamebox[self.othertraitcounter - 3], self.p2counter, 5)
                self.layout.addWidget(self.othertraitlevelbox[self.othertraitcounter - 3], self.p2counter, 6)
                if self.othertraitcount - self.othertraitcounter < len(self.savedothertraitnames):
                    self.othertraitnamebox[self.othertraitcount - self.othertraitcounter].setText(self.savedothertraitnames[self.othertraitcount - self.othertraitcounter].text())
                    self.othertraitlevelbox[self.othertraitcount - self.othertraitcounter].setText(self.savedothertraitlevels[self.othertraitcount - self.othertraitcounter].text())
                if self.othertraitcount - self.othertraitcounter + 1 < len(self.savedothertraitnames):
                    self.othertraitnamebox[self.othertraitcount - self.othertraitcounter + 1].setText(self.savedothertraitnames[self.othertraitcount - self.othertraitcounter + 1].text())
                    self.othertraitlevelbox[self.othertraitcount - self.othertraitcounter + 1].setText(self.savedothertraitlevels[self.othertraitcount - self.othertraitcounter + 1].text())
                if self.othertraitcount - self.othertraitcounter + 2 < len(self.savedothertraitnames):
                    self.othertraitnamebox[self.othertraitcount - self.othertraitcounter + 2].setText(self.savedothertraitnames[self.othertraitcount - self.othertraitcounter + 2].text())
                    self.othertraitlevelbox[self.othertraitcount - self.othertraitcounter + 2].setText(self.savedothertraitlevels[self.othertraitcount - self.othertraitcounter + 2].text())
                self.othertraitcounter -= 3
            elif self.othertraitcounter >= 2:
                self.p2counter += 1
                self.layout.addWidget(self.othertraitnamebox[self.othertraitcounter - 1], self.p2counter, 2)
                self.layout.addWidget(self.othertraitlevelbox[self.othertraitcounter - 1], self.p2counter, 3)
                self.layout.addWidget(self.othertraitnamebox[self.othertraitcounter - 2], self.p2counter, 4)
                self.layout.addWidget(self.othertraitlevelbox[self.othertraitcounter - 2], self.p2counter, 5)
                self.othertraitcounter -= 2
                if self.othertraitcount - self.othertraitcounter < len(self.savedothertraitnames):
                    self.othertraitnamebox[self.othertraitcount - self.othertraitcounter].setText(self.savedothertraitnames[self.othertraitcount - self.othertraitcounter].text())
                    self.othertraitlevelbox[self.othertraitcount - self.othertraitcounter].setText(self.savedothertraitlevels[self.othertraitcount - self.othertraitcounter].text())
                if self.othertraitcount - self.othertraitcounter + 1 < len(self.savedothertraitnames):
                    self.othertraitnamebox[self.othertraitcount - self.othertraitcounter + 1].setText(self.savedothertraitnames[self.othertraitcount - self.othertraitcounter + 1].text())
                    self.othertraitlevelbox[self.othertraitcount - self.othertraitcounter + 1].setText(self.savedothertraitlevels[self.othertraitcount - self.othertraitcounter + 1].text())
            else:
                self.p2counter += 1
                self.layout.addWidget(self.othertraitnamebox[self.othertraitcounter - 1], self.p2counter, 3)
                self.layout.addWidget(self.othertraitlevelbox[self.othertraitcounter - 1], self.p2counter, 4)
                self.othertraitcounter -= 1
                if self.othertraitcount - self.othertraitcounter < len(self.savedothertraitnames):
                    self.othertraitnamebox[self.othertraitcount - self.othertraitcounter].setText(self.savedothertraitnames[self.othertraitcount - self.othertraitcounter].text())
                    self.othertraitlevelbox[self.othertraitcount - self.othertraitcounter].setText(self.savedothertraitlevels[self.othertraitcount - self.othertraitcounter].text())

        self.p2counter += 1
        self.layout.addWidget(self.blanks[7], self.p2counter, 4)

        self.p2counter += 1
        self.layout.addWidget(self.combat, self.p2counter, 3)

        self.p2counter += 1
        self.layout.addWidget(self.weapons, self.p2counter, 3)

        self.p2counter += 1
        self.layout.addWidget(self.attackname, self.p2counter, 0)
        self.layout.addWidget(self.attackdamage, self.p2counter, 1)
        self.layout.addWidget(self.attackrange, self.p2counter, 2)
        self.layout.addWidget(self.attackclip, self.p2counter, 3)
        self.layout.addWidget(self.attackinitiative, self.p2counter, 4)
        self.layout.addWidget(self.attackstrength, self.p2counter, 5)
        self.layout.addWidget(self.attacksize, self.p2counter, 6)

        self.savedattacknames = []
        self.savedattackdamages = []
        self.savedattackranges = []
        self.savedattackclips = []
        self.savedattackinitiatives = []
        self.savedattackstrengths = []
        self.savedattacksizes = []

        for x in range(self.attackcount):
            self.p2counter += 1
            self.layout.addWidget(self.attacknamebox[x], self.p2counter, 0)
            self.layout.addWidget(self.attackdamagebox[x], self.p2counter, 1)
            self.layout.addWidget(self.attackrangebox[x], self.p2counter, 2)
            self.layout.addWidget(self.attackclipbox[x], self.p2counter, 3)
            self.layout.addWidget(self.attackinitiativebox[x], self.p2counter, 4)
            self.layout.addWidget(self.attackstrengthbox[x], self.p2counter, 5)
            self.layout.addWidget(self.attacksizebox[x], self.p2counter, 6)
            if x < len(self.savedattacknames):
                self.attacknamebox[x].setText(self.savedattacknames[x].text())
                self.attackdamagebox[x].setText(self.savedattackdamages[x].text())
                self.attackrangebox[x].setText(self.savedattackranges[x].text())
                self.attackclipbox[x].setText(self.savedattackclips[x].text())
                self.attackinitiativebox[x].setText(self.savedattackinitiatives[x].text())
                self.attackstrengthbox[x].setText(self.savedattackstrengths[x].text())
                self.attacksizebox[x].setText(self.savedattacksizes[x].text())

        self.savedattacknames = []
        self.savedattackdamages = []
        self.savedattackranges = []
        self.savedattackclips = []
        self.savedattackinitiatives = []
        self.savedattackstrengths = []
        self.savedattacksizes = []

        self.p2counter += 1
        self.layout.addWidget(self.blanks[8], self.p2counter, 4)

        self.p2counter += 1
        self.layout.addWidget(self.armortitle, self.p2counter, 3)

        self.p2counter += 1
        self.layout.addWidget(self.armorrating, self.p2counter, 1)
        self.layout.addWidget(self.armorratingbox, self.p2counter, 2)
        self.layout.addWidget(self.armorstrength, self.p2counter, 3)
        self.layout.addWidget(self.armorstrengthbox, self.p2counter, 4)
        self.layout.addWidget(self.armordefense, self.p2counter, 5)
        self.layout.addWidget(self.armordefensebox, self.p2counter, 6)
        self.p2counter += 1
        self.layout.addWidget(self.armorspeed, self.p2counter, 2)
        self.layout.addWidget(self.armorspeedbox, self.p2counter, 3)
        self.layout.addWidget(self.armordescription, self.p2counter, 4)
        self.layout.addWidget(self.armordescriptionbox, self.p2counter, 5)

        #begin page 3

        self.layout.addWidget(self.blanks[9], self.p2counter + 1, 4)
        self.layout.addWidget(self.blanks[10], self.p2counter + 2, 4)
        self.layout.addWidget(self.blanks[11], self.p2counter + 3, 4)
        self.layout.addWidget(self.blanks[12], self.p2counter + 4, 4)
        self.layout.addWidget(self.blanks[13], self.p2counter + 5, 4)

        self.p2counter += 5

        self.p2counter += 1
        self.layout.addWidget(self.expandedmerits, self.p2counter, 3)

        self.p2counter += 1
        self.layout.addWidget(self.emallies, self.p2counter, 1)
        self.layout.addWidget(self.emmentor, self.p2counter, 2)
        self.layout.addWidget(self.emcontacts, self.p2counter, 3)
        self.layout.addWidget(self.emresources, self.p2counter, 4)
        self.layout.addWidget(self.emfame, self.p2counter, 5)
        self.layout.addWidget(self.emretainer, self.p2counter, 6)

        self.savedemallies = []
        self.savedemmentor = []
        self.savedemcontacts = []
        self.savedemresources = []
        self.savedemfame = []
        self.savedemretainer = []

        self.emcount = max(self.emalliescount, self.emmentorcount, self.emcontactscount, self.emresourcescount, self.emfamecount, self.emretainercount)

        for x in range(self.emcount):
            self.p2counter += 1
            self.layout.addWidget(self.emalliesbox[x], self.p2counter, 1)
            self.layout.addWidget(self.emmentorbox[x], self.p2counter, 2)
            self.layout.addWidget(self.emcontactsbox[x], self.p2counter, 3)
            self.layout.addWidget(self.emresourcesbox[x], self.p2counter, 4)
            self.layout.addWidget(self.emfamebox[x], self.p2counter, 5)
            self.layout.addWidget(self.emretainerbox[x], self.p2counter, 6)
            if x < len(self.savedemallies):
                self.emalliesbox[x].setText(self.savedemallies[x].toPlainText())
            if x < len(self.savedemmentor):
                self.emmentorbox[x].setText(self.savedemmentor[x].toPlainText())
            if x < len(self.savedemcontacts):
                self.emcontactsbox[x].setText(self.savedemcontacts[x].toPlainText())
            if x < len(self.savedemresources):
                self.emresourcesbox[x].setText(self.savedemresources[x].toPlainText())
            if x < len(self.savedemfame):
                self.emfamebox[x].setText(self.savedemfame[x].toPlainText())
            if x < len(self.savedemretainer):
                self.emretainerbox[x].setText(self.savedemretainer[x].toPlainText())

        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")
        self.p2counter += 1
        self.layout.addWidget(self.blanks[self.blankcount - 1], self.p2counter, 4)

        self.savedemallies = []
        self.savedemmentor = []
        self.savedemcontacts = []
        self.savedemresources = []
        self.savedemfame = []
        self.savedemretainer = []

        self.setLayout(self.layout)
        self.setGeometry(300, 75, 1024, 768)

        self.makesheetflag = True

    def humantoggledef(self):
        if self.humantoggle.isChecked():
            self.humantoggle.setChecked(True)
            self.vvflag = True

            if self.runonce1:
                self.virtue = QtWidgets.QLabel(self)
                self.virtue.setText("Virtue: ")
                self.boxvirtue = QtWidgets.QLineEdit(self)
                self.vice = QtWidgets.QLabel(self)
                self.vice.setText("Vice: ")
                self.boxvice = QtWidgets.QLineEdit(self)
        else:
            self.humantoggle.setChecked(False)
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

            self.disciplines = QtWidgets.QLabel(self)
            self.disciplines.setText("Disciplines")
            self.disciplines.setFont(self.subtitlefont)
            self.disciplineslevel = QtWidgets.QLabel(self)
            self.disciplineslevel.setText("Level")

            self.bloodpotencytitle = QtWidgets.QLabel(self)
            self.bloodpotencytitle.setText("Blood Potency")
            self.bloodpotencytitle.setFont(self.subtitlefont)

            self.bloodpotencylabel = QtWidgets.QLabel(self)
            self.bloodpotencylabel.setText("Blood Potency: ")
            self.bloodpotencybox = QtWidgets.QLineEdit(self)

            self.vitaetitle = QtWidgets.QLabel(self)
            self.vitaetitle.setText("Vitae")
            self.vitaetitle.setFont(self.subtitlefont)

            self.maxvitaelabel = QtWidgets.QLabel(self)
            self.maxvitaelabel.setText("Max Vitae: ")
            self.maxvitaebox = QtWidgets.QLineEdit(self)

            self.currentvitaelabel = QtWidgets.QLabel(self)
            self.currentvitaelabel.setText("Current Vitae: ")
            self.currentvitaebox = QtWidgets.QLineEdit(self)


            self.humanitytitle = QtWidgets.QLabel(self)
            self.humanitytitle.setText("Humanity")
            self.humanitytitle.setFont(self.subtitlefont)

            self.num1 = QtWidgets.QLabel(self)
            self.num1.setText("1")
            self.num2 = QtWidgets.QLabel(self)
            self.num2.setText("2")
            self.num3 = QtWidgets.QLabel(self)
            self.num3.setText("3")
            self.num4 = QtWidgets.QLabel(self)
            self.num4.setText("4")
            self.num5 = QtWidgets.QLabel(self)
            self.num5.setText("5")
            self.num6 = QtWidgets.QLabel(self)
            self.num6.setText("6")
            self.num7 = QtWidgets.QLabel(self)
            self.num7.setText("7")
            self.num8 = QtWidgets.QLabel(self)
            self.num8.setText("8")
            self.num9 = QtWidgets.QLabel(self)
            self.num9.setText("9")
            self.num10 = QtWidgets.QLabel(self)
            self.num10.setText("10")

            self.humanitybox1 = QtWidgets.QLineEdit(self)
            self.humanitybox2 = QtWidgets.QLineEdit(self)
            self.humanitybox3 = QtWidgets.QLineEdit(self)
            self.humanitybox4 = QtWidgets.QLineEdit(self)
            self.humanitybox5 = QtWidgets.QLineEdit(self)
            self.humanitybox6 = QtWidgets.QLineEdit(self)
            self.humanitybox7 = QtWidgets.QLineEdit(self)
            self.humanitybox8 = QtWidgets.QLineEdit(self)
            self.humanitybox9 = QtWidgets.QLineEdit(self)
            self.humanitybox10 = QtWidgets.QLineEdit(self)

            self.humanitycheck1 = QtWidgets.QCheckBox()
            self.humanitycheck1.clicked.connect(self.humanitycheckdef(1))
            self.humanitycheck2 = QtWidgets.QCheckBox()
            self.humanitycheck2.clicked.connect(self.humanitycheckdef(2))
            self.humanitycheck3 = QtWidgets.QCheckBox()
            self.humanitycheck3.clicked.connect(self.humanitycheckdef(3))
            self.humanitycheck4 = QtWidgets.QCheckBox()
            self.humanitycheck4.clicked.connect(self.humanitycheckdef(4))
            self.humanitycheck5 = QtWidgets.QCheckBox()
            self.humanitycheck5.clicked.connect(self.humanitycheckdef(5))
            self.humanitycheck6 = QtWidgets.QCheckBox()
            self.humanitycheck6.clicked.connect(self.humanitycheckdef(6))
            self.humanitycheck7 = QtWidgets.QCheckBox()
            self.humanitycheck7.clicked.connect(self.humanitycheckdef(7))
            self.humanitycheck8 = QtWidgets.QCheckBox()
            self.humanitycheck8.clicked.connect(self.humanitycheckdef(8))
            self.humanitycheck9 = QtWidgets.QCheckBox()
            self.humanitycheck9.clicked.connect(self.humanitycheckdef(9))
            self.humanitycheck10 = QtWidgets.QCheckBox()
            self.humanitycheck10.clicked.connect(self.humanitycheckdef(10))

            if self.runonce2:
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
                if self.olddisciplinecount >= x:
                    self.layout.removeWidget(self.disciplinenamebox[x])
                    self.disciplinenamebox[x].deleteLater()
                    self.disciplinenamebox[x] = None
                    self.layout.removeWidget(self.disciplinelevelbox[x])
                    self.disciplinelevelbox[x].deleteLater()
                    self.disciplinelevelbox[x] = None

            self.layout.removeWidget(self.bloodpotencytitle)
            self.bloodpotencytitle.deleteLater()
            self.bloodpotencytitle = None

            self.layout.removeWidget(self.bloodpotencylabel)
            self.bloodpotencylabel.deleteLater()
            self.bloodpotencylabel = None
            self.layout.removeWidget(self.bloodpotencybox)
            self.bloodpotencybox.deleteLater()
            self.bloodpotencybox = None

            self.layout.removeWidget(self.vitaetitle)
            self.vitaetitle.deleteLater()
            self.vitaetitle = None

            self.layout.removeWidget(self.maxvitaelabel)
            self.maxvitaelabel.deleteLater()
            self.maxvitaelabel = None
            self.layout.removeWidget(self.maxvitaebox)
            self.maxvitaebox.deleteLater()
            self.maxvitaebox = None
            self.layout.removeWidget(self.currentvitaelabel)
            self.currentvitaelabel.deleteLater()
            self.currentvitaelabel = None
            self.layout.removeWidget(self.currentvitaebox)
            self.currentvitaebox.deleteLater()
            self.currentvitaebox = None

            self.layout.removeWidget(self.humanitytitle)

            self.layout.removeWidget(self.num1)
            self.layout.removeWidget(self.humanitybox1)
            self.humanitybox1.deleteLater()
            self.humanitybox1 = None

            self.layout.removeWidget(self.num2)
            self.layout.removeWidget(self.humanitybox2)
            self.humanitybox2.deleteLater()
            self.humanitybox2 = None

            self.layout.removeWidget(self.num3)
            self.layout.removeWidget(self.humanitybox3)
            self.humanitybox3.deleteLater()
            self.humanitybox3 = None

            self.layout.removeWidget(self.num4)
            self.layout.removeWidget(self.humanitybox4)
            self.humanitybox4.deleteLater()
            self.humanitybox4 = None

            self.layout.removeWidget(self.num5)
            self.layout.removeWidget(self.humanitybox5)
            self.humanitybox5.deleteLater()
            self.humanitybox5 = None

            self.layout.removeWidget(self.num6)
            self.layout.removeWidget(self.humanitybox6)
            self.humanitybox6.deleteLater()
            self.humanitybox6 = None

            self.layout.removeWidget(self.num7)
            self.layout.removeWidget(self.humanitybox7)
            self.humanitybox7.deleteLater()
            self.humanitybox7 = None

            self.layout.removeWidget(self.num8)
            self.layout.removeWidget(self.humanitybox8)
            self.humanitybox8.deleteLater()
            self.humanitybox8 = None

            self.layout.removeWidget(self.num9)
            self.layout.removeWidget(self.humanitybox9)
            self.humanitybox9.deleteLater()
            self.humanitybox9 = None

            self.layout.removeWidget(self.num10)
            self.layout.removeWidget(self.humanitybox10)
            self.humanitybox10.deleteLater()
            self.humanitybox10 = None

            self.layout.removeWidget(self.humanitycheck1)
            self.humanitycheck1.deleteLater()
            self.humanitycheck1 = None

            self.layout.removeWidget(self.humanitycheck2)
            self.humanitycheck2.deleteLater()
            self.humanitycheck2 = None

            self.layout.removeWidget(self.humanitycheck3)
            self.humanitycheck3.deleteLater()
            self.humanitycheck3 = None

            self.layout.removeWidget(self.humanitycheck4)
            self.humanitycheck4.deleteLater()
            self.humanitycheck4 = None

            self.layout.removeWidget(self.humanitycheck5)
            self.humanitycheck5.deleteLater()
            self.humanitycheck5 = None

            self.layout.removeWidget(self.humanitycheck6)
            self.humanitycheck6.deleteLater()
            self.humanitycheck6 = None

            self.layout.removeWidget(self.humanitycheck7)
            self.humanitycheck7.deleteLater()
            self.humanitycheck7 = None

            self.layout.removeWidget(self.humanitycheck8)
            self.humanitycheck8.deleteLater()
            self.humanitycheck8 = None

            self.layout.removeWidget(self.humanitycheck9)
            self.humanitycheck9.deleteLater()
            self.humanitycheck9 = None

            self.layout.removeWidget(self.humanitycheck10)
            self.humanitycheck10.deleteLater()
            self.humanitycheck10 = None

            self.oplinecounter -= 2
            self.oldmeritcount = self.meritcount
            self.runonce2 = True

        self.savesettings()

        self.makesheet()

    def wolftoggledef(self):
        if self.wolftoggle.isChecked():
            self.wolftoggle.setChecked(True)
            self.occultflag[1] = True
            self.oldmeritcount = self.meritcount
            self.oldaspirationcount = self.aspirationcount
            self.oldconditioncount = self.conditioncount
            self.oldbanecount = self.banecount

            self.whealth = True

            self.whealthcounter = 0

            self.whealthtext1 = QtWidgets.QLabel(self)
            self.whealthtext1.setText("(+2 Dalu Form, +4 Gauru")
            self.whealthtext2 = QtWidgets.QLabel(self)
            self.whealthtext2.setText("Form, +3 Urshul Form)")

            # if self.runonce3:
            self.auspice = QtWidgets.QLabel(self)
            self.auspice.setText("Auspice: ")
            self.boxauspice = QtWidgets.QLineEdit(self)
            self.tribe = QtWidgets.QLabel(self)
            self.tribe.setText("Tribe: ")
            self.boxtribe = QtWidgets.QLineEdit(self)
            self.lodge = QtWidgets.QLabel(self)
            self.lodge.setText("Lodge: ")
            self.boxlodge = QtWidgets.QLineEdit(self)

            self.blood = QtWidgets.QLabel(self)
            self.blood.setText("Blood: ")
            self.boxblood = QtWidgets.QLineEdit(self)
            self.bone = QtWidgets.QLabel(self)
            self.bone.setText("Bone: ")
            self.boxbone = QtWidgets.QLineEdit(self)

            self.renown = QtWidgets.QLabel(self)
            self.renown.setText("Renown")
            self.renown.setFont(self.subtitlefont)

            self.purity = QtWidgets.QLabel(self)
            self.purity.setText("Purity: ")
            self.puritybox = QtWidgets.QLineEdit(self)

            self.glory = QtWidgets.QLabel(self)
            self.glory.setText("Glory: ")
            self.glorybox = QtWidgets.QLineEdit(self)

            self.honor = QtWidgets.QLabel(self)
            self.honor.setText("Honor: ")
            self.honorbox = QtWidgets.QLineEdit(self)

            self.wisdom = QtWidgets.QLabel(self)
            self.wisdom.setText("Wisdom: ")
            self.wisdombox = QtWidgets.QLineEdit(self)

            self.cunning = QtWidgets.QLabel(self)
            self.cunning.setText("Cunning: ")
            self.cunningbox = QtWidgets.QLineEdit(self)

            self.primalurgetitle = QtWidgets.QLabel(self)
            self.primalurgetitle.setText("Primal Urge")
            self.primalurgetitle.setFont(self.subtitlefont)

            self.primalurge = QtWidgets.QLabel(self)
            self.primalurge.setText("Primal Urge: ")
            self.primalurgebox = QtWidgets.QLineEdit(self)

            self.essencetitle = QtWidgets.QLabel(self)
            self.essencetitle.setText("Essence")
            self.essencetitle.setFont(self.subtitlefont)

            self.maxessence = QtWidgets.QLabel(self)
            self.maxessence.setText("Max Essence: ")
            self.maxessencebox = QtWidgets.QLineEdit(self)

            self.currentessence = QtWidgets.QLabel(self)
            self.currentessence.setText("Current Essence: ")
            self.currentessencebox = QtWidgets.QLineEdit(self)

            self.harmonytitle = QtWidgets.QLabel(self)
            self.harmonytitle.setText("Harmony")
            self.harmonytitle.setFont(self.subtitlefont)

            self.harmony = QtWidgets.QLabel(self)
            self.harmony.setText("Harmony: ")
            self.harmonybox = QtWidgets.QLineEdit(self)

            self.fleshtouchstonetitle = QtWidgets.QLabel(self)
            self.fleshtouchstonetitle.setText("Flesh Touchstone")
            self.fleshtouchstonetitle.setFont(self.subtitlefont)

            self.fleshtouchstone = QtWidgets.QLabel(self)
            self.fleshtouchstone.setText("Flesh Touchstone: ")
            self.fleshtouchstonebox = QtWidgets.QLineEdit(self)

            self.spirittouchstonetitle = QtWidgets.QLabel(self)
            self.spirittouchstonetitle.setText("Spirit Touchstone")
            self.spirittouchstonetitle.setFont(self.subtitlefont)

            self.spirittouchstone = QtWidgets.QLabel(self)
            self.spirittouchstone.setText("Spirit Touchstone: ")
            self.spirittouchstonebox = QtWidgets.QLineEdit(self)

            self.passivekuruth = QtWidgets.QLabel(self)
            self.passivekuruth.setText("Passive Kuruth Trigger: ")
            self.passivekuruthbox = QtWidgets.QTextEdit(self)

            self.commonkuruth = QtWidgets.QLabel(self)
            self.commonkuruth.setText("Common Kuruth Trigger: ")
            self.commonkuruthbox = QtWidgets.QTextEdit(self)

            self.specifickuruth = QtWidgets.QLabel(self)
            self.specifickuruth.setText("Specific Kuruth Trigger: ")
            self.specifickuruthbox = QtWidgets.QTextEdit(self)
        else:
            self.wolftoggle.setChecked(False)
            self.occultflag[1] = False

            self.whealth = False

            self.layout.removeWidget(self.whealthtext1)
            self.whealthtext1.deleteLater()
            self.whealthtext1 = None
            self.layout.removeWidget(self.whealthtext2)
            self.whealthtext2.deleteLater()
            self.whealthtext2 = None

            self.layout.removeWidget(self.auspice)
            self.auspice.deleteLater()
            self.auspice = None
            self.layout.removeWidget(self.boxauspice)
            self.boxauspice.deleteLater()
            self.boxauspice = None
            self.layout.removeWidget(self.tribe)
            self.tribe.deleteLater()
            self.tribe = None
            self.layout.removeWidget(self.boxtribe)
            self.boxtribe.deleteLater()
            self.boxtribe = None
            self.layout.removeWidget(self.lodge)
            self.lodge.deleteLater()
            self.lodge = None
            self.layout.removeWidget(self.boxlodge)
            self.boxlodge.deleteLater()
            self.boxlodge = None
            self.layout.removeWidget(self.blood)
            self.blood.deleteLater()
            self.blood = None
            self.layout.removeWidget(self.boxblood)
            self.boxblood.deleteLater()
            self.boxblood = None
            self.layout.removeWidget(self.bone)
            self.bone.deleteLater()
            self.bone = None
            self.layout.removeWidget(self.boxbone)
            self.boxbone.deleteLater()
            self.boxbone = None

            self.layout.removeWidget(self.renown)
            self.renown.deleteLater()
            self.renown = None

            self.layout.removeWidget(self.purity)
            self.purity.deleteLater()
            self.purity = None
            self.layout.removeWidget(self.puritybox)
            self.puritybox.deleteLater()
            self.puritybox = None
            self.layout.removeWidget(self.glory)
            self.glory.deleteLater()
            self.glory = None
            self.layout.removeWidget(self.glorybox)
            self.glorybox.deleteLater()
            self.glorybox = None
            self.layout.removeWidget(self.honor)
            self.honor.deleteLater()
            self.honor = None
            self.layout.removeWidget(self.honorbox)
            self.honorbox.deleteLater()
            self.honorbox = None
            self.layout.removeWidget(self.wisdom)
            self.wisdom.deleteLater()
            self.wisdom = None
            self.layout.removeWidget(self.wisdombox)
            self.wisdombox.deleteLater()
            self.wisdombox = None
            self.layout.removeWidget(self.cunning)
            self.cunning.deleteLater()
            self.cunning = None
            self.layout.removeWidget(self.cunningbox)
            self.cunningbox.deleteLater()
            self.cunningbox = None

            self.layout.removeWidget(self.primalurge)
            self.primalurge.deleteLater()
            self.primalurge = None
            self.layout.removeWidget(self.primalurgetitle)
            self.primalurgetitle.deleteLater()
            self.primalurgetitle = None
            self.layout.removeWidget(self.primalurgebox)
            self.primalurgebox.deleteLater()
            self.primalurgebox = None
            self.layout.removeWidget(self.essencetitle)
            self.essencetitle.deleteLater()
            self.essencetitle = None
            self.layout.removeWidget(self.maxessence)
            self.maxessence.deleteLater()
            self.maxessence = None
            self.layout.removeWidget(self.maxessencebox)
            self.maxessencebox.deleteLater()
            self.maxessencebox = None
            self.layout.removeWidget(self.currentessence)
            self.currentessence.deleteLater()
            self.currentessence = None
            self.layout.removeWidget(self.currentessencebox)
            self.currentessencebox.deleteLater()
            self.currentessencebox = None
            self.layout.removeWidget(self.harmony)
            self.harmony.deleteLater()
            self.harmony = None
            self.layout.removeWidget(self.harmonytitle)
            self.harmonytitle.deleteLater()
            self.harmonytitle = None
            self.layout.removeWidget(self.harmonybox)
            self.harmonybox.deleteLater()
            self.harmonybox = None
            self.layout.removeWidget(self.fleshtouchstone)
            self.fleshtouchstone.deleteLater()
            self.fleshtouchstone = None
            self.layout.removeWidget(self.fleshtouchstonetitle)
            self.fleshtouchstonetitle.deleteLater()
            self.fleshtouchstonetitle = None
            self.layout.removeWidget(self.fleshtouchstonebox)
            self.fleshtouchstonebox.deleteLater()
            self.fleshtouchstonebox = None
            self.layout.removeWidget(self.spirittouchstone)
            self.spirittouchstone.deleteLater()
            self.spirittouchstone = None
            self.layout.removeWidget(self.spirittouchstonetitle)
            self.spirittouchstonetitle.deleteLater()
            self.spirittouchstonetitle = None
            self.layout.removeWidget(self.spirittouchstonebox)
            self.spirittouchstonebox.deleteLater()
            self.spirittouchstonebox = None

            self.layout.removeWidget(self.passivekuruth)
            self.passivekuruth.deleteLater()
            self.passivekuruth = None
            self.layout.removeWidget(self.passivekuruthbox)
            self.passivekuruthbox.deleteLater()
            self.passivekuruthbox = None
            self.layout.removeWidget(self.commonkuruth)
            self.commonkuruth.deleteLater()
            self.commonkuruth = None
            self.layout.removeWidget(self.commonkuruthbox)
            self.commonkuruthbox.deleteLater()
            self.commonkuruthbox = None
            self.layout.removeWidget(self.specifickuruth)
            self.specifickuruth.deleteLater()
            self.specifickuruth = None
            self.layout.removeWidget(self.specifickuruthbox)
            self.specifickuruthbox.deleteLater()
            self.specifickuruthbox = None

            self.oplinecounter -= 2
            self.oldmeritcount = self.meritcount
            self.runonce2 = True

        self.savesettings()

        self.makesheet()

    def magetoggledef(self):
        if self.magetoggle.isChecked():
            self.magetoggle.setChecked(True)
            self.occultflag[2] = True
            self.oldmeritcount = self.meritcount
            self.oldaspirationcount = self.aspirationcount
            self.oldconditioncount = self.conditioncount
            self.oldbanecount = self.banecount

            # if self.runonce3:
            self.shadowname = QtWidgets.QLabel(self)
            self.shadowname.setText("Shadow Name: ")
            self.shadownamebox = QtWidgets.QLineEdit(self)

            self.path = QtWidgets.QLabel(self)
            self.path.setText("Path: ")
            self.pathbox = QtWidgets.QLineEdit(self)
            self.order = QtWidgets.QLabel(self)
            self.order.setText("Order: ")
            self.orderbox = QtWidgets.QLineEdit(self)
            self.legacy = QtWidgets.QLabel(self)
            self.legacy.setText("Legacy: ")
            self.legacybox = QtWidgets.QLineEdit(self)

            self.arcana = QtWidgets.QLabel(self)
            self.arcana.setText("Arcana")
            self.arcana.setFont(self.subtitlefont)

            self.death = QtWidgets.QLabel(self)
            self.death.setText("Death: ")
            self.deathbox = QtWidgets.QLineEdit(self)

            self.fate = QtWidgets.QLabel(self)
            self.fate.setText("Fate: ")
            self.fatebox = QtWidgets.QLineEdit(self)

            self.forces = QtWidgets.QLabel(self)
            self.forces.setText("Forces: ")
            self.forcesbox = QtWidgets.QLineEdit(self)

            self.life = QtWidgets.QLabel(self)
            self.life.setText("Life: ")
            self.lifebox = QtWidgets.QLineEdit(self)

            self.matter = QtWidgets.QLabel(self)
            self.matter.setText("Matter: ")
            self.matterbox = QtWidgets.QLineEdit(self)

            self.mind = QtWidgets.QLabel(self)
            self.mind.setText("Mind: ")
            self.mindbox = QtWidgets.QLineEdit(self)

            self.prime = QtWidgets.QLabel(self)
            self.prime.setText("Prime: ")
            self.primebox = QtWidgets.QLineEdit(self)

            self.spirit = QtWidgets.QLabel(self)
            self.spirit.setText("Spirit: ")
            self.spiritbox = QtWidgets.QLineEdit(self)

            self.space = QtWidgets.QLabel(self)
            self.space.setText("Space: ")
            self.spacebox = QtWidgets.QLineEdit(self)

            self.time = QtWidgets.QLabel(self)
            self.time.setText("Time: ")
            self.timebox = QtWidgets.QLineEdit(self)

            self.gnosistitle = QtWidgets.QLabel(self)
            self.gnosistitle.setText("Gnosis")
            self.gnosistitle.setFont(self.subtitlefont)

            self.gnosis = QtWidgets.QLabel(self)
            self.gnosis.setText("Gnosis: ")
            self.gnosisbox = QtWidgets.QLineEdit(self)

            self.manatitle = QtWidgets.QLabel(self)
            self.manatitle.setText("Mana")
            self.manatitle.setFont(self.subtitlefont)

            self.maxmana = QtWidgets.QLabel(self)
            self.maxmana.setText("Max Mana: ")
            self.maxmanabox = QtWidgets.QLineEdit(self)

            self.currentmana = QtWidgets.QLabel(self)
            self.currentmana.setText("Current Mana: ")
            self.currentmanabox = QtWidgets.QLineEdit(self)

            self.mwisdomtitle = QtWidgets.QLabel(self)
            self.mwisdomtitle.setText("Wisdom")
            self.mwisdomtitle.setFont(self.subtitlefont)

            self.mwisdom = QtWidgets.QLabel(self)
            self.mwisdom.setText("Wisdom: ")
            self.mwisdombox = QtWidgets.QLineEdit(self)

            self.obsessiontitle = QtWidgets.QLabel(self)
            self.obsessiontitle.setText("Obsessions")
            self.obsessiontitle.setFont(self.subtitlefont)

            self.obsession1 = QtWidgets.QLabel(self)
            self.obsession1.setText("Obsession 1: ")
            self.obsession1box = QtWidgets.QLineEdit(self)

            self.obsession2 = QtWidgets.QLabel(self)
            self.obsession2.setText("Obsession 2: ")
            self.obsession2box = QtWidgets.QLineEdit(self)

            self.obsession3 = QtWidgets.QLabel(self)
            self.obsession3.setText("Obsession 3: ")
            self.obsession3box = QtWidgets.QLineEdit(self)

            self.obsession4 = QtWidgets.QLabel(self)
            self.obsession4.setText("Obsession 4: ")
            self.obsession4box = QtWidgets.QLineEdit(self)

            self.arcaneexperiences = QtWidgets.QLabel(self)
            self.arcaneexperiences.setText("Arcane Experiences:")
            self.arcaneexperiencesbox = QtWidgets.QLineEdit(self)

            self.arcanebeats = QtWidgets.QLabel(self)
            self.arcanebeats.setText("Arcane Beats:")
            self.arcanebeat1 = QtWidgets.QCheckBox()
            self.arcanebeat1.clicked.connect(self.arcanebeatscheckdef(1))
            self.arcanebeat2 = QtWidgets.QCheckBox()
            self.arcanebeat2.clicked.connect(self.arcanebeatscheckdef(2))
            self.arcanebeat3 = QtWidgets.QCheckBox()
            self.arcanebeat3.clicked.connect(self.arcanebeatscheckdef(3))
            self.arcanebeat4 = QtWidgets.QCheckBox()
            self.arcanebeat4.clicked.connect(self.arcanebeatscheckdef(4))
            self.arcanebeat5 = QtWidgets.QCheckBox()
            self.arcanebeat5.clicked.connect(self.arcanebeatscheckdef(5))
        else:
            self.magetoggle.setChecked(False)
            self.occultflag[2] = False

            self.layout.removeWidget(self.shadowname)
            self.shadowname.deleteLater()
            self.shadowname = None
            self.layout.removeWidget(self.shadownamebox)
            self.shadownamebox.deleteLater()
            self.shadownamebox = None

            self.layout.removeWidget(self.path)
            self.path.deleteLater()
            self.path = None
            self.layout.removeWidget(self.pathbox)
            self.pathbox.deleteLater()
            self.pathbox = None
            self.layout.removeWidget(self.order)
            self.order.deleteLater()
            self.order = None
            self.layout.removeWidget(self.orderbox)
            self.orderbox.deleteLater()
            self.orderbox = None
            self.layout.removeWidget(self.legacy)
            self.legacy.deleteLater()
            self.legacy = None
            self.layout.removeWidget(self.legacybox)
            self.legacybox.deleteLater()
            self.legacybox = None

            self.layout.removeWidget(self.arcana)
            self.arcana.deleteLater()
            self.arcana = None

            self.layout.removeWidget(self.death)
            self.death.deleteLater()
            self.death = None
            self.layout.removeWidget(self.deathbox)
            self.deathbox.deleteLater()
            self.deathbox = None
            self.layout.removeWidget(self.fate)
            self.fate.deleteLater()
            self.fate = None
            self.layout.removeWidget(self.fatebox)
            self.fatebox.deleteLater()
            self.fatebox = None
            self.layout.removeWidget(self.forces)
            self.forces.deleteLater()
            self.forces = None
            self.layout.removeWidget(self.forcesbox)
            self.forcesbox.deleteLater()
            self.forcesbox = None
            self.layout.removeWidget(self.life)
            self.life.deleteLater()
            self.life = None
            self.layout.removeWidget(self.lifebox)
            self.lifebox.deleteLater()
            self.lifebox = None
            self.layout.removeWidget(self.matter)
            self.matter.deleteLater()
            self.matter = None
            self.layout.removeWidget(self.matterbox)
            self.matterbox.deleteLater()
            self.matterbox = None
            self.layout.removeWidget(self.mind)
            self.mind.deleteLater()
            self.mind = None
            self.layout.removeWidget(self.mindbox)
            self.mindbox.deleteLater()
            self.mindbox = None
            self.layout.removeWidget(self.prime)
            self.prime.deleteLater()
            self.prime = None
            self.layout.removeWidget(self.primebox)
            self.primebox.deleteLater()
            self.primebox = None
            self.layout.removeWidget(self.spirit)
            self.spirit.deleteLater()
            self.spirit = None
            self.layout.removeWidget(self.spiritbox)
            self.spiritbox.deleteLater()
            self.spiritbox = None
            self.layout.removeWidget(self.space)
            self.space.deleteLater()
            self.space = None
            self.layout.removeWidget(self.spacebox)
            self.spacebox.deleteLater()
            self.spacebox = None
            self.layout.removeWidget(self.time)
            self.time.deleteLater()
            self.time = None
            self.layout.removeWidget(self.timebox)
            self.timebox.deleteLater()
            self.timebox = None

            self.layout.removeWidget(self.gnosis)
            self.gnosis.deleteLater()
            self.gnosis = None
            self.layout.removeWidget(self.gnosistitle)
            self.gnosistitle.deleteLater()
            self.gnosistitle = None
            self.layout.removeWidget(self.gnosisbox)
            self.gnosisbox.deleteLater()
            self.gnosisbox = None
            self.layout.removeWidget(self.manatitle)
            self.manatitle.deleteLater()
            self.manatitle = None
            self.layout.removeWidget(self.maxmana)
            self.maxmana.deleteLater()
            self.maxmana = None
            self.layout.removeWidget(self.maxmanabox)
            self.maxmanabox.deleteLater()
            self.maxmanabox = None
            self.layout.removeWidget(self.currentmana)
            self.currentmana.deleteLater()
            self.currentmana = None
            self.layout.removeWidget(self.currentmanabox)
            self.currentmanabox.deleteLater()
            self.currentmanabox = None

            self.layout.removeWidget(self.mwisdom)
            self.mwisdom.deleteLater()
            self.mwisdom = None
            self.layout.removeWidget(self.mwisdomtitle)
            self.mwisdomtitle.deleteLater()
            self.mwisdomtitle = None
            self.layout.removeWidget(self.mwisdombox)
            self.mwisdombox.deleteLater()
            self.mwisdombox = None

            self.layout.removeWidget(self.obsessiontitle)
            self.obsessiontitle.deleteLater()
            self.obsessiontitle = None
            self.layout.removeWidget(self.obsession1)
            self.obsession1.deleteLater()
            self.obsession1 = None
            self.layout.removeWidget(self.obsession1box)
            self.obsession1box.deleteLater()
            self.obsession1box = None
            self.layout.removeWidget(self.obsession2)
            self.obsession2.deleteLater()
            self.obsession2 = None
            self.layout.removeWidget(self.obsession2box)
            self.obsession2box.deleteLater()
            self.obsession2box = None
            self.layout.removeWidget(self.obsession3)
            self.obsession3.deleteLater()
            self.obsession3 = None
            self.layout.removeWidget(self.obsession3box)
            self.obsession3box.deleteLater()
            self.obsession3box = None
            self.layout.removeWidget(self.obsession4)
            self.obsession4.deleteLater()
            self.obsession4 = None
            self.layout.removeWidget(self.obsession4box)
            self.obsession4box.deleteLater()
            self.obsession4box = None

            self.layout.removeWidget(self.arcaneexperiences)
            self.arcaneexperiences.deleteLater()
            self.arcaneexperiences = None
            self.layout.removeWidget(self.arcaneexperiencesbox)
            self.arcaneexperiencesbox.deleteLater()
            self.arcaneexperiencesbox = None
            self.layout.removeWidget(self.arcanebeats)
            self.arcanebeats.deleteLater()
            self.arcanebeats = None
            self.layout.removeWidget(self.arcanebeat1)
            self.arcanebeat1.deleteLater()
            self.arcanebeat1 = None
            self.layout.removeWidget(self.arcanebeat2)
            self.arcanebeat2.deleteLater()
            self.arcanebeat2 = None
            self.layout.removeWidget(self.arcanebeat3)
            self.arcanebeat3.deleteLater()
            self.arcanebeat3 = None
            self.layout.removeWidget(self.arcanebeat4)
            self.arcanebeat4.deleteLater()
            self.arcanebeat4 = None
            self.layout.removeWidget(self.arcanebeat5)
            self.arcanebeat5.deleteLater()
            self.arcanebeat5 = None

            self.oplinecounter -= 2
            self.oldmeritcount = self.meritcount

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

    def othertraitdef(self):
        self.oldothertraitcount = self.othertraitcount
        self.othertraitcount = int(self.othertraitslotsbox.text())

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

        self.wolflabel = QtWidgets.QLabel()
        self.wolflabel.setText("Character is Werewolf: ")
        self.wolftoggle = QtWidgets.QCheckBox()
        self.wolftoggle.clicked.connect(self.wolftoggledef)

        self.magelabel = QtWidgets.QLabel()
        self.magelabel.setText("Character is Mage: ")
        self.magetoggle = QtWidgets.QCheckBox()
        self.magetoggle.clicked.connect(self.magetoggledef)

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

        self.othertraitslotslabel = QtWidgets.QLabel()
        self.othertraitslotslabel.setText("Other Trait Slots Available: ")
        self.othertraitslotsbox = QtWidgets.QLineEdit()
        self.othertraitslotsbox.setText(str(self.othertraitcount))
        self.othertraitslotsupdate = QtWidgets.QPushButton('Update Other Trait Slots')
        self.othertraitslotsupdate.clicked.connect(self.othertraitdef)

        self.settingslayout.addWidget(self.settingstitle, 0, 2)

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

        self.settingslayout.addWidget(self.othertraitslotslabel, 5, 0)
        self.settingslayout.addWidget(self.othertraitslotsbox, 5, 1)
        self.settingslayout.addWidget(self.othertraitslotsupdate, 5, 2)

        self.settingslayout.addWidget(self.humanlabel, 7, 2)
        self.settingslayout.addWidget(self.humantoggle, 7, 3)

        self.settingslayout.addWidget(self.vamplabel, 8, 1)
        self.settingslayout.addWidget(self.vamptoggle, 8, 2)
        self.settingslayout.addWidget(self.wolflabel, 8, 3)
        self.settingslayout.addWidget(self.wolftoggle, 8, 4)
        self.settingslayout.addWidget(self.magelabel, 8, 5)
        self.settingslayout.addWidget(self.magetoggle, 8, 6)

        if self.vvflag == True:
            self.humantoggle.setChecked(True)
        if self.occultflag[0] == True:
            self.vamptoggle.setChecked(True)
        if self.occultflag[1] == True:
            self.wolftoggle.setChecked(True)
        if self.occultflag[2] == True:
            self.magetoggle.setChecked(True)

        self.setLayout(self.layout)

    def initsettings(self):
        if path.exists('settings.json'):
            with open('settings.json') as f:
                settingsdict = json.load(f)
            self.oldmeritcount = self.meritcount
            self.meritcount = settingsdict.get('meritslots')
            self.oldaspirationcount = self.aspirationcount
            self.aspirationcount = settingsdict.get('aspirationslots')
            self.oldconditioncount = self.conditioncount
            self.conditioncount = settingsdict.get('conditionslots')
            self.oldbanecount = self.banecount
            self.banecount = settingsdict.get('baneslots')
            if settingsdict.get('hasvicevirtueslots') == True:
                self.vvflag = True
            if settingsdict.get('hasvampireslots') == True:
                self.occultflag[0] = True
                self.oldmeritcount = self.meritcount
                self.oldaspirationcount = self.aspirationcount
                self.oldconditioncount = self.conditioncount
                self.oldbanecount = self.banecount
            if settingsdict.get('disciplineslots') == -1:
                self.olddisciplinecount = self.disciplinecount
                self.disciplinecount = 0
            else:
                self.olddisciplinecount = self.disciplinecount
                self.disciplinecount = settingsdict.get('disciplineslots')
            if settingsdict.get('haswerewolfslots') == True:
                self.occultflag[1] = True
                self.oldmeritcount = self.meritcount
                self.oldaspirationcount = self.aspirationcount
                self.oldconditioncount = self.conditioncount
                self.oldbanecount = self.banecount
            if settingsdict.get('hasmageslots') == True:
                self.occultflag[2] = True
                self.oldmeritcount = self.meritcount
                self.oldaspirationcount = self.aspirationcount
                self.oldconditioncount = self.conditioncount
                self.oldbanecount = self.banecount
            self.oldothertraitcount = self.othertraitcount
            self.othertraitcount = settingsdict.get('othertraitslots')
            self.oldattackcount = self.attackcount
            self.attackcount = settingsdict.get('attackslots')
            if self.attackcount:
                self.attackcount = self.attackcount
            else:
                self.attackcount = 6
            if self.emalliescount:
                self.emalliescount = self.emalliescount
            else:
                self.emalliescount = 4
            if self.emmentorcount:
                self.emmentorcount = self.emmentorcount
            else:
                self.emmentorcount = 4
            if self.emcontactscount:
                self.emcontactscount = self.emcontactscount
            else:
                self.emcontactscount = 4
            if self.emresourcescount:
                self.emresourcescount = self.emresourcescount
            else:
                self.emresourcescount = 4
            if self.emfamecount:
                self.emfamecount = self.emfamecount
            else:
                self.emfamecount = 4
            if self.emretainercount:
                self.emretainercount = self.emretainercount
            else:
                self.emretainercount = 4

        self.resize(1024, 768)
        if self.initmakesheet:
            self.makesheet()
        else:
            self.initmakesheet = True

    def open(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', '', 'Json Files (*.json)')
        if path != ('', 'json'):
            self.loaddef(path[0])

    def save(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save as')
        self.savedef(path[0])


    def __init__(self):
        super(MyWidget, self).__init__()

        self.setGeometry(300, 75, 1024, 768)
        self.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')

        self.allwidgets = {}

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

        self.wasvamp = False

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
        self.runonce2 = True
        self.runonce3 = True
        self.makesheetflag = False

        self.initmakesheet = False

        self.vvflag = False

        self.occultflag = [False, False, False]

        self.savedmeritnames = []
        self.savedmeritlevels = []
        self.savedaspirationnames = []
        self.savedconditionnames = []
        self.savedbanenames = []
        self.saveddisciplinenames = []
        self.saveddisciplinelevels = []

        self.savedothertraitnames = []
        self.savedothertraitlevels = []

        self.othertraitsflag = 1

        self.whealth = False

        self.blankcount = 0
        self.blanks = []

        self.oldothertraitcount = 0
        self.othertraitcount = 9

        self.oldattackcount = 0
        self.attackcount = 6

        self.savedattacknames = []
        self.savedattackdamages = []
        self.savedattackranges = []
        self.savedattackclips = []
        self.savedattackinitiatives = []
        self.savedattackstrengths = []
        self.savedattacksizes = []

        self.emalliescount = 4
        self.emmentorcount = 4
        self.emcontactscount = 4
        self.emresourcescount = 4
        self.emfamecount = 4
        self.emretainercount = 4

        self.oldemalliescount = 4
        self.oldemmentorcount = 4
        self.oldemcontactscount = 4
        self.oldemresourcescount = 4
        self.oldemfamecount = 4
        self.oldemretainercount = 4

        self.savedemallies = []
        self.savedemmentor = []
        self.savedemcontacts = []
        self.savedemresources = []
        self.savedemfame = []
        self.savedemretainer = []

        self.initsettings()

        # menu = self.createMenuBar()

        # exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # exitAction.triggered.connect(self.close)

        saveAction = QtGui.QAction('&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save Character')
        saveAction.triggered.connect(self.save)

        loadAction = QtGui.QAction('&Open', self)
        loadAction.setShortcut('Ctrl+O')
        loadAction.setStatusTip('Open Character')
        loadAction.triggered.connect(self.open)

        QtWidgets.QStatusBar()

        self.menubar = QtWidgets.QMenuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        # self.fileMenu.addAction(exitAction)
        self.fileMenu.addAction(saveAction)
        self.fileMenu.addAction(loadAction)
        # self.editMenu = self.menubar.addMenu("&Edit")
        # self.helpMenu = self.menubar.addMenu("&Help")

        self.title = QtWidgets.QLabel()

        pixMap = QtGui.QPixmap.fromImage('CofD.png')

        self.title.setPixmap( pixMap )
        self.title.show()

        self.settings = QtWidgets.QPushButton('')
        self.allwidgets['settings'] = True
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

        # self.save = QtWidgets.QPushButton('Save')
        # self.allwidgets['save'] = True
        # self.save.clicked.connect(self.savedef)
        # self.load = QtWidgets.QPushButton('Load')
        # self.allwidgets['load'] = True
        # self.load.clicked.connect(self.loaddef)

        # self.title = QtWidgets.QLabel(self)
        # self.title.setText("CofD Interactive Character Sheet")
        # self.title.setFont(self.titlefont)

        # self.saveloclabel = QtWidgets.QLabel(self)
        # self.allwidgets['saveloclabel'] = True
        # self.saveloclabel.setText("Save Location: ")
        # self.saveloc = QtWidgets.QLineEdit(self)
        # self.allwidgets['saveloc'] = True
        # self.loadloclabel = QtWidgets.QLabel(self)
        # self.allwidgets['loadloclabel'] = True
        # self.loadloclabel.setText("Load Location: ")
        # self.loadloc = QtWidgets.QLineEdit(self)
        # self.allwidgets['loadloc'] = True

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.menubar, 0, 0, 0, 8)
        # self.layout.addWidget(self.saveloclabel, 0, 1)
        # self.layout.addWidget(self.saveloc, 0, 2)
        # self.layout.addWidget(self.save, 0, 3)
        # self.layout.addWidget(self.load, 0, 4)
        # self.layout.addWidget(self.loadloclabel, 0, 5)
        # self.layout.addWidget(self.loadloc, 0, 6)

        self.layout.addWidget(self.title, 1, 3, 1, 6)
        self.layout.addWidget(self.settings, 0, 7)

        self.name = QtWidgets.QLabel(self)
        self.allwidgets['name'] = True
        self.name.setText("Name: ")
        self.boxname = QtWidgets.QLineEdit(self)
        self.allwidgets['boxname'] = True
        self.player = QtWidgets.QLabel(self)
        self.allwidgets['player'] = True
        self.player.setText("Player: ")
        self.boxplayer = QtWidgets.QLineEdit(self)
        self.allwidgets['boxplayer'] = True
        self.chronicle = QtWidgets.QLabel(self)
        self.allwidgets['chronicle'] = True
        self.chronicle.setText("Chronicle: ")
        self.boxchronicle = QtWidgets.QLineEdit(self)
        self.allwidgets['boxchronicle'] = True

        self.concept = QtWidgets.QLabel(self)
        self.allwidgets['concept'] = True
        self.boxconcept = QtWidgets.QLineEdit(self)
        self.allwidgets['boxconcept'] = True
        self.concept.setText("Concept: ")

        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")

        self.cat1 = QtWidgets.QLabel(self)
        self.allwidgets['cat1'] = True
        self.cat1.setText("Attributes")
        self.cat1.setFont(self.titlefont)

        self.statsubcat1 = QtWidgets.QLabel(self)
        self.statsubcat1.setText("Power")
        self.statsubcat1.setFont(self.subtitlefont)
        self.statsubcat2 = QtWidgets.QLabel(self)
        self.statsubcat2.setText("Finesse")
        self.statsubcat2.setFont(self.subtitlefont)
        self.statsubcat3 = QtWidgets.QLabel(self)
        self.statsubcat3.setText("Resistance")
        self.statsubcat3.setFont(self.subtitlefont)

        self.intelligence = QtWidgets.QLabel(self)
        self.allwidgets['intelligence'] = True
        self.intelligence.setText("Intelligence: ")
        self.boxintelligence = QtWidgets.QLineEdit(self)
        self.allwidgets['boxintelligence'] = True
        self.boxintelligence.setText("1")
        self.strength = QtWidgets.QLabel(self)
        self.allwidgets['strength'] = True
        self.strength.setText("Strength: ")
        self.boxstrength = QtWidgets.QLineEdit(self)
        self.allwidgets['boxstrength'] = True
        self.boxstrength.setText("1")
        self.presence = QtWidgets.QLabel(self)
        self.allwidgets['presence'] = True
        self.presence.setText("Presence: ")
        self.boxpresence = QtWidgets.QLineEdit(self)
        self.allwidgets['boxpresence'] = True
        self.boxpresence.setText("1")
        self.wits = QtWidgets.QLabel(self)
        self.allwidgets['wits'] = True
        self.wits.setText("Wits: ")
        self.dexterity = QtWidgets.QLabel(self)
        self.allwidgets['dexterity'] = True
        self.boxwits = QtWidgets.QLineEdit(self)
        self.allwidgets['boxwits'] = True
        self.boxwits.setText("1")
        self.dexterity.setText("Dexterity: ")
        self.boxdexterity = QtWidgets.QLineEdit(self)
        self.allwidgets['boxdexterity'] = True
        self.boxdexterity.setText("1")
        self.manipulation = QtWidgets.QLabel(self)
        self.allwidgets['manipulation'] = True
        self.manipulation.setText("Manipulation: ")
        self.boxmanipulation = QtWidgets.QLineEdit(self)
        self.allwidgets['boxmanipulation'] = True
        self.boxmanipulation.setText("1")
        self.resolve = QtWidgets.QLabel(self)
        self.allwidgets['resolve'] = True
        self.resolve.setText("Resolve: ")
        self.boxresolve = QtWidgets.QLineEdit(self)
        self.allwidgets['boxresolve'] = True
        self.boxresolve.setText("1")
        self.stamina = QtWidgets.QLabel(self)
        self.allwidgets['stamina'] = True
        self.stamina.setText("Stamina: ")
        self.boxstamina = QtWidgets.QLineEdit(self)
        self.allwidgets['boxstamina'] = True
        self.boxstamina.setText("1")
        self.composure = QtWidgets.QLabel(self)
        self.allwidgets['composure'] = True
        self.composure.setText("Composure: ")
        self.boxcomposure = QtWidgets.QLineEdit(self)
        self.allwidgets['boxcomposure'] = True
        self.boxcomposure.setText("1")

        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")

        self.cat2 = QtWidgets.QLabel(self)
        self.allwidgets['cat2'] = True
        self.cat2.setText("Skills")
        self.cat2.setFont(self.titlefont)
        self.subcat1 = QtWidgets.QLabel(self)
        self.allwidgets['subcat1'] = True
        self.subcat1.setText("Mental")
        self.subcat1.setFont(self.subtitlefont)
        self.desc1 = QtWidgets.QLabel(self)
        self.allwidgets['desc1'] = True
        self.desc1.setText("(-3 unskilled)")

        self.academics = QtWidgets.QLabel(self)
        self.allwidgets['academics'] = True
        self.academics.setText("Academics: ")
        self.boxacademics = QtWidgets.QLineEdit(self)
        self.boxspecacademics = QtWidgets.QLineEdit(self)
        self.allwidgets['boxacademics'] = True
        self.boxacademics.setText("0")
        self.computer = QtWidgets.QLabel(self)
        self.allwidgets['computer'] = True
        self.computer.setText("Computer: ")
        self.boxcomputer = QtWidgets.QLineEdit(self)
        self.boxspeccomputer = QtWidgets.QLineEdit(self)
        self.allwidgets['boxcomputer'] = True
        self.boxcomputer.setText("0")
        self.crafts = QtWidgets.QLabel(self)
        self.allwidgets['crafts'] = True
        self.crafts.setText("Crafts: ")
        self.boxcrafts = QtWidgets.QLineEdit(self)
        self.boxspeccrafts = QtWidgets.QLineEdit(self)
        self.allwidgets['boxcrafts'] = True
        self.boxcrafts.setText("0")
        self.investigation = QtWidgets.QLabel(self)
        self.allwidgets['investigation'] = True
        self.investigation.setText("Investigation: ")
        self.boxinvestigation = QtWidgets.QLineEdit(self)
        self.boxspecinvestigation = QtWidgets.QLineEdit(self)
        self.allwidgets['boxinvestigation'] = True
        self.boxinvestigation.setText("0")
        self.medicine = QtWidgets.QLabel(self)
        self.allwidgets['medicine'] = True
        self.medicine.setText("Medicine: ")
        self.boxmedicine = QtWidgets.QLineEdit(self)
        self.boxspecmedicine = QtWidgets.QLineEdit(self)
        self.allwidgets['boxmedicine'] = True
        self.boxmedicine.setText("0")
        self.occult = QtWidgets.QLabel(self)
        self.allwidgets['occult'] = True
        self.occult.setText("Occult: ")
        self.boxoccult = QtWidgets.QLineEdit(self)
        self.boxspecoccult = QtWidgets.QLineEdit(self)
        self.allwidgets['boxoccult'] = True
        self.boxoccult.setText("0")
        self.politics = QtWidgets.QLabel(self)
        self.allwidgets['politics'] = True
        self.politics.setText("Politics: ")
        self.boxpolitics = QtWidgets.QLineEdit(self)
        self.boxspecpolitics = QtWidgets.QLineEdit(self)
        self.allwidgets['boxpolitics'] = True
        self.boxpolitics.setText("0")
        self.science = QtWidgets.QLabel(self)
        self.allwidgets['science'] = True
        self.science.setText("Science: ")
        self.boxscience = QtWidgets.QLineEdit(self)
        self.boxspecscience = QtWidgets.QLineEdit(self)
        self.allwidgets['boxscience'] = True
        self.boxscience.setText("0")

        self.subcat2 = QtWidgets.QLabel(self)
        self.allwidgets['subcat2'] = True
        self.subcat2.setText("Physical")
        self.subcat2.setFont(self.subtitlefont)
        self.desc2 = QtWidgets.QLabel(self)
        self.allwidgets['desc2'] = True
        self.desc2.setText("(-1 unskilled)")

        self.athletics = QtWidgets.QLabel(self)
        self.allwidgets['athletics'] = True
        self.athletics.setText("Athletics: ")
        self.boxathletics = QtWidgets.QLineEdit(self)
        self.boxspecathletics = QtWidgets.QLineEdit(self)
        self.allwidgets['boxathletics'] = True
        self.boxathletics.setText("0")
        self.brawl = QtWidgets.QLabel(self)
        self.allwidgets['brawl'] = True
        self.brawl.setText("Brawl: ")
        self.boxbrawl = QtWidgets.QLineEdit(self)
        self.boxspecbrawl = QtWidgets.QLineEdit(self)
        self.allwidgets['boxbrawl'] = True
        self.boxbrawl.setText("0")
        self.drive = QtWidgets.QLabel(self)
        self.allwidgets['drive'] = True
        self.drive.setText("Drive: ")
        self.boxdrive = QtWidgets.QLineEdit(self)
        self.boxspecdrive = QtWidgets.QLineEdit(self)
        self.allwidgets['boxdrive'] = True
        self.boxdrive.setText("0")
        self.firearms = QtWidgets.QLabel(self)
        self.allwidgets['firearms'] = True
        self.firearms.setText("Firearms: ")
        self.boxfirearms = QtWidgets.QLineEdit(self)
        self.boxspecfirearms = QtWidgets.QLineEdit(self)
        self.allwidgets['boxfirearms'] = True
        self.boxfirearms.setText("0")
        self.larceny = QtWidgets.QLabel(self)
        self.allwidgets['larceny'] = True
        self.larceny.setText("Larceny: ")
        self.boxlarceny = QtWidgets.QLineEdit(self)
        self.boxspeclarceny = QtWidgets.QLineEdit(self)
        self.allwidgets['boxlarceny'] = True
        self.boxlarceny.setText("0")
        self.stealth = QtWidgets.QLabel(self)
        self.allwidgets['stealth'] = True
        self.stealth.setText("Stealth: ")
        self.boxstealth = QtWidgets.QLineEdit(self)
        self.boxspecstealth = QtWidgets.QLineEdit(self)
        self.allwidgets['boxstealth'] = True
        self.boxstealth.setText("0")
        self.survival = QtWidgets.QLabel(self)
        self.allwidgets['survival'] = True
        self.survival.setText("Survival: ")
        self.boxsurvival = QtWidgets.QLineEdit(self)
        self.boxspecsurvival = QtWidgets.QLineEdit(self)
        self.allwidgets['boxsurvival'] = True
        self.boxsurvival.setText("0")
        self.weaponry = QtWidgets.QLabel(self)
        self.allwidgets['weaponry'] = True
        self.weaponry.setText("Weaponry: ")
        self.boxweaponry = QtWidgets.QLineEdit(self)
        self.boxspecweaponry = QtWidgets.QLineEdit(self)
        self.allwidgets['boxweaponry'] = True
        self.boxweaponry.setText("0")

        self.subcat3 = QtWidgets.QLabel(self)
        self.allwidgets['subcat3'] = True
        self.subcat3.setText("Social")
        self.subcat3.setFont(self.subtitlefont)
        self.desc3 = QtWidgets.QLabel(self)
        self.allwidgets['desc3'] = True
        self.desc3.setText("(-1 unskilled)")

        self.animalken = QtWidgets.QLabel(self)
        self.allwidgets['animalken'] = True
        self.animalken.setText("Animal Ken: ")
        self.boxanimalken = QtWidgets.QLineEdit(self)
        self.boxspecanimalken = QtWidgets.QLineEdit(self)
        self.allwidgets['boxanimalken'] = True
        self.boxanimalken.setText("0")
        self.empathy = QtWidgets.QLabel(self)
        self.allwidgets['empathy'] = True
        self.empathy.setText("Empathy: ")
        self.boxempathy = QtWidgets.QLineEdit(self)
        self.boxspecempathy = QtWidgets.QLineEdit(self)
        self.allwidgets['boxempathy'] = True
        self.boxempathy.setText("0")
        self.expression = QtWidgets.QLabel(self)
        self.allwidgets['expression'] = True
        self.expression.setText("Expression: ")
        self.boxexpression = QtWidgets.QLineEdit(self)
        self.boxspecexpression = QtWidgets.QLineEdit(self)
        self.allwidgets['boxexpression'] = True
        self.boxexpression.setText("0")
        self.intimidation = QtWidgets.QLabel(self)
        self.allwidgets['intimidation'] = True
        self.intimidation.setText("Intimidation: ")
        self.boxintimidation = QtWidgets.QLineEdit(self)
        self.boxspecintimidation = QtWidgets.QLineEdit(self)
        self.allwidgets['boxintimidation'] = True
        self.boxintimidation.setText("0")
        self.persuasion = QtWidgets.QLabel(self)
        self.allwidgets['persuasion'] = True
        self.persuasion.setText("Persuasion: ")
        self.boxpersuasion = QtWidgets.QLineEdit(self)
        self.boxspecpersuasion = QtWidgets.QLineEdit(self)
        self.allwidgets['boxpersuasion'] = True
        self.boxpersuasion.setText("0")
        self.socialize = QtWidgets.QLabel(self)
        self.allwidgets['socialize'] = True
        self.socialize.setText("Socialize: ")
        self.boxsocialize = QtWidgets.QLineEdit(self)
        self.boxspecsocialize = QtWidgets.QLineEdit(self)
        self.allwidgets['boxsocialize'] = True
        self.boxsocialize.setText("0")
        self.streetwise = QtWidgets.QLabel(self)
        self.allwidgets['streetwise'] = True
        self.streetwise.setText("Streetwise: ")
        self.boxstreetwise = QtWidgets.QLineEdit(self)
        self.boxspecstreetwise = QtWidgets.QLineEdit(self)
        self.allwidgets['boxstreetwise'] = True
        self.boxstreetwise.setText("0")
        self.subterfuge = QtWidgets.QLabel(self)
        self.allwidgets['subterfuge'] = True
        self.subterfuge.setText("Subterfuge: ")
        self.boxsubterfuge = QtWidgets.QLineEdit(self)
        self.boxspecsubterfuge = QtWidgets.QLineEdit(self)
        self.allwidgets['boxsubterfuge'] = True
        self.boxsubterfuge.setText("0")

        self.cat3 = QtWidgets.QLabel(self)
        self.allwidgets['cat3'] = True
        self.cat3.setText("Other Traits")
        self.cat3.setFont(self.titlefont)

        self.merits = QtWidgets.QLabel(self)
        self.allwidgets['merits'] = True
        self.merits.setText("Merits")
        self.merits.setFont(self.subtitlefont)
        self.meritslevel = QtWidgets.QLabel(self)
        self.allwidgets['meritslevel'] = True
        self.meritslevel.setText("Level")

        self.aspirations = QtWidgets.QLabel(self)
        self.aspirations.setText("Aspirations")
        self.aspirations.setFont(self.subtitlefont)

        self.conditions = QtWidgets.QLabel(self)
        self.conditions.setText("Conditions")
        self.conditions.setFont(self.subtitlefont)

        self.banes = QtWidgets.QLabel(self)
        self.banes.setText("Banes")
        self.banes.setFont(self.subtitlefont)

        self.experiencestitle = QtWidgets.QLabel(self)
        self.experiencestitle.setText("Experiences")
        self.experiencestitle.setFont(self.subtitlefont)

        self.experiences = QtWidgets.QLabel(self)
        self.experiences.setText("Experiences:")
        self.experiencesbox = QtWidgets.QLineEdit(self)

        self.beats = QtWidgets.QLabel(self)
        self.beats.setText("Beats:")
        self.beat1 = QtWidgets.QCheckBox()
        self.beat1.clicked.connect(self.beatscheckdef(1))
        self.beat2 = QtWidgets.QCheckBox()
        self.beat2.clicked.connect(self.beatscheckdef(2))
        self.beat3 = QtWidgets.QCheckBox()
        self.beat3.clicked.connect(self.beatscheckdef(3))
        self.beat4 = QtWidgets.QCheckBox()
        self.beat4.clicked.connect(self.beatscheckdef(4))
        self.beat5 = QtWidgets.QCheckBox()
        self.beat5.clicked.connect(self.beatscheckdef(5))

        #begin other traits

        if self.othertraitsflag == 0:
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

            self.healthlabel = QtWidgets.QLabel(self)
            self.healthlabel.setText("Health")
            self.healthlabel.setFont(self.subtitlefont)

            self.maxhealthmodlabel = QtWidgets.QLabel(self)
            self.maxhealthmodlabel.setText("Max Health Mod: ")
            self.maxhealthmodbox = QtWidgets.QLineEdit(self)

            self.maxhealthlabel = QtWidgets.QLabel(self)
            self.maxhealthlabel.setText("Max Health: ")
            self.maxhealthbox = QtWidgets.QLabel(self)
            if self.maxhealthmodbox.text() != "":
                self.maxhealthbox.setText(str(int(self.maxhealthmodbox.text()) + int(self.sizeval.text()) + self.staminastat))
            else:
                self.maxhealthbox.setText(str(int(self.sizeval.text()) + self.staminastat))
            self.bashingdamagelabel = QtWidgets.QLabel(self)
            self.bashingdamagelabel.setText("Bashing Damage: ")
            self.bashingdamagebox = QtWidgets.QLineEdit(self)

            self.lethaldamagelabel = QtWidgets.QLabel(self)
            self.lethaldamagelabel.setText("Lethal Damage: ")
            self.lethaldamagebox = QtWidgets.QLineEdit(self)

            self.aggravateddamagelabel = QtWidgets.QLabel(self)
            self.aggravateddamagelabel.setText("Aggravated Damage: ")
            self.aggravateddamagebox = QtWidgets.QLineEdit(self)

            self.willpowerlabel = QtWidgets.QLabel(self)
            self.willpowerlabel.setText("Willpower")
            self.willpowerlabel.setFont(self.subtitlefont)

            self.willpowerdotlabel = QtWidgets.QLabel(self)
            self.willpowerdotlabel.setText("Willpower Dot: ")
            self.willpowerdotbox = QtWidgets.QLineEdit(self)
            self.willpowerdotbox.setText(str(self.composurestat + self.resolvestat))

            self.willpowerpointlabel = QtWidgets.QLabel(self)
            self.willpowerpointlabel.setText("Willpower Point: ")
            self.willpowerpointbox = QtWidgets.QLineEdit(self)
        elif self.othertraitsflag == 1:
            self.size = QtWidgets.QLabel(self)
            self.size.setText("Size: ")
            self.sizeval = QtWidgets.QLineEdit(self)

            self.speed = QtWidgets.QLabel(self)
            self.speed.setText("Speed: ")
            self.speedval = QtWidgets.QLineEdit(self)

            self.defense = QtWidgets.QLabel(self)
            self.defense.setText("Defense: ")
            self.defenseval = QtWidgets.QLineEdit(self)

            self.armor = QtWidgets.QLabel(self)
            self.armor.setText("Armor: ")
            self.armorval = QtWidgets.QLineEdit(self)

            self.initiative = QtWidgets.QLabel(self)
            self.initiative.setText("Initiative Mod: ")
            self.initiativeval = QtWidgets.QLineEdit(self)

            self.healthlabel = QtWidgets.QLabel(self)
            self.healthlabel.setText("Health")
            self.healthlabel.setFont(self.subtitlefont)

            self.maxhealthlabel = QtWidgets.QLabel(self)
            self.maxhealthlabel.setText("Max Health: ")
            self.maxhealthbox = QtWidgets.QLineEdit(self)

            self.bashingdamagelabel = QtWidgets.QLabel(self)
            self.bashingdamagelabel.setText("Bashing Damage: ")
            self.bashingdamagebox = QtWidgets.QLineEdit(self)

            self.lethaldamagelabel = QtWidgets.QLabel(self)
            self.lethaldamagelabel.setText("Lethal Damage: ")
            self.lethaldamagebox = QtWidgets.QLineEdit(self)

            self.aggravateddamagelabel = QtWidgets.QLabel(self)
            self.aggravateddamagelabel.setText("Aggravated Damage: ")
            self.aggravateddamagebox = QtWidgets.QLineEdit(self)

            self.willpowerlabel = QtWidgets.QLabel(self)
            self.willpowerlabel.setText("Willpower")
            self.willpowerlabel.setFont(self.subtitlefont)

            self.willpowerdotlabel = QtWidgets.QLabel(self)
            self.willpowerdotlabel.setText("Willpower Dot: ")
            self.willpowerdotbox = QtWidgets.QLineEdit(self)
            self.willpowerdotbox.setText(str(self.composurestat + self.resolvestat))

            self.willpowerpointlabel = QtWidgets.QLabel(self)
            self.willpowerpointlabel.setText("Willpower Point: ")
            self.willpowerpointbox = QtWidgets.QLineEdit(self)

        whealthcounter = 0

        if self.vvflag:
            self.virtue = QtWidgets.QLabel(self)
            self.virtue.setText("Virtue: ")
            self.boxvirtue = QtWidgets.QLineEdit(self)
            self.vice = QtWidgets.QLabel(self)
            self.vice.setText("Vice: ")
            self.boxvice = QtWidgets.QLineEdit(self)

        if self.occultflag[0]:
            self.disciplines = QtWidgets.QLabel(self)
            self.disciplines.setText("Disciplines")
            self.disciplines.setFont(self.subtitlefont)
            self.disciplineslevel = QtWidgets.QLabel(self)
            self.disciplineslevel.setText("Level")

            self.bloodpotencytitle = QtWidgets.QLabel(self)
            self.bloodpotencytitle.setText("Blood Potency")
            self.bloodpotencytitle.setFont(self.subtitlefont)

            self.bloodpotencylabel = QtWidgets.QLabel(self)
            self.bloodpotencylabel.setText("Blood Potency: ")
            self.bloodpotencybox = QtWidgets.QLineEdit(self)

            self.vitaetitle = QtWidgets.QLabel(self)
            self.vitaetitle.setText("Vitae")
            self.vitaetitle.setFont(self.subtitlefont)

            self.maxvitaelabel = QtWidgets.QLabel(self)
            self.maxvitaelabel.setText("Max Vitae: ")
            self.maxvitaebox = QtWidgets.QLineEdit(self)

            self.currentvitaelabel = QtWidgets.QLabel(self)
            self.currentvitaelabel.setText("Current Vitae: ")
            self.currentvitaebox = QtWidgets.QLineEdit(self)


            self.humanitytitle = QtWidgets.QLabel(self)
            self.humanitytitle.setText("Humanity")
            self.humanitytitle.setFont(self.subtitlefont)

            self.num1 = QtWidgets.QLabel(self)
            self.num1.setText("1")
            self.num2 = QtWidgets.QLabel(self)
            self.num2.setText("2")
            self.num3 = QtWidgets.QLabel(self)
            self.num3.setText("3")
            self.num4 = QtWidgets.QLabel(self)
            self.num4.setText("4")
            self.num5 = QtWidgets.QLabel(self)
            self.num5.setText("5")
            self.num6 = QtWidgets.QLabel(self)
            self.num6.setText("6")
            self.num7 = QtWidgets.QLabel(self)
            self.num7.setText("7")
            self.num8 = QtWidgets.QLabel(self)
            self.num8.setText("8")
            self.num9 = QtWidgets.QLabel(self)
            self.num9.setText("9")
            self.num10 = QtWidgets.QLabel(self)
            self.num10.setText("10")

            self.humanitybox1 = QtWidgets.QLineEdit(self)
            self.humanitybox2 = QtWidgets.QLineEdit(self)
            self.humanitybox3 = QtWidgets.QLineEdit(self)
            self.humanitybox4 = QtWidgets.QLineEdit(self)
            self.humanitybox5 = QtWidgets.QLineEdit(self)
            self.humanitybox6 = QtWidgets.QLineEdit(self)
            self.humanitybox7 = QtWidgets.QLineEdit(self)
            self.humanitybox8 = QtWidgets.QLineEdit(self)
            self.humanitybox9 = QtWidgets.QLineEdit(self)
            self.humanitybox10 = QtWidgets.QLineEdit(self)

            self.humanitycheck1 = QtWidgets.QCheckBox()
            self.humanitycheck1.clicked.connect(self.humanitycheckdef(1))
            self.humanitycheck2 = QtWidgets.QCheckBox()
            self.humanitycheck2.clicked.connect(self.humanitycheckdef(2))
            self.humanitycheck3 = QtWidgets.QCheckBox()
            self.humanitycheck3.clicked.connect(self.humanitycheckdef(3))
            self.humanitycheck4 = QtWidgets.QCheckBox()
            self.humanitycheck4.clicked.connect(self.humanitycheckdef(4))
            self.humanitycheck5 = QtWidgets.QCheckBox()
            self.humanitycheck5.clicked.connect(self.humanitycheckdef(5))
            self.humanitycheck6 = QtWidgets.QCheckBox()
            self.humanitycheck6.clicked.connect(self.humanitycheckdef(6))
            self.humanitycheck7 = QtWidgets.QCheckBox()
            self.humanitycheck7.clicked.connect(self.humanitycheckdef(7))
            self.humanitycheck8 = QtWidgets.QCheckBox()
            self.humanitycheck8.clicked.connect(self.humanitycheckdef(8))
            self.humanitycheck9 = QtWidgets.QCheckBox()
            self.humanitycheck9.clicked.connect(self.humanitycheckdef(9))
            self.humanitycheck10 = QtWidgets.QCheckBox()
            self.humanitycheck10.clicked.connect(self.humanitycheckdef(10))

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

        if self.occultflag[1]:
            self.whealth = True

            self.whealthtext1 = QtWidgets.QLabel(self)
            self.whealthtext1.setText("(+2 Dalu Form, +4 Gauru")
            self.whealthtext2 = QtWidgets.QLabel(self)
            self.whealthtext2.setText("Form, +3 Urshul Form)")

            self.auspice = QtWidgets.QLabel(self)
            self.auspice.setText("Auspice: ")
            self.boxauspice = QtWidgets.QLineEdit(self)
            self.tribe = QtWidgets.QLabel(self)
            self.tribe.setText("Tribe: ")
            self.boxtribe = QtWidgets.QLineEdit(self)
            self.lodge = QtWidgets.QLabel(self)
            self.lodge.setText("Lodge: ")
            self.boxlodge = QtWidgets.QLineEdit(self)

            self.blood = QtWidgets.QLabel(self)
            self.blood.setText("Blood: ")
            self.boxblood = QtWidgets.QLineEdit(self)
            self.bone = QtWidgets.QLabel(self)
            self.bone.setText("Bone: ")
            self.boxbone = QtWidgets.QLineEdit(self)

            self.renown = QtWidgets.QLabel(self)
            self.renown.setText("Renown")
            self.renown.setFont(self.subtitlefont)

            self.purity = QtWidgets.QLabel(self)
            self.purity.setText("Purity: ")
            self.puritybox = QtWidgets.QLineEdit(self)

            self.glory = QtWidgets.QLabel(self)
            self.glory.setText("Glory: ")
            self.glorybox = QtWidgets.QLineEdit(self)

            self.honor = QtWidgets.QLabel(self)
            self.honor.setText("Honor: ")
            self.honorbox = QtWidgets.QLineEdit(self)

            self.wisdom = QtWidgets.QLabel(self)
            self.wisdom.setText("Wisdom: ")
            self.wisdombox = QtWidgets.QLineEdit(self)

            self.cunning = QtWidgets.QLabel(self)
            self.cunning.setText("Cunning: ")
            self.cunningbox = QtWidgets.QLineEdit(self)

            self.primalurgetitle = QtWidgets.QLabel(self)
            self.primalurgetitle.setText("Primal Urge")
            self.primalurgetitle.setFont(self.subtitlefont)

            self.primalurge = QtWidgets.QLabel(self)
            self.primalurge.setText("Primal Urge: ")
            self.primalurgebox = QtWidgets.QLineEdit(self)

            self.essencetitle = QtWidgets.QLabel(self)
            self.essencetitle.setText("Essence")
            self.essencetitle.setFont(self.subtitlefont)

            self.maxessence = QtWidgets.QLabel(self)
            self.maxessence.setText("Max Essence: ")
            self.maxessencebox = QtWidgets.QLineEdit(self)

            self.currentessence = QtWidgets.QLabel(self)
            self.currentessence.setText("Current Essence: ")
            self.currentessencebox = QtWidgets.QLineEdit(self)

            self.harmonytitle = QtWidgets.QLabel(self)
            self.harmonytitle.setText("Harmony")
            self.harmonytitle.setFont(self.subtitlefont)

            self.harmony = QtWidgets.QLabel(self)
            self.harmony.setText("Harmony: ")
            self.harmonybox = QtWidgets.QLineEdit(self)

            self.fleshtouchstonetitle = QtWidgets.QLabel(self)
            self.fleshtouchstonetitle.setText("Flesh Touchstone")
            self.fleshtouchstonetitle.setFont(self.subtitlefont)

            self.fleshtouchstone = QtWidgets.QLabel(self)
            self.fleshtouchstone.setText("Flesh Touchstone: ")
            self.fleshtouchstonebox = QtWidgets.QLineEdit(self)

            self.spirittouchstonetitle = QtWidgets.QLabel(self)
            self.spirittouchstonetitle.setText("Spirit Touchstone")
            self.spirittouchstonetitle.setFont(self.subtitlefont)

            self.spirittouchstone = QtWidgets.QLabel(self)
            self.spirittouchstone.setText("Spirit Touchstone: ")
            self.spirittouchstonebox = QtWidgets.QLineEdit(self)

            self.passivekuruth = QtWidgets.QLabel(self)
            self.passivekuruth.setText("Passive Kuruth Trigger: ")
            self.passivekuruthbox = QtWidgets.QTextEdit(self)

            self.commonkuruth = QtWidgets.QLabel(self)
            self.commonkuruth.setText("Common Kuruth Trigger: ")
            self.commonkuruthbox = QtWidgets.QTextEdit(self)

            self.specifickuruth = QtWidgets.QLabel(self)
            self.specifickuruth.setText("Specific Kuruth Trigger: ")
            self.specifickuruthbox = QtWidgets.QTextEdit(self)

        if self.occultflag[2]:
            self.shadowname = QtWidgets.QLabel(self)
            self.shadowname.setText("Shadow Name: ")
            self.shadownamebox = QtWidgets.QLineEdit(self)

            self.path = QtWidgets.QLabel(self)
            self.path.setText("Path: ")
            self.pathbox = QtWidgets.QLineEdit(self)
            self.order = QtWidgets.QLabel(self)
            self.order.setText("Order: ")
            self.orderbox = QtWidgets.QLineEdit(self)
            self.legacy = QtWidgets.QLabel(self)
            self.legacy.setText("Legacy: ")
            self.legacybox = QtWidgets.QLineEdit(self)

            self.arcana = QtWidgets.QLabel(self)
            self.arcana.setText("Arcana")
            self.arcana.setFont(self.subtitlefont)

            self.death = QtWidgets.QLabel(self)
            self.death.setText("Death: ")
            self.deathbox = QtWidgets.QLineEdit(self)

            self.fate = QtWidgets.QLabel(self)
            self.fate.setText("Fate: ")
            self.fatebox = QtWidgets.QLineEdit(self)

            self.forces = QtWidgets.QLabel(self)
            self.forces.setText("Forces: ")
            self.forcesbox = QtWidgets.QLineEdit(self)

            self.life = QtWidgets.QLabel(self)
            self.life.setText("Life: ")
            self.lifebox = QtWidgets.QLineEdit(self)

            self.matter = QtWidgets.QLabel(self)
            self.matter.setText("Matter: ")
            self.matterbox = QtWidgets.QLineEdit(self)

            self.mind = QtWidgets.QLabel(self)
            self.mind.setText("Mind: ")
            self.mindbox = QtWidgets.QLineEdit(self)

            self.prime = QtWidgets.QLabel(self)
            self.prime.setText("Prime: ")
            self.primebox = QtWidgets.QLineEdit(self)

            self.spirit = QtWidgets.QLabel(self)
            self.spirit.setText("Spirit: ")
            self.spiritbox = QtWidgets.QLineEdit(self)

            self.space = QtWidgets.QLabel(self)
            self.space.setText("Space: ")
            self.spacebox = QtWidgets.QLineEdit(self)

            self.time = QtWidgets.QLabel(self)
            self.time.setText("Time: ")
            self.timebox = QtWidgets.QLineEdit(self)

            self.gnosistitle = QtWidgets.QLabel(self)
            self.gnosistitle.setText("Gnosis")
            self.gnosistitle.setFont(self.subtitlefont)

            self.gnosis = QtWidgets.QLabel(self)
            self.gnosis.setText("Gnosis: ")
            self.gnosisbox = QtWidgets.QLineEdit(self)

            self.manatitle = QtWidgets.QLabel(self)
            self.manatitle.setText("Mana")
            self.manatitle.setFont(self.subtitlefont)

            self.maxmana = QtWidgets.QLabel(self)
            self.maxmana.setText("Max Mana: ")
            self.maxmanabox = QtWidgets.QLineEdit(self)

            self.currentmana = QtWidgets.QLabel(self)
            self.currentmana.setText("Current Mana: ")
            self.currentmanabox = QtWidgets.QLineEdit(self)

            self.mwisdomtitle = QtWidgets.QLabel(self)
            self.mwisdomtitle.setText("Wisdom")
            self.mwisdomtitle.setFont(self.subtitlefont)

            self.mwisdom = QtWidgets.QLabel(self)
            self.mwisdom.setText("Wisdom: ")
            self.mwisdombox = QtWidgets.QLineEdit(self)

            self.obsessiontitle = QtWidgets.QLabel(self)
            self.obsessiontitle.setText("Obsessions")
            self.obsessiontitle.setFont(self.subtitlefont)

            self.obsession1 = QtWidgets.QLabel(self)
            self.obsession1.setText("Obsession 1: ")
            self.obsession1box = QtWidgets.QLineEdit(self)

            self.obsession2 = QtWidgets.QLabel(self)
            self.obsession2.setText("Obsession 2: ")
            self.obsession2box = QtWidgets.QLineEdit(self)

            self.obsession3 = QtWidgets.QLabel(self)
            self.obsession3.setText("Obsession 3: ")
            self.obsession3box = QtWidgets.QLineEdit(self)

            self.obsession4 = QtWidgets.QLabel(self)
            self.obsession4.setText("Obsession 4: ")
            self.obsession4box = QtWidgets.QLineEdit(self)

            self.arcaneexperiences = QtWidgets.QLabel(self)
            self.arcaneexperiences.setText("Arcane Experiences:")
            self.arcaneexperiencesbox = QtWidgets.QLineEdit(self)

            self.arcanebeats = QtWidgets.QLabel(self)
            self.arcanebeats.setText("Arcane Beats:")
            self.arcanebeat1 = QtWidgets.QCheckBox()
            self.arcanebeat1.clicked.connect(self.arcanebeatscheckdef(1))
            self.arcanebeat2 = QtWidgets.QCheckBox()
            self.arcanebeat2.clicked.connect(self.arcanebeatscheckdef(2))
            self.arcanebeat3 = QtWidgets.QCheckBox()
            self.arcanebeat3.clicked.connect(self.arcanebeatscheckdef(3))
            self.arcanebeat4 = QtWidgets.QCheckBox()
            self.arcanebeat4.clicked.connect(self.arcanebeatscheckdef(4))
            self.arcanebeat5 = QtWidgets.QCheckBox()
            self.arcanebeat5.clicked.connect(self.arcanebeatscheckdef(5))

        #page 2

        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")
        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")
        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")
        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")
        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")

        # self.titlep2 = QtWidgets.QLabel()
        #
        # self.titlep2.setPixmap( pixMap )
        # self.titlep2.show()

        self.othertraits = QtWidgets.QLabel(self)
        self.othertraits.setText("Other Traits")
        self.othertraits.setFont(self.titlefont)

        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")

        self.combat = QtWidgets.QLabel(self)
        self.combat.setText("Combat")
        self.combat.setFont(self.titlefont)

        self.weapons = QtWidgets.QLabel(self)
        self.weapons.setText("Weapon / Attack")
        self.weapons.setFont(self.subtitlefont)

        self.attackname = QtWidgets.QLabel(self)
        self.attackname.setText("Attack")
        self.attackdamage = QtWidgets.QLabel(self)
        self.attackdamage.setText("Damage")
        self.attackrange = QtWidgets.QLabel(self)
        self.attackrange.setText("Range")
        self.attackclip = QtWidgets.QLabel(self)
        self.attackclip.setText("Clip")
        self.attackinitiative = QtWidgets.QLabel(self)
        self.attackinitiative.setText("Initiative")
        self.attackstrength = QtWidgets.QLabel(self)
        self.attackstrength.setText("Strength")
        self.attacksize = QtWidgets.QLabel(self)
        self.attacksize.setText("Size")

        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")

        self.armortitle = QtWidgets.QLabel(self)
        self.armortitle.setText("Armor")
        self.armortitle.setFont(self.subtitlefont)

        self.armorrating = QtWidgets.QLabel(self)
        self.armorrating.setText("Rating: ")
        self.armorratingbox = QtWidgets.QLineEdit(self)
        self.armorstrength = QtWidgets.QLabel(self)
        self.armorstrength.setText("Strength: ")
        self.armorstrengthbox = QtWidgets.QLineEdit(self)
        self.armordefense = QtWidgets.QLabel(self)
        self.armordefense.setText("Defense: ")
        self.armordefensebox = QtWidgets.QLineEdit(self)
        self.armorspeed = QtWidgets.QLabel(self)
        self.armorspeed.setText("Speed: ")
        self.armorspeedbox = QtWidgets.QLineEdit(self)
        self.armordescription = QtWidgets.QLabel(self)
        self.armordescription.setText("Description: ")
        self.armordescriptionbox = QtWidgets.QTextEdit(self)

        #page 3

        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")
        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")
        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")
        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")
        self.blanks.append(QtWidgets.QLabel(self))
        self.blankcount += 1
        self.blanks[self.blankcount - 1].setText(" ")

        self.expandedmerits = QtWidgets.QLabel(self)
        self.expandedmerits.setText("Expanded Merits")
        self.expandedmerits.setFont(self.titlefont)

        self.emallies = QtWidgets.QLabel(self)
        self.emallies.setText("Allies")
        self.emallies.setFont(self.subtitlefont)

        self.emmentor = QtWidgets.QLabel(self)
        self.emmentor.setText("Mentor")
        self.emmentor.setFont(self.subtitlefont)

        self.emcontacts = QtWidgets.QLabel(self)
        self.emcontacts.setText("Contacts")
        self.emcontacts.setFont(self.subtitlefont)

        self.emresources = QtWidgets.QLabel(self)
        self.emresources.setText("Resources")
        self.emresources.setFont(self.subtitlefont)

        self.emfame = QtWidgets.QLabel(self)
        self.emfame.setText("Fame")
        self.emfame.setFont(self.subtitlefont)

        self.emretainer = QtWidgets.QLabel(self)
        self.emretainer.setText("Retainer")
        self.emretainer.setFont(self.subtitlefont)

        self.makesheet()

app = QtWidgets.QApplication([])

widget = MyWidget()
# widget.resize(1024, 768)
# widget.show()

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
