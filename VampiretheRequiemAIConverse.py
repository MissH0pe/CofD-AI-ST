import json
from os import path

counter = 1

file = 'evaconverse.json'

quit = False

flags = [0]

converse = {}

if path.exists(file):
    with open(file) as f:
        converse = json.load(f)

print('You see an unknown vampire, they glance up and gesture for you to come forward.', '\n')

while not quit:
    print('What would you like to say?', '\n')
    dialoguevals = []
    for x, y in converse['p'].items():
        for z in flags:
            if y['said'] == False:
                if y['requires'] == z:
                    print(counter, ' ', y['dialogue'])
                    dialoguevals.append(str(counter)+'.'+str(int(x)))
                    counter += 1
    print('If you want to end the conversation please press e.', '\n')
    counter = 1
    option = input('Please select an option.\n')
    if option == 'e':
        quit = True
    else:
        for x, y in converse['p'].items():
            for z in flags:
                # print(y['requires'], ' ', z)
                if y['requires'] == z:
                    # print(int(option) - 1 == int(x))
                    for m in range(len(dialoguevals)):
                        splitvals = dialoguevals[m].split('.')
                        if int(splitvals[0]) == int(option):
                            if int(splitvals[1]) == int(x):
                                # print('test2')
                                print('You say:', y['dialogue'])
                                for a, b in converse['n'].items():
                                    if int(x) == int(a):
                                        print('They respond:', b['dialogue'])
                                        # print(len(b))
                                        if len(b) == 4:
                                            flags.append(b['unlocks'])
                                        y['said'] = True
    # print(flags)
