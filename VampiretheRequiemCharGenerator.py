import json
from os import path
import random

supernaturalflags = {'vampire': True}

firstname = ''

with open("firstnames.txt") as f:
    randnum = random.randint(0, 4944)
    nonemptylines = [line.strip("\n") for line in f if line != "\n"]
    for i, line in enumerate(nonemptylines):
        if i == randnum:
            firstname = line

surname = ''

with open("surnames.txt") as f:
    randnum = random.randint(0, 88798)
    nonemptylines = [line.strip("\n") for line in f if line != "\n"]
    for i, line in enumerate(nonemptylines):
        if i == randnum:
            surname = line

file = 'samplekindredneonatetable.json'

if path.exists(file):
    with open(file) as f:
        chartable = json.load(f)
else:
    chartable = {}

clanslist = ['Daeva', 'Gangrel', 'Mekhet', 'Nosferatu', 'Ventrue']
covenantslist = ['The Carthian Movement', 'The Circle of the Crone', 'The Invictus', 'The Lancea et Sanctum', 'The Ordo Dracul', 'Unaligned']

chartable[firstname+surname] = {'name': firstname + ' ' + surname,

'supernaturaltags': [],

'stats': {'intelligence': 1, 'strength': 1, 'presence': 1, 'wits': 1, 'dexterity': 1, 'manipulation': 1, 'resolve': 1, 'stamina': 1, 'composure': 1},

'health':
{'maxhealth': 5,
'injuries': {'bashingdmg': 0, 'lethaldmg': 0, 'aggravateddmg': 0}},

'integrity': 7,

'size': 5,
'speed': 5,
'initiativemod': 0,
'defense': 0,
'armor': 0,
'willpower': {'permanentwillpower': 0, 'temporarywillpower': 0},

'skills':{'academics': 0,
'animalken': 0,
'athletics': 0,
'brawl': 0,
'computer': 0,
'crafts': 0,
'drive': 0,
'empathy': 0,
'expression': 0,
'firearms': 0,
'intimidation': 0,
'investigation': 0,
'larceny': 0,
'medicine': 0,
'occult': 0,
'persuasion': 0,
'politics': 0,
'science': 0,
'socialize': 0,
'stealth': 0,
'streetwise': 0,
'subterfuge': 0,
'survival': 0,
'weaponry': 0},

'merits': {},

'aspirations': {},

'notes': {}
}

(chartable[firstname+surname])['speed'] = 5 + ((chartable[firstname+surname])['stats'])['strength'] + ((chartable[firstname+surname])['stats'])['dexterity']
((chartable[firstname+surname])['health'])['maxhealth'] = (chartable[firstname+surname])['size'] + ((chartable[firstname+surname])['stats'])['stamina']
(chartable[firstname+surname])['initiativemod'] = ((chartable[firstname+surname])['stats'])['dexterity'] + ((chartable[firstname+surname])['stats'])['composure']
if ((chartable[firstname+surname])['stats'])['wits'] < ((chartable[firstname+surname])['stats'])['dexterity']:
    (chartable[firstname+surname])['defense'] = ((chartable[firstname+surname])['stats'])['wits'] + ((chartable[firstname+surname])['skills'])['athletics']
else:
    (chartable[firstname+surname])['defense'] = ((chartable[firstname+surname])['stats'])['dexterity'] + ((chartable[firstname+surname])['skills'])['athletics']
(chartable[firstname+surname])['permanentwillpower'] = ((chartable[firstname+surname])['stats'])['resolve'] + ((chartable[firstname+surname])['stats'])['composure']
(chartable[firstname+surname])['temporarywillpower'] = ((chartable[firstname+surname])['stats'])['resolve'] + ((chartable[firstname+surname])['stats'])['composure']

prirandnum = random.randint(0, 3)
pristatdist = [[5, 2, 1], [4, 3, 1], [4, 2, 2], [3, 3, 2]]
preshiftpristatdist = pristatdist[prirandnum]
postshiftpristatdist = []
prishift1 = random.randint(0, 2)
prishift2 = random.randint(0, 1)
postshiftpristatdist.append(preshiftpristatdist[prishift1])
preshiftpristatdist.pop(prishift1)
postshiftpristatdist.append(preshiftpristatdist[prishift2])
preshiftpristatdist.pop(prishift2)
postshiftpristatdist.append(preshiftpristatdist[0])

secrandnum = random.randint(0, 3)
secstatdist = [[5, 1, 1], [4, 2, 1], [3, 3, 1], [3, 2, 2]]
preshiftsecstatdist = secstatdist[secrandnum]
postshiftsecstatdist = []
secshift1 = random.randint(0, 2)
secshift2 = random.randint(0, 1)
postshiftsecstatdist.append(preshiftsecstatdist[secshift1])
preshiftsecstatdist.pop(secshift1)
postshiftsecstatdist.append(preshiftsecstatdist[secshift2])
preshiftsecstatdist.pop(secshift2)
postshiftsecstatdist.append(preshiftsecstatdist[0])

terrandnum = random.randint(0, 2)
terstatdist = [[4, 1, 1], [3, 2, 1], [2, 2, 2]]
preshiftterstatdist = terstatdist[terrandnum]
postshiftterstatdist = []
tershift1 = random.randint(0, 2)
tershift2 = random.randint(0, 1)
postshiftterstatdist.append(preshiftterstatdist[tershift1])
preshiftterstatdist.pop(tershift1)
postshiftterstatdist.append(preshiftterstatdist[tershift2])
preshiftterstatdist.pop(tershift2)
postshiftterstatdist.append(preshiftterstatdist[0])

pristat = random.randint(0, 2)
secstat = random.randint(0, 1)

if pristat == 0:
    if secstat == 0:
        ((chartable[firstname+surname])['stats'])['intelligence'] = postshiftpristatdist[0]
        ((chartable[firstname+surname])['stats'])['wits'] = postshiftpristatdist[1]
        ((chartable[firstname+surname])['stats'])['resolve'] = postshiftpristatdist[2]
        ((chartable[firstname+surname])['stats'])['strength'] = postshiftsecstatdist[0]
        ((chartable[firstname+surname])['stats'])['dexterity'] = postshiftsecstatdist[1]
        ((chartable[firstname+surname])['stats'])['stamina'] = postshiftsecstatdist[2]
        ((chartable[firstname+surname])['stats'])['presence'] = postshiftterstatdist[0]
        ((chartable[firstname+surname])['stats'])['manipulation'] = postshiftterstatdist[1]
        ((chartable[firstname+surname])['stats'])['composure'] = postshiftterstatdist[2]
    else:
        ((chartable[firstname+surname])['stats'])['intelligence'] = postshiftpristatdist[0]
        ((chartable[firstname+surname])['stats'])['wits'] = postshiftpristatdist[1]
        ((chartable[firstname+surname])['stats'])['resolve'] = postshiftpristatdist[2]
        ((chartable[firstname+surname])['stats'])['presence'] = postshiftsecstatdist[0]
        ((chartable[firstname+surname])['stats'])['manipulation'] = postshiftsecstatdist[1]
        ((chartable[firstname+surname])['stats'])['composure'] = postshiftsecstatdist[2]
        ((chartable[firstname+surname])['stats'])['strength'] = postshiftterstatdist[0]
        ((chartable[firstname+surname])['stats'])['dexterity'] = postshiftterstatdist[1]
        ((chartable[firstname+surname])['stats'])['stamina'] = postshiftterstatdist[2]
elif pristat == 1:
    if secstat == 0:
        ((chartable[firstname+surname])['stats'])['strength'] = postshiftpristatdist[0]
        ((chartable[firstname+surname])['stats'])['dexterity'] = postshiftpristatdist[1]
        ((chartable[firstname+surname])['stats'])['stamina'] = postshiftpristatdist[2]
        ((chartable[firstname+surname])['stats'])['intelligence'] = postshiftsecstatdist[0]
        ((chartable[firstname+surname])['stats'])['wits'] = postshiftsecstatdist[1]
        ((chartable[firstname+surname])['stats'])['resolve'] = postshiftsecstatdist[2]
        ((chartable[firstname+surname])['stats'])['presence'] = postshiftterstatdist[0]
        ((chartable[firstname+surname])['stats'])['manipulation'] = postshiftterstatdist[1]
        ((chartable[firstname+surname])['stats'])['composure'] = postshiftterstatdist[2]
    else:
        ((chartable[firstname+surname])['stats'])['strength'] = postshiftpristatdist[0]
        ((chartable[firstname+surname])['stats'])['dexterity'] = postshiftpristatdist[1]
        ((chartable[firstname+surname])['stats'])['stamina'] = postshiftpristatdist[2]
        ((chartable[firstname+surname])['stats'])['presence'] = postshiftsecstatdist[0]
        ((chartable[firstname+surname])['stats'])['manipulation'] = postshiftsecstatdist[1]
        ((chartable[firstname+surname])['stats'])['composure'] = postshiftsecstatdist[2]
        ((chartable[firstname+surname])['stats'])['intelligence'] = postshiftterstatdist[0]
        ((chartable[firstname+surname])['stats'])['wits'] = postshiftterstatdist[1]
        ((chartable[firstname+surname])['stats'])['resolve'] = postshiftterstatdist[2]
else:
    if secstat == 0:
        ((chartable[firstname+surname])['stats'])['presence'] = postshiftpristatdist[0]
        ((chartable[firstname+surname])['stats'])['manipulation'] = postshiftpristatdist[1]
        ((chartable[firstname+surname])['stats'])['composure'] = postshiftpristatdist[2]
        ((chartable[firstname+surname])['stats'])['intelligence'] = postshiftsecstatdist[0]
        ((chartable[firstname+surname])['stats'])['wits'] = postshiftsecstatdist[1]
        ((chartable[firstname+surname])['stats'])['resolve'] = postshiftsecstatdist[2]
        ((chartable[firstname+surname])['stats'])['strength'] = postshiftterstatdist[0]
        ((chartable[firstname+surname])['stats'])['dexterity'] = postshiftterstatdist[1]
        ((chartable[firstname+surname])['stats'])['stamina'] = postshiftterstatdist[2]
    else:
        ((chartable[firstname+surname])['stats'])['presence'] = postshiftpristatdist[0]
        ((chartable[firstname+surname])['stats'])['manipulation'] = postshiftpristatdist[1]
        ((chartable[firstname+surname])['stats'])['composure'] = postshiftpristatdist[2]
        ((chartable[firstname+surname])['stats'])['strength'] = postshiftsecstatdist[0]
        ((chartable[firstname+surname])['stats'])['dexterity'] = postshiftsecstatdist[1]
        ((chartable[firstname+surname])['stats'])['stamina'] = postshiftsecstatdist[2]
        ((chartable[firstname+surname])['stats'])['intelligence'] = postshiftterstatdist[0]
        ((chartable[firstname+surname])['stats'])['wits'] = postshiftterstatdist[1]
        ((chartable[firstname+surname])['stats'])['resolve'] = postshiftterstatdist[2]

prirandnum = random.randint(0, 23)
priskilldist = [[5, 5, 1, 0, 0, 0, 0, 0], [5, 4, 2, 0, 0, 0, 0, 0], [5, 4, 1, 1, 0, 0, 0, 0], [5, 3, 3, 0, 0, 0, 0, 0], [5, 3, 2, 1, 0, 0, 0, 0], [5, 3, 1, 1, 1, 0, 0, 0], [5, 2, 1, 1, 1, 1, 0, 0], [5, 1, 1, 1, 1, 1, 1, 0], [4, 4, 3, 0, 0, 0, 0, 0], [4, 4, 2, 1, 0, 0, 0, 0], [4, 4, 1, 1, 1, 0, 0, 0], [4, 3, 3, 1, 0, 0, 0, 0], [4, 3, 2, 1, 1, 0, 0, 0], [4, 3, 1, 1, 1, 1, 0, 0], [4, 2, 1, 1, 1, 1, 1, 0], [4, 1, 1, 1, 1, 1, 1, 1], [3, 3, 3, 2, 0, 0, 0, 0], [3, 3, 3, 1, 1, 0, 0, 0], [3, 3, 2, 2, 1, 0, 0, 0], [3, 2, 2, 2, 2, 0, 0, 0], [3, 2, 2, 2, 1, 1, 0, 0], [3, 2, 2, 1, 1, 1, 1, 0], [3, 2, 1, 1, 1, 1, 1, 1], [2, 2, 2, 1, 1, 1, 1, 1]]
preshiftpriskilldist = priskilldist[prirandnum]
postshiftpriskilldist = []
prishift1 = random.randint(0, 7)
prishift2 = random.randint(0, 6)
prishift3 = random.randint(0, 5)
prishift4 = random.randint(0, 4)
prishift5 = random.randint(0, 3)
prishift6 = random.randint(0, 2)
prishift7 = random.randint(0, 1)
postshiftpriskilldist.append(preshiftpriskilldist[prishift1])
preshiftpriskilldist.pop(prishift1)
postshiftpriskilldist.append(preshiftpriskilldist[prishift2])
preshiftpriskilldist.pop(prishift2)
postshiftpriskilldist.append(preshiftpriskilldist[prishift3])
preshiftpriskilldist.pop(prishift3)
postshiftpriskilldist.append(preshiftpriskilldist[prishift4])
preshiftpriskilldist.pop(prishift4)
postshiftpriskilldist.append(preshiftpriskilldist[prishift5])
preshiftpriskilldist.pop(prishift5)
postshiftpriskilldist.append(preshiftpriskilldist[prishift6])
preshiftpriskilldist.pop(prishift6)
postshiftpriskilldist.append(preshiftpriskilldist[prishift7])
preshiftpriskilldist.pop(prishift7)
postshiftpriskilldist.append(preshiftpriskilldist[0])

secrandnum = random.randint(0, 12)
secskilldist = [[5, 2, 0, 0, 0, 0, 0, 0], [5, 1, 1, 0, 0, 0, 0, 0], [4, 3, 0, 0, 0, 0, 0, 0], [4, 2, 1, 0, 0, 0, 0, 0], [4, 1, 1, 1, 0, 0, 0, 0], [3, 3, 1, 0, 0, 0, 0, 0], [3, 2, 2, 0, 0, 0, 0, 0], [3, 2, 1, 1, 0, 0, 0, 0], [3, 1, 1, 1, 1, 0, 0, 0], [2, 2, 2, 1, 0, 0, 0, 0], [2, 2, 1, 1, 1, 0, 0, 0], [2, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
preshiftsecskilldist = secskilldist[secrandnum]
postshiftsecskilldist = []
secshift1 = random.randint(0, 7)
secshift2 = random.randint(0, 6)
secshift3 = random.randint(0, 5)
secshift4 = random.randint(0, 4)
secshift5 = random.randint(0, 3)
secshift6 = random.randint(0, 2)
secshift7 = random.randint(0, 1)
postshiftsecskilldist.append(preshiftsecskilldist[secshift1])
preshiftsecskilldist.pop(secshift1)
postshiftsecskilldist.append(preshiftsecskilldist[secshift2])
preshiftsecskilldist.pop(secshift2)
postshiftsecskilldist.append(preshiftsecskilldist[secshift3])
preshiftsecskilldist.pop(secshift3)
postshiftsecskilldist.append(preshiftsecskilldist[secshift4])
preshiftsecskilldist.pop(secshift4)
postshiftsecskilldist.append(preshiftsecskilldist[secshift5])
preshiftsecskilldist.pop(secshift5)
postshiftsecskilldist.append(preshiftsecskilldist[secshift6])
preshiftsecskilldist.pop(secshift6)
postshiftsecskilldist.append(preshiftsecskilldist[secshift7])
preshiftsecskilldist.pop(secshift7)
postshiftsecskilldist.append(preshiftsecskilldist[0])

terrandnum = random.randint(0, 4)
terskilldist = [[4, 0, 0, 0, 0, 0, 0, 0], [3, 1, 0, 0, 0, 0, 0, 0], [2, 2, 0, 0, 0, 0, 0, 0], [2, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
preshiftterskilldist = terskilldist[terrandnum]
postshiftterskilldist = []
tershift1 = random.randint(0, 7)
tershift2 = random.randint(0, 6)
tershift3 = random.randint(0, 5)
tershift4 = random.randint(0, 4)
tershift5 = random.randint(0, 3)
tershift6 = random.randint(0, 2)
tershift7 = random.randint(0, 1)
postshiftterskilldist.append(preshiftterskilldist[tershift1])
preshiftterskilldist.pop(tershift1)
postshiftterskilldist.append(preshiftterskilldist[tershift2])
preshiftterskilldist.pop(tershift2)
postshiftterskilldist.append(preshiftterskilldist[tershift3])
preshiftterskilldist.pop(tershift3)
postshiftterskilldist.append(preshiftterskilldist[tershift4])
preshiftterskilldist.pop(tershift4)
postshiftterskilldist.append(preshiftterskilldist[tershift5])
preshiftterskilldist.pop(tershift5)
postshiftterskilldist.append(preshiftterskilldist[tershift6])
preshiftterskilldist.pop(tershift6)
postshiftterskilldist.append(preshiftterskilldist[tershift7])
preshiftterskilldist.pop(tershift7)
postshiftterskilldist.append(preshiftterskilldist[0])

priskill = random.randint(0, 2)
secskill = random.randint(0, 1)

if priskill == 0:
    if secskill == 0:
        ((chartable[firstname+surname])['skills'])['academics'] = postshiftpriskilldist[0]
        ((chartable[firstname+surname])['skills'])['computer'] = postshiftpriskilldist[1]
        ((chartable[firstname+surname])['skills'])['crafts'] = postshiftpriskilldist[2]
        ((chartable[firstname+surname])['skills'])['investigation'] = postshiftpriskilldist[3]
        ((chartable[firstname+surname])['skills'])['medicine'] = postshiftpriskilldist[4]
        ((chartable[firstname+surname])['skills'])['occult'] = postshiftpriskilldist[5]
        ((chartable[firstname+surname])['skills'])['politics'] = postshiftpriskilldist[6]
        ((chartable[firstname+surname])['skills'])['science'] = postshiftpriskilldist[7]
        ((chartable[firstname+surname])['skills'])['athletics'] = postshiftsecskilldist[0]
        ((chartable[firstname+surname])['skills'])['brawl'] = postshiftsecskilldist[1]
        ((chartable[firstname+surname])['skills'])['drive'] = postshiftsecskilldist[2]
        ((chartable[firstname+surname])['skills'])['firearms'] = postshiftsecskilldist[3]
        ((chartable[firstname+surname])['skills'])['larceny'] = postshiftsecskilldist[4]
        ((chartable[firstname+surname])['skills'])['stealth'] = postshiftsecskilldist[5]
        ((chartable[firstname+surname])['skills'])['survival'] = postshiftsecskilldist[6]
        ((chartable[firstname+surname])['skills'])['weaponry'] = postshiftsecskilldist[7]
        ((chartable[firstname+surname])['skills'])['animalken'] = postshiftterskilldist[0]
        ((chartable[firstname+surname])['skills'])['empathy'] = postshiftterskilldist[1]
        ((chartable[firstname+surname])['skills'])['expression'] = postshiftterskilldist[2]
        ((chartable[firstname+surname])['skills'])['intimidation'] = postshiftterskilldist[3]
        ((chartable[firstname+surname])['skills'])['persuasion'] = postshiftterskilldist[4]
        ((chartable[firstname+surname])['skills'])['socialize'] = postshiftterskilldist[5]
        ((chartable[firstname+surname])['skills'])['streetwise'] = postshiftterskilldist[6]
        ((chartable[firstname+surname])['skills'])['subterfuge'] = postshiftterskilldist[7]
    else:
        ((chartable[firstname+surname])['skills'])['academics'] = postshiftpriskilldist[0]
        ((chartable[firstname+surname])['skills'])['computer'] = postshiftpriskilldist[1]
        ((chartable[firstname+surname])['skills'])['crafts'] = postshiftpriskilldist[2]
        ((chartable[firstname+surname])['skills'])['investigation'] = postshiftpriskilldist[3]
        ((chartable[firstname+surname])['skills'])['medicine'] = postshiftpriskilldist[4]
        ((chartable[firstname+surname])['skills'])['occult'] = postshiftpriskilldist[5]
        ((chartable[firstname+surname])['skills'])['politics'] = postshiftpriskilldist[6]
        ((chartable[firstname+surname])['skills'])['science'] = postshiftpriskilldist[7]
        ((chartable[firstname+surname])['skills'])['animalken'] = postshiftsecskilldist[0]
        ((chartable[firstname+surname])['skills'])['empathy'] = postshiftsecskilldist[1]
        ((chartable[firstname+surname])['skills'])['expression'] = postshiftsecskilldist[2]
        ((chartable[firstname+surname])['skills'])['intimidation'] = postshiftsecskilldist[3]
        ((chartable[firstname+surname])['skills'])['persuasion'] = postshiftsecskilldist[4]
        ((chartable[firstname+surname])['skills'])['socialize'] = postshiftsecskilldist[5]
        ((chartable[firstname+surname])['skills'])['streetwise'] = postshiftsecskilldist[6]
        ((chartable[firstname+surname])['skills'])['subterfuge'] = postshiftsecskilldist[7]
        ((chartable[firstname+surname])['skills'])['athletics'] = postshiftterskilldist[0]
        ((chartable[firstname+surname])['skills'])['brawl'] = postshiftterskilldist[1]
        ((chartable[firstname+surname])['skills'])['drive'] = postshiftterskilldist[2]
        ((chartable[firstname+surname])['skills'])['firearms'] = postshiftterskilldist[3]
        ((chartable[firstname+surname])['skills'])['larceny'] = postshiftterskilldist[4]
        ((chartable[firstname+surname])['skills'])['stealth'] = postshiftterskilldist[5]
        ((chartable[firstname+surname])['skills'])['survival'] = postshiftterskilldist[6]
        ((chartable[firstname+surname])['skills'])['weaponry'] = postshiftterskilldist[7]
elif priskill == 1:
    if secskill == 0:
        ((chartable[firstname+surname])['skills'])['athletics'] = postshiftpriskilldist[0]
        ((chartable[firstname+surname])['skills'])['brawl'] = postshiftpriskilldist[1]
        ((chartable[firstname+surname])['skills'])['drive'] = postshiftpriskilldist[2]
        ((chartable[firstname+surname])['skills'])['firearms'] = postshiftpriskilldist[3]
        ((chartable[firstname+surname])['skills'])['larceny'] = postshiftpriskilldist[4]
        ((chartable[firstname+surname])['skills'])['stealth'] = postshiftpriskilldist[5]
        ((chartable[firstname+surname])['skills'])['survival'] = postshiftpriskilldist[6]
        ((chartable[firstname+surname])['skills'])['weaponry'] = postshiftpriskilldist[7]
        ((chartable[firstname+surname])['skills'])['academics'] = postshiftsecskilldist[0]
        ((chartable[firstname+surname])['skills'])['computer'] = postshiftsecskilldist[1]
        ((chartable[firstname+surname])['skills'])['crafts'] = postshiftsecskilldist[2]
        ((chartable[firstname+surname])['skills'])['investigation'] = postshiftsecskilldist[3]
        ((chartable[firstname+surname])['skills'])['medicine'] = postshiftsecskilldist[4]
        ((chartable[firstname+surname])['skills'])['occult'] = postshiftsecskilldist[5]
        ((chartable[firstname+surname])['skills'])['politics'] = postshiftsecskilldist[6]
        ((chartable[firstname+surname])['skills'])['science'] = postshiftsecskilldist[7]
        ((chartable[firstname+surname])['skills'])['animalken'] = postshiftterskilldist[0]
        ((chartable[firstname+surname])['skills'])['empathy'] = postshiftterskilldist[1]
        ((chartable[firstname+surname])['skills'])['expression'] = postshiftterskilldist[2]
        ((chartable[firstname+surname])['skills'])['intimidation'] = postshiftterskilldist[3]
        ((chartable[firstname+surname])['skills'])['persuasion'] = postshiftterskilldist[4]
        ((chartable[firstname+surname])['skills'])['socialize'] = postshiftterskilldist[5]
        ((chartable[firstname+surname])['skills'])['streetwise'] = postshiftterskilldist[6]
        ((chartable[firstname+surname])['skills'])['subterfuge'] = postshiftterskilldist[7]
    else:
        ((chartable[firstname+surname])['skills'])['athletics'] = postshiftpriskilldist[0]
        ((chartable[firstname+surname])['skills'])['brawl'] = postshiftpriskilldist[1]
        ((chartable[firstname+surname])['skills'])['drive'] = postshiftpriskilldist[2]
        ((chartable[firstname+surname])['skills'])['firearms'] = postshiftpriskilldist[3]
        ((chartable[firstname+surname])['skills'])['larceny'] = postshiftpriskilldist[4]
        ((chartable[firstname+surname])['skills'])['stealth'] = postshiftpriskilldist[5]
        ((chartable[firstname+surname])['skills'])['survival'] = postshiftpriskilldist[6]
        ((chartable[firstname+surname])['skills'])['weaponry'] = postshiftpriskilldist[7]
        ((chartable[firstname+surname])['skills'])['animalken'] = postshiftsecskilldist[0]
        ((chartable[firstname+surname])['skills'])['empathy'] = postshiftsecskilldist[1]
        ((chartable[firstname+surname])['skills'])['expression'] = postshiftsecskilldist[2]
        ((chartable[firstname+surname])['skills'])['intimidation'] = postshiftsecskilldist[3]
        ((chartable[firstname+surname])['skills'])['persuasion'] = postshiftsecskilldist[4]
        ((chartable[firstname+surname])['skills'])['socialize'] = postshiftsecskilldist[5]
        ((chartable[firstname+surname])['skills'])['streetwise'] = postshiftsecskilldist[6]
        ((chartable[firstname+surname])['skills'])['subterfuge'] = postshiftsecskilldist[7]
        ((chartable[firstname+surname])['skills'])['academics'] = postshiftterskilldist[0]
        ((chartable[firstname+surname])['skills'])['computer'] = postshiftterskilldist[1]
        ((chartable[firstname+surname])['skills'])['crafts'] = postshiftterskilldist[2]
        ((chartable[firstname+surname])['skills'])['investigation'] = postshiftterskilldist[3]
        ((chartable[firstname+surname])['skills'])['medicine'] = postshiftterskilldist[4]
        ((chartable[firstname+surname])['skills'])['occult'] = postshiftterskilldist[5]
        ((chartable[firstname+surname])['skills'])['politics'] = postshiftterskilldist[6]
        ((chartable[firstname+surname])['skills'])['science'] = postshiftterskilldist[7]
else:
    if secskill == 0:
        ((chartable[firstname+surname])['skills'])['animalken'] = postshiftpriskilldist[0]
        ((chartable[firstname+surname])['skills'])['empathy'] = postshiftpriskilldist[1]
        ((chartable[firstname+surname])['skills'])['expression'] = postshiftpriskilldist[2]
        ((chartable[firstname+surname])['skills'])['intimidation'] = postshiftpriskilldist[3]
        ((chartable[firstname+surname])['skills'])['persuasion'] = postshiftpriskilldist[4]
        ((chartable[firstname+surname])['skills'])['socialize'] = postshiftpriskilldist[5]
        ((chartable[firstname+surname])['skills'])['streetwise'] = postshiftpriskilldist[6]
        ((chartable[firstname+surname])['skills'])['subterfuge'] = postshiftpriskilldist[7]
        ((chartable[firstname+surname])['skills'])['academics'] = postshiftsecskilldist[0]
        ((chartable[firstname+surname])['skills'])['computer'] = postshiftsecskilldist[1]
        ((chartable[firstname+surname])['skills'])['crafts'] = postshiftsecskilldist[2]
        ((chartable[firstname+surname])['skills'])['investigation'] = postshiftsecskilldist[3]
        ((chartable[firstname+surname])['skills'])['medicine'] = postshiftsecskilldist[4]
        ((chartable[firstname+surname])['skills'])['occult'] = postshiftsecskilldist[5]
        ((chartable[firstname+surname])['skills'])['politics'] = postshiftsecskilldist[6]
        ((chartable[firstname+surname])['skills'])['science'] = postshiftsecskilldist[7]
        ((chartable[firstname+surname])['skills'])['athletics'] = postshiftterskilldist[0]
        ((chartable[firstname+surname])['skills'])['brawl'] = postshiftterskilldist[1]
        ((chartable[firstname+surname])['skills'])['drive'] = postshiftterskilldist[2]
        ((chartable[firstname+surname])['skills'])['firearms'] = postshiftterskilldist[3]
        ((chartable[firstname+surname])['skills'])['larceny'] = postshiftterskilldist[4]
        ((chartable[firstname+surname])['skills'])['stealth'] = postshiftterskilldist[5]
        ((chartable[firstname+surname])['skills'])['survival'] = postshiftterskilldist[6]
        ((chartable[firstname+surname])['skills'])['weaponry'] = postshiftterskilldist[7]
    else:
        ((chartable[firstname+surname])['skills'])['animalken'] = postshiftpriskilldist[0]
        ((chartable[firstname+surname])['skills'])['empathy'] = postshiftpriskilldist[1]
        ((chartable[firstname+surname])['skills'])['expression'] = postshiftpriskilldist[2]
        ((chartable[firstname+surname])['skills'])['intimidation'] = postshiftpriskilldist[3]
        ((chartable[firstname+surname])['skills'])['persuasion'] = postshiftpriskilldist[4]
        ((chartable[firstname+surname])['skills'])['socialize'] = postshiftpriskilldist[5]
        ((chartable[firstname+surname])['skills'])['streetwise'] = postshiftpriskilldist[6]
        ((chartable[firstname+surname])['skills'])['subterfuge'] = postshiftpriskilldist[7]
        ((chartable[firstname+surname])['skills'])['athletics'] = postshiftsecskilldist[0]
        ((chartable[firstname+surname])['skills'])['brawl'] = postshiftsecskilldist[1]
        ((chartable[firstname+surname])['skills'])['drive'] = postshiftsecskilldist[2]
        ((chartable[firstname+surname])['skills'])['firearms'] = postshiftsecskilldist[3]
        ((chartable[firstname+surname])['skills'])['larceny'] = postshiftsecskilldist[4]
        ((chartable[firstname+surname])['skills'])['stealth'] = postshiftsecskilldist[5]
        ((chartable[firstname+surname])['skills'])['survival'] = postshiftsecskilldist[6]
        ((chartable[firstname+surname])['skills'])['weaponry'] = postshiftsecskilldist[7]
        ((chartable[firstname+surname])['skills'])['academics'] = postshiftterskilldist[0]
        ((chartable[firstname+surname])['skills'])['computer'] = postshiftterskilldist[1]
        ((chartable[firstname+surname])['skills'])['crafts'] = postshiftterskilldist[2]
        ((chartable[firstname+surname])['skills'])['investigation'] = postshiftterskilldist[3]
        ((chartable[firstname+surname])['skills'])['medicine'] = postshiftterskilldist[4]
        ((chartable[firstname+surname])['skills'])['occult'] = postshiftterskilldist[5]
        ((chartable[firstname+surname])['skills'])['politics'] = postshiftterskilldist[6]
        ((chartable[firstname+surname])['skills'])['science'] = postshiftterskilldist[7]

if supernaturalflags['vampire']:
    (chartable[firstname+surname])['supernaturaltags'].append('vampire')

    (chartable[firstname+surname])['clan'] = clanslist[random.randint(0, 4)]

    (chartable[firstname+surname])['bloodline'] = 'None'

    if (chartable[firstname+surname])['clan'] == 'Daeva':
        randomnum = random.randint(0, 99)
        if randomnum == 0: #later change the 0 to less than whatever the number of bloodlines is and then randomly pull from an array of daeva bloodlines and based on the randomnum use that from array
            (chartable[firstname+surname])['bloodline'] = 'Septemi'

    (chartable[firstname+surname])['covenant'] = covenantslist[random.randint(0, 5)]

    humnum = random.randint(0, 9)
    if humnum == 0:
        (chartable[firstname+surname])['humanity'] = {'totalhumanity': (chartable[firstname+surname])['integrity'] - 1,
        'touchstone1': 'None',
        'touchstone1desc': 'None'}
    elif humnum == 9:
        (chartable[firstname+surname])['humanity'] = {'totalhumanity': (chartable[firstname+surname])['integrity'] + 1,
        'touchstone1': 'None',
        'touchstone1desc': 'None'}
    else:
        (chartable[firstname+surname])['humanity'] = {'totalhumanity': (chartable[firstname+surname])['integrity'],
        'touchstone1': 'None',
        'touchstone1desc': 'None'}
    (chartable[firstname+surname]).pop('integrity')

    (chartable[firstname+surname])['bloodpotency'] = 1
    (chartable[firstname+surname])['vitae'] = {'maxvitae': 10, 'currentvitae': 0}

    if (chartable[firstname+surname])['clan'] == 'Daeva':
        if (chartable[firstname+surname])['bloodline'] == 'None':
            psdiscdist = []
            discrandnum = random.randint(0, 2)
            disciplinedist = [[3, 0, 0], [2, 1, 0], [1, 1, 1]]
            disciplineset = disciplinedist[discrandnum]
            discrandnum1 = random.randint(0, 2)
            discrandnum2 = random.randint(0, 1)
            psdiscdist.append(disciplineset[discrandnum1])
            disciplineset.pop(discrandnum1)
            psdiscdist.append(disciplineset[discrandnum2])
            disciplineset.pop(discrandnum2)
            psdiscdist.append(disciplineset[0])
            (chartable[firstname+surname])['disciplines'] = []
            (chartable[firstname+surname])['disciplines'].append([{'celerity': {'level': psdiscdist[0]}}])
            if psdiscdist[1] == 5:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[1], 'awe': 1, 'Confidant': 2, 'Green Eyes': 3, 'Loyalty': 4, 'Idol': 5}}])
            elif psdiscdist[1] == 4:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[1], 'awe': 1, 'Confidant': 2, 'Green Eyes': 3, 'Loyalty': 4}}])
            elif psdiscdist[1] == 3:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[1], 'awe': 1, 'Confidant': 2, 'Green Eyes': 3}}])
            elif psdiscdist[1] == 2:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[1], 'awe': 1, 'Confidant': 2}}])
            elif psdiscdist[1] == 1:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[1], 'awe': 1}}])
            else:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[1]}}])
            (chartable[firstname+surname])['disciplines'].append([{'vigor': {'level': psdiscdist[2]}}])
        elif (chartable[firstname+surname])['bloodline'] == 'Septemi':
            psdiscdist = []
            discrandnum = random.randint(0, 2)
            disciplinedist = [[3, 0, 0, 0], [2, 1, 0, 0], [1, 1, 1, 0]]
            disciplineset = disciplinedist[discrandnum]
            discrandnum1 = random.randint(0, 3)
            discrandnum2 = random.randint(0, 2)
            discrandnum2 = random.randint(0, 1)
            psdiscdist.append(disciplineset[discrandnum1])
            disciplineset.pop(discrandnum1)
            psdiscdist.append(disciplineset[discrandnum2])
            disciplineset.pop(discrandnum2)
            psdiscdist.append(disciplineset[discrandnum3])
            disciplineset.pop(discrandnum3)
            psdiscdist.append(disciplineset[0])
            (chartable[firstname+surname])['disciplines'] = []
            if psdiscdist[0] == 5:
                (chartable[firstname+surname])['disciplines'].append([{'abjurism': {'level': psdiscdist[0], 'Buttress the Soul': 1, 'The Light of Truth': 2, 'Cleanse the Mind': 3, 'Banish the Summoned Servitor': 4, 'Break the Weave': 5}}])
            elif psdiscdist[0] == 4:
                (chartable[firstname+surname])['disciplines'].append([{'abjurism': {'level': psdiscdist[0], 'Buttress the Soul': 1, 'The Light of Truth': 2, 'Cleanse the Mind': 3, 'Banish the Summoned Servitor': 4}}])
            elif psdiscdist[0] == 3:
                (chartable[firstname+surname])['disciplines'].append([{'abjurism': {'level': psdiscdist[0], 'Buttress the Soul': 1, 'The Light of Truth': 2, 'Cleanse the Mind': 3}}])
            elif psdiscdist[0] == 2:
                (chartable[firstname+surname])['disciplines'].append([{'abjurism': {'level': psdiscdist[0], 'Buttress the Soul': 1, 'The Light of Truth': 2}}])
            elif psdiscdist[0] == 1:
                (chartable[firstname+surname])['disciplines'].append([{'abjurism': {'level': psdiscdist[0], 'Buttress the Soul': 1}}])
            else:
                (chartable[firstname+surname])['disciplines'].append([{'abjurism': {'level': psdiscdist[0]}}])
            (chartable[firstname+surname])['disciplines'].append([{'celerity': {'level': psdiscdist[1]}}])
            if psdiscdist[2] == 5:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[2], 'Awe': 1, 'Confidant': 2, 'Green Eyes': 3, 'Loyalty': 4, 'Idol': 5}}])
            elif psdiscdist[2] == 4:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[2], 'Awe': 1, 'Confidant': 2, 'Green Eyes': 3, 'Loyalty': 4}}])
            elif psdiscdist[2] == 3:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[2], 'Awe': 1, 'Confidant': 2, 'Green Eyes': 3}}])
            elif psdiscdist[2] == 2:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[2], 'Awe': 1, 'Confidant': 2}}])
            elif psdiscdist[2] == 1:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[2], 'Awe': 1}}])
            else:
                (chartable[firstname+surname])['disciplines'].append([{'majesty': {'level': psdiscdist[2]}}])
            (chartable[firstname+surname])['disciplines'].append([{'vigor': {'level': psdiscdist[3]}}])
    elif (chartable[firstname+surname])['clan'] == 'Gangrel':
        if (chartable[firstname+surname])['bloodline'] == 'None':
            psdiscdist = []
            discrandnum = random.randint(0, 2)
            disciplinedist = [[3, 0, 0], [2, 1, 0], [1, 1, 1]]
            disciplineset = disciplinedist[discrandnum]
            discrandnum1 = random.randint(0, 2)
            discrandnum2 = random.randint(0, 1)
            psdiscdist.append(disciplineset[discrandnum1])
            disciplineset.pop(discrandnum1)
            psdiscdist.append(disciplineset[discrandnum2])
            disciplineset.pop(discrandnum2)
            psdiscdist.append(disciplineset[0])
            (chartable[firstname+surname])['disciplines'] = []
            if psdiscdist[0] == 5:
                (chartable[firstname+surname])['disciplines'].append([{'animalism': {'level': psdiscdist[0], 'Feral Whispers': 1, 'Raise the Familiar': 2, 'Summon the Hunt': 3, 'Feral Infection': 4, 'Lord of the Land': 5}}])
            elif psdiscdist[0] == 4:
                (chartable[firstname+surname])['disciplines'].append([{'animalism': {'level': psdiscdist[0], 'Feral Whispers': 1, 'Raise the Familiar': 2, 'Summon the Hunt': 3, 'Feral Infection': 4}}])
            elif psdiscdist[0] == 3:
                (chartable[firstname+surname])['disciplines'].append([{'animalism': {'level': psdiscdist[0], 'Feral Whispers': 1, 'Raise the Familiar': 2, 'Summon the Hunt': 3}}])
            elif psdiscdist[0] == 2:
                (chartable[firstname+surname])['disciplines'].append([{'animalism': {'level': psdiscdist[0], 'Feral Whispers': 1, 'Raise the Familiar': 2}}])
            elif psdiscdist[0] == 1:
                (chartable[firstname+surname])['disciplines'].append([{'animalism': {'level': psdiscdist[0], 'Feral Whispers': 1}}])
            else:
                (chartable[firstname+surname])['disciplines'].append([{'animalism': {'level': psdiscdist[0]}}])
            if psdiscdist[1] == 5:
                (chartable[firstname+surname])['disciplines'].append([{'protean': {'level': psdiscdist[1], 'Unmarked Grave': 1, 'Predatory Aspect': 2, 'Beast’s Skin': 3, 'Unnatural Aspect': 4, 'Primeval Miasma': 5}}])
            elif psdiscdist[1] == 4:
                (chartable[firstname+surname])['disciplines'].append([{'protean': {'level': psdiscdist[1], 'Unmarked Grave': 1, 'Predatory Aspect': 2, 'Beast’s Skin': 3, 'Unnatural Aspect': 4}}])
            elif psdiscdist[1] == 3:
                (chartable[firstname+surname])['disciplines'].append([{'protean': {'level': psdiscdist[1], 'Unmarked Grave': 1, 'Predatory Aspect': 2, 'Beast’s Skin': 3}}])
            elif psdiscdist[1] == 2:
                (chartable[firstname+surname])['disciplines'].append([{'protean': {'level': psdiscdist[1], 'Unmarked Grave': 1, 'Predatory Aspect': 2}}])
            elif psdiscdist[1] == 1:
                (chartable[firstname+surname])['disciplines'].append([{'protean': {'level': psdiscdist[1], 'Unmarked Grave': 1}}])
            else:
                (chartable[firstname+surname])['disciplines'].append([{'protean': {'level': psdiscdist[1]}}])
            (chartable[firstname+surname])['disciplines'].append([{'resilience': {'level': psdiscdist[2]}}])
    elif (chartable[firstname+surname])['clan'] == 'Mekhet':
        if (chartable[firstname+surname])['bloodline'] == 'None':
            psdiscdist = []
            discrandnum = random.randint(0, 2)
            disciplinedist = [[3, 0, 0], [2, 1, 0], [1, 1, 1]]
            disciplineset = disciplinedist[discrandnum]
            discrandnum1 = random.randint(0, 2)
            discrandnum2 = random.randint(0, 1)
            psdiscdist.append(disciplineset[discrandnum1])
            disciplineset.pop(discrandnum1)
            psdiscdist.append(disciplineset[discrandnum2])
            disciplineset.pop(discrandnum2)
            psdiscdist.append(disciplineset[0])
            (chartable[firstname+surname])['disciplines'] = []
            if psdiscdist[0] == 5:
                (chartable[firstname+surname])['disciplines'].append([{'auspex': {'level': psdiscdist[0], 'Feral Whispers': 1, 'Raise the Familiar': 2, 'Summon the Hunt': 3, 'Feral Infection': 4, 'Lord of the Land': 5}}])
            elif psdiscdist[0] == 4:
                (chartable[firstname+surname])['disciplines'].append([{'auspex': {'level': psdiscdist[0], 'Feral Whispers': 1, 'Raise the Familiar': 2, 'Summon the Hunt': 3, 'Feral Infection': 4}}])
            elif psdiscdist[0] == 3:
                (chartable[firstname+surname])['disciplines'].append([{'auspex': {'level': psdiscdist[0], 'Feral Whispers': 1, 'Raise the Familiar': 2, 'Summon the Hunt': 3}}])
            elif psdiscdist[0] == 2:
                (chartable[firstname+surname])['disciplines'].append([{'auspex': {'level': psdiscdist[0], 'Feral Whispers': 1, 'Raise the Familiar': 2}}])
            elif psdiscdist[0] == 1:
                (chartable[firstname+surname])['disciplines'].append([{'auspex': {'level': psdiscdist[0], 'Feral Whispers': 1}}])
            else:
                (chartable[firstname+surname])['disciplines'].append([{'auspex': {'level': psdiscdist[0]}}])
            (chartable[firstname+surname])['disciplines'].append([{'celerity': {'level': psdiscdist[1]}}])
            if psdiscdist[2] == 5:
                (chartable[firstname+surname])['disciplines'].append([{'obfuscate': {'level': psdiscdist[2], 'Unmarked Grave': 1, 'Predatory Aspect': 2, 'Beast’s Skin': 3, 'Unnatural Aspect': 4, 'Primeval Miasma': 5}}])
            elif psdiscdist[2] == 4:
                (chartable[firstname+surname])['disciplines'].append([{'obfuscate': {'level': psdiscdist[2], 'Unmarked Grave': 1, 'Predatory Aspect': 2, 'Beast’s Skin': 3, 'Unnatural Aspect': 4}}])
            elif psdiscdist[2] == 3:
                (chartable[firstname+surname])['disciplines'].append([{'obfuscate': {'level': psdiscdist[2], 'Unmarked Grave': 1, 'Predatory Aspect': 2, 'Beast’s Skin': 3}}])
            elif psdiscdist[2] == 2:
                (chartable[firstname+surname])['disciplines'].append([{'obfuscate': {'level': psdiscdist[2], 'Unmarked Grave': 1, 'Predatory Aspect': 2}}])
            elif psdiscdist[2] == 1:
                (chartable[firstname+surname])['disciplines'].append([{'obfuscate': {'level': psdiscdist[2], 'Unmarked Grave': 1}}])
            else:
                (chartable[firstname+surname])['disciplines'].append([{'obfuscate': {'level': psdiscdist[2]}}])


#daeva celerity majesty vigor
#gangrel animalism protean resilience
#mekhet auspex celerity obfuscate
#nosferatu nightmare obfuscate vigor
#ventrue animalism dominate resilience

with open(file, 'w') as f:
    json.dump(chartable, f)
