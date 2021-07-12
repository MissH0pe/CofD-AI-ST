import json

converse = {'p':{},'n':{}}
pid = 0
nid = 0

with open("evaconverse.txt") as f:
    nonemptylines = [line.strip("\n") for line in f if line != "\n"]
    for line in nonemptylines:
        array = line.split(']')
        if len(array) == 3:
            if array[0] == 'p':
                (converse['p'])[pid] = {'requires': int(array[1]), 'dialogue': array[2], 'said': False}
                pid += 1
            else:
                (converse['n'])[nid] = {'requires': int(array[1]), 'dialogue': array[2], 'said': False}
                nid += 1
        else:
            if array[0] == 'p':
                (converse['p'])[pid] = {'requires': int(array[1]), 'dialogue': array[2], 'unlocks': int(array[3]), 'said': False}
                pid += 1
            else:
                (converse['n'])[nid] = {'requires': int(array[1]), 'dialogue': array[2], 'unlocks': int(array[3]), 'said': False}
                nid += 1

with open('evaconverse.json', 'w') as f:
    json.dump(converse, f)
