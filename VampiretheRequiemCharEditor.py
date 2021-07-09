import json
from os import path

file = 'samplekine.json'

if path.exists(file):
    with open(file) as f:
        chartable = json.load(f)
else:
    chartable = {}

chartable['samplekine'] = {'name': 'Samplekine',

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

(chartable['samplekine'])['speed'] = 5 + ((chartable['samplekine'])['stats'])['strength'] + ((chartable['samplekine'])['stats'])['dexterity']
((chartable['samplekine'])['health'])['maxhealth'] = (chartable['samplekine'])['size'] + ((chartable['samplekine'])['stats'])['stamina']
(chartable['samplekine'])['initiativemod'] = ((chartable['samplekine'])['stats'])['dexterity'] + ((chartable['samplekine'])['stats'])['composure']
if ((chartable['samplekine'])['stats'])['wits'] < ((chartable['samplekine'])['stats'])['dexterity']:
    (chartable['samplekine'])['defense'] = ((chartable['samplekine'])['stats'])['wits'] + ((chartable['samplekine'])['skills'])['athletics']
else:
    (chartable['samplekine'])['defense'] = ((chartable['samplekine'])['stats'])['dexterity'] + ((chartable['samplekine'])['skills'])['athletics']
(chartable['samplekine'])['permanentwillpower'] = ((chartable['samplekine'])['stats'])['resolve'] + ((chartable['samplekine'])['stats'])['composure']
(chartable['samplekine'])['temporarywillpower'] = ((chartable['samplekine'])['stats'])['resolve'] + ((chartable['samplekine'])['stats'])['composure']

with open(file, 'w') as f:
    json.dump(chartable, f)
