import json

converse = {'p':{},'n':{}}
id = 0

with open("evaconverse.txt") as f:
    nonemptylines = [line.strip("\n") for line in f if line != "\n"]
    for line in nonemptylines:
        array = line.split(']')
        if len(array) == 3:
            if array[0] == 'p':
                (converse['p'])[id] = {'requires': array[1], 'dialogue': array[2]}
            else:
                (converse['n'])[id] = {'requires': array[1], 'dialogue': array[2]}
        else:
            if array[0] == 'p':
                (converse['p'])[id] = {'requires': array[1], 'dialogue': array[2], 'unlocks': array[3]}
            else:
                (converse['n'])[id] = {'requires': array[1], 'dialogue': array[2], 'unlocks': array[3]}
        id += 1

with open('evaconverse.json', 'w') as f:
    json.dump(converse, f)
